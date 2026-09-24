# Guion para estudiantes: Big Data, Machine Learning y fraude

## Pregunta conductora

¿Cómo transformamos grandes cantidades de transacciones en decisiones útiles, medibles y responsables?

## Diccionario esencial

- **Big Data:** problemas en los que la escala, velocidad o diversidad de los datos supera la capacidad práctica de las herramientas habituales.
- **Volumen:** cantidad de datos.
- **Velocidad:** rapidez de generación, llegada y procesamiento.
- **Variedad:** diversidad de fuentes y formatos.
- **Veracidad:** calidad y confiabilidad.
- **Valor:** utilidad obtenida de los datos.
- **Dataset:** colección de observaciones; normalmente las filas son casos y las columnas son variables.
- **Ingesta:** incorporación de datos desde una fuente a una plataforma.
- **Batch:** procesamiento de datos acumulados por lotes.
- **Streaming:** procesamiento continuo o cercano a la llegada de los eventos.
- **Latencia:** demora entre un evento y la respuesta del sistema.
- **Pipeline:** secuencia reproducible de ingesta, validación, transformación, almacenamiento y consumo.
- **Data Lake:** repositorio de datos variados, frecuentemente en su formato original.
- **Data Warehouse:** repositorio organizado para consultas, indicadores y reportes.
- **Feature Store:** sistema para almacenar y reutilizar variables preparadas para modelos.
- **Machine Learning:** métodos que ajustan modelos a partir de datos.
- **Algoritmo:** procedimiento de aprendizaje elegido para ajustar un modelo.
- **Modelo:** representación aprendida que transforma entradas en predicciones.
- **Feature, X:** variable de entrada.
- **Etiqueta, y:** resultado que se desea predecir.
- **Entrenamiento:** ajuste del modelo con ejemplos conocidos.
- **Inferencia:** aplicación del modelo a casos nuevos.
- **Clasificación:** predicción de una categoría, como fraude/no fraude.
- **Regresión:** predicción de un valor numérico continuo.
- **Clustering:** agrupamiento de casos sin etiquetas conocidas.
- **Generalización:** desempeño adecuado ante datos no vistos.
- **Desbalance:** gran diferencia en la frecuencia de las clases.
- **Matriz de confusión:** tabla de aciertos y errores por clase.
- **Falso positivo:** operación legítima marcada como fraude.
- **Falso negativo:** fraude que el sistema deja pasar.
- **Precision:** fracción de alertas que realmente son fraude.
- **Recall:** fracción de fraudes reales detectados.
- **F1:** media armónica entre precision y recall.
- **Umbral:** punto que convierte una probabilidad en una decisión.
- **SMOTE:** técnica que genera ejemplos sintéticos de la clase minoritaria durante el entrenamiento.
- **Fuga de información:** uso accidental de información del test o del futuro al entrenar.
- **Hadoop:** ecosistema de almacenamiento y procesamiento distribuido.
- **HDFS:** sistema de archivos distribuido de Hadoop.
- **MapReduce:** modelo de procesamiento distribuido orientado principalmente a lotes.
- **Spark:** motor distribuido para procesamiento, SQL, streaming y ML.

## Explicación diapositiva por diapositiva

### 1. Portada

Big Data y ML están relacionados, pero no son sinónimos. Big Data aborda cómo capturar, guardar y procesar datos exigentes; ML aprende patrones. Puede existir uno sin el otro.

### 2. Temas

El recorrido va desde los datos hasta la decisión: Big Data, análisis predictivo, ML, estadística e infraestructura. El caso integrador será la detección de fraude.

### 3. Las V

Las V son preguntas de diagnóstico: ¿cuánto dato existe?, ¿con qué rapidez llega?, ¿en qué formatos?, ¿es confiable?, ¿para qué sirve? Existen distintas taxonomías; importa justificar cada dimensión.

### 4. Big Data y ML

ML necesita datos adecuados, no necesariamente masivos. Más registros pueden ayudar, pero la calidad, representatividad y pertinencia son decisivas.

### 5. Cuándo aparece Big Data

El problema aparece cuando las herramientas disponibles ya no alcanzan dentro del tiempo, costo o confiabilidad requeridos. No se define solamente por una cifra de gigabytes.

### 6. Crecimiento de Big Data

Almacenamiento más económico, nube, redes rápidas, mayor cómputo y dispositivos conectados hicieron posible conservar y procesar información antes descartada.

### 7. Tecnologías asociadas

Paralelismo, sistemas distribuidos, bases en memoria, microservicios y contenedores resuelven necesidades diferentes. Primero se define el requisito; luego se elige la herramienta.

### 8. Preparación

Hay que revisar nulos, duplicados, unidades, errores y categorías. Una transformación debe conservar el significado del dato y ajustarse sin mirar el test.

### 9. Tipos de análisis

El análisis descriptivo pregunta qué ocurrió; el predictivo estima algo desconocido. ML es un conjunto de métodos, no simplemente el escalón siguiente de una única jerarquía.

### 10. Describir y predecir

Un reporte de ventas resume el pasado; una estimación de demanda intenta anticipar. Toda predicción tiene incertidumbre y depende de que los patrones sigan siendo pertinentes.

### 11. Demostración

Antes de ejecutar un notebook hay que declarar: problema, entradas, salida y métrica. Una demostración sin esas cuatro piezas muestra código, pero no evidencia aprendizaje.

