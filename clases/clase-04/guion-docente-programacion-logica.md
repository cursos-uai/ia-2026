# Guion docente - Clase 4: Programación lógica con Prolog

Duración base: 120 minutos

Modalidad: explicación dialogada, demostración en vivo y actividad grupal

Material central: `Clase 4 - Programación Lógica.pdf` y `Tutorial de Prolog.pdf`

## Resultados de aprendizaje

Al finalizar la clase, los estudiantes podrán:

1. explicar la diferencia entre programación imperativa y declarativa;
2. representar un dominio pequeño mediante hechos y reglas de Prolog;
3. formular consultas cerradas y consultas con variables;
4. interpretar unificación, múltiples soluciones y backtracking;
5. reconocer el principio de mundo cerrado;
6. distinguir unificación, comparación y evaluación aritmética;
7. escribir y probar una primera relación recursiva.

## Preparación del docente

- Tener disponible SWI-Prolog o un entorno Prolog en línea.
- Crear un archivo `clase4.pl` para la demostración.
- Probar previamente todos los ejemplos de este guion.
- Escribir en el pizarrón:

```text
hechos + reglas + consulta → respuestas
```

- Recordar estas correcciones respecto del material:
  - una consulta comienza con `?-`;
  - el operador correcto es `>=`, no `=>`;
  - `is/2` evalúa una expresión y no funciona automáticamente en sentido inverso;
  - en `mortal(X) :- hombre(X).`, `hombre(X)` es la condición y `mortal(X)` la conclusión.

## 0-10 min | Apertura: de las reglas a un programa ejecutable

### Qué decir

> En la clase anterior representamos conocimiento mediante hechos y reglas. Hoy vamos a escribir esas representaciones en un lenguaje que puede responder preguntas y derivar conclusiones: Prolog.

Recuperar el ejemplo de la Clase 3:

```prolog
humano(socrates).
mortal(X) :- humano(X).
```

Preguntar:

- ¿Qué línea describe un caso particular?
- ¿Cuál expresa conocimiento general?
- ¿La conclusión `mortal(socrates)` está guardada o se deriva?

Ejecutar:

```prolog
?- mortal(socrates).
true.
```

### Idea clave

Prolog recibe una consulta e intenta demostrarla usando la base de conocimiento.

## 10-22 min | Paradigma declarativo

Contrastar dos preguntas:

- Programación imperativa: **¿qué pasos debe ejecutar la computadora?**
- Programación lógica: **¿qué relaciones y condiciones son verdaderas en el dominio?**

Explicar que Prolog no elimina el orden de ejecución ni los problemas algorítmicos. El orden de cláusulas y objetivos puede afectar rendimiento, terminación y orden de las respuestas.

Ejemplo declarativo:

```prolog
puede_rendir(X) :-
    regular(X),
    aprobo_trabajos_practicos(X).
```

Leerlo de derecha a izquierda:

> X puede rendir si X es regular y X aprobó los trabajos prácticos.

Aclarar la sintaxis:

- los átomos empiezan con minúscula: `ana`, `inteligencia_artificial`;
- las variables empiezan con mayúscula o `_`: `X`, `Estudiante`, `_`;
- los hechos y reglas terminan con punto;
- `:-` se lee “si”;
- la coma representa conjunción lógica.

## 22-35 min | Hechos, predicados, relaciones y aridad

Construir en vivo:

```prolog
estudiante(ana).
estudiante(bruno).
regular(ana).
regular(bruno).
aprobo_trabajos_practicos(ana).
cursa(ana, inteligencia_artificial).
cursa(bruno, inteligencia_artificial).
```

Explicar:

- `estudiante/1` expresa una propiedad;
- `cursa/2` expresa una relación;
- la aridad es la cantidad de argumentos;
- `cursa/2` y `cursa/3` serían predicados distintos.

Preguntar:

> ¿Qué convención expresa `cursa(ana, inteligencia_artificial)`? ¿Qué cambiaría si invirtiéramos los argumentos?

### Señal de aprendizaje

El grupo puede identificar nombre, argumentos y aridad de un predicado.

## 35-48 min | Consultas cerradas, variables y múltiples soluciones

Ejecutar consultas cerradas:

```prolog
?- estudiante(ana).
true.

?- estudiante(carla).
false.
```

Luego consultas con variables:

```prolog
?- estudiante(X).
X = ana ;
X = bruno.
```

Explicar que `X` se liga primero con una solución. Al pedir otra con `;`, Prolog vuelve al último punto de elección y busca una alternativa: eso es **backtracking**.

Consultar una relación:

```prolog
?- cursa(Quien, inteligencia_artificial).
Quien = ana ;
Quien = bruno.
```

Mostrar la variable anónima:

```prolog
?- cursa(_, inteligencia_artificial).
true.
```

Se usa `_` cuando interesa que exista algún valor, pero no cuál.

## 48-58 min | Mundo cerrado

Retomar:

```prolog
?- estudiante(carla).
false.
```

Preguntar:

> ¿Prolog demostró que Carla no es estudiante o solamente no pudo demostrar que lo sea con esta base?

Explicar el **principio de mundo cerrado**: aquello que no puede demostrarse con el conocimiento disponible se trata operativamente como falso. No es lo mismo que demostrar falsedad en el mundo real.

Ejemplo profesional:

> Que un sistema académico no encuentre una equivalencia registrada no demuestra que la equivalencia no exista; puede faltar actualizar la base.

## 58-65 min | Pausa breve

