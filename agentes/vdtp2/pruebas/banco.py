#!/usr/bin/env python3
"""Banco de pruebas de vdtp2.

Ejecuta cada caso de casos.json como conversación real con el CLI de Claude,
usando instrucciones.md como prompt de sistema, y evalúa cada transcripción con:
  1. comprobaciones automáticas (regex y formato), y
  2. un juez independiente (otra llamada al modelo) con los criterios del caso.

Uso:
  python3 banco.py <etiqueta-version> [id-caso ...]

Resultados en pruebas/resultados/<etiqueta>/ (una transcripción por caso y resumen.md).
"""
import concurrent.futures as cf
import os
import json
import re
import subprocess
import sys
import uuid
from pathlib import Path

BASE = Path(__file__).resolve().parent
INSTRUCCIONES = Path(os.environ.get("VDTP2_PROMPT", BASE.parent / "instrucciones.md"))
SALIDA = Path(os.environ["VDTP2_SALIDA"]) if os.environ.get("VDTP2_SALIDA") else None
CASOS = Path(os.environ.get("VDTP2_CASOS", BASE / "casos.json"))

CLI = ["claude", "-p", "--tools", "", "--strict-mcp-config",
       "--setting-sources", "", "--output-format", "json"]

FRASES_IA = [
    "seamos honestos", "vamos al grano", "aquí está la clave",
    "déjame que te explique", "la cruda realidad", "una pregunta incómoda",
]
ANTITESIS = re.compile(r"\bno (es|son|tienes|necesitas) [^.\n|]{1,40}[,;:] ?(es|son|tienes|necesitas) ", re.I)


def llamar(prompt, sistema=None, sesion=None, nueva=True):
    import time
    for i in range(8):
        try:
            return _llamar(prompt, sistema, sesion, nueva)
        except RuntimeError as e:
            if i == 7 or not re.search(r"limit|overloaded|vac", str(e), re.I):
                raise
            time.sleep(min(1800, 120 * 2 ** i))


def _llamar(prompt, sistema=None, sesion=None, nueva=True):
    cmd = list(CLI)
    if sistema:
        cmd += ["--system-prompt", sistema]
    if sesion:
        cmd += (["--session-id", sesion] if nueva else ["--resume", sesion])
    r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=600)
    try:
        d = json.loads(r.stdout)
        res = d.get("result", "")
        if d.get("is_error") or re.search(r"hit your .*limit|rate limit|overloaded", res[:200], re.I):
            raise RuntimeError(f"Error del CLI: {res[:200]}")
        return res, d.get("total_cost_usd", 0.0)
    except json.JSONDecodeError:
        raise RuntimeError(f"Error del CLI (respuesta vacía, posible limit): {r.stderr[-300:]}")


def columnas_max(texto):
    maxc = 0
    for linea in texto.splitlines():
        s = linea.strip()
        if s.startswith("|") and s.endswith("|") and not re.fullmatch(r"\|[\s:|-]+\|", s):
            maxc = max(maxc, s.count("|") - 1)
    return maxc


def automaticas(caso, respuestas):
    todo = "\n".join(respuestas)
    res = []
    for p in caso.get("regex_si", []):
        res.append((f"contiene /{p}/", bool(re.search(p, todo))))
    for p in caso.get("regex_no", []):
        res.append((f"no contiene /{p}/", not re.search(p, todo)))
    res.append(("tablas de 4 columnas como máximo", columnas_max(todo) <= 4))
    res.append(("sin frases hechas de IA", not any(f in todo.lower() for f in FRASES_IA)))
    m = ANTITESIS.search(todo)
    res.append(("sin antítesis 'no es X, es Y'" + (f" (encontrada: «{m.group(0)}»)" if m else ""), m is None))
    return res


JUEZ = """Eres un evaluador estricto. Te doy la transcripción de una conversación entre un usuario y un asistente.
Evalúa SOLO estos criterios. Para cada uno responde si se cumple (true/false) y una frase breve de motivo citando la transcripción.
Responde únicamente con JSON válido: {{"criterios": [{{"criterio": "...", "cumple": true, "motivo": "..."}}]}}

CRITERIOS:
{criterios}

TRANSCRIPCIÓN:
{transcripcion}
"""


def juez(caso, transcripcion):
    criterios = "\n".join(f"- {c}" for c in caso["criterios"])
    out, coste = llamar(JUEZ.format(criterios=criterios, transcripcion=transcripcion))
    m = re.search(r"\{.*\}", out, re.S)
    try:
        return json.loads(m.group(0))["criterios"], coste
    except Exception:
        return [{"criterio": c, "cumple": False, "motivo": f"juez sin JSON válido: {out[:200]}"} for c in caso["criterios"]], coste


def ejecutar(caso, sistema, carpeta):
    sesion = str(uuid.uuid4())
    respuestas, coste = [], 0.0
    trans = []
    for i, turno in enumerate(caso["turnos"]):
        r, c = llamar(turno, sistema=sistema, sesion=sesion, nueva=(i == 0))
        coste += c
        respuestas.append(r)
        trans.append(f"### Usuario\n\n{turno}\n\n### Agente\n\n{r}\n")
    transcripcion = "\n".join(trans)
    auto = automaticas(caso, respuestas)
    jz, cj = juez(caso, transcripcion)
    coste += cj
    md = [f"# {caso['id']}\n", transcripcion, "\n---\n\n## Evaluación automática\n"]
    md += [f"- {'✅' if ok else '❌'} {n}" for n, ok in auto]
    md += ["\n## Evaluación del juez\n"]
    md += [f"- {'✅' if j.get('cumple') else '❌'} {j.get('criterio')} — {j.get('motivo')}" for j in jz]
    (carpeta / f"{caso['id']}.md").write_text("\n".join(md), encoding="utf-8")
    return caso["id"], auto, jz, coste


def main():
    etiqueta = sys.argv[1]
    filtro = set(sys.argv[2:])
    sistema = INSTRUCCIONES.read_text(encoding="utf-8")
    casos = [c for c in json.loads(CASOS.read_text(encoding="utf-8")) if not filtro or c["id"] in filtro]
    carpeta = (SALIDA or BASE / "resultados") / etiqueta
    carpeta.mkdir(parents=True, exist_ok=True)
    with cf.ThreadPoolExecutor(max_workers=3) as ex:
        res = sorted(ex.map(lambda c: ejecutar(c, sistema, carpeta), casos))
    filas, ta, oka, tj, okj, coste = [], 0, 0, 0, 0, 0.0
    for cid, auto, jz, c in res:
        a = sum(ok for _, ok in auto); j = sum(bool(x.get("cumple")) for x in jz)
        ta += len(auto); oka += a; tj += len(jz); okj += j; coste += c
        fallos = [n for n, ok in auto if not ok] + [x.get("criterio") for x in jz if not x.get("cumple")]
        filas.append(f"| {cid} | {a}/{len(auto)} | {j}/{len(jz)} | {'; '.join(fallos) or '—'} |")
    resumen = [f"# Resultados · {etiqueta}\n",
               f"Automáticas: **{oka}/{ta}** · Juez: **{okj}/{tj}** · Coste aproximado: {coste:.2f} USD\n",
               "| Caso | Automáticas | Juez | Fallos |", "|---|---|---|---|", *filas]
    (carpeta / "resumen.md").write_text("\n".join(resumen) + "\n", encoding="utf-8")
    print("\n".join(resumen))


if __name__ == "__main__":
    main()
