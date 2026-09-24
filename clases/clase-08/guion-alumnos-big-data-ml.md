# Clase: Big Data y Machine Learning

## Diccionario y guía de lectura para estudiantes

Material elaborado a partir de la presentación de 36 diapositivas compartida para la Unidad 4. El archivo se denomina “clase 8”, aunque el intercambio la identifica como clase 7. La numeración definitiva debe confirmarse con el docente.

Fuente de la presentación: <https://drive.google.com/file/d/1I1lAHNUiOCQxyNSyyUy4wEaGkVMQiIY3/view?usp=sharing>

## Propósito de la clase

Al finalizar, deberías poder:

- explicar qué convierte a un problema de datos en un problema de Big Data;
- distinguir análisis descriptivo, análisis predictivo y Machine Learning;
- reconocer las partes básicas de un problema de aprendizaje supervisado;
- explicar por qué la detección de fraude es una clasificación con datos desbalanceados;
- interpretar falsos positivos, falsos negativos, precision y recall;
- describir, a nivel conceptual, cómo los datos llegan desde sus fuentes hasta un modelo y un reporte.

---

# Parte 1. Diccionario de la clase

## Conceptos de datos y arquitectura

**Big Data**  
Conjunto de problemas en los que el volumen, la velocidad, la variedad u otras características de los datos superan lo que las herramientas tradicionales pueden resolver de manera práctica. Big Data no significa solamente “muchos datos”.

**Volumen**  
Cantidad de datos que deben almacenarse y procesarse. Puede medirse en gigabytes, terabytes, petabytes u otras unidades.

**Velocidad**  
Rapidez con la que los datos se generan, llegan y necesitan ser procesados. No todos los problemas requieren tiempo real.

**Variedad**  
Diversidad de fuentes y formatos: tablas, textos, imágenes, audios, registros de sensores, eventos de aplicaciones, etcétera.

**Veracidad**  
Grado de confianza que podemos tener en los datos. Incluye errores, valores imposibles, duplicados, sesgos y fuentes poco confiables.

**Valor**  
Utilidad que se obtiene al convertir datos en decisiones, mejoras o conocimiento.

**Visualización**  
Representación gráfica de los datos para comunicar patrones, relaciones, excepciones y resultados.

**Viabilidad**  
Posibilidad real de usar los datos considerando costos, tecnología, personas, tiempo, calidad y objetivos. Existen distintas versiones de las “V” de Big Data; por eso conviene indicar qué taxonomía se utiliza.

**Fuente de datos**  
Lugar o sistema del que provienen los datos: una base de datos, archivo, sensor, API, aplicación o servicio externo.

**Ingesta de datos**  
Proceso de recibir o extraer datos desde una o varias fuentes e incorporarlos a una plataforma de procesamiento o almacenamiento.

**Procesamiento por lotes o batch**  
Procesamiento de un conjunto acumulado de datos en una ejecución. Por ejemplo, calcular todas las ventas del día durante la noche.

**Procesamiento en tiempo real o streaming**  
Procesamiento continuo de eventos a medida que llegan, con una demora reducida. Por ejemplo, analizar una transacción mientras está ocurriendo.

**Latencia**  
Tiempo que transcurre desde que ocurre un evento hasta que el sistema produce una respuesta.

**Almacenamiento distribuido**  
Forma de guardar datos en varias máquinas coordinadas, en lugar de depender de un solo servidor.

**Procesamiento paralelo**  
División de una tarea en varias partes que se ejecutan simultáneamente.

**Virtualización de datos**  
Capa que permite consultar distintas fuentes como si fueran una sola, sin mover necesariamente todos los datos a un repositorio común.

**Base de datos en memoria**  
Sistema que mantiene los datos principalmente en memoria RAM para acelerar las consultas.

**Microservicio**  
Componente pequeño de software que cumple una función específica y se comunica con otros componentes mediante interfaces definidas.

**Contenedor**  
Paquete que reúne una aplicación y sus dependencias para ejecutarla de manera consistente. Docker es una tecnología habitual de contenedores.

**Data Lake**  
Repositorio que conserva grandes cantidades de datos, muchas veces en su formato original. Requiere gobierno y catálogo para no transformarse en un depósito difícil de usar.

**Data Warehouse**  
Repositorio organizado y depurado para análisis de negocio, reportes e indicadores.

**Feature Store**  
Sistema para crear, almacenar, versionar y reutilizar variables preparadas para modelos de Machine Learning.

**ETL**  
Sigla de extraer, transformar y cargar. Describe un flujo en el que los datos se obtienen, se limpian o transforman y luego se almacenan.

**Pipeline de datos**  
Secuencia automatizada que mueve y transforma datos desde las fuentes hasta sus consumidores, como reportes o modelos.

**Hadoop**  
Ecosistema para almacenamiento y procesamiento distribuido. HDFS guarda archivos distribuidos y MapReduce procesa grandes lotes. No debe confundirse Hadoop completo con un sistema genérico de respuesta en milisegundos.

**HDFS**  
Sistema de archivos distribuido de Hadoop. Divide y replica archivos entre varias máquinas.

**MapReduce**  
Modelo de procesamiento distribuido orientado principalmente a trabajos por lotes.

**Spark**  
Motor distribuido para procesamiento de datos que puede trabajar en memoria y ejecutar tareas por lotes, análisis y Machine Learning.

**HBase**  
Base de datos distribuida del ecosistema Hadoop, diseñada para lecturas y escrituras aleatorias sobre grandes tablas.

