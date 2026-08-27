# Actividad - Construir y auditar una base de conocimiento en Prolog

## Propósito

Modelar un dominio académico mediante hechos y reglas, formular consultas, interpretar las respuestas de Prolog y detectar límites del modelo.

## Modalidad y duración

- Grupos de 3 o 4 estudiantes.
- 45 minutos.
- Un equipo con SWI-Prolog o un entorno Prolog por grupo.
- Entrega: archivo `grupo_N.pl` y respuestas breves a la auditoría.

## Situación

La universidad necesita un prototipo que responda consultas sobre cursadas y condiciones para rendir. El sistema es solamente didáctico: orienta y explica, pero no reemplaza la verificación administrativa.

## Parte A - Cargar hechos (8 minutos)

Crear un archivo y representar, como mínimo:

- cuatro estudiantes;
- tres materias;
- qué materias cursa cada estudiante;
- quién regularizó cada materia;
- quién aprobó los trabajos prácticos;
- dos correlatividades entre materias.

Pueden comenzar con:

```prolog
estudiante(ana).
estudiante(bruno).
estudiante(carla).
estudiante(diego).

materia(inteligencia_artificial).
materia(programacion_2).
materia(matematica_discreta).

cursa(ana, inteligencia_artificial).
cursa(bruno, inteligencia_artificial).
cursa(carla, programacion_2).

regularizo(ana, inteligencia_artificial).
aprobo_tp(ana, inteligencia_artificial).

correlativa(inteligencia_artificial, programacion_2).
correlativa(inteligencia_artificial, matematica_discreta).
```

Adoptar y documentar esta convención:

```text
correlativa(Materia, Requisito)
```

## Parte B - Escribir reglas (10 minutos)

Agregar estas reglas y al menos una regla propia:

```prolog
puede_rendir(Estudiante, Materia) :-
    regularizo(Estudiante, Materia),
    aprobo_tp(Estudiante, Materia).

companeros(A, B, Materia) :-
    cursa(A, Materia),
    cursa(B, Materia),
    A \= B.

requisito_directo(Materia, Requisito) :-
    correlativa(Materia, Requisito).
```

Explicar con palabras qué significa cada argumento y por qué `A \= B` es necesario en `companeros/3`.

## Parte C - Consultar y registrar resultados (10 minutos)

Ejecutar y copiar las respuestas:

```prolog
?- puede_rendir(ana, inteligencia_artificial).

?- puede_rendir(Quien, inteligencia_artificial).

?- cursa(Quien, Materia).

?- companeros(A, B, inteligencia_artificial).

?- correlativa(inteligencia_artificial, Requisito).
```

Para cada consulta indicar:

1. si es cerrada o contiene variables;
2. qué variables se ligaron;
3. si existen más soluciones y cómo se solicitaron;
4. qué hechos y reglas justifican una respuesta.

## Parte D - Prueba adversarial y mundo cerrado (8 minutos)

Crear tres consultas:

1. una que responda `true`;
2. una que responda `false` porque contradice los hechos disponibles;
3. una que responda `false` solamente porque falta información.

Responder:

- ¿Prolog distingue automáticamente los dos motivos de `false`?
- ¿Qué riesgo tendría interpretar “no demostrado” como “falso” en un sistema académico real?
- ¿Qué dato debería validar una persona antes de tomar una decisión?

## Parte E - Desafío recursivo opcional (5 minutos)

Representar correlatividades directas e indirectas:

```prolog
requiere(Materia, Requisito) :-
    correlativa(Materia, Requisito).

requiere(Materia, Requisito) :-
    correlativa(Materia, Intermedia),
    requiere(Intermedia, Requisito).
```

Agregar hechos que formen una cadena de al menos tres materias y consultar:

```prolog
?- requiere(Materia, Requisito).
```

Identificar el caso base y el caso recursivo. Evitar ciclos como `correlativa(a, b)` y `correlativa(b, a)`, porque esta versión simple puede no terminar.

## Parte F - Cierre (4 minutos)

Cada grupo comparte:

- una consulta con múltiples soluciones;
- una respuesta que pueda explicarse paso a paso;
- un límite o riesgo del modelo;
- una regla que mejoraría antes de usar el sistema.

## Entregable

El grupo entrega:

1. el archivo `.pl` ejecutable;
2. las cinco consultas de la Parte C con sus resultados;
3. las tres consultas adversariales de la Parte D;
4. una explicación de una inferencia;
5. un límite del modelo y una propuesta de mejora.

## Criterios de evaluación

| Criterio | Logrado | En proceso | A revisar |
|---|---|---|---|
| Sintaxis | Hechos, reglas y consultas son válidos | Presenta errores menores | No puede ejecutar la base |
| Modelado | Predicados y argumentos mantienen convenciones claras | Alguna relación es ambigua | Invierte o mezcla argumentos |
| Inferencia | Las conclusiones se derivan y explican | La explicación omite un paso | Confunde hechos con conclusiones |
| Variables y soluciones | Interpreta ligaduras y obtiene alternativas | Encuentra solo la primera solución | Confunde variables con átomos |
| Auditoría | Distingue falta de conocimiento y límite institucional | Identifica un riesgo superficial | Interpreta todo `false` como falsedad real |
| Recursividad opcional | Explica caso base y recursivo | La regla funciona parcialmente | No termina o invierte la relación |

## Solución mínima orientativa para el docente

Con los hechos iniciales, solamente Ana puede demostrar `puede_rendir/2`. Bruno cursa la materia, pero no hay hechos que permitan demostrar que regularizó y aprobó los trabajos prácticos. Esto no prueba que no lo haya hecho: bajo mundo cerrado, la base simplemente no puede demostrarlo.

En `companeros/3`, la condición `A \= B` evita considerar que una persona sea compañera de sí misma. Si aparecen pares duplicados en orden inverso, el grupo puede discutir cómo imponer un orden o aceptar que la relación es simétrica.

La regla recursiva `requiere/2` necesita una base sin ciclos o un mecanismo adicional para registrar nodos visitados. Este límite es útil para mostrar que una definición declarativa clara no garantiza por sí sola terminación eficiente.
