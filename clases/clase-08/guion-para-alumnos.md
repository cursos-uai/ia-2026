# Clase 8 - Guía para alumnos sobre Big Data, Machine Learning y detección de fraude

## Propósito de la clase

Esta guía acompaña las 36 diapositivas de la unidad. El objetivo es comprender:

1. qué diferencia a Big Data de una colección común de datos;
2. cómo se relacionan Big Data, análisis predictivo y Machine Learning;
3. cómo se prepara y procesa la información;
4. cómo se puede plantear la detección de fraude como un problema de clasificación;
5. cómo evaluar un modelo cuando hay muy pocos casos de fraude.

## Diccionario de la clase

### Conceptos de datos

- **Big Data:** conjunto de problemas, métodos y tecnologías para trabajar con datos cuyo volumen, velocidad o complejidad supera a las herramientas tradicionales.
- **Dataset:** colección organizada de datos. Normalmente, cada fila representa un caso y cada columna una característica.
- **Dato estructurado:** dato organizado en filas y columnas, como una tabla de ventas.
- **Dato no estructurado:** dato sin una estructura tabular fija, como imágenes, audio, video o texto libre.
- **Ingesta:** proceso de incorporar datos desde sus fuentes hacia una plataforma de almacenamiento o procesamiento.
- **Pipeline de datos:** secuencia de pasos por la que pasan los datos: origen, ingesta, limpieza, transformación, almacenamiento, análisis y uso.
- **Procesamiento por lotes (batch):** procesamiento de grupos de datos acumulados durante un período.
- **Procesamiento en tiempo real:** procesamiento de los datos a medida que llegan, con baja demora.
- **Almacenamiento distribuido:** conservación de datos en varias computadoras que trabajan coordinadamente.
- **Procesamiento paralelo:** división de un trabajo en partes que se ejecutan simultáneamente.
- **Nube (cloud):** uso remoto y bajo demanda de infraestructura, almacenamiento y servicios informáticos.
- **Curado o limpieza de datos:** detección y corrección de valores faltantes, duplicados, errores e inconsistencias.
- **Valor nulo:** ausencia de un dato en un campo.
- **Codificación:** transformación de categorías o palabras en una representación numérica utilizable por un modelo.

### Las V de Big Data

- **Volumen:** cantidad de datos que debe almacenarse y procesarse.
- **Velocidad:** rapidez con la que los datos se generan, llegan y necesitan ser analizados.
- **Variedad:** diversidad de fuentes, formatos y estructuras.
- **Veracidad:** calidad, confiabilidad y correspondencia de los datos con la realidad.
- **Valor:** utilidad que se obtiene de los datos para tomar decisiones.
- **Variabilidad:** cambios en el significado, la distribución o el comportamiento de los datos a lo largo del tiempo.
- **Visualización:** representación gráfica que permite explorar y comunicar patrones.
- **Viabilidad:** posibilidad práctica y económica de transformar los datos en resultados útiles. Es una extensión usada en algunas clasificaciones, no una V universal.

### Analítica y Machine Learning

- **Análisis descriptivo:** explica qué ocurrió o qué está ocurriendo.
- **Análisis predictivo:** estima qué podría ocurrir a partir de patrones históricos.
- **Machine Learning (ML):** métodos que permiten ajustar modelos a partir de datos para predecir, clasificar o descubrir estructuras.
- **Algoritmo:** procedimiento utilizado para entrenar un modelo o resolver un problema.
- **Modelo:** representación aprendida a partir de los datos. Recibe entradas y produce predicciones.
- **Entrenamiento:** etapa en la que el algoritmo ajusta el modelo utilizando ejemplos.
- **Inferencia:** uso del modelo ya entrenado para producir una predicción sobre un caso nuevo.
- **Característica o feature (X):** variable de entrada utilizada para realizar una predicción.
- **Etiqueta u objetivo (y):** resultado que el modelo debe aprender a predecir.
- **Generalización:** capacidad de funcionar bien con datos nuevos y no solamente con los ejemplos de entrenamiento.
- **Aprendizaje supervisado:** entrenamiento con ejemplos que incluyen la respuesta correcta.
- **Aprendizaje no supervisado:** búsqueda de grupos o estructuras sin etiquetas conocidas.
- **Clasificación:** predicción de una categoría, por ejemplo fraude/no fraude.
- **Regresión:** predicción de un valor numérico continuo, por ejemplo el precio de una vivienda.
- **Clustering:** agrupamiento de casos similares sin una etiqueta previa.
- **Red neuronal:** modelo compuesto por unidades conectadas que ajustan pesos durante el entrenamiento.
- **SVM:** algoritmo que busca una frontera que separe categorías.
- **Árbol de decisión:** modelo que organiza decisiones sucesivas en forma de preguntas y ramas.
- **Regresión logística:** clasificador que estima la probabilidad de pertenecer a una clase.
- **Minería de datos:** exploración de grandes conjuntos de datos para encontrar patrones y relaciones útiles.

