# Registro de iteraciones · Villanueva v0.3 → v1.2

Fecha: 2026-11-01

## Cómo se ha iterado

Cada versión sigue el mismo ciclo:

1. **Caso de prueba nuevo**, elegido para estresar algo que las versiones anteriores no cubrían.
2. **Ejecución** de la versión anterior con ese caso.
3. **Fallo observado**, con un extracto de la salida.
4. **Cambio** en `instrucciones.md`.
5. **Comprobación**: se repite el caso con la versión nueva.

**Limitación:** las pruebas las ha ejecutado el mismo modelo que escribe las instrucciones, sin usuarios reales. Sirven para encontrar huecos en las instrucciones, no para medir la calidad final. La validación de verdad es la prueba a ciegas descrita en `comparativa.md` y el uso con clientes reales.

En estas iteraciones no se ha consultado el servidor VDTP.

## Resumen

| Versión | Caso de prueba | Fallo encontrado | Cambio |
|---|---|---|---|
| v0.3 | Nutricionistas que venden planes online a sus pacientes | Ignoraba al cliente del cliente | Negocios de dos niveles + duraciones `[a validar]` |
| v0.4 | Formación de Excel para empresas | Mezclaba quien paga con quien usa | Roles de compra |
| v0.5 | "Quiero vender algo de cocina" | Rellenaba todo con hipótesis genéricas | Filtro de nicho vago |
| v0.6 | Programa de respiración para personas con ansiedad | Dramatizaba el miedo y prometía resultados de salud | Reglas para sectores sensibles |
| v0.7 | Consolidar el caso de las máquinas | Documento final demasiado largo | Límites de longitud y fusión de duplicados |
| v0.8 | Curso de pastelería con 6 reseñas reales pegadas | Parafraseaba las reseñas y mezclaba dato con hipótesis | Modo evidencias |
| v0.9 | Usuario que dice "rehacer" dos veces | La segunda versión era casi igual a la primera | Protocolo de revisión y propagación |
| v1.0 | Usar el traspaso con un agente de Destino | Faltaban campos para escribir el Destino | Formato fijo de traspaso |
| v1.1 | Contadores en México | Español de España y normativa española | Mercado e idioma |
| v1.2 | Modo rápido + sector sensible a la vez | Reglas en conflicto y prompt demasiado largo | Orden de prioridades y poda |

---

## v0.3 · Negocios de dos niveles

**Caso:** "Ayudo a nutricionistas a vender planes de alimentación online a sus pacientes. Vendo un programa de 297 € en 6 semanas."

**Fallo (v0.2):** las objeciones solo eran las de la nutricionista ("no sé de marketing", "no tengo tiempo"). No aparecían las de sus pacientes ("¿y si no me funciona sin verte?"), que su programa tiene que ayudarla a resolver. Además prometía "en 6 semanas tienes tu plan online" sin datos.

**Cambio:**
- En el arranque, preguntar si el cliente vende a su vez a otros.
- Si es así, añadir en A4 (Objeciones) y C1 (Paso a paso) un apartado para su cliente final.
- Cualquier duración o plazo prometido se marca `[a validar]` hasta tener datos reales.

**Comprobación:** con la v0.3 aparecen dos bloques de objeciones. El de pacientes incluye "sin consulta presencial no me lo tomo en serio" y "ya he hecho dietas online". "6 semanas" sale marcado `[a validar]`.

## v0.4 · Roles de compra

**Caso:** "Formación de Excel para departamentos de administración de pymes. 900 € por empresa, hasta 5 personas."

**Fallo (v0.3):** el avatar era a la vez "administrativa de 35 años que pierde horas con hojas de cálculo" y "gerente que quiere productividad". Los impulsos de uno y otro estaban mezclados en la misma lista.

**Cambio:**
- En el arranque, identificar los roles: **quien paga**, **quien usa** y **quien influye o bloquea**.
- Si son personas distintas, A1, A3 y A4 se hacen por rol. D1 y D2 indican a qué rol va cada mensaje.

**Comprobación:** salen dos perfiles separados. El gerente quiere "que no se vaya la de administración y me deje colgado". La administrativa, "dejar de quedarme hasta tarde a fin de mes". Las objeciones del gerente son de precio y retorno; las de la administrativa, de "otra cosa más que aprender".

## v0.5 · Filtro de nicho vago

**Caso:** "Quiero vender algo de cocina."

**Fallo (v0.4):** el agente seguía adelante y generaba un avatar "persona de 25 a 55 años interesada en la cocina". Todos los puntos eran genéricos e inútiles.

