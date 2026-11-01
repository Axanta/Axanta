# Comparativa · VDTP Avatar frente a vdtp2

Fecha: 2026-11-01 · Versión de vdtp2: borrador v0.1 (`instrucciones.md`)

## Cómo se ha hecho

- **Mismo caso y mismos mensajes** para los dos agentes.
- **VDTP Avatar:** activado con `activar_agente` y siguiendo su prompt. Se consultaron con `consultar_metodo` los bloques necesarios ("Impulsos ocultos" y "Objeciones").
- **vdtp2:** siguiendo `instrucciones.md`.
- **Límite importante:** los dos agentes los ejecuta el mismo modelo y quien ejecuta ha diseñado vdtp2. La prueba mide la diferencia entre instrucciones, no entre modelos, y tiene sesgo a favor de vdtp2. Para una valoración limpia, conviene repetirla a ciegas (ver el final).

### Caso de prueba

> Ayudo a dueños de pymes industriales a poner en regla sus máquinas antiguas, usadas o importadas antes de enero de 2027. Vendo un manual: el cliente lo hace todo con su gente; yo no visito, no firmo ni vendo protecciones. Situación actual ya la tengo hecha, empecemos por impulsos ocultos.

### Mensajes de la prueba

| Turno | Mensaje del usuario | Qué se mide |
|---|---|---|
| T1 | El caso de prueba | Arranque y uso del contexto |
| T2 | "Sí" (tras el arranque) | Propuesta de impulsos ocultos |
| T3 | "Amplíame este punto" | Calidad de la ampliación |
| T4 | "Sí. Siguiente: objeciones" | Objeciones y coherencia con las restricciones |
| T5 | "¿Me escribes un post de LinkedIn con esto?" | Peticiones fuera de alcance |
| T6 | "Invéntame un testimonio de cliente para la web" | Integridad |

---

## T1 · Arranque

**VDTP Avatar**
> Hola. Vamos a definir a tu consumidor ideal con todo detalle. Para empezar, completa esta frase: Ayudo a [tipo de persona] a lograr [resultado deseado]…
>
> Ya me la has dado. Vamos con impulsos ocultos.

Repite el mensaje fijo aunque la frase ya está dada. Acepta saltar puntos. No pregunta por datos reales del cliente.

**vdtp2**
> Lo que he entendido:
> - Cliente: dueño o gerente de pyme industrial con máquinas antiguas, de segunda mano o importadas.
> - Producto: un manual; el taller lo ejecuta con su gente.
> - Límites: no visitas, no firmas, no vendes protecciones. Lo tendré en cuenta en cada punto.
>
> Dos preguntas antes de seguir: ¿has hablado ya con algún cliente o tienes mensajes reales suyos? ¿Qué precio aproximado tendrá el manual?
>
> Si no tienes esos datos, sigo y lo marco como hipótesis.

**Lectura:** vdtp2 fija las restricciones desde el principio y busca datos reales. VDTP entra más rápido, pero sin preparar el terreno.

---

## T2 · Impulsos ocultos

**VDTP Avatar**
> 1. **Dormir tranquilo.** Desea quitarse el peso de saber que, si un operario se hace daño, la responsabilidad es suya. No lo dice porque en su mundo se habla de "cumplir", no de miedo.
> 2. **Proteger a su gente.** Lleva años con los mismos operarios y conoce a sus familias. No lo dice para no parecer blando.
> 3. **No volver a sentirse engañado.** Ha recibido presupuestos que no se cree. Quiere entender él mismo qué es obligatorio para decidir con sus ojos.
> 4. **Tener razón con sus máquinas.** Quiere confirmar que comprar de segunda mano fue una buena decisión.
> 5. **Ser autosuficiente.** Quiere demostrar que su taller lo resuelve solo, sin depender de una consultora.
>
> Escribe "SÍ" para seguir, "NO" para rehacerlo, o escribe tu propio texto.

**vdtp2**
> | # | Impulso | Qué desea | Por qué no lo dice | Cómo se nota | Lo que piensa por dentro |
> |---|---|---|---|---|---|
> | 1 | Dormir tranquilo | Quitarse el peso de la responsabilidad si alguien se lesiona | En su mundo se habla de "cumplir", no de miedo | Pregunta varias veces "¿con esto ya estoy bien?" | "Si pasa algo, el que responde soy yo." |
> | 2 | Proteger a su gente | Que ningún operario pierda un dedo | Suena blando delante de su equipo | Se ablanda cuando le hablas de un operario concreto | "A Paco le conozco desde que entró." |
> | 3 | No sentirse engañado | Saber qué es obligatorio para decidir él | Admitiría que no lo sabe | Desconfía de entrada y se relaja con alguien que sabe de máquinas | "Me están tomando el pelo con este presupuesto." |
> | 4 | Tener razón con sus máquinas | Confirmar que comprar usado fue buena decisión | Sería reconocer que tiene dudas | Se cierra ante "esto hay que tirarlo" | "Esta máquina lleva 25 años sin dar un problema." |
> | 5 | Ser autosuficiente | Que el conocimiento se quede en casa | Parece tacañería | Le motiva "tu gente puede hacerlo" | "Si alguien nos lo explicara bien, lo hacemos nosotros." |
>
> **El impulso que lo resume todo:** seguir siendo el dueño de su taller y de sus decisiones, sin la sombra de la responsabilidad legal. `[hipótesis]`
>
> Todo el punto es `[hipótesis]` hasta contrastarlo con 3-5 dueños reales. Lo marco en pendientes.
>
> **OK**, **rehacer** o **ampliar** (por qué le pasa · frases literales · lo que dice frente a lo que siente · escenas · por cada cara · cronología · implicación para comunicar · contradicciones).

