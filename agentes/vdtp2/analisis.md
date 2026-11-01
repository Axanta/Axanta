# Análisis de salidas del agente Avatar · base para vdtp2

Fuentes analizadas (resultados propios del agente Avatar, dos proyectos distintos):

| Documento | Proyecto | Tamaño | Carácter |
|---|---|---|---|
| `formacion_mecanizado.pdf` | Formación para operarios de mecanizado que quieren pasar a CNC/CAM | 113 págs. | Exploración máxima: cada punto ampliado varias veces |
| `Avatar v2 · Manual de regularización de máquinas` | Manual para que pymes industriales pongan sus máquinas en regla antes de enero de 2027 | 22 págs. | Síntesis validada: segunda versión, compacta y revisada |

Los dos documentos son las dos fases de un mismo proceso: el primero **abre** (genera material en bruto con mucha profundidad) y el segundo **cierra** (filtra, valida y deja solo lo que se puede usar).

---

## 1. Qué hace bien el documento de mecanizado (profundidad)

**Descompone cada punto en muchas subsecciones.** "Situación actual" tiene 31 apartados: quién es, tres caras del avatar, trayectoria, día a día, semana tipo, cuerpo, ambiente en el taller, relación con la empresa, economía, cómo compra, carencias técnicas, entorno técnico, la escalera profesional, mitos, lo que se dice, cómo habla, emociones, escenas que le duelen, entorno personal, tecnología, dónde está en internet, referentes, detonantes, objetivos a 1-3 años, cómo sabría que ha dado el salto y la frase resumen.

**Usa una estructura fija para cada elemento.** Es lo que más calidad da:

- Impulsos ocultos (24): *qué desea · por qué no lo dice · cómo se nota · lo que piensa por dentro*.
- Intentos previos: *qué hizo · qué pasó · por qué falló · cómo se sintió · lo que se quedó pensando*, agrupados por ámbito (dentro del taller, formación reglada, por su cuenta, comunidad, fuera del taller).
- Objeciones: *frase literal · lo que hay detrás · lo que necesita ver*, agrupadas por categoría (tiempo, dinero, capacidad, confianza, aplicación, resultado, entorno, miedos de fondo).

**Concreta con personajes y escenas.** Tres caras del mismo avatar con nombre y edad (Javi 27, Toni 38, Sergio 33), un día bueno y un día malo, escenas que duelen ("en una entrevista le preguntan qué CAM maneja y se queda en blanco").

**Recoge el lenguaje real del cliente.** Frases que se dice, frases que dice en voz alta y un vocabulario del oficio ("atadas, reglaje, cero pieza, plaquita, taladrina") con lo que **no** hay que decirle ("optimización de procesos", "competencias digitales").

**Separa intentos previos de creencias.** Cada intento deja una creencia que hoy le frena. Luego analiza la secuencia que se repite, lo que se llevó y lo que perdió, y lo que habría necesitado en cada intento. Esto alimenta directamente la oferta.

**Baja todo a material usable.** Ejemplos de posts y vídeos cortos, glosario, ideas de producto de entrada. Cuando un ejemplo necesita un caso real, da la alternativa por si no lo hay.

**Problemas detectados:**

- **Demasiado largo para trabajar.** 113 páginas no se pueden revisar ni usar de referencia diaria.
- **Repeticiones.** Varios impulsos se solapan (respeto, orgullo, dejar huella, ser ejemplo para sus hijos) y las mismas ideas reaparecen en emocional, visión de futuro y riesgos.
- **Hipótesis presentadas como hechos.** Personajes, rutinas y emociones son inferencias plausibles sin marcar como tales.
- **Un caso de ejemplo que parece real.** En pruebas sociales aparece "Un operario de un taller de Castellón llevaba años cargando piezas… Hoy prepara él las series" como plantilla. Va acompañado de "siempre que sean reales", pero es fácil que acabe publicado tal cual.
- **Se sale del avatar.** Glosario, posts y productos aspirina son útiles, pero mezclan entregables de otras fases.