## Analítica y Machine Learning

**Análisis descriptivo**  
Describe qué ocurrió o qué está ocurriendo. Ejemplo: ventas totales por producto durante el trimestre.

**Análisis predictivo**  
Estima un resultado futuro o desconocido a partir de patrones observados en datos anteriores.

**Machine Learning o aprendizaje automático**  
Área que desarrolla métodos capaces de ajustar modelos a partir de datos para realizar predicciones, clasificaciones, agrupamientos u otras tareas.

**Algoritmo de aprendizaje**  
Procedimiento que ajusta los parámetros de un modelo usando datos de entrenamiento.

**Modelo**  
Representación matemática aprendida a partir de datos. Recibe entradas y produce una salida.

**Entrenamiento**  
Proceso en el que el algoritmo ajusta el modelo usando ejemplos.

**Inferencia o predicción**  
Uso de un modelo ya entrenado para obtener una salida frente a datos nuevos.

**Generalización**  
Capacidad del modelo de funcionar bien con ejemplos nuevos, no solamente con los que utilizó para aprender.

**Conjunto de entrenamiento**  
Datos que se utilizan para ajustar el modelo.

**Conjunto de prueba o test**  
Datos separados que se utilizan para estimar cómo funcionará el modelo ante casos no vistos.

**Variable o característica, X**  
Dato de entrada que el modelo utiliza para realizar una predicción. En fraude podría ser el monto, la hora o una característica transformada de la transacción.

**Etiqueta u objetivo, y**  
Resultado que el modelo debe aprender a predecir. En fraude suele ser 0 para operación legítima y 1 para fraude.

**Aprendizaje supervisado**  
Aprendizaje realizado con ejemplos que incluyen entradas y respuestas conocidas.

**Aprendizaje no supervisado**  
Análisis de datos sin una etiqueta objetivo conocida. Busca estructuras, grupos o casos inusuales.

**Clasificación**  
Problema en el que la salida pertenece a una categoría. Fraude/no fraude y spam/no spam son clasificaciones.

**Regresión**  
Problema en el que la salida es un valor numérico continuo, como precio, temperatura o demanda.

**Regresión logística**  
Modelo de clasificación que estima la probabilidad de pertenecer a una clase. A pesar de su nombre, se usa para clasificar.

**Regresión lineal**  
Modelo para estimar un valor numérico continuo. No es la opción apropiada para enseñar detección binaria de fraude.

**Red neuronal artificial**  
Modelo compuesto por capas de unidades conectadas que ajustan pesos durante el entrenamiento.

**Máquina de vectores de soporte, SVM**  
Método que busca una frontera capaz de separar clases con el mayor margen posible, con extensiones para fronteras no lineales.

**Árbol de decisión**  
Modelo que divide los datos mediante preguntas sucesivas sobre sus características.

**Bosque aleatorio o Random Forest**  
Conjunto de árboles de decisión cuyas respuestas se combinan para lograr mayor estabilidad.

**Clustering**  
Agrupamiento de ejemplos similares sin utilizar una etiqueta conocida.

**K-Means**  
Algoritmo de clustering que organiza los ejemplos alrededor de una cantidad definida de centros.

**PCA**  
Técnica de reducción de dimensionalidad que crea nuevas variables capaces de resumir gran parte de la variación de los datos.

**Minería de datos**  
Proceso de explorar datos para encontrar patrones, relaciones, grupos o anomalías útiles.

**Estadística**  
Disciplina que permite describir datos, cuantificar incertidumbre, realizar inferencias y evaluar evidencia.

## Evaluación de fraude

**Datos desbalanceados**  
Conjunto en el que una clase aparece mucho menos que otra. En fraude suele haber muchísimas operaciones legítimas y pocos fraudes.

**Baseline**  
Modelo o regla sencilla que sirve como punto de comparación. Un método más complejo debe aportar una mejora relevante frente al baseline.

**Matriz de confusión**  
Tabla que compara predicciones y valores reales mediante verdaderos positivos, falsos positivos, verdaderos negativos y falsos negativos.

**Verdadero positivo**  
Fraude que el modelo detectó correctamente.

**Falso positivo**  
Operación legítima que el modelo marcó como fraude. Puede causar bloqueo o molestia al cliente.

**Verdadero negativo**  
Operación legítima que el modelo identificó correctamente.

**Falso negativo**  
Fraude que el modelo no detectó. Puede producir una pérdida económica.

**Accuracy o exactitud global**  
Proporción total de respuestas correctas. Puede resultar engañosa cuando una clase domina el conjunto.

**Precision**  
Entre todas las alertas de fraude generadas, proporción que realmente era fraude. Una precision baja genera muchas alertas falsas.

**Recall o sensibilidad**  
Entre todos los fraudes reales, proporción que el modelo detectó. Un recall bajo deja pasar muchos fraudes.

**F1**  
Media armónica de precision y recall. Resume ambas métricas, aunque no reemplaza el análisis del costo de cada error.

**Umbral de decisión**  
Valor de probabilidad a partir del cual el sistema asigna una clase. Modificarlo cambia la relación entre fraudes detectados y falsas alarmas.

**Submuestreo o undersampling**  
Reducción de ejemplos de la clase mayoritaria. Acelera el entrenamiento, pero puede descartar información útil.

**Sobremuestreo u oversampling**  
Aumento de la representación de la clase minoritaria mediante repetición o generación de ejemplos.

**SMOTE**  
Técnica que genera ejemplos sintéticos de la clase minoritaria mediante interpolación entre ejemplos cercanos. Solo debe aplicarse al entrenamiento.

