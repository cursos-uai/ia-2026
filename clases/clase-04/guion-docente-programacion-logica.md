# Guion docente - Clase 4: Programación lógica con Prolog

## Propósito de la clase

Pasar de los conceptos de la IA simbólica a una representación ejecutable. Los estudiantes construirán una base de conocimiento pequeña, harán consultas y observarán cómo Prolog encuentra soluciones mediante unificación y backtracking.

## Objetivos de aprendizaje

Al finalizar la clase, los estudiantes deberían poder:

- explicar la diferencia entre programación imperativa y declarativa;
- distinguir hechos, reglas y consultas en Prolog;
- reconocer átomos, variables, predicados, términos y aridad;
- formular consultas cerradas y consultas con variables;
- interpretar unificación, múltiples soluciones y backtracking;
- explicar el principio de mundo cerrado y sus límites;
- escribir y probar una regla recursiva sencilla;
- revisar una base de conocimiento para detectar errores y supuestos riesgosos.

## Duración y recursos

- Duración prevista: 120 minutos.
- Modalidad: explicación dialogada, demostración en vivo y trabajo en grupos.
- Recursos: computadora del docente, proyector, SWI-Prolog local o SWISH en navegador, editor de texto y plantilla de entrega.
- Conocimientos previos: hechos, reglas e inferencia de la Clase 3; nociones elementales de programación.

## Preparación docente

Antes de la clase:

1. Verificar que SWI-Prolog o SWISH funcione y permita cargar un archivo `.pl`.
2. Guardar una copia del ejemplo completo para recuperarse rápidamente de errores de escritura durante la demostración.
3. Preparar grupos de 3 o 4 integrantes.
4. Recordar que el orden de los argumentos debe declararse y mantenerse: en esta clase `progenitor(Progenitor, Hijo)`.
5. No usar información personal real en la práctica; todos los casos son ficticios.

## Secuencia de la clase

### 1. Apertura: de las reglas al programa - 10 minutos

Recuperar el cierre de la Clase 3:

> La clase pasada representamos conocimiento con hechos y reglas. Hoy vamos a hacer que esa representación pueda responder preguntas.

Mostrar el razonamiento:

```text
Hecho: humano(socrates)
Regla: si X es humano, X es mortal
Consulta: ¿Sócrates es mortal?
```

Preguntas de inicio:

- ¿Dónde está expresado el conocimiento?
- ¿Qué parte debería ejecutar una computadora?
- ¿Es necesario indicarle paso a paso cómo encontrar la respuesta?

Señal de aprendizaje: los estudiantes separan el conocimiento del procedimiento que lo consulta.

### 2. Paradigma declarativo - 10 minutos

Explicar la diferencia con un contraste breve:

- En programación imperativa describimos principalmente **cómo** realizar una tarea.
- En programación lógica declaramos **qué relaciones son verdaderas** y consultamos qué se deduce de ellas.

Aclarar que Prolog también tiene un modelo operacional: el orden de cláusulas y objetivos puede cambiar la ejecución. “Declarativo” no significa que todo programa sea automáticamente eficiente ni reversible.

Pregunta de control:

> Si dos programas contienen las mismas relaciones, ¿siempre se ejecutarán igual de rápido?

Respuesta esperada: no; el orden de búsqueda y la formulación de las reglas importan.

### 3. Hechos, predicados y aridad - 15 minutos

Escribir y cargar en vivo:

```prolog
persona(ana).
persona(bruno).
materia(inteligencia_artificial).
aprobo(ana, programacion_1).
aprobo(ana, matematica_discreta).
inscripcion_activa(ana).
```

Señalar:

- los átomos comienzan con minúscula;
- las variables comienzan con mayúscula o `_`;
- cada cláusula termina con punto;
- `aprobo/2` significa predicado `aprobo` de aridad 2;
- el significado de cada posición debe mantenerse estable.

Proponer una traducción oral: “Ana aprobó Programación 1” → `aprobo(ana, programacion_1).`

Error frecuente a mostrar y corregir:

```prolog
aprobo(Ana, programacion_1). % Ana es variable, no el átomo ana
```

### 4. Consultas, variables y mundo cerrado - 15 minutos

Ejecutar:

```prolog
?- persona(ana).
?- aprobo(ana, programacion_1).
?- aprobo(bruno, programacion_1).
?- aprobo(Quien, programacion_1).
?- aprobo(ana, Materia).
```

Pedir que anticipen cada respuesta antes de ejecutarla. Mostrar cómo `;` solicita otra solución.

Explicar el principio de mundo cerrado: si Prolog no puede demostrar una consulta a partir de la base disponible, responde `false`; eso no demuestra necesariamente que la afirmación sea falsa en el mundo real. Puede faltar información.

Pregunta clave:

> Si no figura que Bruno aprobó Programación 1, ¿podemos afirmar que la desaprobó?

Respuesta esperada: no en el dominio real; solo sabemos que la base no permite demostrar que la aprobó.

### 5. Reglas, conjunción y unificación - 15 minutos

Agregar:

