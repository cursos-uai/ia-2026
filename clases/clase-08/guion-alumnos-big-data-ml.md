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

**Idea para recordar:** Primero se define el problema y la evaluación; después se compara qué modelo funciona mejor.

### Cómo funciona cada familia

#### Regresión lineal: predecir una cantidad

La regresión lineal representa una salida continua mediante una suma ponderada:

`ŷ = β₀ + β₁x₁ + ... + βₚxₚ`.

Cada coeficiente `βⱼ` expresa cuánto cambia la predicción cuando aumenta la variable `xⱼ`, manteniendo las demás constantes. El entrenamiento suele elegir los coeficientes que minimizan la suma de errores cuadrados. Elevar el error al cuadrado penaliza especialmente los errores grandes y permite resolver el ajuste con métodos algebraicos o de optimización.

Sirve para cantidades como precio, consumo o demanda. No es adecuada para fraude/no fraude: puede producir valores menores que 0 o mayores que 1 y su función de pérdida no representa bien una etiqueta binaria. Además, `R²` mide qué proporción de la variabilidad de una salida continua explica el modelo; no mide porcentaje de clasificaciones correctas.

**Supuestos que conviene revisar:** relación aproximadamente lineal, residuos independientes, varianza relativamente constante y ausencia de colinealidad extrema. La normalidad de los residuos importa principalmente para ciertos intervalos y pruebas estadísticas, no para calcular la predicción.

#### Regresión logística: estimar una probabilidad de clase

La regresión logística también calcula una combinación lineal `z = β₀ + βᵀx`, pero la transforma con la función sigmoide:

`P(y=1|x) = 1 / (1 + e⁻ᶻ)`.

El resultado queda entre 0 y 1. Durante el entrenamiento se maximizan las probabilidades asignadas a las etiquetas observadas, lo que equivale a minimizar la pérdida logarítmica o *log loss*. Para obtener una clase se aplica un umbral: con `0,5`, por ejemplo, una probabilidad igual o superior se clasifica como positiva. Ese umbral no es una ley; en fraude debe elegirse según el costo de falsos positivos y falsos negativos.

El coeficiente `βⱼ` actúa sobre el *log-odds*: al aumentar una unidad `xⱼ`, las *odds* se multiplican por `e^βⱼ`, si el resto permanece constante. La regularización L1 o L2 limita coeficientes excesivos y ayuda a controlar sobreajuste. Suele ser un buen *baseline* porque es rápida e interpretable, aunque sin transformar variables sólo construye una frontera lineal.

#### Naive Bayes: actualizar probabilidades con evidencia

El teorema de Bayes permite invertir una probabilidad condicional:

`P(clase|x) ∝ P(x|clase) · P(clase)`.

Naive Bayes simplifica el cálculo suponiendo que las características son condicionalmente independientes una vez conocida la clase. Así, `P(x|clase)` se obtiene multiplicando las contribuciones de cada variable. El supuesto suele ser falso en sentido estricto, pero el clasificador puede funcionar bien cuando las variables aportan señales complementarias, especialmente en texto.

Las variantes dependen de los datos: Gaussian Naive Bayes modela variables continuas con distribuciones normales; Multinomial Naive Bayes trabaja bien con conteos, como palabras; Bernoulli Naive Bayes usa variables binarias. Es rápido y útil como referencia, pero probabilidades mal calibradas, variables muy correlacionadas o una distribución elegida incorrectamente pueden perjudicarlo. En fraude, además, el prior de la clase positiva debe reflejar que el evento es raro o ajustarse conscientemente.

#### Árbol de decisión: aprender preguntas sucesivas

Un árbol divide repetidamente los datos con reglas como `monto > 15000`. En clasificación elige cada división buscando reducir la impureza de los nodos. Dos criterios frecuentes son Gini y entropía: ambos son mínimos cuando un nodo contiene una sola clase. Las hojas guardan una clase o una proporción de clases.

Los árboles capturan interacciones y relaciones no lineales sin exigir escalado. También pueden explicarse siguiendo el camino desde la raíz hasta una hoja. Sin límites de profundidad, cantidad mínima de ejemplos por hoja o poda, memorizan detalles del entrenamiento y tienen alta varianza: un pequeño cambio en los datos puede producir otro árbol.

#### Random Forest: promediar muchos árboles distintos

Un bosque aleatorio entrena numerosos árboles sobre muestras *bootstrap* y, en cada división, considera sólo un subconjunto aleatorio de variables. Las dos fuentes de azar reducen la correlación entre árboles. En clasificación se combinan sus votos o probabilidades.

El promedio suele generalizar mejor que un árbol individual y permite modelar relaciones complejas. A cambio, pierde parte de la explicación directa de un solo árbol y puede requerir más memoria y tiempo de inferencia. La importancia de variables basada en reducción de impureza puede favorecer variables continuas o de alta cardinalidad; la importancia por permutación suele ofrecer una comprobación más fiable.