**Fuga de datos o data leakage**  
Situación en la que información del conjunto de prueba influye en el entrenamiento. Produce resultados artificialmente optimistas.

---

# Parte 2. Guion para comprender cada diapositiva

## Diapositiva 1. Portada

**Qué presenta:** Unidad 4, Big Data y Machine Learning.

**Cómo entenderla:** La clase conecta dos temas relacionados pero diferentes. Big Data se ocupa de almacenar y procesar datos que presentan dificultades de escala o complejidad. Machine Learning utiliza datos para ajustar modelos. Podemos aplicar ML sin Big Data y podemos construir soluciones Big Data que no utilicen ML.

**Pregunta para activar conocimientos:** ¿Una planilla con diez millones de filas es siempre Big Data? La respuesta depende de si las herramientas disponibles pueden procesarla dentro del tiempo, costo y calidad necesarios.

## Diapositiva 2. Temas

**Qué presenta:** Big Data, análisis predictivo, Machine Learning y estadística.

**Cómo entenderla:** Los cuatro temas forman una cadena posible: reunimos datos, los comprendemos con estadística, construimos modelos y usamos resultados para tomar decisiones. No toda solución debe recorrer la cadena completa.

**Idea para recordar:** Tecnología, modelo y decisión son capas distintas.

## Diapositiva 3. Las V de Big Data

**Qué presenta:** siete características para describir problemas de Big Data.

**Cómo entenderla:** Las V funcionan como preguntas de diagnóstico. ¿Cuántos datos existen? ¿Con qué rapidez llegan? ¿En cuántos formatos? ¿Son confiables? ¿Podemos utilizarlos? ¿Qué valor producen? ¿Cómo comunicaremos el resultado?

**Aclaración:** Existen distintas listas de V. Algunas incluyen variabilidad en lugar de viabilidad. Lo importante es declarar la versión elegida y usarla con coherencia.

**Actividad breve:** Elegí una aplicación cotidiana y buscá un ejemplo de cada V.

## Diapositiva 4. Big Data en relación con ML

**Qué presenta:** Machine Learning necesita datos adecuados, pero no necesariamente enormes.

**Cómo entenderla:** Más datos no garantizan un mejor modelo. Importan la relevancia, la calidad, la representatividad y la relación entre las variables y el objetivo. Un conjunto pequeño pero bien diseñado puede resultar más útil que millones de registros defectuosos.

**Pregunta:** ¿Qué preferirías: un millón de registros sin etiqueta confiable o diez mil revisados correctamente?

## Diapositiva 5. Cuándo aparece un problema de Big Data

**Qué presenta:** combinación de fuentes, procesamiento a escala, búsqueda de patrones y toma de decisiones.

**Cómo entenderla:** Hablamos de Big Data cuando almacenar, integrar o procesar los datos supera la capacidad práctica de una solución convencional. La necesidad surge del problema, no de una herramienta de moda.

**Ejemplo:** Una cadena de comercios puede combinar ventas, inventario, navegación web y reclamos para anticipar demanda.

## Diapositiva 6. Factores que impulsaron Big Data

**Qué presenta:** reducción de costos, nube y aumento de capacidad.

**Cómo entenderla:** El crecimiento de Big Data no depende de una única invención. Influyen el almacenamiento más barato, las redes, la computación en la nube, los dispositivos conectados y la generación continua de eventos digitales.

**Idea para recordar:** La tecnología volvió posible conservar y procesar datos que antes se descartaban.

## Diapositiva 7. Tecnologías relacionadas

**Qué presenta:** virtualización, paralelismo, almacenamiento distribuido, bases en memoria, microservicios y contenedores.

**Cómo entenderla:** Cada tecnología resuelve una parte distinta. El procesamiento paralelo acelera tareas; el almacenamiento distribuido reparte datos; los contenedores facilitan ejecutar aplicaciones de forma consistente. No son sinónimos ni deben utilizarse todos juntos.

**Pregunta:** ¿Qué problema concreto resuelve cada tecnología dentro de una arquitectura?

## Diapositiva 8. Preparación de los datos

**Qué presenta:** limpieza, transformación de texto, tratamiento de valores nulos y corrección de irregularidades.

**Cómo entenderla:** Los algoritmos necesitan una representación consistente. Preparar datos puede incluir corregir tipos, eliminar duplicados, imputar faltantes, codificar categorías y revisar unidades. Cada transformación debe poder explicarse y repetirse.

**Riesgo:** Si limpiamos usando información del test, generamos fuga de datos.

## Diapositiva 9. De lo descriptivo a lo predictivo

**Qué presenta:** una supuesta progresión desde análisis descriptivo hasta Machine Learning.

**Cómo entenderla:** El análisis descriptivo responde qué ocurrió. El predictivo estima algo desconocido o futuro. Machine Learning ofrece métodos que pueden usarse en problemas predictivos, pero no constituye simplemente un escalón posterior. También se usa para agrupar, recomendar, generar contenido o detectar anomalías.

**Corrección conceptual:** Pensá en “tipos de preguntas y métodos disponibles”, no en una única escalera obligatoria.

## Diapositiva 10. Comparación de enfoques analíticos

**Qué presenta:** ejemplos de análisis descriptivo, predictivo y predictivo con ML.

**Cómo entenderla:** Un reporte de ventas resume el presente o el pasado. Una predicción estima ventas futuras. El uso de ML se justifica si encuentra patrones que generalizan y mejora una referencia simple.