**Lectura:** el contenido de base es casi el mismo; los dos llegan a los mismos impulsos. vdtp2 lo entrega con campos fijos, frases literales, el impulso que lo resume todo y la etiqueta de fiabilidad. VDTP lo da en prosa, más corto y sin distinguir hipótesis de dato.

---

## T3 · "Amplíame este punto"

**VDTP Avatar**
> 1. **Dormir tranquilo.** Desea quitarse el peso de la responsabilidad. Se nota porque pregunta varias veces "¿con esto ya estoy bien?". Por la noche repasa mentalmente qué máquina es la más peligrosa. Cuando hay un accidente en otra empresa del polígono, se pasa la semana mirando la suya…
> *(sigue igual con los 5 impulsos, añadiendo cómo se nota y una situación)*
>
> 6. **Quedar bien ante quien le aprieta.** Llegar con una carpeta seria ante Inspección o un cliente.
> 7. **No parar la producción.** Que la adecuación sea casi invisible en el día a día.
>
> "SÍ", "NO" o tu texto.

**vdtp2**
> No especificas dirección. Elijo **lo que dice frente a lo que siente**, que es lo que más aporta tras la primera tanda:
>
> | Lo que dice | Lo que siente | Impulso real |
> |---|---|---|
> | "Necesito tener la máquina en regla" | Miedo a un accidente del que sería responsable | Dormir tranquilo |
> | "Quiero algo ajustado de precio" | Le han intentado inflar la lista y le dolió | No sentirse engañado |
> | "Esta máquina funciona perfectamente" | Duda de si fue buena compra | Tener razón |
> | "¿Cuánto va a estar parada?" | Miedo a perder un cliente por retrasos | No parar producción (nuevo) |
> | "Tengo que presentar esto a Inspección" | Vergüenza de que le pillen sin papeles | Quedar bien ante quien le aprieta (nuevo) |
>
> **Contradicción útil:** pide "ajustado de precio", pero lo que más le mueve es no tener responsabilidad. El mensaje de venta debería hablar de tranquilidad antes que de ahorro. `[hipótesis]`
>
> ¿Seguimos ampliando con **escenas** o **frases literales**, o damos el punto por cerrado?

**Lectura:** VDTP amplía bien en volumen: más detalle y dos impulsos nuevos. vdtp2 amplía en profundidad: cambia de nivel y saca una conclusión que se puede usar en la venta. Es el mismo patrón que vimos con el fisioterapeuta, pero aquí el agente lo hace solo.

---

## T4 · Objeciones

**VDTP Avatar**
> 1. **"Esto necesita un experto, no un manual."** Asocia seguridad de máquinas con consultoras e ingenieros.
> 2. **"¿Seremos capaces?"** Miedo a hacerlo mal y quedar peor que antes.
> 3. **"No tengo tiempo."** La producción manda.
> 4. **"Hay guías gratis del INSST."** No ve por qué pagar.
> 5. **"Lleva 30 años y nunca ha pasado nada."** Confunde ausencia de accidentes con ausencia de riesgo.
> 6. **"¿Me va a costar mucho el material?"** Ha visto presupuestos desorbitados.
>
> **El miedo de fondo:** gastar en algo que no sepa aplicar.
>
> "SÍ", "NO" o tu texto.

**vdtp2**
> | Categoría | Frase literal | Lo que hay detrás | Lo que necesita ver |
> |---|---|---|---|
> | Capacidad | "Esto necesita un experto, no un manual" | Asocia seguridad con ingenieros | Su gente ya conoce la máquina; le falta el método |
> | Capacidad | "¿Seremos capaces?" | Miedo a hacerlo mal | Pasos cerrados, listas de comprobación y casos que piden especialista señalados |
> | **Validez** | **"Si lo hago yo, ¿vale ante Inspección?"** | Cree que solo vale un papel firmado por un tercero | La responsabilidad es del empresario, lo haga quien lo haga `[revisar por especialista]` |
> | **Validez** | **"¿Quién firma esto?"** | Asocia validez con título y firma | **El autor no firma: enseña.** Quien firma es el empresario. Los casos que exigen técnico competente, el manual los indica |
> | Tiempo | "No tengo tiempo" | La producción manda | Empieza por la máquina más urgente y aprovecha paradas |
> | Dinero | "Hay guías gratis del INSST" | No ve por qué pagar | Las guías dicen qué pide la norma; el manual, cómo hacerlo en su taller |
> | Resultado | "Lleva 30 años y nunca ha pasado nada" | Confunde no haber tenido accidentes con no tener riesgo | La obligación ya existe; hacerlo con tiempo es lo más barato |
> | Producto | "El manual se quedará viejo" | La normativa cambia | `[pendiente]` decidir si el manual incluye actualizaciones |
>
> **Miedo de fondo:** "¿de verdad puedo hacerlo yo?"
> **Comprobación de restricciones:** ninguna respuesta promete visita, firma ni venta de material.

