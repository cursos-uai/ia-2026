# Guion y diccionario para estudiantes

## Pregunta conductora

¿Cómo convertimos un flujo grande de transacciones en alertas de fraude que podamos explicar y evaluar?

## Diccionario mínimo

- **Big Data:** problemas y tecnologías para datos cuya escala, velocidad o diversidad supera las herramientas convencionales disponibles.
- **Volumen, velocidad y variedad:** cantidad, rapidez y diversidad de los datos.
- **Veracidad:** confiabilidad y calidad de los datos.
- **Valor:** utilidad obtenida al convertir datos en decisiones.
- **Dataset:** conjunto de observaciones y variables.
- **Ingesta:** incorporación de datos desde sus fuentes.
- **Batch:** procesamiento de datos acumulados por lotes.
- **Streaming:** procesamiento continuo de eventos a medida que llegan.
- **Machine Learning:** métodos que ajustan modelos a partir de datos.
- **Algoritmo:** procedimiento de entrenamiento elegido por las personas.
- **Modelo:** representación ajustada por el algoritmo.
- **Feature, X:** variable de entrada.
- **Etiqueta, y:** resultado que se quiere predecir.
- **Clasificación:** predicción de una categoría, como fraude/no fraude.
- **Regresión:** predicción de un valor numérico continuo.
- **Generalización:** capacidad de funcionar con datos nuevos.
- **Desbalance:** diferencia grande entre la cantidad de ejemplos de cada clase.
- **Precision:** proporción de alertas positivas que eran realmente positivas.
- **Recall:** proporción de positivos reales que fueron detectados.
- **F1:** media armónica de precision y recall.
- **PR-AUC:** resumen de la curva precision-recall para distintos umbrales.
- **SMOTE:** técnica que crea ejemplos sintéticos de la clase minoritaria únicamente dentro del entrenamiento.
- **Fuga de información:** uso de información de validación o test durante el entrenamiento.
- **HDFS:** sistema distribuido de archivos de Hadoop.
- **MapReduce:** modelo de procesamiento distribuido orientado principalmente a lotes.
- **YARN:** administrador de recursos y ejecución del ecosistema Hadoop.
- **Spark:** motor distribuido para procesamiento, SQL, streaming y ML.

## Guion diapositiva por diapositiva

### 1. Portada

Big Data gestiona problemas de escala y complejidad de datos. Machine Learning aprende patrones. Pueden trabajar juntos, pero no son sinónimos.

### 2. Temas

El recorrido va desde los datos hasta la decisión: Big Data, analítica, aprendizaje automático, infraestructura y fraude.

### 3. Las V

Las V funcionan como preguntas de diagnóstico. No existe una única lista universal. Lo importante es explicar qué dificultad representa cada dimensión.

### 4. Big Data y ML

ML necesita datos adecuados, no necesariamente masivos. Más datos no compensan errores, sesgos o etiquetas poco confiables.

### 5. Cuándo hablamos de Big Data

El problema aparece cuando las herramientas disponibles no alcanzan en tiempo, costo o capacidad para integrar, procesar y consultar los datos.

### 6. Crecimiento de Big Data

Influyeron la reducción del costo de almacenamiento, la nube, las redes y la generación continua de eventos digitales.

### 7. Tecnologías asociadas

Virtualización, paralelismo, almacenamiento distribuido, contenedores y microservicios resuelven necesidades distintas. No son una lista obligatoria.

### 8. Preparación

Limpiar significa revisar faltantes, duplicados, errores, unidades y representaciones. Toda transformación aprendida debe ajustarse sólo con entrenamiento.

### 9. Tipos de análisis

El análisis descriptivo resume qué ocurrió. El predictivo estima algo desconocido. ML aporta métodos y no constituye simplemente un tercer escalón.

### 10. Predicción

Una predicción es una estimación con incertidumbre. Necesita una variable objetivo y una métrica que represente el uso real.

### 11. Demostración

Antes de ejecutar un notebook, definir X, y, el criterio de evaluación y qué decisión se tomará con la salida.

### 12. Programación y ML

En ML, el algoritmo de entrenamiento ajusta un modelo. La persona todavía define datos, objetivo, algoritmo, métrica y condiciones de uso.