**Pregunta:** ¿Qué dato debería permanecer oculto durante el entrenamiento para evaluar honestamente la predicción?

## Diapositiva 11. Ejemplo de predicción

**Qué presenta:** transición hacia un ejercicio en Google Colab.

**Cómo entenderla:** Un notebook permite ejecutar código, ver datos y modificar parámetros. Antes de correrlo, debemos definir qué queremos predecir, cuáles son las entradas y cómo evaluaremos el resultado.

**Advertencia:** “Predicción de poesía” aparece sin contexto suficiente. El docente debería explicar el problema, el dataset y la salida esperada.

## Diapositiva 12. Programación tradicional y Machine Learning

**Qué presenta:** comparación entre reglas escritas por una persona y un modelo aprendido desde ejemplos.

**Cómo entenderla:** En programación tradicional, una persona escribe reglas que transforman entradas en salidas. En aprendizaje supervisado, entregamos ejemplos con sus respuestas y un algoritmo ajusta un modelo. Las personas siguen definiendo el objetivo, seleccionando datos, eligiendo métodos y evaluando consecuencias.

**Corrección:** La máquina no inventa por sí sola “su algoritmo”; el algoritmo de entrenamiento ajusta un modelo.

## Diapositiva 13. Cuándo usar Machine Learning

**Qué presenta:** problemas con muchas observaciones, reglas difíciles de expresar y patrones complejos.

**Cómo entenderla:** ML resulta útil cuando podemos reconocer ejemplos correctos pero no redactar reglas completas y mantenibles. También se usa cuando las reglas cambian o interactúan de formas difíciles de programar.

**Límite:** Si una regla simple y estable resuelve el problema, quizá ML agregue complejidad innecesaria.

## Diapositiva 14. Aprender una función desde ejemplos

**Qué presenta:** pares de entrada y salida, como correos con etiqueta de spam o imágenes de dígitos.

**Cómo entenderla:** Cada ejemplo tiene variables X y una respuesta y. El entrenamiento busca una función aproximada capaz de relacionarlas. El verdadero desafío es que funcione con nuevos ejemplos.

**Ejemplos:** En spam, X representa características del correo e y indica spam/no spam. En dígitos, X representa píxeles e y indica un número del 0 al 9.

## Diapositiva 15. Técnicas para construir modelos

**Qué presenta:** redes neuronales, SVM y árboles de decisión.

**Cómo entenderla:** Son familias de modelos diferentes. Ninguna es mejor para todos los problemas. La elección depende del tipo de datos, cantidad de ejemplos, necesidad de interpretación, costo de entrenamiento y métrica relevante.

### Red neuronal

Una neurona calcula una combinación ponderada `z = w·x + b` y aplica una función no lineal. Al conectar neuronas en capas, la red puede representar fronteras complejas. Durante el entrenamiento, la salida se compara con la etiqueta mediante una función de pérdida; *backpropagation* calcula cómo contribuyó cada peso al error y un optimizador modifica los pesos para reducirlo.

- **Qué aprende:** pesos y sesgos de las conexiones.
- **Hiperparámetros importantes:** cantidad y tamaño de capas, función de activación, tasa de aprendizaje, tamaño de lote, épocas y regularización.
- **Fortaleza:** modela relaciones muy no lineales.
- **Límites:** suele necesitar más datos y cómputo; puede sobreajustar y no siempre es fácil explicar una predicción.

### Máquina de vectores de soporte, SVM

Una SVM lineal busca el hiperplano que separa las clases dejando el mayor margen posible. Los ejemplos que tocan o violan ese margen son los **vectores de soporte**: ellos determinan la frontera. El parámetro `C` controla el compromiso entre un margen amplio y penalizar errores. Con un *kernel*, como RBF, el algoritmo puede construir fronteras no lineales a partir de similitudes entre ejemplos sin calcular explícitamente todas las nuevas variables.

- **Qué aprende:** una frontera definida principalmente por los vectores de soporte.
- **Hiperparámetros importantes:** `C`; tipo de kernel; `gamma` en RBF.
- **Fortaleza:** puede funcionar bien en espacios con muchas variables.
- **Límites:** exige escalar variables; entrenar puede ser costoso con muchos ejemplos y la probabilidad no surge directamente del margen.

### Árbol de decisión

El árbol divide recursivamente los datos mediante preguntas del tipo `monto <= 5000`. En clasificación elige cortes que reduzcan la mezcla de clases, medida habitualmente con impureza de Gini o entropía. Una hoja devuelve la clase o la proporción de clases de los ejemplos que llegaron a ella.

- **Qué aprende:** variable y umbral de cada nodo, y predicción de cada hoja.
- **Hiperparámetros importantes:** profundidad máxima, mínimo de ejemplos para dividir o formar una hoja y criterio de impureza.
- **Fortaleza:** captura interacciones y es relativamente interpretable.
- **Límites:** un árbol profundo puede memorizar ruido y pequeños cambios en los datos pueden cambiar su estructura.

### Random Forest

Entrena muchos árboles sobre muestras *bootstrap* y considera un subconjunto aleatorio de variables en cada corte. En clasificación combina sus votos o probabilidades. Al reducir la correlación entre árboles, suele disminuir la varianza de un árbol individual.

- **Qué aprende:** un conjunto de árboles diferentes.
- **Hiperparámetros importantes:** número y profundidad de árboles, variables candidatas por corte y tamaños mínimos de hojas.
- **Fortaleza:** baseline robusto para datos tabulares y relaciones no lineales.
- **Límites:** el bosque completo es menos interpretable y una importancia de variables no demuestra causalidad.

