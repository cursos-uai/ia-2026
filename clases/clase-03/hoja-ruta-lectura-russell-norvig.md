# Mapeo de temas: Clase 3 vs. Russell y Norvig (AIMA)

Libro: Stuart Russell y Peter Norvig, *Artificial Intelligence: A Modern Approach*, 4.ª edición global.

## Propósito

Esta guía acompaña la lectura vinculada con la Clase 3. No busca recorrer capítulos completos: selecciona tres tramos para comprender:

- por qué los símbolos y el conocimiento explícito ocuparon un lugar central en la historia de la IA;
- por qué los sistemas expertos necesitaron conocimiento específico del dominio;
- cómo funciona conceptualmente un agente basado en conocimiento;
- qué ventajas y límites tiene representar conocimiento mediante reglas.

Tiempo estimado total: 55 a 70 minutos.

> La paginación corresponde a la 4.ª edición global disponible como bibliografía de la materia. Si utilizás otra edición, buscá las secciones por su título en inglés.

## Mapa de correspondencias

La numeración de capítulos cambia entre ediciones y traducciones. Por eso, además del número orientativo, usá el título o el concepto indicado para localizar la lectura.

### 1. Hipótesis del sistema de símbolos físicos

**En la Clase 3:** el razonamiento simbólico se presenta como la capacidad de operar con representaciones abstractas. La computadora no manipula directamente objetos del mundo: transforma estructuras físicas que funcionan como símbolos.

**En AIMA:**

- capítulo 1, apartado histórico sobre los primeros años de la IA (*Early enthusiasm, great expectations*): Newell y Simon y la hipótesis del sistema físico de símbolos;
- capítulo 7, sección sobre agentes basados en conocimiento (*Knowledge-Based Agents*): uso de oraciones representadas y almacenadas para inferir y actuar.

**Pregunta guía:** ¿que un sistema manipule símbolos alcanza para afirmar que comprende aquello que los símbolos representan?

### 2. Modelo simbólico: lógica y búsqueda heurística

**En la Clase 3:** la IA simbólica aparece como un enfoque *top-down*: se definen conceptos, relaciones y reglas explícitas. Dos herramientas centrales son el razonamiento lógico y la búsqueda heurística.

**En AIMA:**

- capítulo 1, sección sobre pensar racionalmente (*Thinking Rationally*): tradición de las leyes del pensamiento y formalización lógica;
- capítulos dedicados a resolución de problemas mediante búsqueda: espacio de estados, búsqueda informada y heurísticas;
- capítulos sobre agentes lógicos y lógica de primer orden: representación formal de hechos, relaciones y reglas.

**Pregunta guía:** ¿qué parte del conocimiento aporta la persona que modela el problema y qué parte obtiene el sistema mediante búsqueda o inferencia?

### 3. Lenguaje natural: símbolos, referencia y significado

**En la Clase 3:** palabras como “manzana” muestran que un mismo símbolo puede tener diferentes referentes y significados según el contexto.

**En AIMA:**

- capítulo de lógica de primer orden, introducción al lenguaje de representación: objetos, propiedades, relaciones y funciones;
- capítulos de procesamiento del lenguaje natural: estructura sintáctica, interpretación y construcción de representaciones;
- discusión sobre la diferencia entre operar con expresiones formales y comprender su significado en contexto.

**Pregunta guía:** ¿qué se pierde cuando una expresión ambigua del lenguaje cotidiano se convierte en una representación formal?

### 4. Sistemas expertos y transición hacia “smart data”

**En la Clase 3:** un sistema experto intenta reproducir parte del razonamiento de una persona especialista en un dominio acotado. Su desempeño depende menos de acumular datos indiscriminadamente que de disponer de conocimiento relevante y bien estructurado.

**En AIMA:**

- capítulo 1, sección *Expert systems*: paso de métodos generales o “débiles” a sistemas intensivos en conocimiento;
- capítulo sobre aprendizaje con conocimiento: el conocimiento previo puede restringir el espacio de hipótesis y reducir los ejemplos necesarios.