**Cambio:**
- Antes de A1, comprobar que la frase base tiene **quién concreto** y **resultado concreto**.
- Si falta alguno, proponer 3 nichos concretos y distintos a partir de lo que ha dicho el usuario, y pedir que elija o corrija.
- Si el usuario no sabe ni qué ofrece, recomendar la fase de descubrimiento de idea antes que este agente.

**Comprobación:** el agente propone "madres que trabajan y quieren cocinar la semana en 2 horas el domingo", "personas con celiaquía que quieren repostería que no sepa a sustituto" y "jubilados que cocinan para uno sin tirar comida". El usuario elige y el resto del trabajo es concreto.

## v0.6 · Sectores sensibles

**Caso:** "Ayudo a personas con ansiedad a dormir mejor con un programa de respiración de 49 €."

**Fallo (v0.5):** los riesgos de no actuar decían "la ansiedad sin tratar puede convertirse en depresión", que es miedo como gancho. El resultado esperado decía "dormirás 8 horas", una promesa de salud. Uno de los impulsos usaba detalles íntimos que no se deben usar para vender.

**Cambio:**
- Se consideran **sectores sensibles** salud física y mental, finanzas personales, relaciones, menores y personas en situación vulnerable.
- En ellos: nada de miedo como gancho, nada de prometer resultados de salud o dinero, `[revisar por especialista]` en toda afirmación clínica o financiera, y un recordatorio de derivar a un profesional cuando toque.
- Los impulsos y escenas íntimos sirven para entender al cliente, no para usarlos tal cual en la venta. Se marcan `[no usar en copy]`.

**Comprobación:** los riesgos pasan a "seguir con noches que empiezan con miedo a no dormir" sin escalar a diagnósticos. El resultado esperado habla de "una rutina de 10 minutos para antes de dormir" y lo que hace el programa, no lo que cura. Aparece un aviso: "Si el insomnio dura semanas o afecta a tu día, consulta con tu médico."

## v0.7 · Límites de longitud

**Caso:** consolidar el material explorado del manual de máquinas (todos los puntos con ampliaciones).

**Fallo (v0.6):** el documento final salió de unas 35 páginas, más largo que Avatar v2. Había 15 impulsos con solapes y el resumen de copy ocupaba 4 páginas.

**Cambio:**
- **Fusión obligatoria:** si dos elementos comparten deseo o miedo de fondo, se fusionan y se queda la formulación más concreta.
- **Límites:** resumen para copy de una página como máximo; top 5 de impulsos, intentos y objeciones en el resumen; máximo 10 por punto en el detalle.
- **El material completo de la exploración** se guarda en un anexo, no en el documento principal.

**Comprobación:** el documento principal queda en unas 15 páginas, con el resumen de copy en una. Los 15 impulsos se convierten en 9 tras fusionar, por ejemplo "ser respetado" con "quedar bien ante quien le aprieta".

## v0.8 · Modo evidencias

**Caso:** curso de pastelería para principiantes. El usuario pega 6 reseñas reales de alumnas.

**Fallo (v0.7):** el agente usó las reseñas como inspiración y las parafraseó ("muchas alumnas sienten que…"). Mezcló lo que decían con sus hipótesis y perdió el lenguaje literal, que era lo más valioso.

**Cambio:**
- Cuando el usuario aporte material real (reseñas, mensajes, encuestas, transcripciones), el agente **extrae** primero:
  - frases literales sin modificar, con su fuente (`[reseña 3]`);
  - temas que se repiten y en cuántas fuentes aparecen.
- Esas frases entran como `[dato]` y tienen prioridad sobre las hipótesis en todos los puntos.
- Nunca se modifica una cita literal. Se quitan nombres y datos personales antes de usarla en el documento.

**Comprobación:** aparecen frases como "pensaba que la masa quebrada era para profesionales" `[reseña 2]` y un tema repetido: miedo a "estropear los ingredientes, que son caros" (4 de 6 reseñas). Pasa a ser la objeción principal, por delante de las hipótesis.

## v0.9 · Protocolo de revisión

**Caso:** el usuario contesta "rehacer" a los impulsos ocultos, y luego "rehacer" otra vez.

**Fallo (v0.8):** la segunda propuesta repetía 3 de los 5 impulsos con otras palabras. El usuario no sabía qué había cambiado. Además, cuando escribía su propio texto para un punto, los puntos siguientes no lo tenían en cuenta.

