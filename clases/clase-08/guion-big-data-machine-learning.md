# Guía para estudiantes: Big Data, Machine Learning y detección de fraude

## Propósito de la clase

Esta clase conecta tres preguntas:

1. ¿Cuándo un problema de datos requiere tecnologías de Big Data?
2. ¿Cómo aprende un modelo de Machine Learning a partir de ejemplos?
3. ¿Cómo se aplica ese aprendizaje a un caso de detección de fraude?

La presentación original contiene 36 diapositivas. Esta guía explica cada una en lenguaje accesible y corrige algunos conceptos y fragmentos de código que quedaron desactualizados.

---

# Diccionario de la clase

## A

**Accuracy o exactitud:** proporción total de predicciones correctas. Puede ser engañosa cuando una clase es muy poco frecuente. Si solo 1 de cada 1.000 operaciones es fraudulenta, un modelo que diga siempre “no fraude” tendrá 99,9 % de accuracy y no detectará ningún fraude.

**Algoritmo:** procedimiento que indica cómo procesar los datos. En Machine Learning, el algoritmo de entrenamiento ajusta un modelo usando ejemplos.

**Algoritmo no supervisado:** método que busca estructuras sin disponer de una etiqueta conocida para cada caso. El clustering y algunos métodos de detección de anomalías pertenecen a este grupo.

**Algoritmo supervisado:** método que aprende a relacionar variables de entrada con una salida conocida. Para detectar fraude, se entrena con operaciones previamente etiquetadas como legítimas o fraudulentas.

**Análisis descriptivo:** estudio de lo que ya ocurrió. Resume datos mediante tablas, gráficos e indicadores.

**Análisis predictivo:** uso de datos históricos para estimar un resultado futuro o desconocido.

**Anomalía:** caso que se aleja del comportamiento habitual. Una anomalía puede ser fraude, aunque no toda anomalía necesariamente lo sea.

## B

**Base de datos en memoria:** sistema que mantiene datos principalmente en memoria RAM para acelerar consultas y procesamiento.

**Big Data:** enfoque para almacenar y procesar datos cuya escala, velocidad o diversidad supera las capacidades prácticas de las herramientas tradicionales disponibles.

## C

**Clase:** categoría que un modelo de clasificación intenta predecir. En fraude hay, por ejemplo, dos clases: “fraude” y “no fraude”.

**Clasificación:** tarea de Machine Learning que asigna una categoría a cada caso.

**Clustering:** técnica no supervisada que agrupa casos similares sin utilizar etiquetas previas.

**Contenedor:** paquete que incluye una aplicación y sus dependencias para ejecutarla de manera consistente. Docker es una tecnología de contenedores.

**Curado de datos:** revisión, limpieza, transformación y documentación de los datos antes de analizarlos o usarlos para entrenar un modelo.

## D

**Data Lake:** repositorio que conserva grandes cantidades de datos, muchas veces en su formato original.

**Data Mining o minería de datos:** exploración de datos para descubrir patrones, relaciones o grupos útiles.

**Dataset:** conjunto de datos organizado para análisis. Las filas suelen representar casos y las columnas, variables.

**Deep Learning:** subcampo de Machine Learning basado en redes neuronales con múltiples capas.

**Desbalance de clases:** situación en la que una clase aparece mucho menos que otra. El fraude suele ser una clase minoritaria.

## E

**Entrenamiento:** etapa en la que el algoritmo ajusta los parámetros del modelo usando datos.

**Etiqueta o variable objetivo (y):** resultado que se desea predecir. En fraude indica si cada transacción fue fraudulenta o legítima.

## F

**F1:** media armónica entre precision y recall. Resulta útil cuando interesa equilibrar ambos criterios.

**Falso negativo:** fraude real que el modelo no detecta. Su costo puede ser una pérdida económica.

**Falso positivo:** operación legítima marcada como fraude. Su costo puede ser bloquear a un cliente o demorar una compra válida.

**Feature o variable de entrada (X):** dato que el modelo utiliza para generar una predicción, como monto, horario, comercio o ubicación.

## H

