# Apunte - Inteligencia Artificial simbólica

## Objetivos

Al finalizar esta lectura deberías poder:

- explicar qué significa representar conocimiento mediante símbolos;
- distinguir hechos, reglas y conclusiones;
- describir cómo funciona un sistema basado en conocimiento;
- reconocer ventajas y límites de la IA simbólica;
- analizar MYCIN como caso histórico de sistema experto;
- relacionar este enfoque con la programación lógica que se abordará en la próxima clase.

## 1. Representar para poder razonar

Un sistema de inteligencia artificial no opera directamente sobre personas, objetos o situaciones del mundo. Opera sobre **representaciones**. Un símbolo sustituye, dentro de un modelo, algo que queremos describir: una persona, una propiedad, una relación o un acontecimiento.

Por ejemplo:

```text
docente(ana)
enseña(ana, inteligencia_artificial)
```

`ana` e `inteligencia_artificial` son símbolos. `docente` representa una propiedad y `enseña` una relación. La representación conserva algunos aspectos del mundo y deja otros afuera. Por eso, modelar no consiste solo en escribir datos: implica decidir qué resulta relevante para el problema.

Un mismo objeto también puede recibir significados diferentes según el contexto. La palabra “manzana” puede referir a una fruta, a una cuadra urbana o a una empresa. Para operar correctamente, el sistema necesita una representación que reduzca esa ambigüedad.

## 2. El enfoque simbólico

La IA simbólica propone representar explícitamente el conocimiento y manipularlo mediante procedimientos definidos. Suele describirse como un enfoque **descendente** o *top-down*: las personas identifican conceptos y relaciones del dominio, los expresan formalmente y construyen mecanismos capaces de razonar con ellos.

Un sistema procesador de símbolos puede:

- almacenar símbolos;
- crear o modificar relaciones entre ellos;
- aplicar reglas;
- producir nuevas representaciones o conclusiones.

El enfoque puede pensarse en tres niveles:

1. **Teoría:** qué capacidad inteligente se intenta explicar o reproducir.
2. **Modelo formal:** cómo se representan objetos, relaciones y reglas.
3. **Implementación:** cómo un programa almacena la representación y ejecuta el razonamiento.

Esta separación es importante: una misma idea puede implementarse de distintas maneras, y una implementación técnicamente correcta puede producir resultados incorrectos si el modelo representa mal el problema.

## 3. Hechos, reglas e inferencia

Una base de conocimiento contiene afirmaciones explícitas sobre un dominio. Algunas pueden tratarse como hechos y otras como reglas generales.

```text
Hecho: Sócrates es humano.
Regla: Si alguien es humano, entonces es mortal.
Conclusión: Sócrates es mortal.
```

La conclusión no necesita estar almacenada como un hecho independiente: puede ser **inferida** al aplicar la regla. La inferencia es el proceso que obtiene una nueva afirmación a partir del conocimiento disponible.

Podemos representarlo de forma simplificada:

```text
humano(socrates)
humano(X) -> mortal(X)
por lo tanto: mortal(socrates)
```

La conclusión será confiable solamente si:

- los hechos de partida son adecuados;
- las reglas están bien formuladas;
- el mecanismo de inferencia aplica correctamente esas reglas;
- el problema real puede representarse razonablemente dentro del modelo.

Una deducción válida no corrige hechos falsos ni reglas defectuosas.

## 4. Del lenguaje a una representación simbólica

El material de la clase usa la pregunta “Hola, ¿cuánta memoria tenés?” para mostrar tres etapas conceptuales:

1. **Interpretación:** se identifican símbolos como saludo, pregunta, acción, actor y objeto.
2. **Razonamiento:** esos símbolos se relacionan con reglas y hechos almacenados, por ejemplo que la computadora tiene 10 GB de memoria.
3. **Verbalización:** la conclusión se convierte en una respuesta comprensible para la persona.

```text
Entrada en lenguaje natural
        ↓
Representación simbólica
        ↓
Reglas + hechos + inferencia
        ↓
Respuesta en lenguaje natural
```

Esto no implica necesariamente que la computadora comprenda la pregunta como una persona. Su significado operativo depende de las categorías, relaciones y reglas previstas por quienes diseñaron el sistema.

## 5. Sistemas basados en conocimiento

Russell y Norvig llaman **agente basado en conocimiento** a un agente cuyo componente central es una base de conocimiento. El agente incorpora información, consulta qué se sigue de ella y elige una acción. En el libro, estas operaciones se presentan con los nombres `TELL` —agregar conocimiento— y `ASK` —consultar lo que puede inferirse—.

El ciclo conceptual es:

```text
percibir → incorporar conocimiento → consultar/inferir → actuar → registrar la acción
```

Esta arquitectura permite describir el comportamiento en dos niveles:

- **nivel de conocimiento:** qué sabe el agente y qué objetivos tiene;
- **nivel de implementación:** qué estructuras de datos y algoritmos utiliza.

El conocimiento declarativo expresa afirmaciones sobre el mundo. El conocimiento procedimental codifica directamente cómo actuar. Los sistemas reales pueden combinar ambos.

## 6. Sistemas expertos

Un sistema experto intenta reproducir parte del razonamiento de especialistas dentro de un dominio acotado. En forma simplificada incluye:

- una **base de conocimiento** con hechos y reglas del dominio;
- información sobre el caso particular;
- un **motor de inferencia** que aplica reglas;
- una salida con conclusiones o recomendaciones;
- cuando el diseño lo permite, una explicación del recorrido seguido.

La especialización es una fortaleza y también un límite. El sistema puede alcanzar buen desempeño en los casos previstos, pero no posee automáticamente conocimiento general para responder ante situaciones nuevas.