> “Smart data” es el término usado en la clase para destacar calidad y pertinencia. AIMA desarrolla las ideas relacionadas mediante conocimiento específico del dominio y conocimiento previo; no necesariamente utiliza esa misma etiqueta.

**Pregunta guía:** ¿por qué una pequeña cantidad de conocimiento pertinente puede resultar más útil que una gran cantidad de datos sin estructura?

### 5. Caso de estudio: MYCIN

**En la Clase 3:** MYCIN se analiza como un sistema experto médico desarrollado en Stanford durante la década de 1970, con cientos de reglas y un mecanismo heurístico para expresar incertidumbre.

**En AIMA:**

- capítulo 1, sección *Expert systems*: MYCIN como sistema basado en conocimiento específico para diagnosticar infecciones de la sangre y recomendar tratamientos;
- capítulo sobre razonamiento probabilístico e incertidumbre, notas históricas: factores de certeza de MYCIN.

La cifra varía según el recorte de reglas y la fuente: AIMA menciona aproximadamente 450 reglas; en clase se redondea a unas 500. Sus factores de certeza no deben confundirse con probabilidades clínicas calibradas.

**Pregunta guía:** ¿qué permite auditar una regla explícita de MYCIN y qué aspectos médicos siguen requiriendo validación humana?

### 6. Límites del modelo simbólico y filosofía de la IA

**En la Clase 3:** se discuten la rigidez frente a excepciones, la dificultad de tratar conocimiento incierto y los límites de equiparar manipulación de símbolos con comprensión. También se problematizan la AGI y la singularidad.

**En AIMA:**

- capítulo sobre filosofía, ética y seguridad de la IA: límites de los sistemas, objeción de la habitación china y debate sobre si una máquina puede pensar;
- capítulo final sobre el futuro de la IA: dificultades técnicas y conceptuales para construir sistemas de propósito general y sistemas beneficiosos.

En la 4.ª edición global estos temas aparecen hacia los capítulos 27 y 28; otras ediciones pueden numerarlos de otra manera.

**Pregunta guía:** ¿la ejecución correcta de reglas sintácticas constituye evidencia suficiente de comprensión semántica? Justificá.

## Antes de leer - Activación (5 minutos)

Escribí una respuesta inicial de no más de tres líneas para cada pregunta:

1. ¿En qué se diferencia una base de conocimiento de una base de datos?
2. ¿Que un sistema pueda explicar una conclusión garantiza que sea correcta?
3. ¿Qué tendría que saber un sistema para actuar como especialista en un dominio?

No consultes el libro todavía. Al terminar la lectura, volverás sobre estas respuestas.

## Tramo 1 - Símbolos y primeras expectativas (10 a 15 minutos)

### Lectura

Capítulo 1, sección 1.3.2, **“Early enthusiasm, great expectations”**, páginas 37-38.

### Buscá estas ideas

- la hipótesis del sistema físico de símbolos;
- el intento de construir solucionadores generales de problemas;
- el *Advice Taker* y la idea de incorporar conocimiento declarativo;
- las expectativas iniciales sobre el alcance de los métodos simbólicos.

### Mientras leés

Completá esta tabla con una frase por celda:

| Idea | ¿Qué prometía? | ¿Qué pregunta te genera? |
|---|---|---|
| Sistema físico de símbolos |  |  |
| Solucionador general |  |  |
| *Advice Taker* |  |  |

### Pausa de comprensión

Explicá con tus palabras por qué “manipular símbolos” no significa manipular directamente los objetos del mundo real.

## Tramo 2 - Del método general al conocimiento experto (15 a 20 minutos)

### Lectura

Capítulo 1, sección 1.3.4, **“Expert systems”**, páginas 40-42.

### Buscá estas ideas

