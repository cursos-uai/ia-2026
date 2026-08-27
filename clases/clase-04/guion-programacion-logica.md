# Guion docente - Clase 4: Programación lógica con Prolog

## Datos generales

- Duración base: 120 minutos.
- Unidad: Lógica simbólica.
- Material principal: `Clase 4 - Programación Lógica.pdf` (59 diapositivas).
- Modalidad: explicación con demostraciones en SWI-Prolog y actividad en parejas.
- Requisito: conceptos de símbolo, hecho, regla e inferencia trabajados en la Clase 3.

## Resultados de aprendizaje

Al terminar la clase, los estudiantes deberían poder:

- explicar la diferencia entre describir conocimiento y programar una secuencia de pasos;
- reconocer individuos, predicados, aridad, hechos, reglas y consultas;
- escribir y ejecutar consultas individuales y existenciales;
- usar variables, variable anónima y búsqueda de múltiples soluciones;
- construir reglas con conjunción y alternativas;
- diferenciar unificación de evaluación aritmética;
- reconocer functores como términos compuestos;
- formular una definición recursiva con caso base y caso recursivo.

## Preparación del docente

1. Tener SWI-Prolog instalado o abrir [SWISH](https://swish.swi-prolog.org/).
2. Cargar `base-inicial.pl` antes de la clase y comprobar las consultas de la actividad.
3. Escribir en el pizarrón:

```text
programa lógico = hechos + reglas
uso del programa = consultas al motor de inferencia
```

4. Recordar que el prompt `?-` pertenece al intérprete: no se escribe dentro del archivo `.pl`.

## 0-10 min | Puente desde la IA simbólica

### Apertura

Decir:

> En la clase anterior diseñamos representaciones y reglas. Hoy vamos a convertir esas ideas en un programa que pueda responder preguntas. En vez de indicar paso por paso cómo buscar una respuesta, declaramos qué sabemos y dejamos que el motor de inferencia intente demostrar la consulta.

Retomar este ejemplo:

```prolog
humano(socrates).
mortal(X) :- humano(X).
```

Preguntar:

- ¿Cuál es el hecho?
- ¿Cuál es la regla?
- ¿La conclusión `mortal(socrates)` está escrita o se deriva?

### Idea de cierre

Prolog pertenece al paradigma declarativo: el programa describe conocimiento mediante cláusulas. Esto no significa que el orden sea siempre irrelevante; el motor sigue una estrategia concreta de búsqueda y el orden de reglas y objetivos puede afectar terminación y eficiencia.

## 10-22 min | Paradigmas, silogismos y programas lógicos

Diapositivas 2-8.

Explicar:

- En el paradigma imperativo se detallan instrucciones para transformar un estado.
- En programación lógica se expresan propiedades y relaciones mediante predicados.
- Un programa Prolog es una base de conocimiento formada por cláusulas.
- El motor responde consultas intentando demostrar que se siguen de los hechos y reglas.

Usar el silogismo:

```text
Sócrates es humano.
Todos los humanos son mortales.
Por lo tanto, Sócrates es mortal.
```

Mostrar su traducción y ejecutar:

```prolog
?- mortal(socrates).
true.

?- mortal(Quien).
Quien = socrates.
```

Destacar que una consulta con una variable no pregunta solo “sí o no”, sino qué sustitución permite satisfacerla.

## 22-38 min | Individuos, predicados y aridad

Diapositivas 9-14.

Proyectar o cargar:

```prolog
hombre(socrates).
ciudad(atenas).
vive(socrates, atenas).
vive(solon, atenas).
vive(arquimedes, siracusa).
```

Explicar:

- Los átomos comienzan con minúscula o se escriben entre comillas simples.
- Las variables comienzan con mayúscula o con guion bajo.
- `hombre/1` expresa una propiedad.
- `vive/2` expresa una relación.
- Nombre y aridad identifican un predicado: `vive/1` y `vive/2` serían predicados distintos.

### Control de comprensión

Pedir que clasifiquen:

```prolog
materia(inteligencia_artificial).
aprobo(ana, algoritmos).
fecha(27, 8, 2026).
```

Respuestas esperadas: predicados de aridad 1, 2 y 3. Aclarar que `fecha(27,8,2026)` podría ser un predicado si aparece como cláusula, o un término compuesto si aparece como argumento de otro predicado.

## 38-52 min | Cláusulas: hechos y reglas

Diapositivas 15-18 y 31-33.

Desarmar visualmente:

```prolog
mortal(X) :- humano(X).
```

- Cabeza o consecuente: `mortal(X)`.
- Cuello: `:-`.
- Cuerpo o antecedente: `humano(X)`.
- Punto final: obligatorio.

### Corrección importante del material

En una diapositiva se invierte verbalmente la condición. La lectura correcta es:

> Para demostrar que `mortal(X)` se cumple, Prolog debe demostrar `humano(X)`.

No debe decirse que la condición es que `X` sea mortal.

Mostrar otro ejemplo:

```prolog
es_hijo_de(Hijo, Padre) :- es_padre_de(Padre, Hijo).
```

Preguntar qué relación se invierte y por qué los nombres de las variables ayudan a leer la regla.

## 52-67 min | Consultas, variables y múltiples soluciones

Diapositivas 19-30.

Cargar:

```prolog
pasta(ravioles).
pasta(fideos).

come(juan, ravioles).
come(melina, ravioles).
come(brenda, fideos).
come(juan, fideos).
```

Ejecutar y anticipar las respuestas antes de presionar Enter:

```prolog
?- pasta(ravioles).
?- pasta(Pasta).
?- pasta(_).
?- come(Persona, ravioles).
?- come(brenda, Comida).
?- come(Persona, Comida).
```

Explicar:

- Una variable nombrada conserva y muestra su unificación.
- `_` representa una variable anónima diferente en cada aparición; se usa cuando el valor no interesa.
- El punto y coma solicita otra solución.
- Enter o punto detiene la búsqueda interactiva, según el entorno.

### Corrección de sintaxis

Las consultas se escriben `?- pasta(ravioles).`, no `?pasta(ravioles)`.

## 67-77 min | Universo cerrado: qué significa `false`

Diapositivas 22-24 y 34-36.

Ejecutar:

```prolog
?- mortal(aristoteles).
false.
```

Preguntar: “¿Acabamos de demostrar que Aristóteles no es mortal?”

Cerrar:

> No. Demostramos que la consulta no puede probarse con esta base y estas reglas. Bajo el supuesto de mundo cerrado, Prolog trata como falso aquello que no logra demostrar, pero ausencia de conocimiento no equivale necesariamente a falsedad en el mundo real.

Relacionar con los riesgos de un sistema experto incompleto.

## 77-82 min | Pausa breve

Dejar proyectado:

> ¿Qué respuesta produce una consulta: un dato almacenado o una demostración construida?

## 82-96 min | Conjunción, alternativas y desigualdad

Diapositivas 38-46.

Usar una base familiar y corregir el caso reflexivo:

```prolog
padre(juan, luis).
padre(juan, ana).
madre(nora, luis).
madre(nora, ana).

mismo_padre(P1, P2) :-
    padre(Padre, P1),
    padre(Padre, P2),
    P1 \= P2.

misma_madre(P1, P2) :-
    madre(Madre, P1),
    madre(Madre, P2),
    P1 \= P2.

hermano(P1, P2) :-
    mismo_padre(P1, P2),
    misma_madre(P1, P2).

hermanastro(P1, P2) :- misma_madre(P1, P2).
hermanastro(P1, P2) :- mismo_padre(P1, P2).
```

Explicar:

- La coma representa conjunción: deben satisfacerse todos los objetivos.
- Varias cláusulas para el mismo predicado ofrecen alternativas lógicas.
- Sin `P1 \= P2`, una persona puede aparecer como hermana de sí misma.
- Las dos cláusulas de `hermanastro/2` también incluyen a hermanos completos y pueden producir soluciones duplicadas. Esto muestra que la semántica pretendida debe revisarse con casos de prueba.

## 96-108 min | Unificación, aritmética y términos compuestos

Diapositivas 47-55.

### Unificación

```prolog
?- juan = juan.
true.

?- juan = pedro.
false.

?- Persona = juan.
Persona = juan.
```

`=/2` unifica términos; no evalúa expresiones aritméticas.

### Aritmética

```prolog
siguiente(N, Siguiente) :- Siguiente is N + 1.
```

Probar:

```prolog
?- siguiente(2, 3).      % true
?- siguiente(3, N).      % N = 4
?- siguiente(N, 4).      % error: N no está instanciada
```

### Correcciones importantes

- Los operadores correctos incluyen `>=` y `=<`; no `=>`.
- `is/2` evalúa su lado derecho y exige que allí las variables ya tengan valor numérico.
- Por eso `siguiente/2` no es reversible en todas las direcciones.

### Términos compuestos o functores

```prolog
nacio(karla, fecha(22, 8, 1979)).
nacio(sergio, fecha(14, 10, 1986)).

?- nacio(Quien, fecha(_, _, 1986)).
Quien = sergio.
```

`fecha(14,10,1986)` es un término compuesto cuando aparece como argumento. No tiene valor de verdad por sí mismo. Para nombres con espacios, preferir átomos entre comillas simples, por ejemplo `'Jorge Luis Borges'`.

## 108-118 min | Recursividad

Diapositivas 56-59.

Definir primero la orientación de la relación:

```prolog
padre(Padre, Hijo).
```

Luego construir:

```prolog
ancestro(Ancestro, Persona) :-
    padre(Ancestro, Persona).

ancestro(Ancestro, Persona) :-
    padre(Ancestro, Intermedio),
    ancestro(Intermedio, Persona).
```

Explicar:

- La primera cláusula es el caso base: un padre es ancestro directo.
- La segunda es el caso recursivo: el ancestro de un antecesor también es ancestro.
- El caso base evita que la definición dependa solo de sí misma.
- El orden de argumentos debe conservarse en hechos, reglas y consultas.

### Corrección importante del material

El ejemplo de las diapositivas usa `padre(Persona, Ancestro)` mientras el texto sugiere “mi padre”, lo que invierte la relación habitual `padre(Padre,Hijo)`. Conviene fijar una convención explícita y mantenerla.

## 118-120 min | Cierre y consigna

Síntesis oral:

> En Prolog escribimos conocimiento como cláusulas y formulamos consultas. El motor busca unificaciones y aplica reglas para demostrar respuestas. La potencia del paradigma está en consultar una misma relación de distintas maneras; sus límites aparecen cuando la base es incompleta, las reglas están mal orientadas, la búsqueda no termina o una operación, como `is/2`, exige argumentos instanciados.

Ticket de salida:

1. Escribí un hecho, una regla y una consulta.
2. ¿Qué diferencia existe entre una variable nombrada y `_`?
3. ¿Por qué `false` no siempre significa “falso en el mundo real”?

Presentar la [actividad práctica](actividad-prolog.md), que implementa una base de conocimiento académica y culmina con una relación recursiva de correlatividades.

## Errores frecuentes y respuestas docentes

| Situación | Intervención sugerida |
|---|---|
| Escriben una variable con minúscula | Recordar: minúscula representa átomo; mayúscula o `_` inicia variable. |
| Olvidan el punto | Señalar que cada cláusula y consulta termina con `.`. |
| Copian `?-` dentro del archivo | Aclarar que el prompt se usa en la consola, no en la base `.pl`. |
| Leen `Cabeza :- Cuerpo` de izquierda a derecha como ejecución | Reformular: “la Cabeza se demuestra si el Cuerpo puede demostrarse”. |
| Confunden `=` con evaluación | `=` unifica; `is` evalúa una expresión aritmética. |
| Esperan que `siguiente(N,4)` despeje `N` | Explicar que `is/2` no resuelve ecuaciones hacia atrás. |
| Una relación devuelve una persona consigo misma | Agregar y discutir `P1 \= P2`. |
| La recursión no termina | Revisar caso base, progreso hacia él y orden de las cláusulas. |

## Adaptación a 90 minutos

- Apertura y conceptos básicos: 15 min.
- Hechos, reglas y consultas: 20 min.
- Variables y múltiples soluciones: 15 min.
- Conjunción, aritmética y functores: 15 min.
- Recursividad: 10 min.
- Inicio de la actividad: 15 min; completar fuera de clase.

## Fuentes

- Gastón Weingand, `Clase 4 - Programación Lógica.pdf`, 59 diapositivas, material de la cátedra.
- Stuart Russell y Peter Norvig, *Artificial Intelligence: A Modern Approach*, Global Edition, 4th ed., capítulo 9, especialmente inferencia hacia atrás y programación lógica.
