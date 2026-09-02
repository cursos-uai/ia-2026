<!-- markdownlint-disable MD013 MD024 MD029 -->

# Guion docente - Clase 4: Programación lógica con Prolog

Esta guía acompaña la clase 4 y está pensada para que el alumno pueda seguir una hoja de ruta paso a paso: primero entiende el concepto, después copia una base de conocimiento, ejecuta consultas y finalmente resuelve ejercicios breves.

## Datos generales

- Duración base: 120 minutos.
- Banco extendido de actividades: hasta 195 minutos si se realizan todos los ejercicios en vivo.
- Unidad: Lógica simbólica.
- Material principal: `Clase 4 - Programación Lógica.pdf` (59 diapositivas).
- Modalidad: explicación conceptual, demostraciones en Prolog y ejercicios guiados.
- Entorno sugerido: [SWISH](https://swish.swi-prolog.org/) o SWI-Prolog local.
- Requisito: conceptos de símbolo, hecho, regla e inferencia trabajados en la Clase 3.

## Resultados de aprendizaje

Al terminar la clase, los estudiantes deberían poder:

- explicar la diferencia entre describir conocimiento y programar una secuencia de pasos;
- reconocer individuos, predicados, aridad, hechos, reglas y consultas;
- escribir y ejecutar consultas individuales y existenciales;
- usar variables, variable anónima y búsqueda de múltiples soluciones;
- construir reglas con conjunción y alternativas;
- comprender el principio de mundo cerrado;
- diferenciar unificación de evaluación aritmética;
- reconocer functores como términos compuestos;
- formular una definición recursiva con caso base y caso recursivo.

## Preparación antes de la clase

1. Abrir [SWISH](https://swish.swi-prolog.org/) o SWI-Prolog local.
2. Tener disponible [`base-inicial.pl`](base-inicial.pl).
3. Recordar esta diferencia:

```text
Archivo .pl: contiene hechos y reglas.
Consola/Query: contiene consultas.
```

4. En SWISH, si se usa la caja de consultas, se escribe la consulta sin el prefijo `?-`.
5. En SWI-Prolog local, el prompt `?-` lo muestra el intérprete: no se tipea dentro del archivo.

Ejemplo de consulta en SWI-Prolog local:

```prolog
?- mortal(socrates).
```

Ejemplo equivalente en la caja de consulta de SWISH:

```prolog
mortal(socrates).
```

## Dinámica de trabajo

Para cada bloque:

1. Leer la explicación conceptual.
2. Copiar el programa base.
3. Ejecutar las consultas sugeridas.
4. Anticipar el resultado antes de ejecutar.
5. Resolver el ejercicio de 10 minutos.
6. Comparar con una solución posible.

### Cómo usar los tiempos

La duración base de la clase es de 120 minutos. El recorrido detallado de este
archivo funciona como banco extendido: incluye más ejemplos y ejercicios de los
que conviene ejecutar completos en una sola clase.

Para una clase estricta de 120 minutos, usar esta tabla como recorrido principal y seleccionar sólo algunos ejercicios en vivo. El resto queda como práctica asincrónica o material de repaso.

| Tiempo | Bloque |
| --- | --- |
| 0-10 | Puente desde IA simbólica |
| 10-22 | Paradigmas y silogismos |
| 22-38 | Base de conocimiento, individuos y predicados |
| 38-52 | Hechos, reglas y consultas |
| 52-67 | Variables, `_` y múltiples soluciones |
| 67-77 | Mundo cerrado |
| 77-95 | Conjunción, disyunción e inversibilidad |
| 95-108 | Aritmética y unificación |
| 108-118 | Functores y recursividad |
| 118-120 | Ticket de salida |

A partir de acá se ofrece el banco extendido, con más desarrollo y ejercicios que los necesarios para una única clase de 120 minutos.

## Banco extendido | 0-10 min | Puente desde IA simbólica

### Concepto

En programación imperativa solemos indicar pasos:

```text
primero hacé esto, después aquello, luego devolvé el resultado
```

En programación lógica hacemos otra cosa: declaramos conocimiento y hacemos preguntas.

```text
programa lógico = hechos + reglas
uso del programa = consultas al motor de inferencia
```

Prolog pertenece al paradigma declarativo: el programa describe propiedades y relaciones de un conjunto de individuos. El motor de inferencia intenta demostrar consultas a partir de esa base.

### Guion oral sugerido

> En esta clase no vamos a pensar primero en algoritmos paso a paso. Vamos a pensar qué sabemos del mundo que queremos modelar. En Prolog escribimos hechos y reglas; después consultamos al motor para que intente probar respuestas.

### Primer ejemplo

Programa:

```prolog
humano(socrates).
mortal(X) :- humano(X).
```

Consultas:

```prolog
mortal(socrates).
```

```prolog
mortal(Quien).
```

### Preguntas de control

- ¿Cuál es el hecho?
- ¿Cuál es la regla?
- ¿La conclusión `mortal(socrates)` está escrita o se deriva?

## 10-22 min | Paradigmas, silogismos y programas lógicos

Diapositivas 2-8.

### Concepto

Un silogismo tiene premisas y conclusión:

```text
Sócrates es humano.
Todos los humanos son mortales.
Por lo tanto, Sócrates es mortal.
```

En Prolog:

```prolog
humano(socrates).
mortal(X) :- humano(X).
```

La regla se lee:

> X es mortal si X es humano.

La parte izquierda es la **cabeza**. La parte derecha es el **cuerpo**. El símbolo `:-` se lee como “si”.

### Demo

Programa:

```prolog
humano(socrates).
humano(hipatia).
humano(ada).

mortal(X) :- humano(X).
```

Consultas:

```prolog
humano(socrates).
```

```prolog
mortal(socrates).
```

```prolog
mortal(Quien).
```

```prolog
mortal(aristoteles).
```

### Qué observar

- `mortal(socrates)` da verdadero aunque no esté escrito como hecho.
- Se deriva por la regla `mortal(X) :- humano(X)`.
- `mortal(aristoteles)` falla si no declaramos `humano(aristoteles)`.

### Ejercicio 10 minutos

Enunciado:

> Modelá una base de conocimiento sobre animales. Declarar al menos 4 animales: algunos mamíferos y otros aves. Luego definir `ser_vivo/1`, que sea verdadero para todo mamífero o ave.

Consultas a resolver:

```prolog
ser_vivo(perro).
ser_vivo(X).
ave(_).
```

Solución posible:

```prolog
mamifero(perro).
mamifero(gato).
ave(paloma).
ave(aguila).

ser_vivo(X) :- mamifero(X).
ser_vivo(X) :- ave(X).
```

## 22-38 min | Base de conocimiento, individuos, predicados y aridad

Diapositivas 9-14.

### Concepto

Un programa Prolog es una **base de conocimiento**. Esa base contiene cláusulas que hablan sobre individuos mediante predicados.

Definiciones:

- **Individuo**: entidad sobre la que queremos expresar conocimiento.
- **Predicado**: propiedad o relación que afirmamos sobre individuos.
- **Aridad**: cantidad de argumentos de un predicado.
- **Propiedad**: predicado de aridad 1.
- **Relación**: predicado de aridad mayor a 1.

Ejemplos:

```prolog
ciudad(atenas).          % ciudad/1
vive(socrates, atenas).  % vive/2
nacio(solon, -634).      % nacio/2
```

`hombre/1` significa: predicado `hombre` con un argumento.

`vive/2` significa: predicado `vive` con dos argumentos.

Nombre y aridad identifican un predicado. Para Prolog, `vive/1` y `vive/2` son predicados distintos.

### Demo

Programa:

```prolog
hombre(socrates).
hombre(solon).
hombre(pericles).
hombre(arquimedes).

ciudad(atenas).
ciudad(siracusa).

vive(socrates, atenas).
vive(solon, atenas).
vive(pericles, atenas).
vive(arquimedes, siracusa).

nacio(solon, -634).
nacio(pericles, -495).
nacio(arquimedes, -287).

mortal(X) :- hombre(X).
son_conciudadanos(P1, P2) :-
    vive(P1, Ciudad),
    vive(P2, Ciudad),
    P1 \= P2.
```

Consultas:

```prolog
hombre(socrates).
ciudad(atenas).
vive(socrates, atenas).
vive(Quien, atenas).
son_conciudadanos(socrates, solon).
son_conciudadanos(X, Y).
```

### Qué remarcar

- `vive(socrates, atenas)` no devuelve un valor: afirma una relación.
- `son_conciudadanos/2` no está listado como hecho: se infiere desde `vive/2`.
- `P1 \= P2` evita que una persona sea conciudadana de sí misma.

### Ejercicio 10 minutos

Enunciado inspirado en la práctica de países:

> Escribí una base de conocimiento sobre países, provincias y departamentos. Incluir estos hechos: Argentina es un país, Uruguay es un país, Santa Cruz es una provincia y Canelones es un departamento. Luego responder consultas sobre información conocida y no conocida.

Programa mínimo:

```prolog
pais(argentina).
pais(uruguay).
provincia(santa_cruz).
departamento(canelones).
```

Consultas:

```prolog
pais(argentina).
pais(marruecos).
lago(ganges).
ciudad(estonia).
pais(X).
```

Preguntas para responder:

- ¿Qué consultas dan `true`?
- ¿Qué consultas dan `false`?
- ¿Por qué `pais(marruecos)` no prueba que Marruecos no sea país en el mundo real?

## 38-52 min | Cláusulas: hechos y reglas

Diapositivas 15-18 y 31-33.

### Concepto

Una cláusula es una unidad de información de la base de conocimiento. Siempre termina con punto.

Una cláusula puede ser:

- **hecho**: afirmación sin condiciones;
- **regla**: afirmación condicionada por otros objetivos.

Hecho:

```prolog
come(juan, ravioles).
```

Regla:

```prolog
mortal(Persona) :- humano(Persona).
```

Lectura correcta:

> Para demostrar `mortal(Persona)`, Prolog debe demostrar `humano(Persona)`.

### Corrección conceptual importante

Si se mira la regla como implicación lógica:

```prolog
mortal(X) :- humano(X).
```

el antecedente es `humano(X)` y el consecuente es `mortal(X)`. No hay que invertirlos.

### Demo

Programa:

```prolog
es_padre_de(paco, pepe).
es_padre_de(juan, ana).

es_hijo_de(Hijo, Padre) :-
    es_padre_de(Padre, Hijo).
```

Consultas:

```prolog
es_padre_de(paco, pepe).
es_hijo_de(pepe, paco).
es_hijo_de(Hijo, paco).
es_hijo_de(ana, Padre).
```

### Ejercicio 10 minutos

Enunciado:

> Modelá cursos y estudiantes. Declarar quiénes son estudiantes y definir `puede_rendir/1`, que sea verdadero para toda persona que sea estudiante.

Consultas:

```prolog
puede_rendir(ana).
puede_rendir(X).
puede_rendir(juan).
```

Solución posible:

```prolog
estudiante(ana).
estudiante(luis).
estudiante(maria).

puede_rendir(X) :- estudiante(X).
```

## 52-67 min | Consultas individuales, existenciales y múltiples soluciones

Diapositivas 17-30.

### Concepto

Las consultas son la forma de usar un programa lógico.

Hay dos tipos iniciales:

- **Individuales**: preguntan por individuos concretos.
- **Existenciales**: preguntan si existe algún valor que satisfaga el predicado.

Consulta individual:

```prolog
mortal(socrates).
```

Consulta existencial:

```prolog
mortal(X).
```

Una consulta sin variables responde `true` o `false`. Una consulta con variables puede devolver valores.

### Demo

Programa:

```prolog
pasta(ravioles).
pasta(fideos).

come(juan, ravioles).
come(melina, ravioles).
come(brenda, fideos).
come(juan, fideos).
```

Consultas:

```prolog
pasta(ravioles).
pasta(Pasta).
pasta(_).
come(juan, ravioles).
come(brenda, ravioles).
come(Persona, ravioles).
come(brenda, Comida).
come(Persona, Comida).
```

### Qué remarcar

- Una variable nombrada, como `Pasta`, conserva y muestra su valor.
- `_` es una variable anónima: hay un valor, pero no nos interesa mostrarlo.
- Cada aparición de `_` es independiente.
- El `;` pide otra solución.
- Enter corta la búsqueda de más soluciones.

### Ejercicio 10 minutos

Enunciado inspirado en la práctica de comidas:

> Escribí la siguiente base de conocimiento y luego construí consultas individuales y existenciales.

Base:

```prolog
come(ramiro, carne).
come(ana, verduras).
no_come(nina, pastas).
no_come(ana, carne).
```

Responder con consultas:

1. ¿Ramiro come carne?
2. ¿Ana come carne?
3. ¿Quién come verduras?
4. ¿Qué no come Ana?
5. ¿Existe alguien que no coma pastas?

Consultas esperadas:

```prolog
come(ramiro, carne).
come(ana, carne).
come(Quien, verduras).
no_come(ana, Que).
no_come(_, pastas).
```

### Nota docente sobre negación

En esta etapa usamos `no_come/2` como un predicado explícito. Todavía no estamos usando negación por fallo (`\+`). Es importante no mezclar ambas ideas demasiado temprano.

## 67-77 min | Universo cerrado: qué significa `false`

Diapositivas 22-24 y 34-36.

### Concepto

Prolog trabaja con el principio de **mundo cerrado**:

> Todo lo que no pueda probarse como verdadero con la base disponible se considera falso.

Esto no significa que sea falso en el mundo real. Significa que el sistema no tiene información suficiente para demostrarlo.

### Demo paso a paso

Programa:

```prolog
hombre(socrates).
mortal(X) :- hombre(X).
```

Consulta:

```prolog
mortal(aristoteles).
```

Razonamiento:

1. Prolog intenta probar `mortal(aristoteles)`.
2. Encuentra la regla `mortal(X) :- hombre(X)`.
3. Unifica `X = aristoteles`.
4. Intenta probar `hombre(aristoteles)`.
5. No encuentra ese hecho.
6. Devuelve `false`.

### Ejercicio 10 minutos

Enunciado:

> Dada la siguiente base, anticipar cuáles consultas dan `true`, cuáles dan `false` y cuáles devuelven variables.

```prolog
perro(tobi).
gato(michi).
mascota(X) :- perro(X).
mascota(X) :- gato(X).
```

Consultas:

```prolog
mascota(tobi).
mascota(luna).
mascota(X).
perro(michi).
gato(michi).
```

Pregunta final:

> ¿Qué información habría que agregar para que `mascota(luna)` sea verdadero?

## 77-82 min | Pausa breve

Dejar proyectada esta pregunta:

> ¿Una respuesta de Prolog es un dato almacenado o una demostración construida?

Respuesta esperada:

> Puede ser ambas cosas: a veces se recupera un hecho; otras veces se deriva una conclusión a partir de reglas.

## 82-96 min | Variables, variable anónima y búsqueda de soluciones

### Concepto

Reglas de nombres:

- variables: empiezan con mayúscula o `_`;
- átomos: normalmente empiezan con minúscula.

Ejemplos:

```prolog
Pasta     % variable
_         % variable anónima
ravioles  % átomo
```

Diferencia clave:

```prolog
come(X, X).
```

exige que ambos argumentos sean iguales.

```prolog
come(_, _).
```

sólo pregunta si existe alguna relación `come/2`, sin importar los valores.

### Demo

Programa:

```prolog
come(juan, ravioles).
come(melina, ravioles).
come(brenda, fideos).
come(juan, fideos).
come(pepe, pepe).
```

Consultas:

```prolog
come(_, ravioles).
come(_, _).
come(X, X).
come(Persona, Comida).
```

### Ejercicio 10 minutos

Enunciado:

> Crear una base `gusta(Persona, Actividad)`. Luego escribir consultas para saber: a quién le gusta fútbol, qué le gusta a Ana, si existe alguien con algún gusto y si existe un caso donde el nombre de la persona coincida con la actividad.

Base sugerida:

```prolog
gusta(ana, musica).
gusta(luis, futbol).
gusta(maria, futbol).
gusta(ajedrez, ajedrez).
```

Consultas esperadas:

```prolog
gusta(Quien, futbol).
gusta(ana, Que).
gusta(_, _).
gusta(X, X).
```

## 96-112 min | Conjunción, disyunción y desigualdad

Diapositivas 37-41.

### Concepto

La conjunción lógica, es decir “Y”, se escribe con coma:

```prolog
condicion1, condicion2
```

La disyunción lógica, es decir “O”, suele modelarse con varias cláusulas para el mismo predicado:

```prolog
p(X) :- condicion_a(X).
p(X) :- condicion_b(X).
```

### Demo

Programa:

```prolog
madre(nora, luis).
madre(nora, ana).
madre(lidia, jose).
madre(dora, juan).

padre(juan, luis).
padre(juan, ana).
padre(juan, jose).
padre(antonio, juan).

mismo_padre(Persona1, Persona2) :-
    padre(Padre, Persona1),
    padre(Padre, Persona2).

misma_madre(Persona1, Persona2) :-
    madre(Madre, Persona1),
    madre(Madre, Persona2).

hermano(Persona1, Persona2) :-
    mismo_padre(Persona1, Persona2),
    misma_madre(Persona1, Persona2),
    Persona1 \= Persona2.

hermanastro(Persona1, Persona2) :-
    mismo_padre(Persona1, Persona2),
    Persona1 \= Persona2.

hermanastro(Persona1, Persona2) :-
    misma_madre(Persona1, Persona2),
    Persona1 \= Persona2.
```

Consultas:

```prolog
mismo_padre(luis, ana).
mismo_padre(luis, luis).
hermano(luis, ana).
hermano(luis, jose).
hermano(X, Y).
hermanastro(luis, jose).
hermanastro(X, Y).
```

### Qué remarcar

- Sin `Persona1 \= Persona2`, una persona podría aparecer relacionada consigo misma.
- `hermanastro/2` como está definido significa “comparte padre o comparte madre”. Esa definición también incluye hermanos completos.
- Si queremos una definición más estricta, hay que escribir esa restricción.

### Ejercicio 10 minutos

Enunciado inspirado en familia Simpsons:

> Crear una base familiar mínima. Declarar padres y madres. Definir `hermano/2` para que dos personas sean hermanos si comparten padre y madre, pero no son la misma persona.

Base sugerida:

```prolog
padre(homero, bart).
padre(homero, lisa).
padre(homero, maggie).
madre(marge, bart).
madre(marge, lisa).
madre(marge, maggie).
```

Solución posible:

```prolog
mismo_padre(A, B) :-
    padre(Padre, A),
    padre(Padre, B).

misma_madre(A, B) :-
    madre(Madre, A),
    madre(Madre, B).

hermano(A, B) :-
    mismo_padre(A, B),
    misma_madre(A, B),
    A \= B.
```

Consultas:

```prolog
hermano(bart, lisa).
hermano(bart, bart).
hermano(X, lisa).
hermano(X, Y).
```

## 112-127 min | Inversibilidad

Diapositivas 42-44.

### Concepto

En muchos lenguajes pensamos en entradas y salidas. En Prolog, si modelamos relaciones, el mismo predicado puede usarse en distintas direcciones.

Ejemplo:

```prolog
hijo(Hijo, Padre) :- padre(Padre, Hijo).
```

Con una sola regla podemos preguntar:

- si Luis es hijo de Juan;
- quiénes son hijos de Juan;
- de quién es hijo Luis;
- todos los vínculos hijo-padre.

### Demo

Programa:

```prolog
padre(juan, luis).
padre(juan, ana).
padre(juan, jose).
padre(antonio, juan).

hijo(Hijo, Padre) :-
    padre(Padre, Hijo).
```

Consultas:

```prolog
hijo(luis, juan).
hijo(Hijo, juan).
hijo(luis, Padre).
hijo(Hijo, Padre).
```

### Segunda demo del material

Programa:

```prolog
vive(ruben, lanus).
vive(ana, lanus).
vive(laura, boedo).
vive(susi, bernal).

son_vecinos(P1, P2) :-
    vive(P1, Barrio),
    vive(P2, Barrio),
    P1 \= P2.

es_del_sur(P) :- vive(P, lanus).
es_del_sur(P) :- vive(P, bernal).
```

Consultas:

```prolog
vive(ruben, B).
vive(P, lanus).
vive(P, B).
son_vecinos(ruben, X).
son_vecinos(X, ruben).
son_vecinos(X, Y).
es_del_sur(susi).
es_del_sur(P).
```

### Ejercicio 10 minutos

Enunciado:

> Definir `docente_de/2` a partir de `cursa/2` y `dicta/2`. El predicado debe permitir preguntar qué docente tiene un alumno, qué alumnos tiene un docente y todos los pares docente-alumno.

Base:

```prolog
cursa(ana, ia).
cursa(luis, ia).
cursa(maria, algebra).

dicta(alejandro, ia).
dicta(sofia, algebra).
```

Solución posible:

```prolog
docente_de(Docente, Alumno) :-
    dicta(Docente, Materia),
    cursa(Alumno, Materia).
```

Consultas:

```prolog
docente_de(alejandro, ana).
docente_de(Docente, ana).
docente_de(alejandro, Alumno).
docente_de(Docente, Alumno).
```

## 127-142 min | Comparación de individuos, números y aritmética

Diapositivas 45-49.

### Concepto

Hay que separar:

1. **Unificación de términos**.
2. **Evaluación aritmética**.

`=` no calcula. `=` intenta unificar.

`is` evalúa una expresión aritmética del lado derecho.

### Demo: individuos

Consultas:

```prolog
juan = pedro.
juan = juan.
tobi \= juan.
X = juan.
f(3) = f(X).
```

### Demo: aritmética

Programa:

```prolog
siguiente(N, Siguiente) :-
    Siguiente is N + 1.
```

Consultas:

```prolog
siguiente(2, 3).
siguiente(3, N).
siguiente(N, 4).
```

Consultas directas:

```prolog
X = 3 + 2.
X is 3 + 2.
5 =:= 3 + 2.
5 = 3 + 2.
7 > 3 + 2.
4 =< 3 + 2.
```

### Qué remarcar

- `X = 3 + 2` liga `X` al término `3+2`, no al número 5.
- `X is 3 + 2` liga `X` al número 5.
- `siguiente(N, 4)` no despeja `N`; en SWI-Prolog normalmente produce un error de instanciación, porque `is` necesita que `N` ya tenga valor.
- Ese error es esperado y sirve para mostrar que `is/2` no resuelve ecuaciones hacia atrás.
- Operadores de comparación correctos: `<`, `>`, `=<`, `>=`, `=:=`, `=\=`.

### Ejercicio 10 minutos

Enunciado:

> Definir `mayor_de_edad/1` a partir de hechos `edad/2`.

Base:

```prolog
edad(ana, 22).
edad(luis, 17).
edad(maria, 19).
```

Solución posible:

```prolog
mayor_de_edad(Persona) :-
    edad(Persona, Edad),
    Edad >= 18.
```

Consultas:

```prolog
mayor_de_edad(ana).
mayor_de_edad(luis).
mayor_de_edad(X).
```

## 142-152 min | Strings, átomos con espacios y nombres propios

Diapositiva 50.

### Concepto

En los ejemplos usamos átomos simples:

```prolog
socrates.
```

Cuando un nombre tiene espacios, conviene usar comillas simples:

```prolog
escritor('Jorge Luis Borges').
```

En SWI-Prolog, las comillas dobles pueden representar strings; para una clase inicial, usar comillas simples evita ambigüedades cuando queremos átomos.

### Demo

Programa:

```prolog
escritor('Jorge Luis Borges').
escritor('Paulo Coelho').
escritor('Florencia Bonelli').
```

Consultas:

```prolog
escritor('Jorge Luis Borges').
escritor(X).
```

### Ejercicio 10 minutos

Enunciado:

> Declarar tres películas con títulos que tengan espacios y consultar todas las películas cargadas.

Solución posible:

```prolog
pelicula('El secreto de sus ojos').
pelicula('Nueve reinas').
pelicula('Relatos salvajes').
```

Consulta:

```prolog
pelicula(X).
```

## 152-167 min | Functores como individuos compuestos

Diapositivas 51-55.

### Concepto

Un functor puede usarse para construir un dato compuesto.

Ejemplo:

```prolog
vende(pepe, tornillo(5, parker)).
vende(tony, canilla(redonda, hierro, azul)).
```

Acá:

- `vende/2` es el predicado consultable;
- `tornillo(5, parker)` es un término compuesto usado como dato;
- `canilla(redonda, hierro, azul)` también es un término compuesto usado como dato.

No todo lo que tiene forma `nombre(...)` es necesariamente un predicado consultable en la base. Depende de dónde aparece.

### Demo

Programa:

```prolog
vende(pepe, tornillo(5, parker)).
vende(tony, canilla(redonda, hierro, azul)).

nacio(karla, fecha(22, 8, 1979)).
nacio(sergio, fecha(14, 10, 1986)).
nacio(maria, fecha(3, 5, 1986)).
```

Consultas:

```prolog
vende(pepe, Producto).
vende(Vendedor, tornillo(5, Marca)).
nacio(Quien, fecha(_, _, 1986)).
nacio(_, fecha(_, _, Anio)).
```

Error útil:

```prolog
canilla(X, hierro, Y).
```

### Qué remarcar

Si Prolog dice que `canilla/3` no existe, está bien: nunca declaramos un predicado `canilla/3`; declaramos un término `canilla(...)` dentro de `vende/2`.

### Ejercicio 10 minutos

Enunciado:

> Modelar ventas de libros usando un término compuesto `libro(Titulo, Autor, Anio)`. Consultar quién vende libros de cierto autor y qué libros son de cierto año.

Base posible:

```prolog
vende(ana, libro('Ficciones', borges, 1944)).
vende(luis, libro('Rayuela', cortazar, 1963)).
vende(maria, libro('El aleph', borges, 1949)).
```

Consultas esperadas:

```prolog
vende(Quien, libro(_, borges, _)).
vende(_, libro(Titulo, _, 1949)).
vende(_, libro(_, _, Anio)).
```

## 167-182 min | Recursividad

Diapositivas 56-59.

### Concepto

La recursividad en programación lógica consiste en definir un predicado en términos de sí mismo.

Ejemplo conceptual:

> Mis ancestros son mis padres y los ancestros de mis padres.

Una definición recursiva necesita:

- caso base;
- caso recursivo;
- avance hacia el caso base.

### Convención importante

Para evitar confusiones, usamos esta orientación:

```prolog
padre(Padre, Hijo).
```

Entonces `padre(juan, luis)` significa que Juan es padre de Luis.

### Demo

Programa:

```prolog
padre(juan, luis).
padre(antonio, juan).
padre(roberto, antonio).
padre(nora, ana).

ancestro(Ancestro, Persona) :-
    padre(Ancestro, Persona).

ancestro(Ancestro, Persona) :-
    padre(Ancestro, Intermedio),
    ancestro(Intermedio, Persona).
```

Consultas:

```prolog
ancestro(juan, luis).
ancestro(antonio, luis).
ancestro(X, luis).
ancestro(roberto, Persona).
```

### Lectura de las reglas

Caso base:

> Un padre directo es ancestro.

Caso recursivo:

> Si alguien es padre de un intermedio, y ese intermedio es ancestro de una persona, entonces ese alguien también es ancestro de esa persona.

### Ejercicio 10 minutos

Enunciado:

> Extender el árbol familiar con al menos cinco personas y consultar todos los ancestros de una persona.

Base sugerida:

```prolog
padre(mario, sofia).
padre(carlos, mario).
padre(oscar, carlos).
padre(pedro, oscar).
```

Regla esperada:

```prolog
ancestro(Ancestro, Persona) :-
    padre(Ancestro, Persona).

ancestro(Ancestro, Persona) :-
    padre(Ancestro, Intermedio),
    ancestro(Intermedio, Persona).
```

Consulta:

```prolog
ancestro(X, sofia).
```

Preguntas:

- ¿Cuál es el caso base?
- ¿Cuál es el caso recursivo?
- ¿Qué pasaría si cargamos un ciclo, por ejemplo `padre(sofia, pedro)`?

## 182-195 min | Mini práctica integradora: correlatividades académicas

Esta parte conecta con [`actividad-prolog.md`](actividad-prolog.md).

### Contexto

La universidad necesita una herramienta didáctica que responda consultas sobre estudiantes, materias aprobadas y correlatividades.

Relación:

```prolog
correlativa(Materia, Requisito).
```

Ejemplo:

```prolog
correlativa(inteligencia_artificial, algoritmos).
```

se lee:

> Algoritmos es requisito directo de Inteligencia Artificial.

### Base inicial

Usar [`base-inicial.pl`](base-inicial.pl).

Consultas iniciales:

```prolog
estudiante(ana).
aprobo(ana, Materia).
aprobo(Estudiante, algoritmos).
aprobo(Estudiante, Materia).
aprobo(_, programacion_2).
```

### Regla de cursada

Completar:

```prolog
puede_cursar(Estudiante, inteligencia_artificial) :-
    estudiante(Estudiante),
    inscripcion_activa(Estudiante),
    aprobo(Estudiante, algoritmos),
    sin_superposicion(Estudiante, inteligencia_artificial),
    hay_cupo(inteligencia_artificial).
```

Consultas:

```prolog
puede_cursar(ana, inteligencia_artificial).
puede_cursar(bruno, inteligencia_artificial).
puede_cursar(carla, inteligencia_artificial).
puede_cursar(Quien, inteligencia_artificial).
```

### Ejercicio 10 minutos

Enunciado:

> Explicar por qué cada estudiante puede o no puede cursar Inteligencia Artificial. Para cada `false`, identificar qué condición no se pudo demostrar.

Preguntas:

- ¿Quién tiene inscripción activa?
- ¿Quién aprobó Algoritmos?
- ¿Quién no tiene superposición horaria?
- ¿Hay cupo?
- ¿Qué condición falla para Bruno?
- ¿Qué condición falla para Carla?

### Puente hacia la actividad completa

Esta mini práctica sólo cubre la primera parte de [`actividad-prolog.md`](actividad-prolog.md). Si hay tiempo o se deja como tarea, continuar con:

1. **Autorización excepcional**: agregar una segunda cláusula de `puede_cursar/2` para modelar una alternativa controlada.
2. **Correlatividades recursivas**: definir `requisito/2` para encontrar requisitos directos e indirectos.
3. **Auditoría entre pares**: revisar sintaxis, consultas, recursión y riesgos de automatizar decisiones académicas.

Ejemplo de relación recursiva para continuar:

```prolog
requisito(Materia, Requisito) :-
    correlativa(Materia, Requisito).

requisito(Materia, Requisito) :-
    correlativa(Materia, Intermedia),
    requisito(Intermedia, Requisito).
```

Consultas sugeridas:

```prolog
requisito(inteligencia_artificial, programacion_1).
requisito(inteligencia_artificial, Requisito).
requisito(Materia, programacion_1).
```

## Cierre de la clase

### Síntesis oral

- Prolog no parte de instrucciones, parte de conocimiento.
- Un programa Prolog es una base de hechos y reglas.
- Las consultas son objetivos que Prolog intenta probar.
- Las variables permiten pedir respuestas, no sólo validar casos.
- El mundo cerrado hace que lo no demostrable sea tratado como falso.
- La inversibilidad aparece cuando modelamos relaciones, no procedimientos.
- La recursividad permite expresar relaciones transitivas como `ancestro/2` o `requisito/2`.

### Ticket de salida

Responder antes de cerrar:

1. Escribí un hecho, una regla y una consulta.
2. ¿Qué significa `predicado/aridad`?
3. ¿Qué diferencia existe entre una variable nombrada y `_`?
4. ¿Por qué `false` no siempre significa “falso en el mundo real”?
5. ¿Por qué `X = 3 + 2` no da `X = 5`?
6. ¿Qué ventaja tiene que `hijo/2` sea inversible?
7. ¿Por qué `canilla/3` puede no existir aunque aparezca `canilla(...)` dentro de `vende/2`?

## Errores frecuentes y respuesta docente

| Situación | Intervención sugerida |
| --- | --- |
| Escriben una variable con minúscula | Recordar: minúscula representa átomo; mayúscula o `_` inicia variable. |
| Olvidan el punto final | Toda cláusula y toda consulta terminan con `.`. |
| Copian `?-` dentro del archivo | El prompt pertenece a la consola, no al archivo `.pl`. |
| Leen `Cabeza :- Cuerpo` como ejecución imperativa | Reformular: “la cabeza se demuestra si el cuerpo puede demostrarse”. |
| Confunden `=` con cálculo | `=` unifica; `is` evalúa aritmética. |
| Esperan que `siguiente(N, 4)` despeje `N` | `is/2` no resuelve ecuaciones hacia atrás; puede aparecer un error de instanciación. |
| Una relación devuelve una persona consigo misma | Agregar y discutir `A \= B`. |
| La recursión no termina | Revisar caso base, avance y posible ciclo en los datos. |
| Confunden functor con predicado | Revisar si aparece como cláusula o como argumento dentro de otro predicado. |

## Comandos útiles

Ver todo lo cargado:

```prolog
listing.
```

Ver un predicado puntual:

```prolog
listing(hombre/1).
listing(padre/2).
```

Cargar o recargar un archivo:

```prolog
consult('base-inicial.pl').
```

Salir de SWI-Prolog local:

```prolog
halt.
```

Pedir más soluciones:

```text
;
```

Cortar la búsqueda:

```text
Enter
```

## Adaptación a 120 minutos

Si la clase debe durar estrictamente 120 minutos, usar esta versión compacta:

| Tiempo | Bloque |
| --- | --- |
| 0-10 | Puente desde IA simbólica |
| 10-22 | Paradigmas y silogismos |
| 22-38 | Base de conocimiento, individuos y predicados |
| 38-52 | Hechos, reglas y consultas |
| 52-67 | Variables, `_` y múltiples soluciones |
| 67-77 | Mundo cerrado |
| 77-95 | Conjunción, disyunción e inversibilidad |
| 95-108 | Aritmética y unificación |
| 108-118 | Functores y recursividad |
| 118-120 | Ticket de salida |

Los ejercicios pueden quedar como pausas de 10 minutos durante la clase o como trabajo asincrónico, según el ritmo del grupo.

## Prácticas complementarias sugeridas

Estas consignas retoman la plancha de ejercicios de la materia.

### Práctica A — Pokémon

Enunciado:

> Escribir una base de conocimiento con predicados `fuego/1`, `hierba/1` y `electrico/1`. Pikachu y Raichu son eléctricos; Bulbasaur es de hierba; Charmander y Charizard son de fuego.

Consultas:

```prolog
electrico(pikachu).
fuego(X).
hierba(charizard).
electrico(_).
```

### Práctica B — Personajes y barrios

Enunciado:

> Modelar personajes, barrio donde viven y ocupación. Debe poder consultarse `vive_en/2` y ocupaciones como `poeta/1`, `poligrafo/1` o `tahur/1`.

Base posible:

```prolog
vive_en(jorge, flores).
vive_en(manuel, flores).
vive_en(bernardo, flores).
vive_en(el_diablo, villa_crespo).

poeta(jorge).
poligrafo(manuel).
tahur(bernardo).
apodo(bernardo, ruso).
```

Consultas:

```prolog
vive_en(jorge, flores).
vive_en(Quien, flores).
poeta(el_diablo).
apodo(bernardo, Apodo).
```

### Práctica C — Candidatos laborales

Enunciado:

> Una empresa busca candidatos. Roque es contador, honesto y joven. Ana es ingeniera y honesta, pero no joven. Cecilia es abogada. Crear la base y consultas.

Base posible:

```prolog
contador(roque).
honesto(roque).
joven(roque).

ingeniera(ana).
honesto(ana).

abogada(cecilia).
```

Consultas:

```prolog
honesto(ana).
joven(ana).
contador(Quien).
honesto(Quien).
```

Extensión con regla:

```prolog
candidato_junior(X) :-
    joven(X),
    honesto(X).
```

Consulta:

```prolog
candidato_junior(X).
```

## Fuentes

- `Clase 4 - Programación Lógica.pdf`, material de la cátedra.
- `Tutorial de Prolog.pdf`, material complementario de sintaxis, unificación, predicados, listas y recursividad.
- Plancha de ejercitación de programación lógica compartida para la materia.
- [`actividad-prolog.md`](actividad-prolog.md) y [`base-inicial.pl`](base-inicial.pl), materiales de soporte de esta carpeta.