Dejar proyectada esta consigna:

> Escribí un hecho, una regla y una consulta sobre la cursada. Marcá qué palabras deben comenzar con mayúscula.

## 65-80 min | Reglas, conjunción y alternativas

Agregar:

```prolog
puede_rendir(X) :-
    estudiante(X),
    regular(X),
    aprobo_trabajos_practicos(X).
```

Consultar:

```prolog
?- puede_rendir(ana).
true.

?- puede_rendir(bruno).
false.

?- puede_rendir(X).
X = ana.
```

Subrayar que en:

```prolog
mortal(X) :- humano(X).
```

`humano(X)` es la condición y `mortal(X)` es la conclusión.

Para expresar alternativas, preferir inicialmente varias cláusulas:

```prolog
modalidad_recomendada(X, presencial) :- vive_cerca(X).
modalidad_recomendada(X, virtual) :- vive_lejos(X).
```

Mencionar que `;` representa disyunción, aunque múltiples cláusulas suelen ser más legibles al comenzar.

## 80-92 min | Unificación

Definir la unificación como el proceso de encontrar ligaduras que vuelvan compatibles dos términos.

Probar:

```prolog
?- X = ana.
X = ana.

?- cursa(X, inteligencia_artificial) = cursa(ana, Y).
X = ana,
Y = inteligencia_artificial.

?- cursa(ana, ia) = cursa(ana, matematica).
false.
```

Preguntas:

- ¿Qué variables quedaron ligadas?
- ¿Por qué falla el tercer caso?
- ¿`=` significa asignación como en otros lenguajes?

Respuesta esperada: en estos ejemplos, `=` intenta unificar; no evalúa una expresión aritmética.

## 92-103 min | Comparación y aritmética

Distinguir:

```prolog
?- X = 2 + 3.
X = 2+3.

?- X is 2 + 3.
X = 5.

?- 5 =:= 2 + 3.
true.

?- 5 >= 4.
true.

?- 4 =< 5.
true.
```

Explicar:

- `=` unifica términos sin calcular;
- `is` evalúa la expresión de la derecha y unifica el resultado;
- `=:=` compara valores numéricos;
- `>=` y `=<` son comparaciones numéricas.

Mostrar el límite de `is/2`:

```prolog
?- 4 is N + 1.
```

La consulta produce un error porque `N` no tiene valor. La declaratividad no garantiza que todas las relaciones sean ejecutables en cualquier dirección.

## 103-113 min | Primera relación recursiva

Definir explícitamente la convención `padre(Progenitor, Hijo)`:

```prolog
padre(ana, bruno).
padre(bruno, carla).
padre(carla, diego).

ancestro(A, D) :-
    padre(A, D).

ancestro(A, D) :-
    padre(A, X),
    ancestro(X, D).
```

Explicar:

- primera cláusula: caso base, una persona es ancestro directo de su hijo;
- segunda cláusula: caso recursivo, sigue un eslabón y vuelve a consultar;
- el orden de argumentos se mantiene siempre: ancestro primero, descendiente después.

Probar:

```prolog
?- ancestro(ana, diego).
true.

?- ancestro(Quien, diego).
Quien = carla ;
Quien = ana ;
Quien = bruno.
```

El orden exacto de respuestas puede depender del orden de hechos y reglas; lo importante es el conjunto de soluciones.

## 113-120 min | Cierre y ticket de salida

### Síntesis oral

> En Prolog describimos conocimiento mediante hechos y reglas, y planteamos consultas. Las variables se ligan por unificación; Prolog explora alternativas mediante backtracking. La base define qué puede demostrarse, y el orden del programa todavía importa.

### Ticket de salida

1. Escribí un hecho, una regla y una consulta válida.
2. Explicá la diferencia entre `=` e `is`.
3. ¿Qué significa `false` bajo el principio de mundo cerrado?
4. ¿Qué papel cumple el caso base en una regla recursiva?

### Puente

> En la actividad vamos a diseñar una base de conocimiento académica, consultarla y buscar casos que revelen reglas incompletas o mal modeladas.

## Adaptación a 90 minutos

- Apertura y paradigma declarativo: 15 min.
- Hechos, reglas y consultas: 25 min.
- Variables, unificación y backtracking: 20 min.
- Mundo cerrado y aritmética: 10 min.
- Recursividad: 10 min.
- Cierre: 10 min.

La actividad puede realizarse en una instancia separada o reducirse a las partes A, B y C.

## Errores frecuentes y respuesta docente

| Error | Corrección pedagógica |
|---|---|
| Escribir variables en minúscula | Mostrar que `ana` es átomo y `Ana` es variable |
| Omitir el punto final | Señalar que cierra hechos y reglas |
| Escribir `?consulta(X)` | Usar `?- consulta(X).` |
| Leer `:-` al revés | Leer primero la cabeza: “conclusión si condiciones” |
| Usar `=>` | Usar `>=` |
| Esperar que `is` despeje variables | Evaluar primero la expresión derecha o reformular la relación |
| Confundir `false` con falsedad comprobada | Recordar mundo cerrado y conocimiento incompleto |
| Invertir argumentos en recursividad | Declarar y mantener una convención explícita |

## Verificación docente

Antes de cerrar la clase, comprobar que los estudiantes pueden:

- reconocer hechos, reglas y consultas;
- explicar una ligadura de variable;
- solicitar más de una solución;
- anticipar por qué una consulta falla;
- distinguir unificación de evaluación aritmética;
- identificar caso base y caso recursivo.