**Idea para recordar:** Primero se define el problema y la evaluación; después se compara qué modelo funciona mejor.

## Diapositiva 16. IA, ML y aprendizaje profundo

**Qué presenta:** relación de inclusión entre inteligencia artificial, Machine Learning y deep learning.

**Cómo entenderla:** IA es el campo más amplio. Machine Learning es un conjunto de métodos dentro de IA. El aprendizaje profundo utiliza redes neuronales con múltiples capas y forma parte de ML.

**Aclaración:** Esta diapositiva repite la lista anterior, pero el diagrama aporta la relación jerárquica.

## Diapositiva 17. Estadística, minería de datos y ML

**Qué presenta:** roles de la estadística y la minería de datos.

**Cómo entenderla:** La estadística ayuda a describir datos, estimar incertidumbre y evaluar si un patrón podría deberse al azar. La minería de datos busca patrones útiles a escala. Machine Learning construye modelos capaces de generalizar. Las fronteras entre estos campos se superponen.

**Pregunta:** ¿Un resultado predictivo puede considerarse útil si no entendemos su incertidumbre ni su forma de evaluación?

## Diapositiva 18. Herramientas y organizaciones

**Qué presenta:** Python, Spark, R, Elasticsearch, Kibana y ejemplos de uso organizacional.

**Cómo entenderla:** La diapositiva mezcla lenguajes, motores de procesamiento, búsqueda y visualización. Python y R sirven para programar análisis; Spark procesa datos distribuidos; Elasticsearch indexa y busca; Kibana visualiza información asociada a Elasticsearch.

**Idea para recordar:** Una herramienta debe asociarse a una tarea concreta dentro del flujo.

## Diapositiva 19. Arquitectura moderna de datos

**Qué presenta:** fuentes, almacenamiento distribuido, procesamiento y consumo.

**Cómo entenderla:** Los datos ingresan desde distintas fuentes, se almacenan, se transforman y terminan en reportes o aplicaciones. El diagrama debe leerse de izquierda a derecha, siguiendo el recorrido del dato.

**Pregunta:** ¿Dónde controlarías calidad, permisos y trazabilidad?

## Diapositiva 20. Procesos con Hadoop

**Qué presenta:** procesamiento por lotes, almacenamiento histórico, algoritmos distribuidos y HBase.

**Cómo entenderla:** Hadoop reúne componentes para trabajar con datos distribuidos. HDFS almacena archivos; MapReduce procesa lotes; otras herramientas del ecosistema cubren consultas, bases y flujos. Spark puede integrarse, pero es un proyecto distinto.

**Advertencia:** No todos los componentes ofrecen la misma latencia ni sirven para la misma tarea.

## Diapositiva 21. Hadoop y detección de fraude

**Qué presenta:** argumentos comerciales para usar una plataforma distribuida.

**Cómo entenderla:** Una solución de fraude necesita integrar transacciones, perfiles y señales históricas. La arquitectura debe responder dentro del tiempo exigido por el negocio. El nombre “Hadoop” por sí solo no garantiza milisegundos: esa capacidad depende de los componentes y del diseño completo.

**Pregunta:** ¿La decisión debe tomarse antes de autorizar la compra o puede llegar minutos después?

## Diapositiva 22. Patrón de arquitectura para fraude

**Qué presenta:** fuentes que ingresan a una plataforma, procesos y consumidores.

**Cómo entenderla:** Identificá cuatro zonas: origen, ingesta, almacenamiento/procesamiento y salida. La arquitectura permite que varios consumidores, como Python, SAS o reportes, utilicen los datos preparados.

**Actividad:** Dibujá el camino de una transacción desde que ocurre hasta que genera una alerta.

## Diapositiva 23. Plataforma de datos semántica

**Qué presenta:** fuentes, cargadores, lago de datos, catálogo, linaje y destinos.

**Cómo entenderla:** El dato no solo se guarda. También necesita descripción, descubrimiento, reglas de calidad y registro de su origen. El linaje permite saber de dónde vino y qué transformaciones recibió.

**Idea para recordar:** Sin catálogo y gobierno, un repositorio grande puede volverse difícil de comprender y reutilizar.

## Diapositiva 24. Ingesta y productos de datos

**Qué presenta:** fuentes que alimentan un lago y pipelines que producen conjuntos listos para consumo.

**Cómo entenderla:** Un producto de datos es un conjunto preparado para un propósito concreto. Diferentes equipos pueden consumirlo desde notebooks, aplicaciones o herramientas de inteligencia de negocio.

**Pregunta:** ¿Qué contrato de calidad debería cumplir antes de llamarlo producto de datos?

## Diapositiva 25. Flujo de tratamiento

**Qué presenta:** ingesta batch y streaming, procesamiento, consumo y analítica en tiempo real.

**Cómo entenderla:** Batch acumula y procesa; streaming analiza eventos continuos. Ambos pueden convivir. La elección depende de la latencia requerida, costo, volumen y complejidad operacional.

**Ejemplo:** Un cierre contable puede procesarse por lote; una autorización de tarjeta exige una respuesta mucho más rápida.

## Diapositiva 26. Data Lake, Data Warehouse y Feature Store

**Qué presenta:** funciones de tres repositorios dentro de una arquitectura analítica.

**Cómo entenderla:** El Data Lake conserva datos diversos; el Data Warehouse prepara información para reportes; el Feature Store administra variables reutilizables por modelos. ETL conecta y transforma estos componentes.