- por qué el conocimiento específico del dominio ganó importancia;
- DENDRAL como antecedente de los sistemas expertos;
- MYCIN como sistema basado en reglas para un dominio médico acotado;
- el papel de la ingeniería de conocimiento;
- las dificultades para adquirir, mantener y ampliar bases de reglas.

### Mientras leés

Registrá un ejemplo para cada categoría:

| Categoría | Ejemplo tomado de la lectura |
|---|---|
| Conocimiento específico del dominio |  |
| Regla o forma de inferencia |  |
| Resultado valioso |  |
| Límite de escalabilidad o mantenimiento |  |

### Pausa de comprensión

Respondé:

> ¿Por qué agregar más reglas no resuelve necesariamente todos los límites de un sistema experto?

Incluí al menos dos razones.

## Tramo 3 - Agentes basados en conocimiento (20 minutos)

### Lectura

Capítulo 7, sección 7.1, **“Knowledge-Based Agents”**, páginas 227-228.

### Buscá estas ideas

- qué contiene una base de conocimiento;
- qué función cumplen las oraciones o afirmaciones representadas;
- qué hacen las operaciones `TELL` y `ASK`;
- cómo se relacionan percepción, inferencia y acción;
- la diferencia entre nivel de conocimiento y nivel de implementación;
- la construcción declarativa de un agente.

### Reconstruí el ciclo

Numerá estas acciones en el orden conceptual en que ocurren:

- consultar qué acción se sigue del conocimiento disponible;
- recibir una percepción;
- ejecutar una acción;
- incorporar la percepción a la base de conocimiento;
- registrar la acción realizada.

### Aplicación a un caso universitario

Imaginá un agente que orienta sobre la posibilidad de rendir un examen. Completá:

- **Percepción o dato nuevo:**
- **Conocimiento general del dominio:**
- **Ejemplo de `TELL`:**
- **Ejemplo de `ASK`:**
- **Acción sugerida:**
- **Dato que debería verificar una persona:**

## Tramo opcional - Puente hacia la Clase 4 (10 minutos)

Si querés anticipar programación lógica, leé el comienzo del capítulo 7, sección 7.3, **“Logic”**.

Identificá tres componentes:

1. **sintaxis:** qué expresiones están bien formadas;
2. **semántica:** qué significan esas expresiones;
3. **inferencia:** cómo se obtienen conclusiones.

Este tramo prepara la transición hacia hechos, reglas y consultas en Prolog.

## Después de leer - Revisión (5 minutos)

Volvé a tus respuestas iniciales y corregilas con otro color o bajo el título “Después de la lectura”. Luego redactá una síntesis de entre 80 y 120 palabras que incluya obligatoriamente:

- símbolos;
- conocimiento del dominio;
- inferencia;
- `TELL` y `ASK`;
- una fortaleza y un límite de los sistemas expertos.

## Autoevaluación de opción múltiple

Elegí una sola respuesta por pregunta. No consultes la clave hasta completar las doce.

### 1. ¿Qué caracteriza mejor al enfoque simbólico presentado en la lectura?

A. Sustituye toda representación por datos sin estructura.
B. Representa conocimiento explícito y opera sobre símbolos mediante procesos de inferencia.
C. Aprende exclusivamente por ajuste estadístico de grandes conjuntos de ejemplos.
D. Reproduce necesariamente el funcionamiento biológico del cerebro.

### 2. ¿Cuál fue una idea importante del *Advice Taker*?

A. Incorporar conocimiento declarativo que pudiera utilizarse para obtener conclusiones.
B. Entrenar redes neuronales profundas con conversaciones humanas.
C. Eliminar la representación del conocimiento del diseño de agentes.
D. Reemplazar la inferencia por una lista fija de respuestas.

### 3. ¿Qué aprendizaje histórico impulsó el desarrollo de sistemas expertos?