### Evaluación y fraude

- **Conjunto de entrenamiento:** datos usados para ajustar el modelo.
- **Conjunto de prueba:** datos reservados para evaluar el modelo con casos no usados durante el entrenamiento.
- **Desbalance de clases:** situación en la que una clase aparece mucho menos que otra; en fraude suele haber muy pocos casos positivos.
- **RUS (submuestreo):** reducción de ejemplos de la clase mayoritaria.
- **ROS (sobremuestreo):** duplicación o aumento de ejemplos de la clase minoritaria.
- **SMOTE:** técnica que crea ejemplos sintéticos de la clase minoritaria a partir de casos cercanos.
- **Matriz de confusión:** tabla que compara las clases reales con las predicciones.
- **Verdadero positivo:** fraude correctamente detectado.
- **Falso positivo:** operación legítima marcada como fraude.
- **Falso negativo:** fraude que el modelo no detectó.
- **Precision:** proporción de alertas de fraude que realmente eran fraude.
- **Recall o sensibilidad:** proporción de fraudes reales que el modelo logró detectar.
- **F1:** combinación equilibrada de precision y recall.
- **Accuracy:** proporción total de predicciones correctas. Puede ser engañosa cuando las clases están desbalanceadas.
- **Umbral:** probabilidad mínima elegida para convertir una predicción probabilística en una decisión.
- **PR-AUC:** resumen del equilibrio entre precision y recall para distintos umbrales; suele ser útil en clases muy desbalanceadas.

### Tecnologías

- **Hadoop:** ecosistema para almacenar y procesar datos de forma distribuida. Su núcleo histórico incluye HDFS y MapReduce.
- **HDFS:** sistema distribuido de archivos de Hadoop.
- **MapReduce:** modelo de procesamiento distribuido orientado principalmente a trabajos por lotes.
- **Spark:** motor de procesamiento distribuido que puede trabajar en memoria y ejecutar análisis, SQL y Machine Learning.
- **HBase:** base de datos distribuida orientada a columnas que opera sobre el ecosistema Hadoop.
- **NoSQL:** familia de bases de datos que no exige el modelo relacional tradicional.
- **Microservicio:** componente pequeño e independiente que cumple una función dentro de una aplicación.
- **Contenedor:** paquete ejecutable que incluye una aplicación y sus dependencias; Docker es una tecnología popular de contenedores.

## Guion de lectura diapositiva por diapositiva

### Diapositiva 1 - Presentación de la unidad

La unidad conecta dos temas: Big Data y Machine Learning. Big Data se ocupa del ciclo de vida de datos complejos o masivos; ML utiliza datos para ajustar modelos capaces de hacer predicciones o clasificaciones. No son sinónimos y ninguno exige automáticamente al otro.

**Pregunta guía:** ¿cómo convertimos una gran cantidad de transacciones en decisiones útiles?

### Diapositiva 2 - Mapa de temas

La clase avanza desde los datos hacia la decisión: primero define Big Data, luego introduce el análisis predictivo y ML, y finalmente relaciona estas ideas con estadística y minería de datos.

**Idea clave:** conocer muchas tecnologías no alcanza; debemos entender qué problema resuelve cada una.

### Diapositiva 3 - Las V de Big Data

Las V permiten describir por qué un problema de datos puede requerir herramientas especiales. Las cinco más aceptadas son volumen, velocidad, variedad, veracidad y valor. Otras clasificaciones agregan variabilidad y visualización; algunas también hablan de viabilidad.

**Ejemplo:** una plataforma de pagos recibe millones de operaciones, desde distintos canales, en segundos, y necesita distinguir datos confiables de errores o intentos de fraude.

### Diapositiva 4 - Big Data y ML no son lo mismo

ML puede utilizar conjuntos pequeños o grandes. Lo decisivo no es solamente la cantidad, sino la calidad y pertinencia de los ejemplos. Big Data facilita almacenar y procesar grandes fuentes; ML busca aprender patrones a partir de ellas.

