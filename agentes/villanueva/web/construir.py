#!/usr/bin/env python3
"""Genera index.html a partir de plantilla.html y las instrucciones vigentes de las cuatro fases."""
import json
from pathlib import Path
B = Path(__file__).resolve().parent
A = B.parent
prompts = {
    "descubre": (A / "descubre.md").read_text(encoding="utf-8"),
    "cliente": (A / "instrucciones.md").read_text(encoding="utf-8"),
    "destino": (A / "destino.md").read_text(encoding="utf-8"),
    "producto": (A / "producto-entrada.md").read_text(encoding="utf-8"),
}
datos = json.dumps(prompts, ensure_ascii=False).replace("</", "<\\/")
html = (B / "plantilla.html").read_text(encoding="utf-8").replace("__PROMPTS__", datos)
(B / "index.html").write_text(html, encoding="utf-8")
print("index.html", len(html), "bytes")