### 12. Programación y ML

En programación tradicional se escriben reglas. En ML, un algoritmo elegido por personas ajusta un modelo usando ejemplos. La máquina no inventa por sí sola su algoritmo.

### 13. Cuándo usar ML

Conviene cuando hay patrones aprendibles difíciles de traducir a reglas. Si una regla simple y verificable resuelve el problema, ML puede agregar complejidad innecesaria.

### 14. Aprender una función

Cada ejemplo supervisado tiene una entrada `X` y una respuesta `y`. El objetivo es generalizar: funcionar con ejemplos nuevos, no memorizar el entrenamiento.

### 15. Familias de modelos

Redes neuronales, SVM y árboles representan relaciones de formas distintas. Se comparan por desempeño, interpretabilidad, costo y adecuación a los datos.

### 16. IA, ML y deep learning

IA es el campo amplio; ML forma parte de IA; deep learning es una familia de ML basada en redes de múltiples capas.

### 17. Estadística y minería

La estadística describe y cuantifica incertidumbre; la minería descubre patrones; ML busca modelos que generalicen. Sus fronteras se superponen.

### 18. Herramientas

Python y R permiten programar análisis; Spark procesa datos distribuidos; Elasticsearch indexa y busca; Kibana visualiza. Una herramienta no reemplaza una metodología.

### 19. Arquitectura distribuida

Los datos recorren fuentes, ingesta, almacenamiento, procesamiento y consumo. Hay que identificar responsabilidades, no memorizar logotipos.

### 20. Hadoop

HDFS distribuye archivos y MapReduce procesa principalmente lotes. Spark y HBase cubren necesidades diferentes dentro de arquitecturas más amplias.

### 21. Hadoop y fraude

Una plataforma distribuida puede apoyar el análisis histórico, pero “Hadoop” no garantiza respuesta en milisegundos. La baja latencia depende del diseño y de componentes específicos.

### 22. Patrón de arquitectura

Leé el diagrama de izquierda a derecha: fuentes, ingesta, procesamiento, almacenamiento y consumidores. Ubicá dónde se controla calidad y dónde se ejecuta el modelo.

### 23. Ingesta

Los datos llegan desde aplicaciones, archivos, bases o eventos. La ingesta debe registrar origen, tiempo, formato y controles de calidad.

### 24. Productos de datos

Un mismo conjunto preparado puede alimentar reportes, modelos o APIs. El valor surge cuando los datos se conectan con un uso y una decisión.

### 25. Batch y streaming

Un cierre mensual admite lotes; una autorización de tarjeta necesita baja latencia. Ambos enfoques pueden convivir en una arquitectura.

### 26. Lake, Warehouse y Feature Store

El Lake conserva datos variados; el Warehouse organiza información analítica; el Feature Store asegura variables consistentes para entrenamiento e inferencia.

### 27. Fraude

El modelo estima riesgo; no demuestra culpabilidad. La salida puede combinarse con reglas y revisión humana. También importan privacidad, sesgo y explicabilidad.

### 28. Supervisado y no supervisado

Con etiquetas fraude/no fraude se puede entrenar un clasificador. Sin etiquetas, clustering o anomalías ayudan a explorar, pero una anomalía no equivale automáticamente a fraude.

### 29. Dataset

`shape = (5050, 30)` significa 5.050 casos y 30 columnas. Falta conocer fuente, significado, variable objetivo, nulos y distribución de clases.

### 30. Exploración

Los gráficos permiten observar escalas, extremos y diferencias entre clases. No reemplazan una evaluación con datos reservados.

### 31. RUS, ROS y SMOTE

RUS elimina ejemplos mayoritarios; ROS repite minoritarios; SMOTE crea casos sintéticos. Cada alternativa tiene riesgos y debe compararse con un baseline.

### 32. División y remuestreo

Primero se separa entrenamiento y test con estratificación. El remuestreo se aplica sólo al entrenamiento. La API actual usa `fit_resample`; Borderline-SMOTE tiene su propia clase.

### 33. Reglas

Las reglas son claras y auditables, pero pueden volverse rígidas. Constituyen un baseline valioso y suelen combinarse con modelos.

### 34. Límites de las reglas

Umbrales aislados no siempre capturan interacciones. Sin embargo, un modelo también utiliza umbrales y necesita monitoreo; no elimina las decisiones humanas.

### 35. Aportes y límites de ML

Un clasificador combina variables y genera una puntuación. No se adapta mágicamente: hay que reentrenar, validar y monitorear cambios.

### 36. Corrección imprescindible

Fraude/no fraude es clasificación binaria. `LinearRegression` y R² no corresponden; R² no es “porcentaje de acierto”. El baseline puede ser `LogisticRegression` y debe evaluarse con matriz de confusión, precision, recall, F1 y curva precision-recall.

## Preguntas para cerrar

1. ¿Por qué Big Data y ML no significan lo mismo?
2. ¿Qué diferencia existe entre algoritmo, modelo e inferencia?
3. ¿Por qué accuracy puede engañar en fraude?
4. ¿Qué costo tiene cada tipo de error?
5. ¿Por qué SMOTE no debe aplicarse al test?
6. ¿Qué evidencia exigirías antes de recomendar un modelo?

## Frase guía

> ¿Qué datos tenemos, qué queremos predecir, cómo evaluamos el error y qué decisión tomaremos con el resultado?