**Idea clave:** más datos pueden ayudar, pero datos incorrectos o irrelevantes no mejoran automáticamente un modelo.

### Diapositiva 5 - Cuándo aparece un problema de Big Data

Big Data se vuelve necesario cuando las soluciones tradicionales ya no alcanzan para combinar fuentes, procesar grandes volúmenes, responder a tiempo o encontrar patrones complejos.

**Ejemplo:** unir compras, ubicación, dispositivo, historial y reclamos para evaluar una transacción.

### Diapositiva 6 - Por qué creció Big Data

El crecimiento se explica por la reducción del costo de almacenamiento, el aumento de la capacidad de cómputo, los servicios en la nube y la generación permanente de datos digitales.

**Idea clave:** no sólo aumentaron los datos; también mejoró nuestra capacidad para conservarlos y procesarlos.

### Diapositiva 7 - Tecnologías relacionadas

La virtualización, el procesamiento paralelo, los sistemas distribuidos, las bases en memoria, los microservicios y los contenedores resuelven partes diferentes del problema.

**No memorizar como lista:** preguntarse si cada tecnología ayuda a almacenar, procesar, desplegar o integrar.

### Diapositiva 8 - Preparación de los datos

Antes de entrenar un modelo hay que limpiar y transformar los datos: completar o tratar valores nulos, corregir errores, convertir categorías a números y verificar que cada variable tenga sentido.

**Idea clave:** la calidad del modelo depende fuertemente de la calidad del proceso de preparación.

### Diapositiva 9 - De describir a predecir

El análisis descriptivo resume lo ocurrido. El análisis predictivo usa patrones históricos para estimar resultados futuros. ML no debe pensarse simplemente como un “tercer escalón”: es un conjunto de métodos que puede utilizarse dentro de la analítica predictiva y en otras tareas.

### Diapositiva 10 - Descriptivo, predictivo y ML

“¿Qué productos se vendieron más?” es una pregunta descriptiva. “¿Qué productos se venderán más?” es predictiva. Un modelo de ML puede aprender relaciones entre temporada, precio, promociones e historial para estimar esa demanda.

**Idea clave:** una predicción siempre tiene incertidumbre; no es una certeza sobre el futuro.

### Diapositiva 11 - Ejemplo práctico

La diapositiva anuncia una demostración en Colab. Para conservar el hilo de la unidad, conviene usar el mismo caso de fraude que aparece luego, en lugar de introducir una predicción de poesía sin conexión suficiente.

### Diapositiva 12 - Programación tradicional y ML

En programación tradicional, una persona escribe reglas y la computadora produce resultados. En ML, una persona elige datos, objetivo, algoritmo y evaluación; el algoritmo ajusta un modelo a partir de ejemplos.

**Corrección importante:** la máquina no “crea su propio algoritmo”; aprende los parámetros de un modelo mediante un algoritmo elegido por personas.

### Diapositiva 13 - Cuándo usar ML

ML es útil cuando existen ejemplos y patrones, pero resulta difícil escribir todas las reglas a mano. Reconocer voz, imágenes, spam o fraude son ejemplos habituales.

**No usar ML automáticamente:** si una regla simple resuelve bien el problema, puede ser más clara, económica y controlable.

### Diapositiva 14 - Aprender una función

Cada ejemplo de entrenamiento contiene una entrada `x` y, en aprendizaje supervisado, una respuesta `y`. El modelo intenta aproximar una función que transforme nuevas entradas en salidas útiles.

**Ejemplos:** correo -> spam/no spam; píxeles -> dígito; transacción -> fraude/no fraude.

### Diapositiva 15 - Familias de modelos

Redes neuronales, SVM y árboles de decisión son formas diferentes de representar la relación entre entradas y salidas. No existe un único modelo mejor para todos los problemas.

**Idea clave:** se elige comparando desempeño, interpretabilidad, costo y características de los datos.

### Diapositiva 16 - Relación entre IA, ML y aprendizaje profundo

La inteligencia artificial es el campo más amplio. Machine Learning es una parte de la IA. El aprendizaje profundo es una familia de técnicas de ML basada en redes neuronales con múltiples capas.

**Idea clave:** todo deep learning es ML, pero no todo ML es deep learning.

### Diapositiva 17 - Estadística y minería de datos

La estadística ayuda a describir datos, estimar incertidumbre y extraer conclusiones. La minería de datos busca patrones útiles en grandes colecciones. ML utiliza muchas ideas estadísticas para construir modelos predictivos.

### Diapositiva 18 - Herramientas y actores

