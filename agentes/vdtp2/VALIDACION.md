# Validación de los agentes vdtp2

Estado a 2026-11-02. Versión vigente congelada en `versiones/2026-11-02/`, con sumas SHA-256 en `SHA256SUMS`. La versión anterior queda en `versiones/2026-11-01/`.

## Versiones validadas

| Agente | Archivo vivo | Copia congelada | Versión |
|---|---|---|---|
| Cliente ideal | `instrucciones.md` | `versiones/2026-11-02/cliente-ideal-v1.7.md` | v1.7 |
| Descubre tu idea | `descubre.md` | `versiones/2026-11-02/descubre-v1.1.md` | v1.1 |
| Destino | `destino.md` | `versiones/2026-11-02/destino-v1.1.md` | v1.1 |
| Producto de entrada | `producto-entrada.md` | `versiones/2026-11-02/producto-entrada-v1.1.md` | v1.1 |

Las versiones v1.0 de los tres agentes se guardaron en el commit `610321b`, **antes** de consultar los métodos de VDTP de esas fases. Así no hay contaminación con su contenido.

## Cómo se ha validado

- **Ejecución real:** cada agente se ejecuta con el CLI de Claude en una instancia independiente que solo recibe sus instrucciones (`pruebas/banco.py`, `pruebas/competicion/competicion.py`).
- **Evaluación doble:** comprobaciones automáticas (regex y formato) y un juez independiente (otra llamada al modelo) con criterios por caso.
- **Competición:** cadenas completas de cuatro fases contra los agentes de VDTP, con una persona simulada idéntica para las dos y un juez ciego que valora dos veces con el orden invertido (`pruebas/competicion/juez.py`).

---

## 1. Cliente ideal · banco de 13 casos

| Versión | Automáticas | Juez | Notas |
|---|---|---|---|
| v1.2 | 54/55 | 23/26 | 11 casos. Un fallo automático era un falso positivo de la prueba |
| v1.3 | 55/55 | 24/26 | |
| v1.4 | 54/55 | 25/26 | Un fallo automático era un falso positivo de la prueba |
| v1.5 (2 ejecuciones) | 55/55 · 53/55 | 25/26 · 26/26 | |
| v1.6 (2 ejecuciones) | 52/52 · 52/52 | 26/26 · 25/26 | |
| **v1.7** | **62/63** | **30/31** | 13 casos (dos nuevos, más difíciles) |
| VDTP Avatar (referencia) | 53/63 | 14/31 | Mismos 13 casos |

Fallos que quedan en la v1.7: una antítesis "no es X, son Y" en el caso 01 y un dato sin etiquetar en el documento consolidado del caso 13.

Cambios de la v1.3 a la v1.7, todos salidos de fallos reales del banco:
- **v1.3:** línea "Base: hipótesis salvo lo marcado `[dato]`" en cada punto · plazos de resultado siempre `[a validar]` · en el segundo "rehacer", cambio de eje obligatorio.
- **v1.4:** `[dato]` solo para lo literal · las citas adaptadas se marcan `[adaptada de reseña N]`.
- **v1.5:** gramática del mercado (ustedes, pretérito simple, sin leísmo).
- **v1.6:** revisión antes de enviar (antítesis, deducciones, citas, plazos, restricciones, formato).
- **v1.7:** prohibido escribir piezas de otras fases (posts, anuncios…), aunque se pidan como borrador.

**Sesgo:** este banco se diseñó para medir lo que vdtp2 pretende hacer (etiquetas, `[CASO REAL]`, roles…). La puntuación de VDTP aquí indica sobre todo que no hace lo que vdtp2 hace, no que sea peor en todo.

## 2. Competición por fases · persona Andrés (electricista, Murcia)

Juicio ciego, A = VDTP, B = vdtp2. Puntuación sobre 30 (6 criterios), media de las dos pasadas.

