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

**Qué presenta:** redes neuronales, máquinas de vectores de soporte (SVM) y árboles de decisión. Para compararlas, conviene sumar dos referencias básicas: regresión logística y Naive Bayes.

### Regresión logística: una probabilidad a partir de una combinación lineal

Para una entrada con variables \(x_1,\ldots,x_p\), calcula primero un puntaje

\[
z=b+w_1x_1+\cdots+w_px_p
\]

y lo transforma con la función sigmoide:

\[
P(y=1\mid x)=\sigma(z)=\frac{1}{1+e^{-z}}.
\]

El entrenamiento busca los pesos que minimizan la *log loss* o entropía cruzada: asignar baja probabilidad a la clase verdadera recibe una penalización grande. Un umbral —no necesariamente 0,5— convierte la probabilidad en clase. La frontera es lineal en las variables de entrada, aunque pueden agregarse interacciones o transformaciones no lineales.

**Supuestos y límites:** las observaciones deben aportar información suficiente y la relación entre variables y *log-odds* debe poder aproximarse linealmente. Variables muy correlacionadas vuelven inestables los coeficientes; regularización L1 o L2 ayuda a limitar su magnitud. Los coeficientes describen cambios en *log-odds*, no causalidad.

### Naive Bayes: actualizar una probabilidad con evidencia

Parte del teorema de Bayes:

\[
P(y\mid x)=\frac{P(x\mid y)P(y)}{P(x)}.
\]

Para decidir una clase basta comparar \(P(y)P(x\mid y)\). La simplificación "naive" supone independencia condicional entre características dada la clase:

\[
P(x\mid y)=\prod_j P(x_j\mid y).
\]

El algoritmo estima una probabilidad previa \(P(y)\) y la distribución de cada variable dentro de cada clase. Gaussian Naive Bayes modela variables continuas con gaussianas; Multinomial NB se usa con conteos —por ejemplo, palabras— y Bernoulli NB con presencia/ausencia. Se calculan logaritmos para evitar subdesbordamiento numérico.

**Fortalezas y límites:** es rápido y funciona bien con pocos datos o alta dimensionalidad, especialmente en texto. La independencia rara vez se cumple exactamente; aun así puede clasificar bien. Sus probabilidades pueden quedar mal calibradas y una frecuencia cero requiere suavizado, como Laplace.

### SVM: buscar una frontera con margen máximo

Una SVM lineal busca el hiperplano \(w^Tx+b=0\) que separa las clases dejando el mayor margen posible. Sólo algunos casos cercanos a la frontera —los **vectores de soporte**— determinan la solución. Si hay solapamiento, el parámetro \(C\) equilibra margen amplio y penalización de errores: un \(C\) grande castiga más los errores; uno pequeño regulariza más.

Un *kernel* reemplaza el producto interno por una función de similitud y permite fronteras no lineales sin construir explícitamente todas las nuevas dimensiones. En el kernel RBF, \(\gamma\) controla cuánto influye cada ejemplo. Las variables deben escalarse y \(C\), \(\gamma\) y el kernel deben elegirse con validación, no con el test final.

**Fortalezas y límites:** puede funcionar muy bien en espacios de muchas dimensiones, pero entrenar y ajustar kernels puede ser costoso en datasets grandes. El puntaje de una SVM no es una probabilidad salvo que se agregue calibración.

### Árbol de decisión y Random Forest

Un árbol elige preguntas del tipo \(x_j<t\) que vuelven más puros los nodos hijos. En clasificación suelen usarse impureza Gini o entropía. El proceso continúa de manera voraz: el mejor corte local no garantiza el árbol global óptimo. Profundidad, cantidad mínima de ejemplos por hoja y poda controlan el sobreajuste.

Random Forest entrena muchos árboles sobre muestras *bootstrap* y prueba un subconjunto aleatorio de variables en cada división. La predicción se obtiene por voto o promedio. La aleatoriedad reduce la correlación entre árboles y el promedio reduce varianza; no elimina sesgos del dataset ni vuelve causal la importancia de variables.

### Red neuronal: composición de transformaciones

Cada neurona calcula \(a=\phi(w^Tx+b)\), donde \(\phi\) es una activación no lineal. Al apilar capas, la red puede representar relaciones complejas. Durante *forward propagation* produce una salida; la función de pérdida mide el error; *backpropagation* aplica la regla de la cadena para obtener gradientes, y un optimizador actualiza los pesos.