## 7. El caso MYCIN

MYCIN fue desarrollado en Stanford durante la década de 1970 para apoyar la identificación de infecciones bacterianas y la selección de tratamientos. Su conocimiento estaba organizado en cientos de reglas obtenidas mediante trabajo con especialistas. Además, incorporaba **factores de certeza** para tratar la incertidumbre de las conclusiones médicas.

MYCIN es relevante porque permite observar varios rasgos de los sistemas expertos:

- conocimiento específico de un dominio;
- reglas explícitas;
- recomendaciones derivadas de datos del caso;
- capacidad de explicar parte del razonamiento;
- dificultad para validar, mantener y desplegar un sistema en un contexto de alto riesgo.

Las evaluaciones históricas mostraron resultados competitivos en escenarios controlados, pero esto no equivale a una validación clínica integral. Una explicación visible tampoco garantiza que una recomendación sea correcta, segura o justa.

El caso abre una pregunta que sigue vigente: si una recomendación automatizada produce daño, la responsabilidad no puede analizarse mirando solo el algoritmo. También intervienen la calidad del conocimiento, la validación, la institución, el contexto de uso y la supervisión profesional.

## 8. Ventajas de la IA simbólica

- **Conocimiento explícito:** las reglas pueden inspeccionarse y discutirse.
- **Trazabilidad:** es posible reconstruir cómo se obtuvo una conclusión.
- **Eficacia con pocos datos:** no siempre necesita grandes conjuntos de entrenamiento.
- **Control:** las restricciones importantes pueden expresarse directamente.
- **Utilidad en dominios estructurados:** funciona bien cuando los conceptos y reglas son relativamente estables.

## 9. Límites

- **Rigidez:** las excepciones pueden exigir nuevas reglas o cambios en reglas existentes.
- **Cuello de botella del conocimiento:** obtener y formalizar el saber de especialistas demanda tiempo.
- **Mantenimiento:** muchas reglas pueden interactuar, contradecirse o quedar desactualizadas.
- **Incertidumbre y ambigüedad:** no siempre se reducen bien a reglas binarias.
- **Escalabilidad:** una solución efectiva en un dominio pequeño puede fallar al crecer la cantidad de casos y combinaciones.
- **Aprendizaje limitado:** un sistema puramente simbólico no incorpora experiencia automáticamente, salvo que se agreguen mecanismos específicos.

Estas limitaciones contribuyeron a períodos de caída de expectativas y financiamiento conocidos como **inviernos de la IA**. No hubo una única causa ni un único episodio: influyeron promesas exageradas, límites de cómputo, problemas de escalabilidad y dificultades para construir y mantener sistemas complejos.

## 10. IA simbólica, aprendizaje automático y sistemas híbridos

| Aspecto | IA simbólica | Aprendizaje automático |
|---|---|---|
| Origen del conocimiento | Reglas y representaciones diseñadas | Patrones aprendidos de datos |
| Explicación | El recorrido puede ser trazable | Puede resultar difícil de interpretar |
| Necesidad principal | Ingeniería de conocimiento | Datos y entrenamiento |
| Fortaleza típica | Problemas estructurados y restricciones | Variabilidad, percepción y generalización empírica |
| Riesgo típico | Rigidez y reglas incompletas | Sesgos de datos y comportamiento opaco |

La división no es absoluta. Un sistema híbrido puede, por ejemplo, usar un modelo aprendido para detectar un patrón y reglas explícitas para validar restricciones legales o de seguridad.

## 11. Lectura del libro de la materia

Lectura principal:

- Stuart Russell y Peter Norvig, *Artificial Intelligence: A Modern Approach*, 4.ª edición global, **capítulo 7, sección 7.1, “Knowledge-Based Agents”, páginas 227-228**.

Durante la lectura, identificar:

1. qué es una base de conocimiento;
2. qué funciones cumplen `TELL` y `ASK`;
3. qué diferencia hay entre nivel de conocimiento y nivel de implementación;
4. cómo se distinguen los enfoques declarativo y procedimental.

Lectura histórica complementaria:

- Capítulo 1, sección 1.3.2, “Early enthusiasm, great expectations”, especialmente la hipótesis del sistema físico de símbolos y el *Advice Taker*, páginas 37-38.
- Capítulo 1, sección 1.3.4, “Expert systems”, páginas 40-42, con atención a DENDRAL, MYCIN, la importancia del conocimiento específico y las dificultades de mantenimiento.

### Preguntas de lectura

1. ¿Por qué una base de conocimiento no es solamente una colección de datos?
2. ¿Qué ventaja ofrece separar qué sabe el agente de cómo está implementado?
3. ¿Qué cambió cuando los investigadores pasaron de métodos generales a conocimiento específico del dominio?
4. ¿Qué diferencias encontrás entre la presentación de MYCIN del libro y la del material de clase?
5. ¿Qué limitación histórica de los sistemas expertos sigue siendo relevante hoy?

## 12. Síntesis

La IA simbólica representa conocimiento mediante símbolos y reglas explícitas. A partir de hechos, un mecanismo de inferencia puede derivar conclusiones y explicar parte del recorrido. Esta transparencia resulta valiosa, pero no elimina los problemas de modelado, incertidumbre, excepciones, mantenimiento y responsabilidad.

En la próxima clase, estas ideas se traducirán a una forma ejecutable mediante programación lógica: hechos, reglas, consultas, variables y unificación.

## Fuentes

- Gastón Weingand, `Clase 3 - IA simbólica.pdf`, 25 diapositivas, material de la cátedra.
- Stuart Russell y Peter Norvig, *Artificial Intelligence: A Modern Approach*, Global Edition, 4th ed., capítulos 1 y 7, material bibliográfico de la materia.
