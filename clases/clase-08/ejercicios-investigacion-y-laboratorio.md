# Ejercicios de indagación y laboratorio

Los ejercicios priorizan lectura de fuentes primarias, inspección de código abierto y experimentación reproducible. Cada entrega debe registrar enlaces consultados, versión o commit cuando corresponda, procedimiento, resultados y limitaciones.

## 1. Las V de Big Data en la literatura

**Objetivo:** comprobar que no existe una única taxonomía universal.

1. Buscar dos artículos académicos o capítulos universitarios que definan las V.
2. Registrar autores, año, publicación y enlace persistente o DOI.
3. Comparar las dimensiones: ¿incluyen variabilidad, visualización o viabilidad?
4. Aplicar ambas taxonomías al mismo caso, por ejemplo pagos, salud o movilidad.
5. Concluir cuál resulta más útil para el caso y justificar.

**Entrega:** tabla comparativa de una página y bibliografía.

## 2. Mapa de un proyecto open source

**Objetivo:** reconocer cómo se organiza una biblioteca científica real.

Repositorio: [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn)

1. Leer README, guía de contribución y licencia.
2. Ubicar los directorios de documentación, ejemplos, pruebas y código fuente.
3. Elegir una métrica de clasificación y localizar su documentación y su implementación.
4. Seguir el vínculo entre documentación, función y al menos una prueba automática.
5. Explicar por qué las pruebas forman parte de la confiabilidad de una herramienta científica.

**Entrega:** mapa del repositorio con enlaces permanentes a archivos o líneas.

## 3. Accuracy frente a clases desbalanceadas

**Objetivo:** demostrar por qué accuracy aislada puede engañar.

1. Ejecutar `laboratorio_desbalance.py`.
2. Comparar el clasificador constante con regresión logística.
3. Registrar accuracy, balanced accuracy, precision, recall, F1 y average precision.
4. Cambiar el peso de la clase minoritaria de 1 % a 5 % y 15 %.
5. Explicar qué métricas cambian y por qué.

**Entrega:** tabla de resultados y una conclusión de hasta 300 palabras.

## 4. Reproducir un ejemplo de precision-recall

**Objetivo:** conectar una publicación con una implementación.

Fuentes:

- [Ejemplo oficial de precision-recall de scikit-learn](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)
- Saito y Rehmsmeier, 2015, DOI [10.1371/journal.pone.0118432](https://doi.org/10.1371/journal.pone.0118432)
- Davis y Goadrich, 2006, DOI [10.1145/1143844.1143874](https://doi.org/10.1145/1143844.1143874)

1. Reproducir el ejemplo oficial.
2. Modificar la proporción de positivos.
3. Comparar ROC-AUC y PR-AUC.
4. Explicar, con apoyo en uno de los artículos, por qué las curvas comunican aspectos diferentes.

**Entrega:** notebook, dos gráficos y citas de los pasajes utilizados sin copiar extensamente.

## 5. SMOTE bajo inspección

**Objetivo:** comprender una técnica desde el artículo, la documentación y el código.

Fuentes:

- Chawla et al., 2002, DOI [10.1613/jair.953](https://doi.org/10.1613/jair.953)
- [Repositorio imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn)
- [Documentación de SMOTE](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html)

1. Explicar con un dibujo o ejemplo numérico cómo se genera un punto sintético.
2. Ubicar la clase `SMOTE` y el método que realiza el remuestreo en el repositorio.
3. Comparar sin remuestreo, `class_weight="balanced"`, RandomOverSampler y SMOTE.
4. Aplicar el remuestreo sólo dentro del entrenamiento.
5. Identificar un escenario donde SMOTE pueda generar puntos poco realistas.

**Entrega:** notebook y nota técnica de 500 palabras.

## 6. Pipeline sin fuga de información

**Objetivo:** detectar y corregir un experimento contaminado.

1. Construir una versión incorrecta que aplique SMOTE antes de separar test.
2. Construir una versión correcta con `imblearn.pipeline.Pipeline` y validación cruzada estratificada.
3. Comparar resultados.
4. Explicar por qué la primera versión sobrestima el rendimiento.
5. Agregar una prueba o aserción que verifique que el test no fue remuestreado.

**Entrega:** código, resultados y explicación causal del error.

## 7. Explorar Spark desde su repositorio oficial

**Objetivo:** distinguir capacidades del ecosistema y ejecutar un ejemplo mínimo.

Repositorio: [apache/spark](https://github.com/apache/spark)

1. Leer el README y localizar `examples` y la documentación de ML.
2. Identificar componentes para SQL/DataFrames, ML y Structured Streaming.
3. Ejecutar un ejemplo local con PySpark o el contenedor oficial.
4. Comparar qué parte corresponde a procesamiento por lotes y cuál a streaming.
5. Documentar requisitos, tiempo de ejecución y recursos usados.

**Entrega:** bitácora reproducible con comandos y salida abreviada.

> No es necesario compilar Spark desde el código fuente. El repositorio se usa para estudiar organización, ejemplos y documentación; la ejecución puede realizarse con una distribución oficial.

## 8. Hadoop: afirmaciones y evidencia

**Objetivo:** verificar afirmaciones tecnológicas con documentación oficial.

Fuentes:

- [Repositorio apache/hadoop](https://github.com/apache/hadoop)
- [Documentación oficial de HDFS](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)
- [Documentación oficial de YARN](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html)

1. Encontrar evidencia para describir HDFS, YARN y MapReduce.
2. Clasificar cada componente por almacenamiento, recursos o procesamiento.
3. Evaluar críticamente la frase “Hadoop detecta fraude en milisegundos”.
4. Proponer qué componentes adicionales harían falta para baja latencia.

**Entrega:** informe de 600 palabras con citas y diagrama propio.

## 9. Revisión de literatura sobre fraude

**Objetivo:** formular una síntesis basada en evidencia.

Punto de partida: Cherif et al., 2023, revisión sistemática, DOI [10.1016/j.jksuci.2022.11.008](https://doi.org/10.1016/j.jksuci.2022.11.008).

1. Buscar dos revisiones adicionales publicadas desde 2020.
2. Registrar bases consultadas y cadena de búsqueda.
3. Comparar datasets, algoritmos, métricas y tratamiento del desbalance.
4. Identificar dos amenazas a la validez o limitaciones recurrentes.
5. Proponer una pregunta de investigación que no quede respondida.

**Entrega:** matriz de literatura con al menos tres revisiones y síntesis de 800 palabras.

## 10. Diseño de una política de decisión

**Objetivo:** conectar métricas con costos reales.

Supongan que un falso negativo cuesta 500 unidades y una revisión manual cuesta 4. Con las probabilidades del laboratorio:

1. Probar al menos cinco umbrales.
2. Calcular falsos positivos, falsos negativos y costo total.
3. Elegir un umbral y justificarlo.
4. Analizar qué cambia si el costo reputacional de bloquear una compra aumenta.
5. Proponer cuándo la decisión debe pasar a revisión humana.

**Entrega:** tabla, gráfico costo-umbral y recomendación ejecutiva.

## Criterios de evaluación

- 25 % calidad y trazabilidad de fuentes;
- 25 % reproducibilidad técnica;
- 20 % interpretación de resultados;
- 20 % análisis crítico de limitaciones;
- 10 % claridad de comunicación.

No alcanza con obtener una métrica alta. La entrega debe explicar el procedimiento, el costo de los errores y los límites de la evidencia.