Sin activaciones no lineales, muchas capas equivaldrían a una sola transformación lineal. Profundidad, cantidad de unidades, tasa de aprendizaje, regularización y datos disponibles determinan el resultado. Las redes son flexibles, pero suelen necesitar más datos y cómputo, y no garantizan interpretabilidad ni buena calibración.

**Idea para recordar:** no existe un algoritmo universalmente mejor. Primero se fija el problema, la métrica y el protocolo de evaluación; luego se comparan modelos bajo las mismas particiones y costos.

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

**Cómo entenderla:** Si conocemos qué transacciones fueron fraude, podemos entrenar un clasificador supervisado: regresión logística, Naive Bayes, SVM, árboles o redes aprenden una relación entre \(X\) e \(y\). Si no tenemos etiquetas, los métodos no supervisados sólo encuentran estructura en \(X\); no saben por sí mismos qué grupo significa "fraude".

### K-Means

Busca \(K\) centroides que minimicen la suma de distancias cuadradas de cada punto a su centro asignado. Alterna dos pasos: asignar cada ejemplo al centro más cercano y recalcular cada centro como la media de sus ejemplos. Cada iteración no aumenta el objetivo, pero puede converger a un mínimo local; por eso se prueban varias inicializaciones, habitualmente `k-means++`.

**Supuestos y límites:** favorece grupos aproximadamente esféricos, de escala y densidad semejantes. Es sensible a escala, valores extremos y elección de \(K\). Debe estandarizarse cuando las unidades difieren. Un clúster pequeño o lejano no es automáticamente fraude.

### PCA

Centra los datos y encuentra direcciones ortogonales de máxima varianza. Algebraicamente, son los autovectores de la matriz de covarianza; en la práctica suele calcularse con descomposición en valores singulares (SVD). El primer componente explica la mayor varianza posible, el segundo la mayor varianza restante y así sucesivamente.

**Supuestos y límites:** PCA es una proyección lineal y no usa la etiqueta. Mucha varianza no equivale a mucha capacidad predictiva: una señal de fraude con poca varianza podría descartarse. El escalado modifica el resultado y los componentes son combinaciones de variables que pueden ser difíciles de interpretar.

**Aclaración:** supervisado y no supervisado responden preguntas distintas y pueden complementarse. K-Means y PCA sirven para explorar o construir variables, pero su salida debe validarse contra etiquetas y decisiones del negocio antes de llamarla detector de fraude.

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

**Cómo entenderla:** RUS elimina al azar ejemplos de la clase mayoritaria; reduce tiempo y puede equilibrar el aprendizaje, pero descarta información. ROS replica ejemplos minoritarios; no pierde datos, aunque repetirlos puede favorecer sobreajuste.

SMOTE elige un ejemplo minoritario \(x_i\), uno de sus vecinos minoritarios \(x_j\) y genera

\[
x_{nuevo}=x_i+\lambda(x_j-x_i),\qquad \lambda\in[0,1].
\]

El nuevo punto queda sobre el segmento entre ambos ejemplos. No es una copia, pero tampoco es una observación real. Si los vecinos mezclan regiones o contienen ruido, SMOTE puede crear puntos ambiguos; además, la interpolación ordinaria no corresponde directamente a categorías sin un método adaptado.

Borderline-SMOTE concentra la generación en ejemplos minoritarios cercanos a la frontera. `class_weight` ofrece otra estrategia: conserva los datos y aumenta el costo de equivocarse en la clase minoritaria. Ninguna técnica debe aceptarse sólo porque equilibra conteos: hay que comparar precision, recall, PR-AUC, calibración y costo operativo.

**Regla crítica:** separar primero el test. Dentro de validación cruzada, el remuestreo debe ajustarse nuevamente sólo con el fold de entrenamiento. Remuestrear antes de dividir permite que información derivada de validación o test llegue al entrenamiento y produce una evaluación optimista.

## Diapositiva 32. División y entrenamiento

**Qué presenta:** 80% para entrenamiento, 20% para prueba, SMOTE y regresión logística.

**Cómo entenderla:** Primero se separa el test. Luego se aplica el remuestreo únicamente al entrenamiento. Finalmente se entrena el clasificador y se evalúa con datos nunca usados para ajustar el modelo.

**Actualización técnica:** La API mostrada está desactualizada. En versiones actuales se utiliza `fit_resample`. Para Borderline-SMOTE se usa una clase específica. También conviene `stratify=y` y `random_state` en la separación.

**Buena práctica:** Integrar preprocesamiento, remuestreo y modelo en un pipeline durante la validación cruzada.