**Aclaración:** No toda organización necesita los tres. La arquitectura debe responder al problema real.

## Diapositiva 27. Caso práctico de predicción de fraude

**Qué presenta:** usos de ML en finanzas y una explicación de detección de fraude.

**Cómo entenderla:** El modelo aprende patrones de transacciones anteriores y asigna una probabilidad de fraude a una nueva operación. Una anomalía no equivale automáticamente a fraude; el sistema necesita un criterio de decisión y revisión.

**Pregunta central:** ¿Qué cuesta más: dejar pasar un fraude o bloquear una compra legítima?

## Diapositiva 28. Aprendizaje supervisado y no supervisado

**Qué presenta:** algoritmos de ambas familias.

**Cómo entenderla:** Si conocemos qué transacciones fueron fraude, podemos entrenar un clasificador supervisado. Si tenemos pocas etiquetas, podemos buscar casos atípicos o grupos mediante métodos no supervisados. PCA reduce dimensiones; K-Means agrupa ejemplos.

### Regresión lineal y regresión logística no resuelven lo mismo

La **regresión lineal** estima un valor continuo: `ŷ = β₀ + β₁x₁ + ... + βₚ xₚ`. Sus coeficientes suelen ajustarse minimizando la suma de errores cuadrados. La salida puede ser cualquier número, por lo que no representa necesariamente una probabilidad y no es adecuada como clasificador binario.

La **regresión logística** primero calcula una combinación lineal y luego aplica la sigmoide: `p(y=1|x) = 1 / (1 + exp(-z))`. Se ajusta maximizando la verosimilitud, equivalente a minimizar la pérdida logarítmica. La clase se obtiene comparando la probabilidad con un umbral que no tiene por qué ser 0,5.

- **Qué aprende:** un coeficiente por variable y un intercepto.
- **Interpretación:** `exp(βⱼ)` es el cambio multiplicativo en los *odds* por una unidad de `xⱼ`, manteniendo las demás variables constantes.
- **Hiperparámetros:** fuerza y tipo de regularización (`L1`, `L2`), pesos de clase y algoritmo de optimización.
- **Límite:** la frontera es lineal en las variables suministradas; para interacciones o curvas hay que construir nuevas variables o elegir otro modelo.

### Clasificador bayesiano ingenuo, Naive Bayes

Aplica el teorema de Bayes: `P(clase|x) ∝ P(clase) P(x|clase)`. La simplificación "ingenua" supone que las variables son condicionalmente independientes dada la clase, lo cual permite factorizar `P(x|clase)` como un producto. En la práctica se calculan logaritmos para evitar problemas numéricos.

- **Variantes:** Gaussian NB para variables continuas aproximadamente gaussianas por clase; Multinomial NB para conteos, frecuente en texto; Bernoulli NB para variables binarias.
- **Qué aprende:** probabilidad previa de cada clase y parámetros de la distribución de cada variable condicionada a la clase.
- **Fortaleza:** es rápido, requiere pocos datos y constituye un baseline valioso.
- **Límite:** variables muy dependientes pueden contar la misma evidencia varias veces; sus probabilidades pueden necesitar calibración.

### K-Means

K-Means busca `k` centroides que minimicen la suma de distancias cuadráticas de cada punto a su centro asignado. Alterna dos pasos: asignar cada ejemplo al centroide más cercano y recalcular cada centroide como la media de su grupo. Converge a un óptimo local, por eso se prueban varias inicializaciones.

- **Hiperparámetros:** número de grupos `k`, inicialización y número de reinicios.
- **Supuestos prácticos:** variables comparables en escala y grupos aproximadamente compactos según distancia euclídea.
- **Límite en fraude:** un grupo pequeño o un punto lejano no es automáticamente fraude; el algoritmo no conoce esa etiqueta.

### PCA

PCA centra los datos y busca direcciones ortogonales que capturen la mayor varianza. Puede calcularse mediante descomposición en valores singulares, SVD. Cada componente es una combinación lineal de las variables originales; los primeros componentes conservan la mayor parte de la varianza, no necesariamente la información más útil para predecir fraude.

- **Qué aprende:** ejes principales y la varianza explicada por cada uno.
- **Hiperparámetro principal:** cantidad de componentes o proporción de varianza a conservar.
- **Fortaleza:** reduce redundancia y facilita visualización o compresión.
- **Límites:** es lineal, sensible a las escalas y reduce interpretabilidad.

**Aclaración:** Supervisado y no supervisado responden preguntas distintas y pueden complementarse.

## Diapositiva 29. Lectura del dataset

**Qué presenta:** carga de `creditcard_data.csv`, vista inicial y forma `(5050, 30)`.

**Cómo entenderla:** Hay 5050 filas y 30 columnas. Antes de entrenar, necesitamos conocer el significado de las columnas, identificar la etiqueta, contar clases, buscar faltantes y documentar la fuente.

**Código orientativo:** `df['Class'].value_counts()` permite observar cuántas operaciones existen por clase.

**Pregunta:** ¿Qué porcentaje corresponde a fraude?

## Diapositiva 30. Aplicación de remuestreo

**Qué presenta:** comparación visual antes y después de equilibrar clases.

**Cómo entenderla:** El objetivo es evitar que el modelo ignore la clase minoritaria. Sin embargo, equilibrar los datos no garantiza un buen modelo. Debemos conservar intacto el test y evaluar con métricas adecuadas.

**Riesgo:** Aplicar el remuestreo antes de separar los datos genera fuga de información.