### 13. Cuándo usar ML

Resulta útil cuando hay patrones aprendibles difíciles de expresar con reglas. Si una regla simple resuelve el problema, puede ser preferible.

### 14. Aprendizaje supervisado

Cada ejemplo contiene una entrada X y una respuesta y. Generalizar significa funcionar con ejemplos nuevos, no memorizar el entrenamiento.

### 15. Familias de modelos

Redes neuronales, SVM y árboles de decisión representan relaciones de formas diferentes. Ninguna familia gana en todos los problemas.

### 16. IA, ML y aprendizaje profundo

Machine Learning forma parte de IA y Deep Learning forma parte de ML. La inclusión no implica que toda IA aprenda con datos.

### 17. Estadística y minería

La estadística cuantifica patrones e incertidumbre. La minería explora grandes conjuntos. ML construye modelos que intentan generalizar.

### 18. Herramientas

Python, Spark y herramientas de visualización cumplen funciones distintas. Primero se define el problema; después se elige la herramienta.

### 19. Procesamiento distribuido

Una arquitectura distribuida reparte almacenamiento y cálculo. Conviene separar fuentes, ingesta, almacenamiento, procesamiento y consumo.

### 20. Hadoop

HDFS distribuye archivos, YARN administra recursos y MapReduce procesa lotes. Spark puede integrarse, pero es un proyecto diferente.

### 21. Hadoop y fraude

Hadoop puede sostener análisis histórico. Una decisión en milisegundos requiere componentes específicos de streaming y servicio de inferencia.

### 22. Patrón de arquitectura

Seguir una transacción desde su origen hasta la alerta. Identificar dónde se valida calidad, dónde se almacena y dónde se ejecuta el modelo.

### 23. Ingesta

La ingesta puede ser periódica o por eventos. Debe registrar origen, momento, formato y controles de calidad.

### 24. Productos de datos

Los datos preparados pueden alimentar modelos, reportes, APIs u otros equipos. Almacenar no genera valor por sí solo.

### 25. Tratamiento

Las transformaciones deben ser reproducibles y auditables. Un error temprano puede propagarse hasta la decisión final.

### 26. Warehouse y feature store

El warehouse organiza información para análisis. El feature store administra variables reutilizables y consistentes entre entrenamiento e inferencia.

### 27. Caso de fraude

El modelo estima riesgo. El negocio define el umbral y decide si aprueba, revisa o rechaza. Una anomalía no prueba por sí sola un fraude.

### 28. Supervisado y no supervisado

Con etiquetas usamos clasificación supervisada. Sin ellas podemos explorar grupos o anomalías. PCA reduce dimensiones y K-Means agrupa.

### 29. Carga del dataset

`shape` sólo informa filas y columnas. También necesitamos fuente, significado, variable objetivo, faltantes y proporción de clases.

### 30. Exploración

Los gráficos ayudan a formular hipótesis, pero no prueban generalización. El test debe permanecer fuera del desarrollo del modelo.

### 31. Desbalance

Undersampling elimina ejemplos, oversampling repite y SMOTE sintetiza. Cada técnica tiene riesgos y debe compararse contra un baseline.

### 32. División y SMOTE

Primero se separa test. Después se remuestrea únicamente entrenamiento. La API actual usa `fit_resample`; Borderline-SMOTE tiene su propia clase.

### 33. Reglas

Las reglas son claras y auditables. Resultan útiles para restricciones obligatorias y como baseline.

### 34. Límites de reglas

Los umbrales fijos pueden quedar obsoletos y capturar pocas interacciones. Reglas y modelos pueden complementarse.

### 35. Ventajas y límites de ML

Un modelo combina variables y genera un puntaje, pero no se adapta solo. Necesita monitoreo, validación y reentrenamiento controlado.

### 36. Corrección del ejemplo final

Fraude/no fraude es clasificación. `LinearRegression` y R² no corresponden y 0,82 de R² no significa 82 % de acierto. Usar un clasificador y evaluar matriz de confusión, precision, recall, F1 y PR-AUC.

## Frase de cierre

¿Qué datos tenemos, qué queremos predecir, cómo medimos los errores y qué decisión tomaremos con el resultado?

