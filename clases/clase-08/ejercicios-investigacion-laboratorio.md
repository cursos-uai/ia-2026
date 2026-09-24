# Ejercicios de investigación y laboratorio

## Propósito

Estas actividades conectan la presentación con literatura académica, documentación técnica y repositorios de código. No se busca copiar definiciones: cada respuesta debe relacionar una afirmación con una fuente y, cuando corresponda, con evidencia de ejecución.

## Reglas de trabajo

- Trabajar en parejas, salvo indicación docente.
- Registrar título, autor u organización, año, enlace y fecha de consulta de cada fuente.
- Distinguir entre paper, documentación oficial, repositorio de código y publicación informal.
- Para cada prueba, conservar comando o notebook, versión de herramientas, salida obtenida y una breve interpretación.
- No incorporar datos personales o financieros reales. Utilizar datos públicos, anonimizados o sintéticos.
- Si un ejemplo no funciona, documentar el error exacto y la hipótesis sobre su causa; eso también constituye evidencia.

## Ejercicio 1 - Investigar las V de Big Data

**Duración estimada:** 35 minutos.

### Consigna

1. Localicen tres fuentes que definan las dimensiones de Big Data. Al menos una debe ser académica o institucional y otra debe provenir de documentación de una empresa tecnológica reconocida.
2. Construyan una tabla comparativa con: V utilizada, definición, ejemplo y fuente.
3. Identifiquen qué dimensiones aparecen en las tres fuentes y cuáles cambian.
4. Analicen la diapositiva 3 y respondan si “viabilidad” y “visualización” son parte de una taxonomía universal.
5. Propongan una versión de cinco a siete dimensiones para un sistema de pagos y justifiquen cada elección.

### Evidencia a entregar

- Tabla comparativa con citas enlazadas.
- Un párrafo de 150 a 250 palabras que explique por qué existen taxonomías diferentes.
- Un ejemplo propio que no aparezca en las fuentes.

### Criterio de calidad

Una respuesta sólida no decide la lista correcta por cantidad de resultados en un buscador: compara procedencia, fecha, propósito y significado de cada dimensión.

## Ejercicio 2 - Leer el paper de MapReduce como investigadores

**Duración estimada:** 50 minutos.

### Fuente principal

- Dean y Ghemawat, [MapReduce: Simplified Data Processing on Large Clusters](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/) (OSDI 2004).

### Consigna

1. Lean el resumen, la introducción y las secciones dedicadas al modelo de programación y tolerancia a fallos.
2. Expliquen con sus palabras qué reciben y qué producen las funciones `map` y `reduce`.
3. Dibujen el recorrido de un registro desde la entrada hasta la salida.
4. Identifiquen dos responsabilidades que asume el runtime en lugar del programador.
5. Busquen en el paper una limitación, decisión de diseño o contexto histórico que no aparezca en las diapositivas.
6. Comparen lo leído con las afirmaciones de las diapositivas 20 y 21. Clasifiquen cada afirmación como respaldada, demasiado general o no respaldada por el paper.

### Evidencia a entregar

- Diagrama propio del flujo.
- Tres fragmentos localizados por número de sección, parafraseados y no copiados extensamente.
- Matriz “afirmación de la clase / evidencia / veredicto”.

### Pregunta de transferencia

¿Por qué un modelo pensado para procesar grandes lotes no garantiza por sí mismo detectar fraude en pocos milisegundos?

## Ejercicio 3 - Auditar y ejecutar WordCount en Hadoop

**Duración estimada:** 45 minutos de análisis y 30 minutos opcionales de ejecución.

### Repositorio

