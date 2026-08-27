# Actividad en clase - De reglas académicas a un programa Prolog

## Propósito

Construir y consultar una base de conocimiento en Prolog para aplicar hechos, reglas, variables, unificación, múltiples soluciones, conjunción y recursividad. La actividad continúa el sistema de orientación académica diseñado conceptualmente en la Clase 3.

## Modalidad y duración

- Trabajo en parejas.
- Duración: 50 minutos.
- Entorno: SWI-Prolog local o [SWISH](https://swish.swi-prolog.org/).
- Archivo inicial: [`base-inicial.pl`](base-inicial.pl).

## Contexto

La universidad necesita una herramienta didáctica que responda consultas sobre estudiantes, materias aprobadas y correlatividades. El programa es un ejercicio: no reemplaza al sistema académico ni toma decisiones reales.

La relación se leerá así:

```prolog
correlativa(Materia, Requisito).
```

Por ejemplo, `correlativa(inteligencia_artificial, algoritmos)` significa que Algoritmos es requisito directo de Inteligencia Artificial.

## Parte 1 - Cargar y explorar la base (8 minutos)

1. Abran `base-inicial.pl`.
2. Carguen el archivo en Prolog.
3. Ejecuten estas consultas y registren todas las respuestas:

```prolog
?- estudiante(ana).
?- aprobo(ana, Materia).
?- aprobo(Estudiante, algoritmos).
?- aprobo(Estudiante, Materia).
?- aprobo(_, programacion_2).
```

Respondan:

- ¿Cuál consulta es individual?
- ¿Cuáles son existenciales?
- ¿Qué diferencia hay entre `Materia` y `_`?
- ¿Cómo se solicita la siguiente solución?

## Parte 2 - Escribir reglas de cursada (12 minutos)

Completen `puede_cursar/2` para Inteligencia Artificial. La recomendación debe exigir:

- que la persona sea estudiante;
- que tenga inscripción activa;
- que haya aprobado Algoritmos;
- que no tenga superposición horaria con la materia;
- que exista cupo.

Plantilla:

```prolog
puede_cursar(Estudiante, inteligencia_artificial) :-
    % completar cinco objetivos separados por comas
    .
```

Prueben:

```prolog
?- puede_cursar(ana, inteligencia_artificial).
?- puede_cursar(bruno, inteligencia_artificial).
?- puede_cursar(carla, inteligencia_artificial).
?- puede_cursar(Quien, inteligencia_artificial).
```

Para cada resultado `false`, expliquen qué objetivo no pudo demostrarse. No escriban la conclusión como hecho: debe derivarse de la regla.

## Parte 3 - Alternativas y casos de prueba (10 minutos)

La dirección de carrera permite una excepción cuando existe una autorización explícita. Agreguen una segunda cláusula de `puede_cursar/2`:

```prolog
puede_cursar(Estudiante, Materia) :-
    autorizacion_excepcional(Estudiante, Materia),
    inscripcion_activa(Estudiante),
    sin_superposicion(Estudiante, Materia),
    hay_cupo(Materia).
```

Agreguen un único hecho de autorización para Carla y vuelvan a ejecutar las cuatro consultas.

Respondan:

- ¿Por qué dos cláusulas representan una alternativa?
- ¿Qué riesgo tendría una autorización sin identificación de responsable o vencimiento?
- ¿Qué control debe quedar fuera de este programa didáctico y bajo supervisión humana?

## Parte 4 - Correlatividades recursivas (12 minutos)

Definan `requisito/2` para que encuentre requisitos directos e indirectos:

```prolog
requisito(Materia, Requisito) :-
    correlativa(Materia, Requisito).

requisito(Materia, Requisito) :-
    correlativa(Materia, Intermedia),
    requisito(Intermedia, Requisito).
```

Ejecuten:

```prolog
?- requisito(inteligencia_artificial, algoritmos).
?- requisito(inteligencia_artificial, programacion_2).
?- requisito(inteligencia_artificial, programacion_1).
?- requisito(inteligencia_artificial, Requisito).
?- requisito(Materia, programacion_1).
```

Identifiquen:

- el caso base;
- el caso recursivo;
- qué argumento permanece como objetivo y cuál avanza por la cadena;
- qué podría ocurrir si la base contiene un ciclo de correlatividades.

## Parte 5 - Auditoría final (8 minutos)

Intercambien el archivo con otra pareja. El grupo revisor debe comprobar:

1. que todas las cláusulas terminan con punto;
2. que variables y átomos usan correctamente mayúsculas y minúsculas;
3. que `puede_cursar/2` deriva respuestas y no las almacena como hechos;
4. que las consultas de prueba producen los resultados esperados;
5. que la recursión tiene un caso base;
6. que no se incorporaron datos personales innecesarios.

Corrijan al menos un problema o documenten que no encontraron ninguno.

## Entregable

Entregar:

- el archivo `.pl` completo;
- las consultas ejecutadas y sus respuestas;
- una explicación de una inferencia exitosa;
- una explicación de un `false`;
- el riesgo detectado en la excepción;
- la respuesta sobre ciclos en la relación recursiva.

## Criterios de evaluación

| Criterio | Logrado | En proceso | A revisar |
|---|---|---|---|
| Sintaxis | Hechos y reglas cargan sin errores | Presenta errores menores corregibles | No distingue hechos, reglas o consultas |
| Consultas | Usa individuos, variables y `_` correctamente | Recupera solo parte de las soluciones | Confunde variables con átomos |
| Regla de cursada | La conclusión se deriva de todos los objetivos | Falta una condición o una prueba | Guarda la conclusión como hecho |
| Alternativa | Modela y explica la segunda cláusula | La alternativa funciona sin justificación | La excepción elimina controles esenciales |
| Recursividad | Distingue caso base y paso recursivo | La relación funciona solo en algunos casos | No termina o invierte los argumentos |
| Auditoría | Prueba, explica y corrige el programa | Prueba sin explicar resultados | No presenta evidencia de ejecución |

## Desafío opcional

Prolog puede repetir soluciones si existen distintos caminos hacia el mismo requisito. Investiguen `setof/3` y construyan una consulta que devuelva una lista sin duplicados:

```prolog
?- setof(R, requisito(inteligencia_artificial, R), Requisitos).
```

Expliquen por qué esto no modifica la base de conocimiento, sino la forma de reunir las respuestas.