## 2. Qué hace bien Avatar v2 (disciplina)

**Las condiciones del negocio se aplican a todo el documento.** El modelo cambió a "manual: el cliente lo hace todo, el autor no visita, no firma, no vende protecciones". Esa restricción aparece coherente en todos los puntos: quién queda fuera, objeciones ("¿Quién firma esto?" → "El autor no firma nada: enseña"), guía, paso a paso y riesgos.

**Marca lo que no está validado.** "Cifra concreta sin validar", "Contenidos que consume (a validar)", "Aficiones: sin datos validados", "Pendiente de medir con el grupo piloto".

**No inventa pruebas.** "Hoy no hay testimonios ni casos de seguridad de máquinas. No se ha inventado ninguno." Separa lo que hay hoy (prueba indirecta de oficio) de cómo conseguir las pruebas que faltan.

**Tiene una lista de pendientes.** Una lista de comprobación final con todo lo que falta para que el documento sea sólido: máquinas reales, grupo piloto, revisión por técnico titulado, versión del Destino sin fecha, datos "a validar".

**Cuida la precisión legal.** Cita RD 1215/1997 y Reglamento (UE) 2023/1230 (aplicable desde el 20 de enero de 2027) y el recargo de prestaciones del 30-50 %. Marca la revisión por técnico como pendiente.

**Avisa de cuándo caduca el Destino.** "Este Destino caduca el 20 de enero de 2027; para vender después hará falta una versión sin fecha."

**Pone el nivel por área y su consecuencia.** Tabla de *ámbito · nivel · qué implica al comunicarle*. "Avanzado en máquinas → nunca explicarle cómo funciona su máquina". "Principiante en normativa → traducir a lenguaje de taller".

**Distingue grados de conciencia según el detonante.** Con presión externa, tras una compra reciente o sin detonante. Cada uno pide un mensaje distinto.

**Abre con un resumen para copywriting.** Destino, punto de partida, a dónde llega, mensaje emocional central, argumento racional central, top 5 impulsos y top 5 intentos. Después va el detalle.

**Enlaza con la siguiente fase.** "Producto de entrada que lleva a este manual: Producto aspirina · Cuenta Atrás 2027".

**Problemas detectados:**

- Pierde parte de la riqueza del primero: menos escenas, sin personajes, sin vocabulario explícito ni bloque "cómo habla".
- Algunos puntos quedan muy secos ("Tranquilidad." como resultado esperado, sin desarrollo).

## 3. Conclusión para vdtp2

El mejor resultado sale de **combinar los dos modos** en un mismo agente:

1. **Explorar** cada punto con estructuras fijas y ampliaciones dirigidas (lo del documento de mecanizado).
2. **Consolidar** en un documento corto, coherente con las restricciones del negocio, con todo lo no validado marcado y una lista de pendientes (lo de Avatar v2).

Además de los dos modos, conviene incorporar:

- **Restricciones del negocio desde el arranque**, para que cada punto las respete.
- **Etiquetas de fiabilidad**: `[dato del usuario]`, `[hipótesis]`, `[a validar]`, `[pendiente]`.
- **Plantillas de campos por punto**, con las que mejor han funcionado.
- **Menú de ampliación dirigida**, para que ampliar profundice en lugar de repetir.
- **Detección de solapes** antes de consolidar.
- **Comprobación de afirmaciones legales, técnicas o con cifras**, marcadas para revisión.
- **Fecha de caducidad** de cualquier mensaje con plazo.
- **Resumen de traspaso** para Destino y Producto de entrada.

La estructura narrativa de fondo (cliente, guía, plan, llamada a la acción, éxito y fracaso) es la de marcos públicos de *storytelling* de marca. El valor diferencial de vdtp2 está en las plantillas de campos, la ampliación dirigida y la disciplina de validación, que salen de vuestro propio trabajo.