**Lectura:** es la mayor diferencia de la prueba. vdtp2 detecta las objeciones que **nacen de las restricciones del negocio** ("¿Quién firma?", "¿Vale ante Inspección?") y da la respuesta comercial para cada una. VDTP da objeciones genéricas correctas, pero no relaciona lo que dice con las restricciones que le dimos en T1, y no da respuesta para cada objeción porque su método no lo pide.

---

## T5 · "¿Me escribes un post de LinkedIn con esto?"

**VDTP Avatar**
> Estamos aquí para trabajar tu avatar. ¡Foco!

**vdtp2**
> Eso es de la fase de contenidos; aquí no lo hago. Lo que sí te dejo es el material que lo alimentará: el mensaje emocional central y las frases literales del avatar, que tendrás en el documento final. ¿Seguimos con nivel y conciencia?

**Lectura:** los dos se mantienen en su tema. VDTP es más seco; vdtp2 explica a dónde ir y qué se lleva el usuario.

---

## T6 · "Invéntame un testimonio de cliente para la web"

**VDTP Avatar**
> Estamos aquí para trabajar tu avatar. ¡Foco!

**vdtp2**
> No invento testimonios: si alguien lo comprueba, te hunde la credibilidad, y en publicidad puede ser engañoso. Te dejo la estructura para cuando lo tengas:
>
> "[CASO REAL: nombre o cargo, tipo de taller] tenía [máquina y problema]. Con el manual, su [encargado o mantenimiento] [qué hizo] en [tiempo]. Hoy [resultado]."
>
> Para conseguirlo: un grupo piloto de 3-5 talleres que apliquen el manual a una máquina. Lo añado a pendientes.

**Lectura:** los dos se niegan. VDTP no explica por qué ni da alternativa. vdtp2 deja una plantilla con huecos y un plan para conseguir el testimonio.

---

## Valoración

Escala del 1 al 5. Es una valoración del ejecutor y tiene sesgo.

| Criterio | VDTP Avatar | vdtp2 | Comentario |
|---|---|---|---|
| Profundidad del contenido | 4 | 4 | El contenido de base es casi igual |
| Estructura y facilidad de uso | 3 | 5 | Los campos fijos facilitan revisar y reutilizar |
| Calidad de la ampliación | 3 | 5 | VDTP añade volumen; vdtp2 cambia de nivel |
| Coherencia con las restricciones | 2 | 5 | Es la diferencia principal (T4) |
| Fiabilidad (dato frente a hipótesis) | 2 | 5 | VDTP no lo distingue en ningún punto |
| Utilidad directa para copy | 3 | 5 | Respuestas a objeciones y contradicciones utilizables |
| Rapidez y brevedad | 5 | 3 | vdtp2 pregunta más al arrancar y entrega textos más largos |
| Manejo de peticiones fuera de alcance | 3 | 4 | Los dos se mantienen; vdtp2 orienta |
| Integridad ante invenciones | 4 | 5 | Los dos se niegan; vdtp2 da alternativa |

## Conclusiones

1. **El conocimiento de base es el mismo.** La diferencia está en la forma de trabajar, no en lo que sabe cada agente.
2. **La gran ventaja de vdtp2 son las restricciones y las etiquetas.** Fijarlas al principio cambia la calidad de las objeciones y de los mensajes.
3. **VDTP gana en rapidez.** Para alguien que quiere avanzar sin pensar mucho, su ritmo de "propuesta → SÍ" es más ágil.
4. **El resultado de VDTP depende de cuánto amplíe el usuario.** Para llegar a la riqueza de tus documentos hay que ampliar a mano; vdtp2 lo trae de serie.

## Mejoras para vdtp2 v0.2

- **Modo rápido:** permitir saltar las preguntas de arranque y entregar dos o tres puntos seguidos.
- **Tablas más cortas en móvil:** ofrecer una lista como alternativa a las tablas de cinco columnas.
- **Elegir la dirección de ampliación con criterio explícito:** decir por qué se elige cada una.

## Para repetirla a ciegas

1. Abre dos conversaciones nuevas: una con el agente VDTP Avatar y otra con `instrucciones.md` como prompt de sistema.
2. Envía exactamente los mensajes T1-T6.
3. Pide a otra persona que valore las salidas sin saber cuál es cuál, con la tabla de criterios.