**Hadoop:** ecosistema para almacenar y procesar datos de forma distribuida. HDFS distribuye archivos y MapReduce procesa lotes. Otros componentes pueden cumplir funciones diferentes.

**HBase:** base de datos distribuida del ecosistema Hadoop, orientada al acceso a grandes tablas.

## I

**IA o Inteligencia Artificial:** área que desarrolla sistemas capaces de realizar tareas asociadas con percepción, razonamiento, aprendizaje o toma de decisiones.

**Ingesta:** proceso de recibir y trasladar datos desde sus fuentes hacia una plataforma de almacenamiento o procesamiento.

**Inferencia:** uso de un modelo ya entrenado para producir predicciones sobre datos nuevos.

## M

**Machine Learning:** subcampo de la IA en el que un algoritmo ajusta un modelo a partir de datos para predecir, clasificar, agrupar o detectar patrones.

**MapReduce:** modelo de procesamiento distribuido por lotes que divide una tarea, procesa sus partes y combina los resultados.

**Matriz de confusión:** tabla que compara las clases reales con las predichas y permite contar verdaderos positivos, falsos positivos, verdaderos negativos y falsos negativos.

**Modelo:** representación aprendida a partir de datos. Recibe variables de entrada y produce una salida.

## N

**NoSQL:** familia de bases de datos que no sigue exclusivamente el modelo relacional tradicional y puede priorizar escalabilidad, flexibilidad de estructura o distribución.

**Null:** ausencia de un valor. No siempre significa cero y requiere una decisión de tratamiento.

## P

**Pipeline:** secuencia organizada de pasos para transformar datos, entrenar un modelo y producir resultados.

**Precision:** entre las operaciones señaladas como fraude, proporción que realmente era fraudulenta. Una precision baja genera muchas falsas alarmas.

**PR-AUC:** resumen del equilibrio entre precision y recall para distintos umbrales. Suele ser especialmente informativo cuando la clase positiva es poco frecuente.

**Procesamiento distribuido:** ejecución de una tarea entre varias computadoras conectadas.

## R

**R²:** métrica para problemas de regresión que expresa cuánto de la variación de una variable numérica explica el modelo. No representa un porcentaje de aciertos y no corresponde como métrica principal para clasificación de fraude.

**Recall o sensibilidad:** entre todos los fraudes reales, proporción que el modelo detectó. Un recall bajo deja pasar muchos fraudes.

**Regresión:** tarea que predice un valor numérico continuo, como precio o demanda.

**Regresión logística:** modelo de clasificación que estima la probabilidad de pertenecer a una clase. Aunque su nombre contiene “regresión”, se usa habitualmente para clasificación.

**Regla de negocio:** condición definida por personas, por ejemplo: “revisar compras mayores a determinado monto realizadas fuera del país”.

## S

**Scoring:** cálculo de un puntaje o probabilidad para un caso nuevo mediante un modelo.

**SMOTE:** técnica que crea ejemplos sintéticos de la clase minoritaria para reducir el desbalance durante el entrenamiento. Debe aplicarse únicamente a los datos de entrenamiento.

**Spark:** motor de procesamiento distribuido que permite trabajar con datos por lotes y otros tipos de cargas analíticas.

**SVM:** familia de modelos que busca una frontera que separe clases con el mayor margen posible.

## T

**Test set:** parte de los datos reservada para evaluar el modelo con casos que no utilizó durante el entrenamiento.

**Training set:** parte del dataset que el algoritmo utiliza para ajustar el modelo.

## U

**Umbral:** valor a partir del cual una probabilidad se transforma en una decisión. Cambiar el umbral modifica la cantidad de falsos positivos y falsos negativos.

## V

**Las V de Big Data:** dimensiones usadas para describir desafíos de datos. Las más habituales son volumen, velocidad, variedad, veracidad y valor. Algunas clasificaciones agregan variabilidad, visualización o viabilidad.

**Valor:** utilidad que una organización obtiene de los datos al tomar mejores decisiones o mejorar procesos.

**Variedad:** diversidad de fuentes, estructuras y formatos de datos.