Python, R, Spark, herramientas de visualización y plataformas empresariales participan en distintas etapas. Una organización necesita además personas que entiendan el problema, los datos y las consecuencias de las decisiones.

**Idea clave:** la solución no es una herramienta aislada, sino un proceso interdisciplinario.

### Diapositiva 19 - Entrada al procesamiento distribuido

Esta lámina abre el bloque tecnológico. El problema central es cómo dividir almacenamiento y cálculo entre varias máquinas cuando una sola no alcanza.

### Diapositiva 20 - Ecosistema Hadoop

Hadoop permite distribuir almacenamiento y procesamiento. HDFS almacena archivos en varios nodos y MapReduce ejecuta trabajos por lotes. Spark, HBase y otras herramientas pueden integrarse en arquitecturas más amplias.

**Aclaración:** no todas las capacidades enumeradas pertenecen a Hadoop por sí solo.

### Diapositiva 21 - Hadoop y fraude

Una arquitectura distribuida puede reunir y procesar grandes volúmenes de operaciones para alimentar sistemas antifraude. Sin embargo, MapReduce se orienta principalmente a lotes; la respuesta en milisegundos requiere componentes específicos de baja latencia o streaming.

### Diapositiva 22 - Patrón de arquitectura

El diagrama representa un flujo: varias fuentes generan eventos, una capa los recibe, otra los almacena o procesa y finalmente distintos servicios consumen los resultados.

**Forma de leerlo:** recorrerlo de izquierda a derecha y preguntar qué entra, qué transformación ocurre y quién utiliza la salida.

### Diapositiva 23 - Ingesta de datos

Los datos pueden llegar desde sistemas de ventas, aplicaciones, sensores, archivos o servicios externos. La ingesta los incorpora a la plataforma para que puedan ser almacenados y procesados.

### Diapositiva 24 - Almacenamiento y distribución

Después de ingresar, los datos se distribuyen hacia repositorios y servicios. No todos los datos deben guardarse del mismo modo: algunos se consultan inmediatamente y otros se conservan para análisis históricos.

### Diapositiva 25 - Tratamiento de los datos

El flujo incorpora limpieza, transformación, combinación y creación de características. El resultado puede alimentar modelos de ML, reportes o conjuntos compartidos con otros equipos.

### Diapositiva 26 - De los datos a los resultados

La arquitectura completa conecta fuentes con productos de información. El valor no está en acumular datos, sino en generar decisiones, alertas, reportes o predicciones verificables.

### Diapositiva 27 - Caso práctico: predicción de fraude

El fraude se puede estudiar como una desviación respecto de patrones normales, pero una diferencia no siempre significa fraude. El sistema produce una probabilidad o señal que luego debe convertirse en una decisión.

**Pregunta central:** ¿qué cuesta más, dejar pasar un fraude o bloquear una compra legítima?

### Diapositiva 28 - Algoritmos supervisados y no supervisados

Los métodos supervisados aprenden con ejemplos etiquetados como fraude/no fraude. Los no supervisados buscan grupos, anomalías o estructuras sin necesitar todas las etiquetas.

**Aclaración:** la regresión lineal no es adecuada para clasificar fraude; la regresión logística sí puede usarse como baseline.

### Diapositiva 29 - Carga y exploración del dataset

`read_csv` carga los datos en una tabla. `head()` permite observar las primeras filas y `shape` informa cuántas filas y columnas existen. Aquí aparecen 5.050 casos y 30 variables.

**Antes de entrenar:** identificar la fuente, el significado de las columnas, la variable objetivo, los valores faltantes y la proporción de fraudes.

### Diapositiva 30 - Exploración visual

Los gráficos ayudan a comparar la distribución de las variables entre operaciones legítimas y fraudulentas. Una separación visible puede indicar que una variable será útil, aunque no garantiza el desempeño del modelo.

### Diapositiva 31 - Tratamiento del desbalance

RUS elimina parte de la clase mayoritaria; es rápido, pero puede perder información. ROS repite casos minoritarios; es simple, pero puede favorecer sobreajuste. SMOTE genera ejemplos sintéticos; puede ayudar, aunque también introducir ruido.

**Regla:** aplicar estas técnicas sólo sobre entrenamiento, nunca sobre el conjunto de prueba.

### Diapositiva 32 - División, remuestreo y entrenamiento

Se separan datos de entrenamiento y prueba. Luego se remuestrea únicamente el entrenamiento, se ajusta el modelo y se evalúa con el test original.

