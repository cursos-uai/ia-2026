# Actividad práctica - Construimos y auditamos una base de conocimiento en Prolog

## Desafío

La universidad necesita un **prototipo educativo** que permita consultar qué estudiantes ficticios reúnen condiciones para cursar una materia. El prototipo no toma decisiones reales: sirve para practicar representación, inferencia, pruebas y revisión de reglas.

## Objetivos

- Modelar un dominio pequeño con hechos y reglas.
- Formular consultas cerradas y con variables.
- Observar unificación, múltiples soluciones y backtracking.
- Distinguir ausencia de evidencia de una negación real.
- Probar, explicar y mejorar una base de conocimiento.

## Organización

- Grupos de 3 o 4 integrantes.
- Duración: 50 minutos.
- Herramienta: SWI-Prolog o SWISH.
- Entrega: un archivo `grupo_N.pl` y una bitácora breve con consultas, resultados y correcciones.

## Roles

Los roles rotan después de la primera ejecución:

- **Modelador/a:** propone hechos y reglas.
- **Operador/a:** escribe y ejecuta el código.
- **Tester:** diseña casos que deberían aprobar y fallar.
- **Auditor/a:** registra supuestos, errores y cambios.

En grupos de tres, tester y auditor pueden ser la misma persona.

## Parte 1 - Construcción inicial (15 minutos)

Completen y amplíen esta base con al menos tres estudiantes ficticios:

```prolog
% Convención: aprobo(Estudiante, Materia).
aprobo(ana, programacion_1).
aprobo(ana, matematica_discreta).
inscripcion_activa(ana).

aprobo(bruno, programacion_1).

% Una persona puede cursar IA si aprobó ambas correlativas
% y tiene la inscripción activa.
puede_cursar(X, inteligencia_artificial) :-
    aprobo(X, programacion_1),
    aprobo(X, matematica_discreta),
    inscripcion_activa(X).
```

Requisitos mínimos:

1. Incluir al menos ocho hechos.
2. Lograr que una persona cumpla la regla y otra no pueda demostrarse que la cumple.
3. Agregar una segunda forma de habilitación mediante `autorizacion_excepcional/2` usando otra cláusula de `puede_inscribirse/2`.
4. Documentar con un comentario el significado y orden de los argumentos de cada predicado de aridad 2.

## Parte 2 - Laboratorio de consultas (10 minutos)

Antes de ejecutar, escriban la predicción. Luego registren el resultado real.

```prolog
?- aprobo(ana, programacion_1).
?- aprobo(bruno, matematica_discreta).
?- aprobo(Quien, programacion_1).
?- aprobo(ana, Materia).
?- puede_cursar(Quien, inteligencia_artificial).
?- puede_inscribirse(Quien, inteligencia_artificial).
```

Para cada consulta indiquen:

- si es cerrada o contiene variables;
- qué sustitución obtuvo la variable;
- si existen más soluciones y cómo las solicitaron;
- si `false` significa “falso en la realidad” o “no demostrable con esta base”.

## Parte 3 - Pruebas y depuración (10 minutos)

Diseñen cuatro pruebas:

1. un caso positivo;
2. un caso con una correlativa faltante;
3. un caso sin inscripción activa;
4. un caso con autorización excepcional.

Completen la tabla en la bitácora:

| Consulta | Resultado esperado | Resultado real | Explicación |
|---|---|---|---|
|  |  |  |  |

Si una prueba no coincide con lo esperado, corrijan la base y documenten:

```text
Problema observado → cambio realizado → nueva evidencia
```

## Parte 4 - Auditoría cruzada (10 minutos)

Intercambien el archivo con otro grupo. Sin modificarlo todavía, el grupo revisor debe:

1. ejecutar dos consultas existentes;
2. proponer una consulta adversarial o un caso límite;
3. detectar un supuesto no declarado;
4. revisar si el orden de los argumentos es consistente;
5. identificar una interpretación incorrecta del mundo cerrado, si la hubiera.

El grupo autor recupera el archivo y realiza al menos una mejora justificada.

## Parte 5 - Extensión y cierre (5 minutos)

Si terminaron, agreguen una relación recursiva con datos completamente ficticios:

```prolog
progenitor(ana, bruno).
progenitor(bruno, clara).

ancestro(X, Y) :- progenitor(X, Y).
ancestro(X, Y) :-
    progenitor(X, Z),
    ancestro(Z, Y).
```

Prueben `ancestro(ana, clara)` y `ancestro(Quien, clara)`. Marquen el caso base y el caso recursivo.

## Entregables

1. Archivo `.pl` ejecutable y comentado.
2. Bitácora con las seis consultas obligatorias y sus resultados.
3. Tabla de cuatro pruebas.
4. Hallazgo de la auditoría cruzada.
5. Regla o hecho corregido, con justificación.
6. Explicación individual, en no más de cinco líneas: “¿Por qué `false` no siempre significa que algo sea falso en el mundo real?”.

## Criterios de evaluación

| Criterio | Logrado | En proceso | A revisar |
|---|---|---|---|
| Modelado | Hechos, predicados y argumentos son consistentes | Hay ambigüedades menores | Las relaciones cambian de significado |
| Reglas | La conclusión se deriva de condiciones claras | Falta una condición o alternativa | La conclusión fue cargada como hecho o no se deriva |
| Consultas | Usa individuos y variables e identifica soluciones múltiples | Ejecuta, pero explica parcialmente | No interpreta sustituciones ni resultados |
| Mundo cerrado | Distingue no demostrable de falso en la realidad | Reconoce la diferencia con ayuda | Interpreta `false` como negación real automática |
| Pruebas | Incluye casos positivos, negativos y excepcionales | Las pruebas cubren pocos caminos | No contrasta resultados esperados y reales |
| Revisión | Incorpora una mejora con evidencia | Cambia sin justificar claramente | No revisa el modelo |
| Trazabilidad | Entrega consultas, resultados y cambios | Falta parte del registro | Solo entrega código final |

## Uso responsable de asistentes de IA

Pueden pedir a un asistente que sugiera consultas de prueba o explique un error del intérprete. El grupo sigue siendo responsable de:

- no compartir datos personales;
- ejecutar cada sugerencia;
- verificar el resultado;
- poder explicar cada hecho y regla;
- registrar qué sugerencia aceptó, modificó o rechazó.

El código generado que no pueda ser explicado y probado por el grupo no se considera evidencia de aprendizaje.