**Velocidad:** rapidez con la que los datos se generan, llegan y necesitan ser procesados.

**Veracidad:** grado de confiabilidad, precisión y calidad de los datos.

**Volumen:** cantidad de datos que deben almacenarse y procesarse.

---

# Guion de comprensión, diapositiva por diapositiva

## Diapositiva 1. Presentación de la unidad

La unidad introduce Big Data y Machine Learning. La idea central es comprender que no son sinónimos. Big Data se ocupa de los desafíos de almacenar y procesar datos; Machine Learning utiliza datos para ajustar modelos capaces de producir predicciones o clasificaciones.

**Para recordar:** se puede hacer Machine Learning sin Big Data y se puede usar Big Data sin entrenar modelos.

## Diapositiva 2. Temas de la clase

La clase recorre conceptos y tecnologías de Big Data, análisis predictivo, Machine Learning y el papel de la estadística. Estos temas se conectan en el caso práctico final: detectar posibles fraudes a partir de transacciones.

**Pregunta guía:** ¿cómo pasamos de una gran colección de datos a una decisión útil?

## Diapositiva 3. Las V de Big Data

Las V describen distintos desafíos. Volumen se refiere a la cantidad; velocidad, a la rapidez; variedad, a los formatos y fuentes; veracidad, a la calidad; y valor, a la utilidad obtenida. Algunas clasificaciones agregan visualización, viabilidad o variabilidad. No existe una única lista universal de siete V.

**Ejemplo:** una plataforma de pagos recibe millones de operaciones, desde distintas aplicaciones, en tiempo real y con datos que pueden contener errores.

## Diapositiva 4. Big Data en relación con Machine Learning

Un modelo necesita datos pertinentes y de calidad. Tener más datos puede ayudar, pero no garantiza un mejor resultado. Un conjunto pequeño y bien etiquetado puede ser más útil que millones de registros incompletos.

**Para recordar:** calidad, representatividad y relación con el objetivo importan tanto como cantidad.

## Diapositiva 5. Cuándo hablamos de Big Data

Big Data aparece cuando las herramientas disponibles ya no resultan suficientes para combinar fuentes, procesar el volumen requerido o responder a la velocidad necesaria. También permite buscar patrones y apoyar decisiones basadas en datos.

**Ejemplo:** integrar compras, reclamos, ubicaciones y actividad web para estimar riesgo en pocos segundos.

## Diapositiva 6. Razones del crecimiento de Big Data

El auge de Big Data se explica por el menor costo de almacenamiento, la disponibilidad de servicios en la nube, las mejoras de redes y procesamiento, y la generación continua de datos digitales.

**Idea clave:** no solo aumentaron los datos; también mejoraron las herramientas para conservarlos y analizarlos.

## Diapositiva 7. Tecnologías asociadas

La virtualización, el procesamiento paralelo, los sistemas de archivos distribuidos, las bases en memoria, los microservicios y los contenedores resuelven problemas distintos. No hace falta usar todas las tecnologías en cada proyecto.

**Pregunta de diseño:** ¿qué requisito concreto resuelve cada tecnología: escala, velocidad, aislamiento, despliegue o disponibilidad?

## Diapositiva 8. Preparación de datos para Machine Learning

Antes de entrenar hay que revisar faltantes, valores erróneos, duplicados, unidades y formatos. Los algoritmos suelen necesitar representaciones numéricas, por lo que el texto o las categorías deben codificarse de forma adecuada.

**Advertencia:** completar valores faltantes sin comprender su origen puede introducir sesgos.

## Diapositiva 9. Análisis descriptivo, predictivo y Machine Learning

El análisis descriptivo resume el pasado. El predictivo estima resultados desconocidos. Machine Learning aporta métodos que pueden utilizarse para predicción, clasificación, segmentación y otras tareas. Por eso no conviene presentarlo simplemente como el “tercer nivel” posterior al análisis predictivo.

**Ejemplo:** ventas del trimestre es descriptivo; demanda del mes próximo es predictivo; el método usado para estimarla puede ser un modelo de Machine Learning.