```prolog
puede_cursar(X, inteligencia_artificial) :-
    aprobo(X, programacion_1),
    aprobo(X, matematica_discreta),
    inscripcion_activa(X).
```

Consultar:

```prolog
?- puede_cursar(ana, inteligencia_artificial).
?- puede_cursar(Quien, inteligencia_artificial).
```

Representar el recorrido en el pizarrón:

```text
X = ana
  ├─ aprobo(ana, programacion_1)        ✓
  ├─ aprobo(ana, matematica_discreta)   ✓
  └─ inscripcion_activa(ana)            ✓
Resultado: true
```

Definir unificación como el proceso de hacer compatibles dos términos mediante sustituciones. Evitar presentarla como una simple asignación destructiva de variables.

### 6. Backtracking y alternativas - 10 minutos

Agregar más hechos ficticios:

```prolog
aprobo(bruno, programacion_1).
aprobo(bruno, matematica_discreta).
inscripcion_activa(bruno).
```

Ejecutar `?- puede_cursar(Quien, inteligencia_artificial).` y solicitar sucesivas soluciones. Narrar cómo Prolog vuelve al último punto de elección para buscar otra combinación.

Para alternativas, preferir dos cláusulas legibles:

```prolog
puede_inscribirse(X, M) :- puede_cursar(X, M).
puede_inscribirse(X, M) :- autorizacion_excepcional(X, M).
```

Señal de aprendizaje: los estudiantes pueden explicar por qué una consulta devuelve más de una solución sin decir que Prolog “adivinó”.

### 7. Actividad grupal - 50 minutos

Realizar la actividad [Construimos y auditamos una base de conocimiento](actividad-base-conocimiento-prolog.md).

Durante el trabajo, circular con estas preguntas:

- ¿Qué significa cada argumento y en qué orden está?
- ¿La conclusión se deriva o la escribieron como hecho?
- ¿Qué ocurre cuando falta un dato?
- ¿La consulta devuelve todos los casos esperados?
- ¿Qué prueba podría refutar que la regla está bien modelada?

### 8. Recursividad y cierre - 15 minutos

Si el tiempo lo permite, presentar:

```prolog
progenitor(ana, bruno).
progenitor(bruno, clara).

ancestro(X, Y) :- progenitor(X, Y).
ancestro(X, Y) :-
    progenitor(X, Z),
    ancestro(Z, Y).
```

Consultar:

```prolog
?- ancestro(ana, clara).
?- ancestro(Quien, clara).
```

Identificar caso base y caso recursivo. Reforzar que la convención es `progenitor(Progenitor, Hijo)`.

Cierre individual, en tres minutos:

1. Escribir una diferencia entre un hecho y una regla.
2. Explicar qué significa `false` bajo mundo cerrado.
3. Predecir una solución para `ancestro(X, clara)`.

## Recorte para una clase de 90 minutos

- Mantener apertura, hechos, consultas, mundo cerrado y reglas: 40 minutos.
- Reducir la actividad a 40 minutos, omitiendo la extensión recursiva.
- Usar los últimos 10 minutos para puesta en común y salida individual.
- Retomar recursividad al inicio de la clase siguiente.

## Errores frecuentes y respuestas docentes

| Error | Intervención sugerida |
|---|---|
| Escribir variables con minúscula | Pedir que prueben dos personas distintas y observen por qué el átomo no cambia. |
| Olvidar el punto final | Leer el mensaje del intérprete y localizar dónde termina la cláusula. |
| Cambiar el orden de argumentos | Solicitar una frase en lenguaje natural que documente el predicado. |
| Confundir `false` con falsedad real | Preguntar si la base podría estar incompleta. |
| Usar `is/2` como igualdad reversible | Comparar `X is 2 + 2` con `4 is X + 2` y discutir qué debe estar instanciado. |
| Crear recursión sin caso base | Dibujar dónde debería detenerse la búsqueda. |
| Obtener una sola respuesta y detenerse | Recordar que `;` solicita la siguiente solución. |

## Evaluación formativa

Evidencias a observar:

- sintaxis válida en hechos, reglas y consultas;
- explicación verbal de una sustitución de variables;
- recuperación de múltiples soluciones;
- distinción entre “no demostrable” y “falso en el mundo”;
- uso de pruebas positivas y negativas;
- corrección de una regla después de la revisión cruzada.

## Riesgos y resguardos

- No usar datos reales de estudiantes en las bases de conocimiento.
- No presentar la elegibilidad académica ficticia como normativa real.
- Mantener supervisión humana sobre cualquier decisión institucional.
- Conservar consultas y resultados en la entrega para dar trazabilidad.
- Si se utiliza un asistente de IA, exigir que el grupo pruebe el código y explique cada cláusula; una respuesta generada no sustituye la comprensión ni la ejecución.

## Fuentes de la propuesta

- `Clase 4 - Programación Lógica.pdf`, material de la cátedra.
- `Tutorial de Prolog.pdf`, material complementario de la materia.
- Programa oficial `T12340 Inteligencia Artificial (Pons 2024).pdf`.
- Continuidad pedagógica con los materiales de la Clase 3 publicados en este repositorio.