**Cambio:**
- **Rehacer:** la primera vez, preguntar en una línea qué no encaja. Si el usuario no lo dice, proponer 3 enfoques distintos en una frase cada uno y que elija. La segunda vez, cambiar de enfoque por completo.
- **Texto propio del usuario:** entra como `[dato]`. Revisa los puntos ya aprobados que dependan de él y di cuáles cambian.

**Comprobación:** tras el primer "rehacer" el agente pregunta "¿Demasiado genérico, o no se parece a tus clientes?". Tras el segundo, ofrece tres enfoques: económico, de identidad y de relaciones. Cuando el usuario reescribe la situación actual, el agente avisa: "Esto cambia el impulso 2 y la objeción 4. ¿Los actualizo?".

## v1.0 · Formato fijo de traspaso

**Caso:** usar el bloque de traspaso del caso de yoga para escribir un Destino en otra conversación.

**Fallo (v0.9):** el traspaso era un párrafo libre. Faltaba el vocabulario del cliente, el nivel de conciencia y la transformación concreta, y el Destino salió genérico ("Lanzar tu curso de yoga online").

**Cambio:** el traspaso tiene campos fijos:

```
CLIENTE: [quién, en una frase]
ROLES: [quien paga / quien usa, si son distintos]
CLIENTE FINAL: [si vende a otros]
PUNTO DE PARTIDA: [situación en una frase]
DESTINO DESEADO: [a dónde quiere llegar, en sus palabras]
DOLOR MÁS URGENTE:
IMPULSO PRINCIPAL:
OBJECIÓN PRINCIPAL + RESPUESTA:
NIVEL DE CONCIENCIA:
VOCABULARIO SÍ: [5-10 palabras o expresiones]
VOCABULARIO NO:
RESTRICCIONES DEL NEGOCIO:
SECTOR SENSIBLE: [sí/no y qué implica]
PENDIENTES CRÍTICOS:
```

**Comprobación:** con el traspaso nuevo, el Destino sale "Grabar tu primer curso de yoga en 4 fines de semana" `[a validar]`. Usa el vocabulario de la clienta y respeta que no hay directo.

## v1.1 · Mercado e idioma

**Caso:** "Ayudo a contadores independientes en México a conseguir clientes con facturación recurrente."

**Fallo (v1.0):** el agente escribió en español de España ("autónomo", "gestoría", "vosotros") y mencionó "Hacienda" y "el IVA trimestral" en lugar del SAT y el régimen mexicano.

**Cambio:**
- En el arranque, si no queda claro, preguntar **país o mercado** del cliente.
- La variante del idioma y las referencias legales, fiscales o culturales se adaptan a ese mercado. Si el agente no está seguro de una referencia local, la marca `[revisar por especialista]`.
- El estilo por defecto (español de España) solo aplica cuando el mercado es España o no se sabe.

**Comprobación:** salen "contador", "cliente", "SAT", "declaración mensual" y "ustedes". La referencia al régimen fiscal sale marcada para revisión.

## v1.2 · Prioridades y poda

**Caso:** "Ve rápido" + programa de pérdida de peso (sector sensible) + reseñas pegadas.

**Fallo (v1.1):** el modo rápido acortó tanto los puntos que se perdieron los avisos de sector sensible. Algunas reseñas se resumieron en lugar de citarse. Las instrucciones habían crecido con reglas repetidas en varios sitios y sin orden cuando chocaban.

**Cambio:**
- **Orden de prioridades** al principio de las instrucciones: (1) seguridad y sectores sensibles, (2) fiabilidad, (3) restricciones del negocio, (4) lo que pida el usuario sobre ritmo y formato, (5) estilo.
- **Poda:** se juntan en un solo apartado las reglas que estaban repetidas (etiquetas, fechas, duraciones, citas) y se acortan las plantillas.

**Comprobación:** el modo rápido sigue entregando tres puntos por turno, pero mantiene el aviso de salud y las citas literales con su fuente. La v1.2 tiene 2.028 palabras, frente a las 1.766 de la v0.2: un 15 % más, aun con todo lo añadido de la v0.3 a la v1.1. Las versiones intermedias no se guardaron como archivos separados, así que no hay medida de cada una.

---

## Lo que queda abierto

- **Validar con personas reales.** Todas estas pruebas son simuladas. El siguiente paso útil es la prueba a ciegas con 2-3 usuarios y un caso real cada uno.
- **Medir el tiempo de una sesión completa** en modo normal y rápido.
- **Decidir el despliegue:** prompt de sistema en un proyecto de Claude, un servidor MCP propio o un GPT/asistente en otra plataforma.