## Diapositiva 10. Comparación entre tipos de análisis

La lámina contrasta comprender lo ocurrido con anticipar lo que podría ocurrir. El análisis predictivo busca patrones en datos históricos y los utiliza para estimar casos nuevos.

**Límite importante:** una predicción expresa una estimación con incertidumbre, no una certeza sobre el futuro.

## Diapositiva 11. Ejemplo de predicción

La diapositiva introduce una práctica en Google Colab. Colab permite ejecutar notebooks de Python desde el navegador. En una demostración conviene identificar las variables de entrada, la salida que se quiere predecir y la métrica de evaluación antes de ejecutar el código.

**Antes de programar:** definir claramente X, y y qué significa una predicción correcta.

## Diapositiva 12. Programación tradicional y Machine Learning

En programación tradicional, una persona escribe reglas y el programa las aplica a datos. En Machine Learning, la persona elige un algoritmo, prepara ejemplos y define un objetivo; el algoritmo ajusta un modelo a partir de esos ejemplos.

**Corrección conceptual:** la máquina no “crea su propio algoritmo”; el algoritmo de entrenamiento ajusta los parámetros de un modelo.

## Diapositiva 13. Cuándo resulta útil Machine Learning

Machine Learning ayuda cuando existen patrones difíciles de expresar como reglas manuales y hay datos adecuados para aprenderlos. También puede ser útil si las reglas cambian o si la cantidad de variables vuelve inmanejable un sistema manual.

**No conviene usarlo** si una regla sencilla, estable y verificable resuelve bien el problema.

## Diapositiva 14. Aprender una función a partir de ejemplos

Cada ejemplo contiene una entrada X y, en aprendizaje supervisado, una salida conocida y. El entrenamiento busca una función aproximada que relacione ambas. Para spam, X puede representar el contenido del correo e y indicar “spam” o “no spam”.

**Objetivo:** que el modelo generalice a ejemplos nuevos, no que memorice el conjunto de entrenamiento.

## Diapositiva 15. Técnicas para construir modelos

Redes neuronales, máquinas de soporte vectorial y árboles de decisión son familias de modelos. Cada una representa la relación entre entradas y salidas de una manera diferente.

**Elección del modelo:** depende del tipo de dato, el tamaño del conjunto, la necesidad de explicar decisiones y la métrica buscada.

## Diapositiva 16. Relación entre IA, ML y Deep Learning

La relación correcta es de inclusión: Deep Learning forma parte de Machine Learning, y Machine Learning forma parte de la Inteligencia Artificial. IA también incluye enfoques que no aprenden a partir de datos, como ciertos sistemas de reglas o métodos de búsqueda.

**Esquema:** IA contiene ML; ML contiene Deep Learning.

## Diapositiva 17. Estadística, minería de datos y Machine Learning

La estadística ayuda a describir datos, estimar incertidumbre y extraer conclusiones. La minería de datos busca patrones en grandes conjuntos. Machine Learning construye modelos que generalizan a casos nuevos. Sus límites se superponen y las tres áreas comparten herramientas.

**Idea clave:** no son disciplinas rivales; se complementan.

## Diapositiva 18. Ecosistema de análisis de datos

La lámina reúne herramientas y aplicaciones vinculadas con finanzas, organizaciones, Python, Spark y minería de datos. Conviene leerla como un mapa de ecosistema, no como una arquitectura obligatoria.

**Para comprenderla:** primero se define el problema; después se eligen las herramientas.

## Diapositiva 19. Técnicas de procesamiento

La arquitectura mostrada representa componentes que reciben, almacenan y procesan datos. Su propósito es distribuir trabajo y permitir que distintos servicios cumplan funciones especializadas.

**Pregunta:** ¿qué componente recibe los datos, cuál los almacena y cuál produce un resultado analítico?

## Diapositiva 20. Procesamiento con Hadoop

Hadoop permite distribuir almacenamiento y procesamiento entre varias máquinas. HDFS se utiliza para archivos distribuidos; MapReduce procesa principalmente lotes; HBase ofrece acceso a grandes tablas. Spark puede complementar el ecosistema con otro motor de procesamiento.