## Diapositiva 31. RUS, ROS y SMOTE

**Qué presenta:** tres estrategias ante el desbalance.

**Cómo entenderla:** RUS elimina ejemplos de la clase mayoritaria; ROS repite ejemplos minoritarios; SMOTE genera ejemplos sintéticos. Cada método tiene ventajas y riesgos. Debe compararse contra un baseline sin remuestreo.

**Corrección:** Los ejemplos de SMOTE son sintéticos, no simplemente “falsos”. Pueden ayudar, pero también crear puntos poco realistas.

### Qué hace exactamente cada técnica

- **Random Under-Sampling (RUS):** selecciona al azar una parte de la clase mayoritaria. Cambia la distribución del entrenamiento y reduce costo, pero descarta observaciones que podrían describir fronteras importantes.
- **Random Over-Sampling (ROS):** muestrea con reemplazo observaciones minoritarias hasta alcanzar la proporción elegida. No inventa información nueva y hace que algunos ejemplos influyan más veces en la pérdida.
- **SMOTE:** para un ejemplo minoritario `xᵢ`, elige uno de sus vecinos minoritarios `xⱼ` y genera `x_nuevo = xᵢ + λ(xⱼ - xᵢ)`, con `λ` entre 0 y 1. El nuevo punto queda sobre el segmento entre ambos.
- **Borderline-SMOTE:** prioriza ejemplos minoritarios rodeados por muchos vecinos mayoritarios, es decir, cercanos a una posible frontera. Puede concentrar información útil, pero también amplificar ruido o etiquetas incorrectas.

SMOTE usa distancias: las variables deben tener una representación y escala coherentes. Interpolar categorías codificadas como números puede producir combinaciones sin sentido; para datos mixtos existen variantes como SMOTENC. Ninguna de estas técnicas garantiza una mejora: se comparan mediante validación y con la métrica de negocio elegida.

## Diapositiva 32. División y entrenamiento

**Qué presenta:** 80% para entrenamiento, 20% para prueba, SMOTE y regresión logística.

**Cómo entenderla:** Primero se separa el test. Luego se aplica el remuestreo únicamente al entrenamiento. Finalmente se entrena el clasificador y se evalúa con datos nunca usados para ajustar el modelo.

**Actualización técnica:** La API mostrada está desactualizada. En versiones actuales se utiliza `fit_resample`. Para Borderline-SMOTE se usa una clase específica. También conviene `stratify=y` y `random_state` en la separación.

**Buena práctica:** Integrar preprocesamiento, remuestreo y modelo en un pipeline durante la validación cruzada.

### Por qué el orden evita una evaluación engañosa

1. Separar el test preserva una muestra del problema real.
2. Dentro de cada partición de entrenamiento se ajustan escalado, imputación y SMOTE.
3. Esas transformaciones ya ajustadas se aplican a validación sin aprender de ella.
4. Recién después de elegir el procedimiento se usa una sola vez el test final.

Si se aplica SMOTE antes de dividir, un punto sintético del entrenamiento puede haber sido construido usando un vecino que luego aparece en test. La prueba deja de ser independiente. `stratify=y` conserva aproximadamente la proporción de clases, pero si los datos tienen tiempo, clientes repetidos o comercios compartidos puede ser necesario dividir por tiempo o por grupo para evitar otra forma de fuga.

## Diapositiva 33. Sistema de reglas

**Qué presenta:** una decisión basada en umbrales y reglas predefinidas.

**Cómo entenderla:** Un sistema de reglas puede decir, por ejemplo, que una compra se revise si supera cierto monto y ocurre lejos del patrón habitual. Es fácil de explicar, pero puede volverse rígido y complejo cuando crecen las excepciones.

**Idea para recordar:** Las reglas constituyen un baseline útil y pueden combinarse con modelos.

## Diapositiva 34. Limitaciones de las reglas

**Qué presenta:** umbrales fijos, respuesta binaria y dificultad para capturar interacciones.

**Cómo entenderla:** Una regla analiza condiciones explícitas. Un modelo puede aprender combinaciones entre monto, hora, comercio y comportamiento previo. Aun así, un modelo también falla y necesita monitoreo.

**Pregunta:** ¿Qué reglas conservarías aunque exista un modelo?

## Diapositiva 35. Ventajas potenciales de ML

**Qué presenta:** adaptación a datos, combinación de variables, puntaje de riesgo y mejora de rendimiento.

**Cómo entenderla:** Un clasificador puede producir una probabilidad o puntaje, permitiendo distintos tratamientos. Por ejemplo, aprobar riesgo bajo, pedir verificación adicional en riesgo medio y bloquear riesgo alto.

**Aclaración:** Un modelo no se adapta automáticamente de manera segura. Debe reentrenarse, validarse, desplegarse y monitorearse bajo supervisión.

## Diapositiva 36. Código final y supuesto 82% de acierto

**Qué presenta:** regresión lineal, `r2_score` y una interpretación como porcentaje de acierto.

**Corrección imprescindible:** Este ejemplo no debe utilizarse como demostración válida de fraude. Fraude/no fraude es clasificación. `LinearRegression` y `R²` corresponden a regresión; un R² de 0,821 no equivale a 82% de predicciones correctas.

**Cómo debería resolverse:** Entrenar un clasificador, por ejemplo regresión logística. Obtener probabilidades, elegir un umbral y mostrar la matriz de confusión. Luego comparar precision, recall, F1 y PR-AUC. La métrica elegida debe reflejar el costo de dejar pasar fraudes y el costo de bloquear operaciones legítimas.