#### SVM: buscar una frontera con margen amplio

Una máquina de vectores de soporte busca el hiperplano que separa clases dejando el mayor margen posible. Sólo algunos casos cercanos a la frontera —los vectores de soporte— determinan la solución. El parámetro `C` controla el compromiso entre margen amplio y penalización de errores: un `C` grande castiga más las clasificaciones incorrectas y puede producir una frontera menos regularizada.

Mediante un *kernel*, como el radial RBF, puede representar fronteras no lineales calculando similitudes sin construir explícitamente todas las nuevas dimensiones. SVM es sensible a la escala de las variables y sus probabilidades requieren una calibración adicional. Puede rendir bien con muchas dimensiones, pero el entrenamiento se vuelve costoso con conjuntos muy grandes.

#### Red neuronal: componer transformaciones

Una neurona calcula una suma ponderada, agrega un sesgo y aplica una función no lineal. Al apilar capas, la red puede representar relaciones complejas que una combinación lineal no capturaría. La salida binaria suele usar una sigmoide y pérdida logarítmica.

El entrenamiento realiza una pasada hacia adelante para calcular la predicción, usa *backpropagation* para obtener derivadas mediante la regla de la cadena y actualiza los pesos con descenso por gradiente o una variante. La profundidad y las funciones de activación permiten aprender representaciones, pero no garantizan generalización: hacen falta validación, regularización, datos suficientes y monitoreo. En datos tabulares pequeños, un modelo más simple puede igualar o superar a una red y ser más fácil de explicar.

### Comparación conceptual rápida

| Técnica | Qué aprende | Frontera sin extensiones | Fortaleza típica | Riesgo principal |
|---|---|---|---|---|
| Regresión logística | probabilidad mediante log-odds | lineal | baseline interpretable | no captar relaciones no lineales |
| Naive Bayes | probabilidades generativas por clase | depende de la distribución | rapidez y pocos datos | independencia/distribución irreales |
| Árbol | reglas jerárquicas | no lineal | interacción y explicación local | sobreajuste e inestabilidad |
| Random Forest | promedio de árboles | no lineal | robustez en datos tabulares | menor interpretabilidad |
| SVM | frontera de margen máximo | lineal o no lineal con kernel | buen desempeño en alta dimensión | escalado y costo en grandes datos |
| Red neuronal | composición de representaciones | no lineal | gran flexibilidad | datos, ajuste y explicación |