A. Un método completamente general siempre supera al conocimiento especializado.
B. El conocimiento específico del dominio puede ser decisivo para resolver problemas difíciles.
C. Los sistemas inteligentes no necesitan conocimiento si poseen suficiente velocidad.
D. Toda decisión experta puede reducirse a una única regla.

### 4. ¿Por qué DENDRAL y MYCIN se consideran sistemas de dominio acotado?

A. Porque solamente podían ejecutarse en una computadora a la vez.
B. Porque su conocimiento y sus reglas estaban orientados a áreas específicas.
C. Porque no utilizaban ningún procedimiento de inferencia.
D. Porque respondían al azar fuera de una lista de ejemplos memorizados.

### 5. ¿Cuál describe mejor el cuello de botella de adquisición de conocimiento?

A. La dificultad de obtener conocimiento experto, formalizarlo y mantenerlo actualizado.
B. La imposibilidad de almacenar más de una regla en una computadora.
C. La necesidad de convertir todas las reglas en imágenes.
D. La falta de un lenguaje natural común entre computadoras.

### 6. Que un sistema experto pueda mostrar las reglas aplicadas significa que:

A. todas sus recomendaciones son necesariamente correctas;
B. puede ofrecer trazabilidad, pero aún puede partir de datos o reglas defectuosos;
C. ya no necesita validación ni supervisión humana;
D. puede actuar correctamente en cualquier dominio.

### 7. En un agente basado en conocimiento, ¿qué contiene principalmente la base de conocimiento?

A. Solamente registros de acciones pasadas sin significado.
B. Afirmaciones representadas acerca del mundo y del dominio.
C. Únicamente el código fuente del motor de inferencia.
D. Una copia completa del entorno real.

### 8. ¿Qué operación se asocia con incorporar información a la base de conocimiento?

A. `ASK`
B. `TELL`
C. `UNDO`
D. `SEARCH`

### 9. ¿Qué operación se utiliza para consultar qué se sigue del conocimiento disponible?

A. `TELL`
B. `STORE`
C. `ASK`
D. `TRAIN`

### 10. ¿Qué expresa la diferencia entre nivel de conocimiento y nivel de implementación?

A. El primero describe qué sabe el agente; el segundo, cómo está representado y procesado.
B. El primero corresponde al hardware; el segundo, a los objetivos del agente.
C. Ambos niveles son exactamente lo mismo.
D. El nivel de implementación determina por sí solo si el conocimiento es verdadero.

### 11. ¿Qué enfoque construye un agente agregando afirmaciones sobre el dominio y permitiendo que infiera cómo actuar?

A. Exclusivamente procedimental.
B. Declarativo.
C. Puramente aleatorio.
D. Exclusivamente perceptivo.

### 12. Un sistema no logra demostrar que un estudiante puede rendir porque falta registrar una equivalencia. ¿Cuál es la interpretación más adecuada?

A. El estudiante definitivamente no puede rendir.
B. El motor de inferencia debería inventar la equivalencia faltante.
C. La conclusión depende del conocimiento disponible y requiere verificar la información ausente.
D. Todo sistema simbólico debe reemplazarse inmediatamente por aprendizaje automático.

## Criterio de autoevaluación

- **10 a 12 respuestas correctas:** comprensión sólida; justificá oralmente dos respuestas elegidas al azar.
- **7 a 9:** comprensión general; releé los tramos asociados con las respuestas incorrectas.
- **0 a 6:** releé los tres tramos y reconstruí el ciclo `TELL`–`ASK` con un ejemplo propio.

La validación no termina en elegir una opción: el docente puede solicitar que justifiques una respuesta citando la idea o el ejemplo del tramo correspondiente.

## Entrega sugerida

Entregar:

1. la tabla del Tramo 1;
2. la tabla del Tramo 2;
3. el caso universitario del Tramo 3;
4. la síntesis final;
5. las letras elegidas en las doce preguntas.

No copies fragmentos extensos del libro. Parafraseá las ideas y anotá la sección utilizada.