### Qué optimiza cada modelo y qué significa su salida

- `LinearRegression` minimiza errores cuadrados entre un valor numérico real y uno estimado. `R²` compara ese error con el de predecir siempre la media; puede ser negativo y no mide aciertos de clase.
- `LogisticRegression` minimiza pérdida logarítmica para estimar `P(fraude|x)`. El umbral transforma esa estimación en una decisión.
- Un umbral menor suele aumentar recall y falsas alarmas; uno mayor suele aumentar precision y dejar pasar más fraudes. La curva precision-recall muestra ese intercambio.
- `class_weight="balanced"` aumenta la penalización de equivocarse en la clase escasa. No crea ejemplos y no es equivalente a SMOTE, aunque ambos intentan evitar que la mayoría domine el aprendizaje.

**Pregunta de cierre:** ¿Qué resultado necesitarías para recomendar el modelo y qué daño podría causar una decisión equivocada?

---

# Parte 3. Referencias para profundizar en las técnicas

Las referencias de documentación sirven como puente hacia la implementación; los artículos originales permiten estudiar la formulación y los experimentos que introdujeron cada método.

- Scikit-learn, [modelos lineales y regresión logística](https://scikit-learn.org/stable/modules/linear_model.html).
- Scikit-learn, [Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html).
- Scikit-learn, [máquinas de vectores de soporte](https://scikit-learn.org/stable/modules/svm.html); Cortes y Vapnik (1995), [*Support-vector networks*](https://doi.org/10.1007/BF00994018).
- Scikit-learn, [árboles de decisión](https://scikit-learn.org/stable/modules/tree.html) y [métodos de ensamble](https://scikit-learn.org/stable/modules/ensemble.html); Breiman (2001), [*Random Forests*](https://doi.org/10.1023/A:1010933404324).
- Scikit-learn, [redes neuronales supervisadas](https://scikit-learn.org/stable/modules/neural_networks_supervised.html).
- Scikit-learn, [K-Means](https://scikit-learn.org/stable/modules/clustering.html#k-means) y [PCA](https://scikit-learn.org/stable/modules/decomposition.html#pca).
- Chawla, Bowyer, Hall y Kegelmeyer (2002), [*SMOTE: Synthetic Minority Over-sampling Technique*](https://doi.org/10.1613/jair.953); imbalanced-learn, [guía de remuestreo](https://imbalanced-learn.org/stable/user_guide.html).
- Scikit-learn, [precision, recall y F-measure](https://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measure-metrics) y [ajuste del umbral de decisión](https://scikit-learn.org/stable/modules/classification_threshold.html).

## Guía de lectura teórica

Para cada algoritmo, intentá responder en este orden:

1. ¿Qué representa una entrada y cuál es la salida?
2. ¿Qué parámetros aprende a partir de los datos?
3. ¿Qué función objetivo o criterio intenta optimizar?
4. ¿Qué supuestos hace sobre los datos?
5. ¿Qué hiperparámetros decide la persona antes de entrenar?
6. ¿Qué error puede cometer y con qué métrica se observa?
7. ¿Cómo sabríamos si la salida puede usarse para tomar una decisión real?

# Parte 4. Recorrido de estudio sugerido

## Antes de la clase

1. Leé el diccionario hasta “Machine Learning”.
2. Elegí un sistema cotidiano que genere datos.
3. Escribí qué podría predecirse y qué decisión tomaría una persona con esa predicción.

## Durante la clase

En cada bloque completá cuatro preguntas:

1. ¿Cuál es el problema?
2. ¿Qué datos entran?
3. ¿Qué transformación o modelo se aplica?
4. ¿Cómo sabremos si el resultado sirve?

## Después de la clase

Prepará una ficha con:

- descripción del problema de fraude;
- variables de entrada y etiqueta;
- diferencia entre regla y modelo;
- matriz de confusión explicada con palabras;
- métrica principal y justificación;
- una limitación técnica;
- un riesgo ético o de privacidad.

# Parte 5. Autoevaluación

1. ¿Por qué Big Data no significa solamente gran volumen?
2. ¿Puede existir Machine Learning sin Big Data? Incluí un ejemplo.
3. ¿Qué diferencia existe entre algoritmo, modelo, entrenamiento e inferencia?
4. ¿Por qué accuracy puede engañar en fraude?
5. ¿Qué significa un falso positivo para el cliente?
6. ¿Qué significa un falso negativo para la organización?
7. ¿Por qué SMOTE se aplica solo al entrenamiento?
8. ¿Qué diferencia existe entre procesamiento batch y streaming?
9. ¿Qué funciones cumplen Data Lake, Data Warehouse y Feature Store?
10. ¿Por qué `LinearRegression` con `R²` no valida un detector binario de fraude?
11. ¿Qué diferencia existe entre los parámetros que aprende un modelo y sus hiperparámetros?
12. ¿Qué supuesto de Naive Bayes se considera “ingenuo” y por qué aun así puede funcionar bien?
13. ¿Qué ejemplos determinan principalmente la frontera de una SVM?
14. ¿Por qué un Random Forest suele ser más estable que un único árbol?
15. ¿Por qué un clúster pequeño de K-Means no equivale a fraude?
16. ¿Qué problema puede aparecer si aplicamos SMOTE a categorías codificadas como enteros?

# Frase guía de la clase

**¿Qué datos tenemos, qué queremos predecir, cómo evaluamos el error y qué decisión tomaremos con el resultado?**