**Referencias para profundizar:** [regresión lineal](https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares), [regresión logística](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression), [Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html), [árboles](https://scikit-learn.org/stable/modules/tree.html), [Random Forest](https://scikit-learn.org/stable/modules/ensemble.html#forest), [SVM](https://scikit-learn.org/stable/modules/svm.html) y [redes neuronales](https://www.deeplearningbook.org/contents/mlp.html).

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

**Aclaración:** Supervisado y no supervisado responden preguntas distintas y pueden complementarse.

### Qué optimizan los algoritmos mencionados

En aprendizaje supervisado, cada ejemplo contiene una etiqueta y la función de pérdida indica cuán costosa fue la predicción. Regresión logística, SVM, árboles, Naive Bayes y redes neuronales pueden producir clasificadores, pero llegan a la decisión por mecanismos diferentes: probabilidad discriminativa, margen, particiones, modelo probabilístico generativo y composición de transformaciones, respectivamente.

En aprendizaje no supervisado no hay una respuesta correcta `y` con la cual calcular error de clasificación:

- **K-Means** elige `k` centroides y alterna dos pasos: asigna cada caso al centro más cercano y recalcula cada centro como la media de su grupo. Minimiza la suma de distancias cuadradas dentro de los grupos. Por eso favorece grupos aproximadamente compactos y de escala semejante, es sensible al escalado, a valores extremos, a la inicialización y al valor de `k`. Un grupo pequeño no equivale por sí mismo a fraude.
- **PCA** centra los datos y encuentra direcciones ortogonales de máxima varianza. Matemáticamente puede obtenerse mediante autovectores de la matriz de covarianza o mediante SVD. Cada componente es una combinación lineal de variables; los primeros componentes conservan tanta varianza como sea posible, pero no necesariamente la información más útil para distinguir fraude.
- **SVD** factoriza una matriz `X` como `UΣVᵀ`. Los valores singulares de `Σ` ordenan la importancia de direcciones latentes. Truncar la factorización produce una aproximación de menor rango. PCA y SVD están relacionados, pero no son nombres intercambiables: PCA sobre datos centrados puede calcularse con SVD.

**Referencias:** [K-Means](https://scikit-learn.org/stable/modules/clustering.html#k-means), [PCA](https://scikit-learn.org/stable/modules/decomposition.html#pca) y [SVD truncada](https://scikit-learn.org/stable/modules/decomposition.html#truncated-singular-value-decomposition-and-latent-semantic-analysis).

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

### Cómo funcionan en detalle

- **Random Under-Sampling (RUS):** selecciona al azar sólo una parte de la clase mayoritaria. Cambia la distribución de entrenamiento y reduce el costo computacional, pero puede descartar casos que definían regiones importantes de la frontera.
- **Random Over-Sampling (ROS):** vuelve a muestrear con reemplazo casos de la clase minoritaria. No agrega información geométrica nueva; al repetir observaciones aumenta su influencia en la función de pérdida y puede favorecer el sobreajuste.
- **SMOTE:** para cada ejemplo minoritario elegido, busca vecinos minoritarios cercanos, toma uno y crea `x_nuevo = x + λ(x_vecino - x)`, con `λ` entre 0 y 1. El punto sintético queda en el segmento que une ambos ejemplos. La técnica densifica regiones minoritarias, pero si hay ruido, superposición de clases o variables categóricas mal tratadas puede crear casos ambiguos o imposibles.
- **Borderline-SMOTE:** concentra la síntesis en ejemplos minoritarios rodeados por muchos vecinos mayoritarios, es decir, cerca de la frontera. Puede ser útil porque refuerza la zona difícil, pero también amplifica ruido si esas observaciones están mal etiquetadas.
- **Pesos de clase:** en vez de modificar los datos, asignan mayor costo a equivocarse en la clase minoritaria. En regresión logística o SVM esto modifica la función de pérdida. Es una alternativa importante para comparar con SMOTE.

La distancia usada por SMOTE depende de la escala: una variable numéricamente grande puede dominar la noción de vecino. El escalado debe aprenderse dentro de cada partición de entrenamiento. Para datos mixtos existen variantes como SMOTENC; convertir categorías nominales en números y aplicar SMOTE estándar puede inventar valores sin significado.

**Regla metodológica:** separación, imputación, escalado, selección de variables y remuestreo deben organizarse de modo que ningún dato de validación o test influya en el ajuste. En validación cruzada, SMOTE se ejecuta nuevamente dentro de cada *fold* de entrenamiento mediante un pipeline de `imbalanced-learn`.

**Referencias:** [artículo original de SMOTE](https://www.jair.org/index.php/jair/article/view/10302), [guía de over-sampling](https://imbalanced-learn.org/stable/over_sampling.html) y [pipeline de imbalanced-learn](https://imbalanced-learn.org/stable/references/pipeline.html).

## Diapositiva 32. División y entrenamiento

**Qué presenta:** 80% para entrenamiento, 20% para prueba, SMOTE y regresión logística.

**Cómo entenderla:** Primero se separa el test. Luego se aplica el remuestreo únicamente al entrenamiento. Finalmente se entrena el clasificador y se evalúa con datos nunca usados para ajustar el modelo.

**Actualización técnica:** La API mostrada está desactualizada. En versiones actuales se utiliza `fit_resample`. Para Borderline-SMOTE se usa una clase específica. También conviene `stratify=y` y `random_state` en la separación.

**Buena práctica:** Integrar preprocesamiento, remuestreo y modelo en un pipeline durante la validación cruzada.

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

**Pregunta de cierre:** ¿Qué resultado necesitarías para recomendar el modelo y qué daño podría causar una decisión equivocada?

### Fundamento de la evaluación correcta

La regresión logística se entrena minimizando *log loss*, pero el sistema se evalúa de acuerdo con la decisión de negocio. Si `TP`, `FP`, `TN` y `FN` representan las cuatro celdas de la matriz de confusión:

- `precision = TP / (TP + FP)`: de las alertas generadas, cuántas eran fraude;
- `recall = TP / (TP + FN)`: de los fraudes reales, cuántos fueron detectados;
- `F1 = 2 · precision · recall / (precision + recall)`;
- `accuracy = (TP + TN) / total`.

Cambiar el umbral mueve el equilibrio entre precision y recall. La curva precision-recall muestra ese intercambio para muchos umbrales y resulta especialmente informativa cuando la clase positiva es rara. PR-AUC resume la curva, pero siempre debe acompañarse con la prevalencia, el protocolo de validación y métricas en un umbral operativo.

Las probabilidades también deben comprobarse. Un modelo está bien calibrado si, entre los casos a los que asigna aproximadamente 0,20, cerca del 20 % resulta positivo. Buena discriminación y buena calibración son propiedades distintas. En producción, el umbral puede elegirse minimizando un costo esperado, por ejemplo `costo_FP·FP + costo_FN·FN`, además de restricciones como la capacidad diaria del equipo que revisa alertas.

**Referencias:** [precision-recall](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html), [calibración de probabilidades](https://scikit-learn.org/stable/modules/calibration.html) y [evaluación de clasificadores](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics).

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