| Fase | VDTP | vdtp2 | Turnos VDTP / vdtp2 | Ganador |
|---|---|---|---|---|
| Descubre | 21,0 | **27,0** | 8 / 10 | vdtp2 (2 de 2) |
| Cliente ideal | 18,5 | **28,0** | 6 / 4 | vdtp2 (2 de 2) |
| Destino | 19,5 | **27,0** | 3 / 2 | vdtp2 (2 de 2) |
| Producto de entrada | 19,5 | **25,0** | 5 / 3 | vdtp2 (2 de 2) |

| Criterio (sobre 5) | VDTP | vdtp2 |
|---|---|---|
| Utilidad | 3,25 | **4,75** |
| Profundidad | 3,12 | **5,00** |
| Fiabilidad | 2,12 | **5,00** |
| Adaptación a la persona | 2,88 | **5,00** |
| Poca carga para el usuario | **4,12** | 3,12 |
| Claridad | **4,12** | 3,88 |

Detalle y motivos del juez: `pruebas/competicion/juicio-andres.md`.

**Puntos débiles de vdtp2 que hay que trabajar:** carga para el usuario y claridad. Entrega más texto, más etiquetas y más preguntas por turno.

**Limitación:** en la fase de cliente ideal, la versión de VDTP de la prueba solo tenía los bloques de su primer bloque. El juez anotó un "fallo de acceso" al final que viene de la prueba, no del agente.

## 3. Competición · persona Lucía (maestra de infantil, Valencia)

**Pendiente.** Las respuestas de VDTP ya están generadas (`pruebas/referencia-vdtp/cadena-lucia/`). La cadena de vdtp2 y su juicio están en marcha. Resultado en `pruebas/competicion/juicio-lucia.md` cuando termine.

## 4. Casos difíciles por fase

| Agente | VDTP (juez) | vdtp2 v1.0 (juez) | vdtp2 v1.1 (automáticas · juez) |
|---|---|---|---|
| Destino (ansiedad, ingresos sin datos, fecha de caducidad) | 3/6 | 5/6 | **9/9 · 6/6** |
| Producto de entrada (deudas, poca capacidad) | 1/5 | 5/5 | **6/6 · 5/5** |
| Descubre (salud mental, fontanero) | 4/4 | 4/4 | **6/6 · 4/4** |
| **Total** | **8/15** | **14/15** | **21/21 · 15/15** |

Cambios de la v1.0 a la v1.1, salidos de fallos reales:
- **Destino:** la familia "resultado con plazo" proponía "Duérmete antes en dos semanas" para un programa de ansiedad. En sectores sensibles, esa familia ya solo usa datos del producto, nunca resultados de salud, dinero o relaciones con plazo.
- **Producto de entrada y Descubre:** tablas de puntuación de hasta 4 columnas, con el desglose en lista.

Nota: en la primera ejecución de Producto v1.1, el caso de deudas salió 0/3 porque el JSON del juez era inválido (el juez decía "cumple": true). El banco ahora repite la llamada al juez en ese caso. La segunda ejecución salió 3/3.

Casos en `pruebas/casos_destino.json`, `casos_producto.json` y `casos_descubre.json`.

---

## Referencia VDTP y cierre del servicio

- Las respuestas de los agentes de VDTP se generaron antes de las 23:00 UTC del 2026-11-01 (medianoche en España), cuando cerró el acceso. Se guardan como referencia en `pruebas/referencia-vdtp/`.
- **No se guardan sus prompts ni los bloques de su método.** Las copias locales usadas para generar las respuestas se borraron a las 23:00 UTC y no se volvieron a ejecutar.

## Límites de toda la validación

- Todas las ejecuciones las hace el mismo modelo, y las instrucciones de vdtp2 las escribió ese mismo modelo.
- Las personas son simuladas. La validación que falta es con usuarios reales: se propone una prueba a ciegas con 2-3 personas en la presentación de la semana que viene.
- Hay variación entre ejecuciones (ver v1.5 y v1.6). Las cifras son orientativas, no exactas.