### Qué aprende la regresión logística en este flujo

El modelo no aprende una regla fija de fraude: ajusta un peso por variable para minimizar la entropía cruzada regularizada. Con `class_weight="balanced"`, los errores de la clase escasa pesan más durante el ajuste; con SMOTE cambia la muestra usada para estimar la frontera. Son intervenciones diferentes y deben compararse, no acumularse automáticamente.

El método `predict_proba` entrega un puntaje entre 0 y 1 según el modelo. El umbral se selecciona con validación y una función de costo; elegirlo mirando el test contamina la evaluación final. Si se necesita interpretar el puntaje como probabilidad, también debe revisarse su calibración.

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

### Por qué regresión lineal y R² no responden esta pregunta

La regresión lineal minimiza errores cuadrados para una variable continua y puede producir valores menores que 0 o mayores que 1. \(R^2=1-SS_{res}/SS_{tot}\) compara ese error cuadrático con predecir la media: no cuenta aciertos ni define una clase. Tratar sus salidas como probabilidades viola la forma del problema.

La regresión logística, en cambio, limita la salida a \([0,1]\) y optimiza una pérdida diseñada para etiquetas binarias. Esto no la vuelve automáticamente buena: aún necesita partición correcta, comparación con baselines, métricas por clase, selección de umbral y validación temporal cuando el fraude cambia con el tiempo.

**Pregunta de cierre:** ¿Qué resultado necesitarías para recomendar el modelo y qué daño podría causar una decisión equivocada?

---

# Referencias para profundizar en los algoritmos

Las referencias de implementación ayudan a reproducir los métodos; los artículos y libros explican su fundamento. Conviene leer ambas capas.

- Scikit-learn, [guía de modelos supervisados](https://scikit-learn.org/stable/supervised_learning.html): regresión logística, Naive Bayes, SVM, árboles, ensembles y redes neuronales, con formulación matemática y parámetros.
- Scikit-learn, [K-Means](https://scikit-learn.org/stable/modules/clustering.html#k-means) y [PCA](https://scikit-learn.org/stable/modules/decomposition.html#pca): objetivos, algoritmos, complejidad y límites prácticos.
- Cortes, C. y Vapnik, V. (1995), [Support-Vector Networks](https://doi.org/10.1007/BF00994018), *Machine Learning* 20: fundamento del margen máximo y los kernels.
- Breiman, L. et al. (1984), [Classification and Regression Trees](https://doi.org/10.1201/9781315139470): referencia clásica sobre construcción y poda de árboles.
- Breiman, L. (2001), [Random Forests](https://doi.org/10.1023/A:1010933404324), *Machine Learning* 45: árboles aleatorizados, voto, fuerza y correlación del ensemble.
- Rumelhart, D. E., Hinton, G. E. y Williams, R. J. (1986), [Learning representations by back-propagating errors](https://doi.org/10.1038/323533a0), *Nature* 323: formulación clásica de backpropagation.
- Ng, A. y Jordan, M. (2002), [On Discriminative vs. Generative Classifiers](https://proceedings.neurips.cc/paper/2001/hash/7b7a53e239400a13bd6be6c91c4f6c4e-Abstract.html): comparación teórica entre regresión logística y Naive Bayes.
- Lloyd, S. (1982), [Least Squares Quantization in PCM](https://doi.org/10.1109/TIT.1982.1056489), *IEEE Transactions on Information Theory*: base del algoritmo iterativo asociado a K-Means.
- Jolliffe, I. T. y Cadima, J. (2016), [Principal component analysis: a review and recent developments](https://doi.org/10.1098/rsta.2015.0202): interpretación y fundamentos de PCA.
- Chawla, N. V. et al. (2002), [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953), *Journal of Artificial Intelligence Research* 16: método original y evaluación.
- Imbalanced-learn, [errores comunes y fuga de información al remuestrear](https://imbalanced-learn.org/stable/common_pitfalls.html): ejemplos reproducibles de por qué el test debe quedar intacto.
- Saito, T. y Rehmsmeier, M. (2015), [The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets](https://doi.org/10.1371/journal.pone.0118432): fundamento para usar curvas precision-recall con clases escasas.

---

# Parte 3. Recorrido de estudio sugerido

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

# Parte 4. Autoevaluación

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

# Frase guía de la clase

**¿Qué datos tenemos, qué queremos predecir, cómo evaluamos el error y qué decisión tomaremos con el resultado?**