**Corrección:** no todos los componentes ni todas las cargas funcionan en tiempo real.

## Diapositiva 21. Hadoop aplicado a fraude

Hadoop puede sostener el almacenamiento histórico y el análisis de grandes volúmenes de transacciones. Para responder en milisegundos suele hacer falta una capa adicional de streaming y un servicio de inferencia en línea.

**Separación útil:** entrenamiento histórico del modelo y decisión en tiempo real son procesos relacionados, pero distintos.

## Diapositiva 22. Patrón de arquitectura para detección

El diagrama muestra cómo múltiples fuentes ingresan a una plataforma, atraviesan procesos y producen salidas para usuarios o sistemas. Las flechas representan movimiento y transformación de información.

**Forma de leerlo:** de izquierda a derecha: fuentes, ingesta, procesamiento, almacenamiento, análisis y consumo.

## Diapositiva 23. Ejemplo de ingesta de datos

La ingesta reúne datos desde bases, archivos, aplicaciones o eventos. Esos datos pueden alimentar modelos de fraude, reportes o intercambios con otros sistemas.

**Control necesario:** registrar origen, momento de llegada, formato y reglas de calidad.

## Diapositiva 24. Utilidades posteriores a la ingesta

Una misma plataforma de datos puede servir a distintos consumidores. El modelo necesita variables; los reportes necesitan agregaciones; otros sistemas pueden necesitar datos procesados.

**Idea clave:** almacenar datos no genera valor por sí solo; el valor aparece cuando se conectan con decisiones y usos concretos.

## Diapositiva 25. Flujo de tratamiento

La imagen amplía el pipeline: obtención, preparación, almacenamiento y producción de resultados. En cada etapa pueden aparecer errores, demoras o pérdidas de información.

**Pregunta de control:** ¿cómo se verifica la calidad antes de que los datos lleguen al modelo?

## Diapositiva 26. Data Warehouse y Feature Store

El diagrama diferencia datos preparados para reportes de variables preparadas para modelos. Un Data Warehouse organiza información para análisis empresarial; un Feature Store administra variables reutilizables para entrenamiento e inferencia.

**Riesgo a evitar:** calcular una variable de manera diferente durante el entrenamiento y durante la operación real.

## Diapositiva 27. Caso práctico de fraude

La detección de fraude combina procesamiento rápido, segmentación y gestión de riesgo. El objetivo es asignar un puntaje a cada operación y decidir si se aprueba, se rechaza o se deriva a revisión.

**Pregunta central:** ¿qué error cuesta más en este contexto: dejar pasar un fraude o bloquear una compra legítima?

## Diapositiva 28. Métodos supervisados y no supervisados

Los métodos supervisados aprenden de operaciones etiquetadas. Los no supervisados buscan grupos o comportamientos inusuales sin requerir una etiqueta para cada caso. En la práctica pueden combinarse.

**Ejemplo:** una regresión logística predice fraude usando etiquetas; un detector de anomalías señala operaciones alejadas de lo habitual.

## Diapositiva 29. Carga inicial del dataset

El código lee un archivo CSV y muestra su forma. El resultado `(5050, 30)` significa 5.050 filas y 30 columnas. Antes de modelar hay que identificar la columna objetivo, revisar tipos de datos y medir cuántos fraudes contiene el conjunto.

**Chequeo mínimo:** distribución de clases, valores faltantes, duplicados y posible filtración de información.

## Diapositiva 30. Exploración y aplicación de Machine Learning

Los gráficos permiten comparar la distribución de datos antes de entrenar. La exploración ayuda a encontrar valores extremos, escalas diferentes y separación entre clases.

**Cuidado:** observar todo el dataset antes de separar entrenamiento y prueba puede influir indebidamente en decisiones de preparación.

## Diapositiva 31. Técnicas para clases desbalanceadas

Random Under Sampling reduce casos de la clase mayoritaria y puede perder información. Random Over Sampling duplica casos minoritarios y puede favorecer la memorización. SMOTE crea ejemplos sintéticos combinando casos cercanos de la minoría.