**Actualización técnica:** usar `BorderlineSMOTE(...).fit_resample(...)`; añadir `stratify=y` y una semilla. Un pipeline ayuda a evitar fugas de información.

### Diapositiva 33 - Sistemas basados en reglas

Un sistema tradicional puede decir: “si el monto supera cierto límite y el país es inusual, bloquear”. Las reglas son claras y fáciles de auditar, pero requieren mantenimiento y pueden ser rígidas.

### Diapositiva 34 - Limitaciones de las reglas

Los umbrales fijos no capturan bien interacciones complejas ni cambios de comportamiento. Además, una decisión puramente binaria no expresa incertidumbre.

**Importante:** esto no vuelve inútiles a las reglas; en producción suelen combinarse con modelos y revisión humana.

### Diapositiva 35 - Ventajas y límites de ML

Un modelo puede combinar muchas variables y generar una probabilidad. Puede actualizarse con nuevos datos, pero también degradarse si cambia la realidad. Necesita monitoreo, explicabilidad y control de sesgos.

**Corrección:** no entrega un “porcentaje de acierto” por caso; entrega una puntuación o probabilidad que debe evaluarse y convertirse en decisión mediante un umbral.

### Diapositiva 36 - Corrección del ejemplo final

La diapositiva usa regresión lineal y `R²`, herramientas destinadas a predecir valores continuos. Fraude/no fraude es una clasificación binaria, por lo que corresponde un clasificador, por ejemplo regresión logística.

Un flujo correcto sería:

1. separar `X` e `y`;
2. dividir con estratificación;
3. aplicar SMOTE sólo sobre entrenamiento si resulta conveniente;
4. entrenar un clasificador;
5. predecir probabilidades y clases;
6. observar matriz de confusión, precision, recall, F1 y PR-AUC;
7. elegir un umbral según el costo de cada error.

**Advertencia:** un `R² = 0,82` no significa 82 % de acierto. Incluso una accuracy alta puede ocultar que el modelo no detecta ningún fraude.

## Síntesis final

- Big Data resuelve desafíos de escala, rapidez y diversidad de datos.
- ML aprende modelos a partir de ejemplos; no reemplaza la definición humana del problema.
- Los datos deben limpiarse, transformarse y dividirse correctamente.
- Detección de fraude es normalmente clasificación desbalanceada.
- No alcanza con decir que un modelo “acierta mucho”: debemos estudiar qué errores comete y cuánto cuesta cada uno.
- La solución real suele combinar arquitectura de datos, reglas, modelos, monitoreo y decisión humana.

## Preguntas de autoevaluación

1. ¿Cuál es la diferencia entre Big Data y Machine Learning?
2. ¿Qué representa cada una de las cinco V principales?
3. ¿Qué diferencia existe entre algoritmo y modelo?
4. ¿Por qué el conjunto de prueba no debe ser remuestreado con SMOTE?
5. ¿Qué diferencia hay entre falso positivo y falso negativo en fraude?
6. ¿Por qué accuracy puede ser engañosa?
7. ¿Cuándo priorizarías recall y cuándo precision?
8. ¿Por qué regresión lineal y R² no son apropiados para el ejemplo final?

## Frase para recordar la clase

> Los datos sólo generan valor cuando un proceso confiable los convierte en decisiones que podemos explicar, evaluar y mejorar.

## Lecturas y repositorios para continuar

- Jeffrey Dean y Sanjay Ghemawat, [MapReduce: Simplified Data Processing on Large Clusters](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/).
- Matei Zaharia y colaboradores, [Resilient Distributed Datasets](https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/zaharia).
- Nitesh Chawla y colaboradores, [SMOTE: Synthetic Minority Over-sampling Technique](https://www.jair.org/index.php/jair/article/view/10302).
- [Ejemplo oficial de precision-recall de scikit-learn](https://github.com/scikit-learn/scikit-learn/blob/main/examples/model_selection/plot_precision_recall.py).
- [Repositorio oficial de imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn).
- [Inicio rápido oficial de Apache Spark](https://github.com/apache/spark/blob/master/docs/quick-start.md).
- [WordCount oficial de Apache Hadoop](https://github.com/apache/hadoop/blob/trunk/hadoop-mapreduce-project/hadoop-mapreduce-examples/src/main/java/org/apache/hadoop/examples/WordCount.java).

Las actividades de indagación y experimentación vinculadas con estas fuentes están en [ejercicios de investigación y laboratorio](ejercicios-investigacion-laboratorio.md).