- [WordCount oficial de Apache Hadoop](https://github.com/apache/hadoop/blob/trunk/hadoop-mapreduce-project/hadoop-mapreduce-examples/src/main/java/org/apache/hadoop/examples/WordCount.java).

### Consigna

1. Abran el archivo del repositorio y localicen `TokenizerMapper`, `IntSumReducer` y `main`.
2. Anoten qué pares clave-valor emite el mapper para la frase `big data big machine learning`.
3. Simulen manualmente el agrupamiento intermedio y la salida del reducer.
4. Expliquen para qué se configura el reducer también como combiner y por qué eso no sería seguro para cualquier operación.
5. Identifiquen dónde se declaran rutas de entrada y salida y qué ocurre si la cantidad de argumentos es insuficiente.

### Extensión ejecutable

Quienes dispongan de un entorno Hadoop pueden clonar el repositorio oficial y ejecutar el ejemplo incluido en la distribución. Si no cuentan con ese entorno, deben completar la simulación y comparar el código con la salida esperada.

### Evidencia a entregar

- Tabla con salida del mapper, agrupamiento y salida del reducer.
- Enlace permanente al archivo o commit analizado.
- Captura o registro de ejecución; si no se ejecutó, explicación del requisito faltante.

## Ejercicio 4 - Probar el mismo patrón con Apache Spark

**Duración estimada:** 60 minutos.

### Repositorios y lectura

- [Inicio rápido oficial de Apache Spark](https://github.com/apache/spark/blob/master/docs/quick-start.md).
- [Repositorio oficial de Apache Spark](https://github.com/apache/spark).
- Para profundizar: Zaharia y colaboradores, [Resilient Distributed Datasets](https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/zaharia) (NSDI 2012).

### Consigna

1. Sigan el ejemplo de conteo de palabras del inicio rápido utilizando PySpark local o un notebook con PySpark disponible.
2. Cambien el texto de entrada por un archivo breve elegido por el grupo y documenten su licencia o procedencia.
3. Expliquen qué operaciones transforman datos y cuál provoca la ejecución y devuelve un resultado.
4. Ejecuten dos veces una consulta antes y después de utilizar `cache()`. No es necesario demostrar una mejora significativa con un archivo pequeño; deben explicar qué intenta mostrar el experimento.
5. Comparen el ejemplo con WordCount de Hadoop: código, modelo mental, ejecución local y rol del almacenamiento.

### Evidencia a entregar

- Notebook o script reproducible.
- Salida de cinco palabras y sus frecuencias.
- Comparación de 200 a 300 palabras entre Hadoop MapReduce y Spark.
- Una limitación del experimento local frente a un clúster real.

## Ejercicio 5 - Demostrar por qué accuracy puede engañar

**Duración estimada:** 50 minutos.

### Repositorio y ejemplo

- [Ejemplo oficial de precision-recall de scikit-learn](https://github.com/scikit-learn/scikit-learn/blob/main/examples/model_selection/plot_precision_recall.py).
- [Documentación ejecutable de precision-recall](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html).

### Consigna

1. Lean la introducción del ejemplo y definan precision y recall utilizando la matriz de confusión.
2. Generen un dataset sintético con 99 % de clase 0 y 1 % de clase 1 mediante `make_classification`.
3. Construyan un baseline que siempre prediga la clase mayoritaria.
4. Calculen accuracy, precision, recall, F1 y matriz de confusión.
5. Entrenen una regresión logística y generen la curva precision-recall.
6. Seleccionen dos umbrales: uno que priorice recall y otro que priorice precision. Expliquen el costo de cada decisión en un caso de fraude.

### Evidencia a entregar

- Código o notebook ejecutable.
- Matriz de confusión de ambos modelos.
- Curva precision-recall con los dos umbrales señalados.
- Respuesta: ¿qué modelo recomendarían y bajo qué supuesto de costo?

### Condición de logro

La conclusión debe interpretar falsos positivos y falsos negativos. Informar sólo accuracy no completa el ejercicio.

## Ejercicio 6 - Comparar estrategias para clases desbalanceadas

**Duración estimada:** 75 minutos.

### Literatura y repositorio

- Chawla y colaboradores, [SMOTE: Synthetic Minority Over-sampling Technique](https://www.jair.org/index.php/jair/article/view/10302) (JAIR 2002).
- Lemaître, Nogueira y Aridas, [Imbalanced-learn: A Python Toolbox to Tackle the Curse of Imbalanced Datasets in Machine Learning](https://jmlr.org/papers/v18/16-365.html) (JMLR 2017).
- [Repositorio oficial de imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn).

### Consigna

1. Lean el resumen y la explicación del algoritmo SMOTE. Describan qué significa crear un ejemplo sintético entre vecinos.
2. Clonen o exploren el repositorio de imbalanced-learn e identifiquen dónde se implementa SMOTE y dónde están los ejemplos.
3. Sobre el dataset sintético del ejercicio anterior, comparen:
   - regresión logística sin ajuste;
   - regresión logística con `class_weight="balanced"`;
   - `RandomUnderSampler` seguido del clasificador;
   - `RandomOverSampler` seguido del clasificador;
   - `SMOTE` seguido del clasificador.
4. Implementen los remuestreos dentro de un `imblearn.pipeline.Pipeline` para que se apliquen sólo durante el ajuste.
5. Evalúen todos los enfoques sobre el mismo conjunto de prueba sin remuestrear.
6. Comparen precision, recall, F1 y average precision. Incluyan tiempo de ajuste como observación secundaria.

### Evidencia a entregar

- Tabla de resultados con semilla y versiones registradas.
- Código reproducible.
- Gráfico que muestre el efecto de al menos una estrategia de remuestreo.
- Discusión de 250 a 400 palabras sobre beneficios, riesgos y límites de SMOTE.

### Pregunta crítica

¿Por qué describir los ejemplos sintéticos simplemente como “datos falsos” es insuficiente? ¿En qué situaciones podrían resultar poco realistas o perjudiciales?

## Entrega integradora

Cada pareja entregará un informe breve con esta estructura:

1. **Afirmación investigada:** una idea concreta de las diapositivas.
2. **Fuentes:** al menos un paper y una fuente oficial de software.
3. **Experimento:** repositorio, versión, datos, pasos y resultado.
4. **Interpretación:** qué demuestra y qué no demuestra la prueba.
5. **Decisión:** recomendación para un sistema de fraude y métrica prioritaria.
6. **Limitación:** un riesgo técnico, ético, de privacidad o de generalización.

Extensión sugerida: 1.200 a 1.800 palabras, más código, tablas y figuras.

## Rúbrica

| Criterio | Logrado | En proceso | A revisar |
|---|---|---|---|
| Fuentes | Usa papers y repositorios oficiales, con referencias localizables | Usa fuentes pertinentes pero incompletas | Basa conclusiones en fuentes sin autoría o no verificables |
| Reproducibilidad | Registra versiones, semilla, datos, código y salida | Falta uno de los elementos | No permite repetir el experimento |
| Comprensión | Relaciona resultados con arquitectura, modelo y decisión | Describe resultados con poca conexión conceptual | Enumera términos sin explicar relaciones |
| Evaluación | Interpreta precision, recall, errores y umbrales | Calcula métricas con interpretación parcial | Informa sólo accuracy o R² |
| Pensamiento crítico | Expone límites y distingue evidencia de inferencia | Menciona una limitación sin desarrollarla | Generaliza más allá de la evidencia |
| Comunicación | Presenta un argumento claro y cita correctamente | La estructura es comprensible con omisiones | Resulta difícil rastrear fuentes o resultados |

## Lista de control antes de entregar

- [ ] Todos los enlaces fueron abiertos y corresponden a la fuente citada.
- [ ] Cada afirmación técnica importante tiene una referencia o evidencia.
- [ ] El código se ejecutó desde un entorno limpio o se documentaron las dependencias.
- [ ] El conjunto de prueba permaneció separado y sin remuestrear.
- [ ] No se interpretó R² como porcentaje de aciertos.
- [ ] Se explicó el costo de falsos positivos y falsos negativos.
- [ ] Se diferenciaron resultados observados, interpretaciones y recomendaciones.
