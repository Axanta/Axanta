#!/usr/bin/env python3
"""Juez ciego por fases. Compara dos conversaciones (A y B) sin saber de qué agente es cada una.

Uso: python3 juez.py <carpeta-A> <carpeta-B> <salida.md>
Cada fase se juzga dos veces con el orden invertido para reducir el sesgo de posición.
"""
import json, re, subprocess, sys
from pathlib import Path

CLI = ["claude", "-p", "--tools", "", "--strict-mcp-config", "--setting-sources", "", "--output-format", "json"]
import os
PERSONA_DESC = os.environ.get("PERSONA_DESC", "Andrés, electricista autónomo en Murcia que quiere vivir de enseñar por internet; tiene 6 h/semana, 500 € y no quiere vender por teléfono")
FASES = ["descubre", "avatar", "destino", "producto"]
CRITERIOS = [
    ("utilidad", "Utilidad práctica del resultado final para la persona: ¿podría usarlo mañana?"),
    ("profundidad", "Profundidad y concreción: detalle específico de su caso, no genérico."),
    ("fiabilidad", "Fiabilidad: no inventa datos ni resultados, distingue lo comprobado de lo supuesto, no promete lo que no puede sostener."),
    ("adaptacion", "Adaptación a la persona: usa su oficio, su historia y sus restricciones de tiempo, dinero y lo que no quiere hacer."),
    ("carga", "Poca carga para el usuario: le pide lo justo, no le abruma con texto ni preguntas innecesarias (5 = muy poca carga)."),
    ("claridad", "Claridad y estilo: se entiende a la primera, sin relleno ni muletillas."),
]

PROMPT = """Eres un evaluador experto en marketing para formadores y en calidad de asistentes conversacionales.
Vas a comparar dos conversaciones, X e Y, de dos asistentes distintos con el mismo usuario simulado ({persona}). Fase evaluada: {fase}.

Puntúa cada asistente de 1 a 5 en cada criterio y elige un ganador global de la fase (X, Y o empate). Sé estricto y concreto. Ignora la longitud por sí misma salvo en el criterio de carga.

CRITERIOS:
{criterios}

Responde SOLO con JSON válido:
{{"X": {{"utilidad": n, "profundidad": n, "fiabilidad": n, "adaptacion": n, "carga": n, "claridad": n}},
  "Y": {{...igual...}},
  "ganador": "X" | "Y" | "empate",
  "motivo": "dos o tres frases con ejemplos concretos de las conversaciones"}}

=== CONVERSACIÓN X ===
{x}

=== CONVERSACIÓN Y ===
{y}
"""


def juzgar(fase, x, y):
    crit = "\n".join(f"- {k}: {d}" for k, d in CRITERIOS)
    r = subprocess.run(CLI, input=PROMPT.format(fase=fase, criterios=crit, x=x, y=y, persona=PERSONA_DESC), capture_output=True, text=True, timeout=900)
    d = json.loads(r.stdout)
    res = d.get("result", "")
    if d.get("is_error") or re.search(r"hit your .*limit", res[:200], re.I):
        raise RuntimeError(res[:200])
    return json.loads(re.search(r"\{.*\}", res, re.S).group(0)), d.get("total_cost_usd", 0.0)


def main():
    a, b, salida = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    filas, detalle, total = [], [], 0.0
    sumas = {"A": {k: 0 for k, _ in CRITERIOS}, "B": {k: 0 for k, _ in CRITERIOS}}
    victorias = {"A": 0, "B": 0, "empate": 0}
    for f in FASES:
        ta, tb = (a / f"{f}.md").read_text(encoding="utf-8"), (b / f"{f}.md").read_text(encoding="utf-8")
        ja, jb = json.loads((a / f"{f}.json").read_text()), json.loads((b / f"{f}.json").read_text())
        # Quitar la cabecera con la etiqueta para que el juez no sepa quién es quién.
        ta, tb = ta.split("\n", 1)[1], tb.split("\n", 1)[1]
        r1, c1 = juzgar(f, ta, tb)   # A = X
        r2, c2 = juzgar(f, tb, ta)   # A = Y
        total += c1 + c2
        pa = {k: (r1["X"][k] + r2["Y"][k]) / 2 for k, _ in CRITERIOS}
        pb = {k: (r1["Y"][k] + r2["X"][k]) / 2 for k, _ in CRITERIOS}
        for k in pa:
            sumas["A"][k] += pa[k]; sumas["B"][k] += pb[k]
        g1 = {"X": "A", "Y": "B"}.get(r1["ganador"], "empate")
        g2 = {"X": "B", "Y": "A"}.get(r2["ganador"], "empate")
        g = g1 if g1 == g2 else "empate"
        victorias[g] += 1
        filas.append(f"| {f} | {sum(pa.values()):.1f} | {sum(pb.values()):.1f} | {ja['turnos']} / {jb['turnos']} | {g} ({g1}, {g2}) |")
        detalle.append(f"### {f}\n\n- Pasada 1 (A=X): ganador {g1}. {r1['motivo']}\n- Pasada 2 (A=Y): ganador {g2}. {r2['motivo']}\n")
    md = [f"# Juicio ciego · A = {a.name} · B = {b.name}\n",
          "Puntuación por fase: suma de 6 criterios (máx. 30), media de las dos pasadas. Ganador: solo si las dos pasadas coinciden.\n",
          "| Fase | A | B | Turnos A / B | Ganador (pasada 1, pasada 2) |", "|---|---|---|---|---|", *filas,
          f"\nVictorias: A {victorias['A']} · B {victorias['B']} · empates {victorias['empate']}\n",
          "## Media por criterio (sobre 5)\n", "| Criterio | A | B |", "|---|---|---|",
          *[f"| {k} | {sumas['A'][k]/len(FASES):.2f} | {sumas['B'][k]/len(FASES):.2f} |" for k, _ in CRITERIOS],
          "\n## Motivos del juez\n", *detalle, f"\nCoste del juicio: {total:.2f} USD"]
    salida.write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
