# Actividad en clase - Rutas inteligentes con Prolog

Duración: 40 minutos. Modalidad: grupos de 3 o 4 integrantes.

## Propósito

Construir y consultar una base de conocimiento que permita recomendar trayectos de transporte, y analizar cómo influyen la representación, el orden de las reglas y la información ausente.

## Preparación

1. Abrir SWI-Prolog o [SWISH](https://swish.swi-prolog.org/).
2. Copiar o abrir [`actividad_base.pl`](actividad_base.pl).
3. En SWI-Prolog local, cargar el archivo con:

```prolog
?- [actividad_base].
```

Si no hay un entorno disponible, resolver las consultas en papel narrando la unificación y el backtracking.

## Dominio

La base describe conexiones directas entre lugares y medios de transporte.

```prolog
conexion(campus, centro, colectivo).
conexion(centro, terminal, subte).
conexion(campus, parque, bicicleta).
conexion(parque, centro, bicicleta).
conexion(terminal, aeropuerto, colectivo).
conexion(centro, aeropuerto, tren).

habilitado(ana, colectivo).
habilitado(ana, subte).
habilitado(ana, tren).
habilitado(bruno, bicicleta).
habilitado(bruno, colectivo).
```

La convención es:

```text
conexion(Origen, Destino, Medio)
habilitado(Persona, Medio)
```

## Parte 1 - Consultas básicas (8 minutos)

Antes de ejecutarlas, anotar qué respuesta esperan.

1. ¿Existe conexión directa entre `campus` y `centro`?
2. ¿Qué medios conectan directamente `campus` con algún destino?
3. ¿A qué destinos puede llegar Ana en un solo tramo?
4. ¿Existe alguna persona habilitada para usar bicicleta sin importar quién sea?

Escribir las cuatro consultas con sintaxis Prolog y luego comprobarlas.

## Parte 2 - Primera regla (8 minutos)

Completar:

```prolog
puede_viajar_directo(Persona, Origen, Destino) :-
    % deben cumplirse una conexión y una habilitación compatibles
    true.
```

La regla debe relacionar el mismo medio de transporte en ambas condiciones.

Probar:

```prolog
?- puede_viajar_directo(ana, campus, centro).
?- puede_viajar_directo(bruno, campus, centro).
?- puede_viajar_directo(Persona, campus, Destino).
```

Pedir todas las soluciones con `;` y explicar de dónde surge cada una.

## Parte 3 - Viaje con una escala (10 minutos)

Definir:

```prolog
puede_viajar_con_una_escala(Persona, Origen, Escala, Destino) :-
    % primer tramo
    % segundo tramo
    true.
```

Condiciones:

- deben existir dos conexiones consecutivas;
- la persona debe estar habilitada para el medio de cada tramo;
- `Origen`, `Escala` y `Destino` deben ser lugares diferentes.

Probar consultas que permitan:

1. verificar si Ana puede ir de `campus` a `terminal`;
2. descubrir la escala;
3. listar todos los trayectos de una escala disponibles para cualquier persona.

## Parte 4 - Auditoría: lo que no sabemos (8 minutos)

Ejecutar:

```prolog
?- habilitado(carla, tren).
```

Responder:

1. ¿La respuesta demuestra que Carla no está habilitada en la realidad?
2. ¿Qué demuestra exactamente sobre esta base de conocimiento?
3. ¿Qué riesgo aparece si el sistema interpreta ausencia de datos como prohibición definitiva?
4. ¿Cuándo correspondería devolver `requiere_revision` en vez de aprobar o rechazar?

Agregar un hecho o una regla que modele explícitamente un caso pendiente de revisión.

## Parte 5 - Prueba cruzada (4 minutos)

Intercambiar el código con otro grupo. El grupo revisor debe encontrar al menos uno de estos problemas:

- una variable que no conecta correctamente dos condiciones;
- una regla que admite viajar sin habilitación;
- un resultado duplicado;
- un trayecto circular;
- una consulta que debería devolver varias soluciones y no lo hace.

Corregir el problema o explicar por qué el comportamiento es válido.

## Entrega (2 minutos)

Entregar:

- archivo `.pl` completo;
- cuatro consultas básicas;
- resultados de tres consultas con variables;
- explicación paso a paso de un caso de backtracking;
- respuesta a la auditoría de mundo cerrado;
- corrección realizada tras la prueba cruzada.

## Criterios de evaluación

| Criterio | Logrado | En proceso |
|---|---|---|
| Sintaxis | Hechos, reglas y consultas están bien formados. | Faltan puntos, hay mayúsculas incorrectas o consultas dentro del archivo. |
| Modelado | Los argumentos mantienen una convención coherente. | El significado cambia según la cláusula. |
| Unificación | Las variables conectan correctamente las condiciones. | Las condiciones usan variables independientes por error. |
| Soluciones | Obtiene e interpreta múltiples respuestas. | Solo comprueba el primer resultado. |
| Auditoría | Distingue fallo de prueba de falsedad real. | Interpreta todo `false` como hecho del mundo. |

## Desafío opcional

Definir un predicado recursivo `puede_llegar/3` para rutas de cualquier cantidad de tramos. Evitar ciclos llevando una lista de lugares visitados.

Este desafío requiere listas y recursividad; no es obligatorio para alcanzar los objetivos de la clase.
