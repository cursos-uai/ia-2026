<!-- markdownlint-disable MD013 MD024 MD029 MD051 -->

# Guion docente - Clase 4: Programación lógica con Prolog

Esta guía acompaña la clase 4 y está pensada para que el alumno pueda seguir una hoja de ruta paso a paso: primero entiende el concepto, después copia una base de conocimiento, ejecuta consultas y finalmente resuelve ejercicios breves.

## Índice

- [1. Datos generales](#1-datos-generales)
- [2. Resultados de aprendizaje](#2-resultados-de-aprendizaje)
- [3. Preparación antes de la clase](#3-preparacion-antes-de-la-clase)
- [4. Dinámica de trabajo](#4-dinamica-de-trabajo)
  - [4.1. Cómo usar el recorrido](#41-como-usar-el-recorrido)
- [5. Puente desde IA simbólica](#5-puente-desde-ia-simbolica)
  - [5.1. Concepto](#51-concepto)
  - [5.2. Guion oral sugerido](#52-guion-oral-sugerido)
  - [5.3. Primer ejemplo](#53-primer-ejemplo)
  - [5.4. Preguntas de control](#54-preguntas-de-control)
- [6. Paradigmas, silogismos y programas lógicos](#6-paradigmas-silogismos-y-programas-logicos)
  - [6.1. Concepto](#61-concepto)
  - [6.2. Demo](#62-demo)
  - [6.3. Qué observar](#63-que-observar)
  - [6.4. Ejercicio guiado](#64-ejercicio-guiado)
- [7. Base de conocimiento, individuos, predicados y aridad](#7-base-de-conocimiento-individuos-predicados-y-aridad)
  - [7.1. Concepto](#71-concepto)
  - [7.2. Demo](#72-demo)
  - [7.3. Qué remarcar](#73-que-remarcar)
  - [7.4. Ejercicio guiado](#74-ejercicio-guiado)
- [8. Cláusulas: hechos y reglas](#8-clausulas-hechos-y-reglas)
  - [8.1. Concepto](#81-concepto)
  - [8.2. Corrección conceptual importante](#82-correccion-conceptual-importante)
  - [8.3. Demo](#83-demo)
  - [8.4. Ejercicio guiado](#84-ejercicio-guiado)
- [9. Consultas individuales, existenciales y múltiples soluciones](#9-consultas-individuales-existenciales-y-multiples-soluciones)
  - [9.1. Concepto](#91-concepto)
  - [9.2. Demo](#92-demo)
  - [9.3. Qué remarcar](#93-que-remarcar)
  - [9.4. Ejercicio guiado](#94-ejercicio-guiado)
  - [9.5. Nota docente sobre negación](#95-nota-docente-sobre-negacion)
- [10. Universo cerrado: qué significa `false`](#10-universo-cerrado-que-significa-false)
  - [10.1. Concepto](#101-concepto)
  - [10.2. Demo paso a paso](#102-demo-paso-a-paso)
  - [10.3. Ejercicio guiado](#103-ejercicio-guiado)
- [11. Pregunta bisagra](#11-pregunta-bisagra)
- [12. Variables, variable anónima y búsqueda de soluciones](#12-variables-variable-anonima-y-busqueda-de-soluciones)
  - [12.1. Concepto](#121-concepto)
  - [12.2. Demo](#122-demo)
  - [12.3. Ejercicio guiado](#123-ejercicio-guiado)
- [13. Conjunción, disyunción y desigualdad](#13-conjuncion-disyuncion-y-desigualdad)
  - [13.1. Concepto](#131-concepto)
  - [13.2. Demo](#132-demo)
  - [13.3. Qué remarcar](#133-que-remarcar)
  - [13.4. Ejercicio guiado](#134-ejercicio-guiado)
- [14. Inversibilidad](#14-inversibilidad)
  - [14.1. Concepto](#141-concepto)
  - [14.2. Demo](#142-demo)
  - [14.3. Segunda demo del material](#143-segunda-demo-del-material)
  - [14.4. Ejercicio guiado](#144-ejercicio-guiado)
- [15. Comparación de individuos, números y aritmética](#15-comparacion-de-individuos-numeros-y-aritmetica)
  - [15.1. Concepto](#151-concepto)
  - [15.2. Demo: individuos](#152-demo-individuos)
  - [15.3. Demo: aritmética](#153-demo-aritmetica)
  - [15.4. Qué remarcar](#154-que-remarcar)
  - [15.5. Ejercicio guiado](#155-ejercicio-guiado)
- [16. Strings, átomos con espacios y nombres propios](#16-strings-atomos-con-espacios-y-nombres-propios)
  - [16.1. Concepto](#161-concepto)
  - [16.2. Demo](#162-demo)
  - [16.3. Ejercicio guiado](#163-ejercicio-guiado)
- [17. Functores como individuos compuestos](#17-functores-como-individuos-compuestos)
  - [17.1. Concepto](#171-concepto)
  - [17.2. Demo](#172-demo)
  - [17.3. Qué remarcar](#173-que-remarcar)
  - [17.4. Ejercicio guiado](#174-ejercicio-guiado)
- [18. Recursividad](#18-recursividad)
  - [18.1. Concepto](#181-concepto)
  - [18.2. Convención importante](#182-convencion-importante)
  - [18.3. Demo](#183-demo)
  - [18.4. Lectura de las reglas](#184-lectura-de-las-reglas)
  - [18.5. Ejercicio guiado](#185-ejercicio-guiado)
- [19. Mini práctica integradora: correlatividades académicas](#19-mini-practica-integradora-correlatividades-academicas)
  - [19.1. Contexto](#191-contexto)
  - [19.2. Base inicial](#192-base-inicial)
  - [19.3. Regla de cursada](#193-regla-de-cursada)
  - [19.4. Ejercicio guiado](#194-ejercicio-guiado)
  - [19.5. Puente hacia la actividad completa](#195-puente-hacia-la-actividad-completa)
- [20. Cierre de la clase](#20-cierre-de-la-clase)
  - [20.1. Síntesis oral](#201-sintesis-oral)
  - [20.2. Ticket de salida](#202-ticket-de-salida)
- [21. Errores frecuentes y respuesta docente](#21-errores-frecuentes-y-respuesta-docente)
- [22. Comandos útiles](#22-comandos-utiles)
- [23. Recorrido compacto sugerido](#23-recorrido-compacto-sugerido)
- [24. Prácticas complementarias sugeridas](#24-practicas-complementarias-sugeridas)
  - [24.1. Práctica A — Pokémon](#241-practica-a-pokemon)
  - [24.2. Práctica B — Personajes y barrios](#242-practica-b-personajes-y-barrios)
  - [24.3. Práctica C — Candidatos laborales](#243-practica-c-candidatos-laborales)
- [25. Fuentes](#25-fuentes)

## 1. Datos generales

- Unidad: Lógica simbólica.
- Material principal: `Clase 4 - Programación Lógica.pdf` (59 diapositivas).
- Modalidad: explicación conceptual, demostraciones en Prolog y ejercicios guiados.
- Entorno sugerido: [SWISH](https://swish.swi-prolog.org/) o SWI-Prolog local.
- Requisito: conceptos de símbolo, hecho, regla e inferencia trabajados en la Clase 3.

## 2. Resultados de aprendizaje

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

## 3. Preparación antes de la clase

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

## 4. Dinámica de trabajo

Para cada bloque:

1. Leer la explicación conceptual.
2. Copiar el programa base.
3. Ejecutar las consultas sugeridas.
4. Anticipar el resultado antes de ejecutar.
5. Resolver el ejercicio guiado.
6. Comparar con una solución posible.

### 4.1. Cómo usar el recorrido

El archivo funciona como una hoja de ruta guiada y como banco de actividades.
No hace falta ejecutar todos los ejemplos en una única clase: elegí los bloques
según el ritmo del grupo y dejá el resto como práctica asincrónica o material
de repaso.

Recorrido sugerido para una clase compacta:

| Orden | Bloque |
| --- | --- |
| 1 | Puente desde IA simbólica |
| 2 | Paradigmas y silogismos |
| 3 | Base de conocimiento, individuos y predicados |
| 4 | Hechos, reglas y consultas |
| 5 | Variables, `_` y múltiples soluciones |
| 6 | Mundo cerrado |
| 7 | Conjunción, disyunción e inversibilidad |
| 8 | Aritmética y unificación |
| 9 | Functores y recursividad |
| 10 | Ticket de salida |

A partir de acá se ofrece el recorrido detallado, con más desarrollo y
ejercicios que los necesarios para una única clase.

## 5. Puente desde IA simbólica

### 5.1. Concepto

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

### 5.2. Guion oral sugerido

> En esta clase no vamos a pensar primero en algoritmos paso a paso. Vamos a pensar qué sabemos del mundo que queremos modelar. En Prolog escribimos hechos y reglas; después consultamos al motor para que intente probar respuestas.

### 5.3. Primer ejemplo

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

### 5.4. Preguntas de control

- ¿Cuál es el hecho?
- ¿Cuál es la regla?
- ¿La conclusión `mortal(socrates)` está escrita o se deriva?

## 6. Paradigmas, silogismos y programas lógicos

Diapositivas 2-8.

### 6.1. Concepto

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

### 6.2. Demo

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

### 6.3. Qué observar

- `mortal(socrates)` da verdadero aunque no esté escrito como hecho.
- Se deriva por la regla `mortal(X) :- humano(X)`.
- `mortal(aristoteles)` falla si no declaramos `humano(aristoteles)`.

### 6.4. Ejercicio guiado

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

## 7. Base de conocimiento, individuos, predicados y aridad

Diapositivas 9-14.

### 7.1. Concepto

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

### 7.2. Demo

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

### 7.3. Qué remarcar

- `vive(socrates, atenas)` no devuelve un valor: afirma una relación.
- `son_conciudadanos/2` no está listado como hecho: se infiere desde `vive/2`.
- `P1 \= P2` evita que una persona sea conciudadana de sí misma.

### 7.4. Ejercicio guiado

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

## 8. Cláusulas: hechos y reglas

Diapositivas 15-18 y 31-33.

### 8.1. Concepto

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

### 8.2. Corrección conceptual importante

Si se mira la regla como implicación lógica:

```prolog
mortal(X) :- humano(X).
```

el antecedente es `humano(X)` y el consecuente es `mortal(X)`. No hay que invertirlos.

### 8.3. Demo

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

### 8.4. Ejercicio guiado

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

## 9. Consultas individuales, existenciales y múltiples soluciones

Diapositivas 17-30.

### 9.1. Concepto

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

### 9.2. Demo

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

### 9.3. Qué remarcar

- Una variable nombrada, como `Pasta`, conserva y muestra su valor.
- `_` es una variable anónima: hay un valor, pero no nos interesa mostrarlo.
- Cada aparición de `_` es independiente.
- El `;` pide otra solución.
- Enter corta la búsqueda de más soluciones.

### 9.4. Ejercicio guiado

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

### 9.5. Nota docente sobre negación

En esta etapa usamos `no_come/2` como un predicado explícito. Todavía no estamos usando negación por fallo (`\+`). Es importante no mezclar ambas ideas demasiado temprano.

## 10. Universo cerrado: qué significa `false`

Diapositivas 22-24 y 34-36.

### 10.1. Concepto

Prolog trabaja con el principio de **mundo cerrado**:

> Todo lo que no pueda probarse como verdadero con la base disponible se considera falso.

Esto no significa que sea falso en el mundo real. Significa que el sistema no tiene información suficiente para demostrarlo.

### 10.2. Demo paso a paso

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

### 10.3. Ejercicio guiado

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

## 11. Pregunta bisagra

Dejar proyectada esta pregunta:

> ¿Una respuesta de Prolog es un dato almacenado o una demostración construida?

Respuesta esperada:

> Puede ser ambas cosas: a veces se recupera un hecho; otras veces se deriva una conclusión a partir de reglas.

## 12. Variables, variable anónima y búsqueda de soluciones

### 12.1. Concepto

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

### 12.2. Demo

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

### 12.3. Ejercicio guiado

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

## 13. Conjunción, disyunción y desigualdad

Diapositivas 37-41.

### 13.1. Concepto

La conjunción lógica, es decir “Y”, se escribe con coma:

```prolog
condicion1, condicion2
```

La disyunción lógica, es decir “O”, suele modelarse con varias cláusulas para el mismo predicado:

```prolog
p(X) :- condicion_a(X).
p(X) :- condicion_b(X).
```

### 13.2. Demo

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

### 13.3. Qué remarcar

- Sin `Persona1 \= Persona2`, una persona podría aparecer relacionada consigo misma.
- `hermanastro/2` como está definido significa “comparte padre o comparte madre”. Esa definición también incluye hermanos completos.
- Si queremos una definición más estricta, hay que escribir esa restricción.

### 13.4. Ejercicio guiado

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

## 14. Inversibilidad

Diapositivas 42-44.

### 14.1. Concepto

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

### 14.2. Demo

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

### 14.3. Segunda demo del material

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

### 14.4. Ejercicio guiado

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

## 15. Comparación de individuos, números y aritmética

Diapositivas 45-49.

### 15.1. Concepto

Hay que separar:

1. **Unificación de términos**.
2. **Evaluación aritmética**.

`=` no calcula. `=` intenta unificar.

`is` evalúa una expresión aritmética del lado derecho.

### 15.2. Demo: individuos

Consultas:

```prolog
juan = pedro.
juan = juan.
tobi \= juan.
X = juan.
f(3) = f(X).
```

### 15.3. Demo: aritmética

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

### 15.4. Qué remarcar

- `X = 3 + 2` liga `X` al término `3+2`, no al número 5.
- `X is 3 + 2` liga `X` al número 5.
- `siguiente(N, 4)` no despeja `N`; en SWI-Prolog normalmente produce un error de instanciación, porque `is` necesita que `N` ya tenga valor.
- Ese error es esperado y sirve para mostrar que `is/2` no resuelve ecuaciones hacia atrás.
- Operadores de comparación correctos: `<`, `>`, `=<`, `>=`, `=:=`, `=\=`.

### 15.5. Ejercicio guiado

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

## 16. Strings, átomos con espacios y nombres propios

Diapositiva 50.

### 16.1. Concepto

En los ejemplos usamos átomos simples:

```prolog
socrates.
```

Cuando un nombre tiene espacios, conviene usar comillas simples:

```prolog
escritor('Jorge Luis Borges').
```

En SWI-Prolog, las comillas dobles pueden representar strings; para una clase inicial, usar comillas simples evita ambigüedades cuando queremos átomos.

### 16.2. Demo

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

### 16.3. Ejercicio guiado

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

## 17. Functores como individuos compuestos

Diapositivas 51-55.

### 17.1. Concepto

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

### 17.2. Demo

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

### 17.3. Qué remarcar

Si Prolog dice que `canilla/3` no existe, está bien: nunca declaramos un predicado `canilla/3`; declaramos un término `canilla(...)` dentro de `vende/2`.

### 17.4. Ejercicio guiado

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

## 18. Recursividad

Diapositivas 56-59.

### 18.1. Concepto

La recursividad en programación lógica consiste en definir un predicado en términos de sí mismo.

Ejemplo conceptual:

> Mis ancestros son mis padres y los ancestros de mis padres.

Una definición recursiva necesita:

- caso base;
- caso recursivo;
- avance hacia el caso base.

### 18.2. Convención importante

Para evitar confusiones, usamos esta orientación:

```prolog
padre(Padre, Hijo).
```

Entonces `padre(juan, luis)` significa que Juan es padre de Luis.

### 18.3. Demo

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

### 18.4. Lectura de las reglas

Caso base:

> Un padre directo es ancestro.

Caso recursivo:

> Si alguien es padre de un intermedio, y ese intermedio es ancestro de una persona, entonces ese alguien también es ancestro de esa persona.

### 18.5. Ejercicio guiado

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

## 19. Mini práctica integradora: correlatividades académicas

Esta parte conecta con [`actividad-prolog.md`](actividad-prolog.md).

### 19.1. Contexto

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

### 19.2. Base inicial

Usar [`base-inicial.pl`](base-inicial.pl).

Consultas iniciales:

```prolog
estudiante(ana).
aprobo(ana, Materia).
aprobo(Estudiante, algoritmos).
aprobo(Estudiante, Materia).
aprobo(_, programacion_2).
```

### 19.3. Regla de cursada

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

### 19.4. Ejercicio guiado

Enunciado:

> Explicar por qué cada estudiante puede o no puede cursar Inteligencia Artificial. Para cada `false`, identificar qué condición no se pudo demostrar.

Preguntas:

- ¿Quién tiene inscripción activa?
- ¿Quién aprobó Algoritmos?
- ¿Quién no tiene superposición horaria?
- ¿Hay cupo?
- ¿Qué condición falla para Bruno?
- ¿Qué condición falla para Carla?

### 19.5. Puente hacia la actividad completa

Esta mini práctica sólo cubre la primera parte de [`actividad-prolog.md`](actividad-prolog.md). Como continuación o tarea, seguir con:

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

## 20. Cierre de la clase

### 20.1. Síntesis oral

- Prolog no parte de instrucciones, parte de conocimiento.
- Un programa Prolog es una base de hechos y reglas.
- Las consultas son objetivos que Prolog intenta probar.
- Las variables permiten pedir respuestas, no sólo validar casos.
- El mundo cerrado hace que lo no demostrable sea tratado como falso.
- La inversibilidad aparece cuando modelamos relaciones, no procedimientos.
- La recursividad permite expresar relaciones transitivas como `ancestro/2` o `requisito/2`.

### 20.2. Ticket de salida

Responder antes de cerrar:

1. Escribí un hecho, una regla y una consulta.
2. ¿Qué significa `predicado/aridad`?
3. ¿Qué diferencia existe entre una variable nombrada y `_`?
4. ¿Por qué `false` no siempre significa “falso en el mundo real”?
5. ¿Por qué `X = 3 + 2` no da `X = 5`?
6. ¿Qué ventaja tiene que `hijo/2` sea inversible?
7. ¿Por qué `canilla/3` puede no existir aunque aparezca `canilla(...)` dentro de `vende/2`?

## 21. Errores frecuentes y respuesta docente

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

## 22. Comandos útiles

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

## 23. Recorrido compacto sugerido

Si necesitás una versión más breve, usar esta secuencia:

| Orden | Bloque |
| --- | --- |
| 1 | Puente desde IA simbólica |
| 2 | Paradigmas y silogismos |
| 3 | Base de conocimiento, individuos y predicados |
| 4 | Hechos, reglas y consultas |
| 5 | Variables, `_` y múltiples soluciones |
| 6 | Mundo cerrado |
| 7 | Conjunción, disyunción e inversibilidad |
| 8 | Aritmética y unificación |
| 9 | Functores y recursividad |
| 10 | Ticket de salida |

Los ejercicios pueden resolverse durante la clase o quedar como trabajo asincrónico, según el ritmo del grupo.

## 24. Prácticas complementarias sugeridas

Estas consignas retoman la plancha de ejercicios de la materia.

### 24.1. Práctica A — Pokémon

Enunciado:

> Escribir una base de conocimiento con predicados `fuego/1`, `hierba/1` y `electrico/1`. Pikachu y Raichu son eléctricos; Bulbasaur es de hierba; Charmander y Charizard son de fuego.

Consultas:

```prolog
electrico(pikachu).
fuego(X).
hierba(charizard).
electrico(_).
```

### 24.2. Práctica B — Personajes y barrios

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

### 24.3. Práctica C — Candidatos laborales

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

## 25. Fuentes

- `Clase 4 - Programación Lógica.pdf`, material de la cátedra.
- `Tutorial de Prolog.pdf`, material complementario de sintaxis, unificación, predicados, listas y recursividad.
- Plancha de ejercitación de programación lógica compartida para la materia.
- [`actividad-prolog.md`](actividad-prolog.md) y [`base-inicial.pl`](base-inicial.pl), materiales de soporte de esta carpeta.
