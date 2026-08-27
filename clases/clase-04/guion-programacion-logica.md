# Guion docente - Clase 4: Programación lógica con Prolog

Duración base: 120 minutos. Modalidad: presencial o sincrónica con práctica.

Material central: `Clase 4 - Programación Lógica.pdf` y `Tutorial de Prolog.pdf`.

## Resultados de aprendizaje

Al finalizar, los estudiantes podrán:

1. distinguir el paradigma lógico del imperativo;
2. modelar conocimiento mediante hechos, reglas y predicados;
3. formular consultas con individuos y variables;
4. explicar unificación, múltiples soluciones y *backtracking*;
5. reconocer los efectos del supuesto de mundo cerrado;
6. ejecutar y corregir una base de conocimiento pequeña en SWI-Prolog.

## Preparación previa

- Verificar que SWI-Prolog esté instalado o disponer de [SWISH](https://swish.swi-prolog.org/) en el navegador.
- Proyectar el archivo `actividad_base.pl`.
- Preparar una pizarra con tres columnas: `hechos`, `reglas`, `consultas`.
- Recordar la fórmula de la clase anterior:

```text
IA simbólica = representación explícita + reglas + inferencia
```

## 0-10 min - Puente desde IA simbólica

### Qué decir

“En la clase anterior diseñamos sistemas con símbolos y reglas. Hoy vamos a expresar ese conocimiento en un lenguaje ejecutable. En lugar de indicar paso a paso cómo resolver el problema, describiremos qué sabemos y qué relaciones deben cumplirse.”

Escribir:

```text
Sócrates es humano.
Todo humano es mortal.
¿Sócrates es mortal?
```

Preguntar:

- ¿Cuáles son los hechos?
- ¿Cuál es la regla?
- ¿Cuál es la consulta?
- ¿La respuesta estaba escrita o fue inferida?

Cerrar:

“Esa separación entre conocimiento y mecanismo de inferencia caracteriza al paradigma lógico.”

## 10-22 min - Paradigmas: describir qué, no cada paso

### Qué explicar

En un programa imperativo solemos escribir una secuencia de instrucciones. En programación lógica declaramos relaciones y dejamos que el motor busque valores que satisfagan las consultas.

```prolog
humano(socrates).
mortal(X) :- humano(X).
```

Leer la regla de derecha a izquierda:

> `X` es mortal si `X` es humano.

### Aclaración importante

En `mortal(X) :- humano(X).`, el cuerpo `humano(X)` es la condición y la cabeza `mortal(X)` es la conclusión. El material de diapositivas invierte esta explicación en un pasaje; corregirlo oralmente.

### Pregunta de control

“¿Prolog sabe qué significa ser humano o mortal?”

Respuesta esperada: no en un sentido general; opera con los símbolos, hechos y reglas definidos en la base de conocimiento.

## 22-38 min - Individuos, predicados, aridad y cláusulas

### Ejemplo guiado

```prolog
persona(ana).
vive(ana, rosario).
enseña(ana, inteligencia_artificial).
```

Explicar:

- `ana`, `rosario` e `inteligencia_artificial` son átomos;
- `persona/1`, `vive/2` y `enseña/2` son predicados;
- la cantidad de argumentos es la aridad;
- cada cláusula termina con punto;
- los nombres en minúscula son átomos; los que comienzan con mayúscula son variables.

### Preguntas al grupo

- ¿Qué propiedad expresa `persona/1`?
- ¿Qué relación expresa `vive/2`?
- ¿`vive(ana, rosario)` y `vive(rosario, ana)` significan lo mismo?

Idea a fijar: el orden de los argumentos forma parte del significado que el equipo definió para el predicado.

## 38-52 min - Consultas individuales y existenciales

Abrir SWI-Prolog o SWISH y consultar:

```prolog
?- persona(ana).
?- vive(ana, rosario).
?- vive(ana, cordoba).
?- vive(Quien, rosario).
?- vive(_, rosario).
```

Explicar:

- una consulta con individuos pregunta por un caso específico;
- una variable solicita valores que hagan verdadera la relación;
- `_` es una variable anónima: importa que exista un valor, pero no cuál;
- la sintaxis de la consola comienza con `?-`; el archivo `.pl` contiene hechos y reglas, no el prefijo de consulta.

### Mini desafío

Con estos hechos:

```prolog
come(juan, ravioles).
come(melina, ravioles).
come(brenda, fideos).
come(juan, fideos).
```

Pedir consultas para:

1. saber si Juan come ravioles;
2. obtener quiénes comen ravioles;
3. obtener qué come Brenda;
4. comprobar si existe alguien que coma fideos sin recuperar su nombre.

## 52-62 min - Múltiples soluciones y backtracking

Ejecutar:

```prolog
?- come(Persona, ravioles).
```

Mostrar que `;` solicita otra solución. Explicar que Prolog prueba cláusulas en orden, conserva puntos de elección y retrocede cuando una alternativa falla o cuando pedimos otra respuesta.

### Demostración breve

```prolog
p(1).
p(2).
q(2).
```

Consulta:

```prolog
?- p(X), q(X).
```

Narrar el proceso:

1. prueba `X = 1`;
2. `q(1)` falla;
3. retrocede;
4. prueba `X = 2`;
5. `q(2)` tiene éxito.

## 62-70 min - Pausa

Dejar proyectada esta pregunta:

> Si Prolog no puede probar un hecho, ¿significa que el hecho es falso en el mundo real?

## 70-82 min - Mundo cerrado y ausencia de conocimiento

Usar:

```prolog
humano(socrates).
mortal(X) :- humano(X).
```

Consultar:

```prolog
?- mortal(aristoteles).
```

Prolog responde `false` porque no puede demostrar la consulta con la base disponible. Esto corresponde operativamente al supuesto de mundo cerrado: lo no demostrable se trata como falso para la consulta.

### Debate breve

- ¿“No consta aprobado” equivale a “está desaprobado”?
- ¿Qué riesgo tendría esa confusión en un sistema universitario o médico?

Idea a fijar: fallo de prueba y falsedad en la realidad no son necesariamente lo mismo.

## 82-95 min - Reglas, conjunción y alternativas

Escribir:

```prolog
madre(nora, luis).
madre(nora, ana).
padre(juan, luis).
padre(juan, ana).

mismo_padre(P1, P2) :-
    padre(Padre, P1),
    padre(Padre, P2),
    P1 \= P2.

misma_madre(P1, P2) :-
    madre(Madre, P1),
    madre(Madre, P2),
    P1 \= P2.

hermanos(P1, P2) :-
    mismo_padre(P1, P2),
    misma_madre(P1, P2).
```

Explicar:

- la coma representa conjunción;
- varias cláusulas para el mismo predicado expresan alternativas;
- `\=` comprueba que dos términos no unifican;
- sin `P1 \= P2`, una persona podría aparecer como hermana de sí misma.

## 95-105 min - Aritmética e inversibilidad: una trampa útil

Mostrar:

```prolog
siguiente(N, Siguiente) :-
    Siguiente is N + 1.
```

Probar:

```prolog
?- siguiente(3, X).
?- siguiente(X, 4).
```

La primera consulta funciona; la segunda produce un error porque `is/2` necesita que su expresión derecha ya esté instanciada. Esto demuestra que un predicado lógico no es automáticamente inversible en todos sus argumentos.

### Correcciones de sintaxis

- mayor o igual: `>=`;
- menor o igual: `=<`;
- evaluación aritmética: `is`;
- igualdad aritmética: `=:=`;
- unificación: `=`.

No usar `=>` como operador de comparación.

## 105-115 min - Inicio de la actividad práctica

Presentar la [actividad](actividad-base-conocimiento.md) y formar grupos de 3 o 4. Cada grupo construirá una base sobre trayectos de transporte, formulará consultas y auditará un caso de mundo cerrado.

Durante el trabajo preguntar:

- “¿La conclusión está escrita como hecho o se deriva?”
- “¿Qué variable queda ligada?”
- “¿En qué orden probará Prolog las cláusulas?”
- “¿Qué consulta debería devolver más de una solución?”

La actividad continúa 25 minutos después de este primer bloque o puede ocupar un bloque práctico separado de 40 minutos.

## 115-120 min - Cierre

### Síntesis oral

“Programar en lógico significa describir individuos, relaciones y reglas para luego consultar qué se puede demostrar. Prolog busca soluciones mediante unificación y backtracking. Su potencia declarativa no elimina la necesidad de diseñar bien los predicados, entender el mundo cerrado y controlar el orden de evaluación.”

### Ticket de salida

1. Escribí un hecho, una regla y una consulta.
2. Explicá qué hace una variable en una consulta.
3. ¿Por qué `false` no siempre significa falso en el mundo real?
4. ¿Qué diferencia existe entre `=` e `is`?

### Puente

“En las próximas clases veremos cómo estos mecanismos se relacionan con búsqueda, representación de conocimiento y formas más complejas de inferencia.”

## Adaptación a 90 minutos

- Puente y paradigma: 15 min.
- Hechos, predicados y consultas: 20 min.
- Variables, soluciones y backtracking: 20 min.
- Mundo cerrado y reglas: 15 min.
- Actividad: 15 min.
- Cierre: 5 min.

Dejar aritmética y recursividad para una práctica posterior.

## Alertas docentes

- No describir las variables de Prolog como celdas cuyo valor cambia: son variables lógicas que se ligan durante una derivación.
- No afirmar que todo predicado es inversible; depende de los operadores y de cómo está definido.
- Distinguir átomos con comillas simples de cadenas con comillas dobles, cuyo tratamiento depende de la configuración.
- Mantener una convención explícita para el orden de argumentos, por ejemplo `padre(Padre, Hijo)`.
- Introducir recursividad solo si el grupo domina hechos, reglas, variables y backtracking.
- En ejemplos de parentesco, excluir reflexividad cuando corresponda.

## Fuentes

- Material de cátedra, `Clase 4 - Programación Lógica.pdf`.
- Material de cátedra, `Tutorial de Prolog.pdf`.
- SWI-Prolog, documentación del lenguaje y entorno de práctica.
