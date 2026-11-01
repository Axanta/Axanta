#!/usr/bin/env python3
"""Competición por fases: cadena de agentes A contra cadena B, con la misma persona simulada.

Uso: python3 competicion.py <carpeta-salida> <etiqueta> <descubre> <avatar> <destino> <producto>
Cada argumento de agente es la ruta a su prompt de sistema.
"""
import json, re, subprocess, sys, uuid
from pathlib import Path

BASE = Path(__file__).resolve().parent
PERSONA = (BASE / "persona.md").read_text(encoding="utf-8")
CLI = ["claude", "-p", "--tools", "", "--strict-mcp-config", "--setting-sources", "", "--output-format", "json"]

FASES = [
    ("descubre", 12, "Fase DESCUBRIR IDEA. Termina cuando el agente te haya dado tu frase final o idea elegida con su cierre."),
    ("avatar", 12, "Fase CLIENTE IDEAL. Termina cuando hayas validado el punto sobre el NIVEL del cliente (el último del bloque sobre el cliente: nivel, o nivel y conciencia). No sigas más allá."),
    ("destino", 8, "Fase DESTINO. Termina cuando hayas elegido un Destino y el agente te lo haya confirmado o te haya dado la versión final."),
    ("producto", 8, "Fase PRODUCTO DE ENTRADA. Termina cuando el agente te haya presentado la oferta completa del producto elegido y la hayas aprobado. No sigas a crear el contenido."),
]


def llamar(prompt, sistema=None, sesion=None, nueva=True):
    cmd = list(CLI)
    if sistema:
        cmd += ["--system-prompt", sistema]
    if sesion:
        cmd += (["--session-id", sesion] if nueva else ["--resume", sesion])
    r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=900)
    d = json.loads(r.stdout)
    res = d.get("result", "")
    if d.get("is_error") or re.search(r"hit your .*limit|rate limit|overloaded", res[:200], re.I):
        raise RuntimeError(f"Error del CLI: {res[:200]}")
    return res, d.get("total_cost_usd", 0.0)


def fase(nombre, max_turnos, alcance, sistema_agente, previo):
    s_agente, s_user = str(uuid.uuid4()), str(uuid.uuid4())
    sis_user = PERSONA + f"\n\n## Alcance de esta conversación\n{alcance}\nCuando se cumpla, en lugar de responder escribe exactamente: [FIN]"
    coste = 0.0
    apertura, c = llamar("Vas a empezar a hablar con un asistente nuevo. Escribe tu primer mensaje: un saludo y en una frase qué buscas.", sis_user, s_user, True)
    coste += c
    if previo:
        apertura += "\n\nEsto es lo que salió en la fase anterior:\n\n" + previo[-12000:]
    trans, msg_user, primera = [], apertura, True
    for _ in range(max_turnos):
        resp, c = llamar(msg_user, sistema_agente, s_agente, primera); coste += c; primera = False
        trans.append(("Andrés", msg_user)); trans.append(("Agente", resp))
        msg_user, c = llamar(f"El asistente te dice:\n\n{resp}\n\nResponde como Andrés (o [FIN] si se ha cumplido el alcance).", sis_user, s_user, False); coste += c
        if "[FIN]" in msg_user:
            break
    salida = "\n\n".join(t for q, t in trans if q == "Agente")
    return trans, salida, coste


def main():
    out, etiqueta = Path(sys.argv[1]), sys.argv[2]
    prompts = [Path(p).read_text(encoding="utf-8") for p in sys.argv[3:7]]
    out.mkdir(parents=True, exist_ok=True)
    previo, total = "", 0.0
    for (nombre, mt, alcance), sistema in zip(FASES, prompts):
        trans, salida, coste = fase(nombre, mt, alcance, sistema, previo)
        total += coste
        md = [f"# {etiqueta} · {nombre}\n"] + [f"### {q}\n\n{t}\n" for q, t in trans]
        (out / f"{nombre}.md").write_text("\n".join(md), encoding="utf-8")
        (out / f"{nombre}.json").write_text(json.dumps({"turnos": len(trans) // 2, "coste": coste, "trans": trans}, ensure_ascii=False), encoding="utf-8")
        previo = salida
        print(f"{etiqueta} {nombre}: {len(trans)//2} turnos, {coste:.2f} USD", flush=True)
    print(f"{etiqueta} total {total:.2f} USD")


if __name__ == "__main__":
    main()