**Regla esencial:** cualquier remuestreo debe aplicarse solo sobre el conjunto de entrenamiento.

## Diapositiva 32. Separación y SMOTE

Se reserva una parte para entrenamiento y otra para evaluación. Conviene mantener la proporción de clases mediante `stratify=y`. Después se aplica el remuestreo únicamente a entrenamiento y se ajusta un clasificador.

**Código actualizado:** usar `BorderlineSMOTE(kind='borderline-1')` y el método `fit_resample`. La API antigua `SMOTE(kind='borderline1')` con `fit_sample` ya no corresponde.

## Diapositiva 33. Detección basada en reglas

Un sistema tradicional evalúa condiciones definidas de antemano. Las reglas son claras y fáciles de auditar, pero pueden volverse numerosas, rígidas y difíciles de mantener.

**Ejemplo:** bloquear una transacción si supera un monto y ocurre en un país nuevo para el cliente.

## Diapositiva 34. Limitaciones de las reglas

Los umbrales fijos simplifican una realidad compleja. Además, una regla suele mirar pocas variables a la vez y puede no capturar interacciones. Sin embargo, las reglas siguen siendo útiles para restricciones obligatorias o patrones conocidos.

**Conclusión:** reglas y modelos pueden complementarse.

## Diapositiva 35. Ventajas y límites de Machine Learning

Un modelo combina muchas variables y puede devolver una probabilidad, lo que permite ajustar el umbral. También puede reentrenarse cuando cambian los datos. No se adapta automáticamente: hace falta monitoreo, nuevos ejemplos, evaluación y un proceso de actualización.

**Decisión de negocio:** el umbral se elige según el costo de cada tipo de error.

## Diapositiva 36. Corrección del ejemplo final

La lámina original usa `LinearRegression` y `r2_score`. Ese enfoque corresponde a regresión numérica, no a clasificación binaria. Un R² de 0,821 no significa “82 % de acierto”. Para fraude conviene usar un clasificador como `LogisticRegression`, generar probabilidades y evaluar matriz de confusión, precision, recall, F1 y PR-AUC.

**Versión conceptual del flujo correcto:** separar datos de manera estratificada, preparar solo con entrenamiento, ajustar el clasificador, obtener probabilidades sobre test, elegir un umbral y medir los errores.

---

# Síntesis final

- Big Data resuelve desafíos de almacenamiento y procesamiento; Machine Learning aprende modelos a partir de datos.
- La preparación y la calidad de los datos condicionan el resultado.
- Fraude es un problema de clasificación con fuerte desbalance de clases.
- Accuracy por sí sola no alcanza. Precision, recall, F1, PR-AUC y la matriz de confusión muestran tipos de error diferentes.
- SMOTE se aplica únicamente al entrenamiento.
- Un modelo no reemplaza automáticamente las reglas. Ambos pueden integrarse según el riesgo y la necesidad de explicación.

# Preguntas de autoevaluación

1. ¿Cuál es la diferencia entre Big Data y Machine Learning?
2. ¿Qué representan X e y en un problema supervisado?
3. ¿Por qué una accuracy de 99 % puede ser mala en detección de fraude?
4. ¿Qué diferencia existe entre precision y recall?
5. ¿Por qué SMOTE no debe aplicarse al conjunto de test?
6. ¿Qué error representa un falso positivo en una compra?
7. ¿Qué error representa un falso negativo?
8. ¿Por qué R² no debe interpretarse como porcentaje de aciertos?
9. ¿Qué función puede cumplir Hadoop en una solución de fraude?
10. ¿Cómo elegiría el umbral de decisión de un modelo?

# Fuentes de actualización técnica

- Scikit-learn, métricas de clasificación: https://scikit-learn.org/stable/api/sklearn.metrics.html
- Scikit-learn, precision-recall en clasificación desbalanceada: https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html
- Imbalanced-learn, BorderlineSMOTE: https://imbalanced-learn.org/dev/references/generated/imblearn.over_sampling.BorderlineSMOTE.html
- Apache Hadoop: https://hadoop.apache.org/docs/current/

