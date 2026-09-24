# Ejercicios de investigación y experimentación

## Propósito

Estas actividades amplían la clase con lectura de literatura académica, inspección de repositorios y ejecución de ejemplos. Cada entrega debe diferenciar:

- lo que afirma la fuente;
- lo que el equipo observó al ejecutar o modificar el ejemplo;
- la interpretación propia y sus límites.

## Reglas de trabajo

1. Registrar título, autores, año y enlace de cada fuente.
2. Indicar versión de Python y bibliotecas utilizadas.
3. Guardar comandos, código modificado y salidas relevantes.
4. No presentar una ejecución exitosa como prueba general de que un método siempre funciona.
5. No cargar datos personales, credenciales ni información sensible en servicios públicos.

---

## Ejercicio 1. ¿Cuántas V tiene Big Data?

**Tipo:** indagación bibliográfica en parejas. 35 minutos.

### Consigna

Busquen tres fuentes de distinta procedencia que definan dimensiones de Big Data. Al menos una debe ser un artículo académico o informe técnico y otra, documentación de una organización tecnológica reconocida.

Construyan una tabla con estas columnas:

| Fuente | Año | V utilizadas | Definición de cada V | Ejemplo propio | Diferencias con la clase |
| --- | --- | --- | --- | --- | --- |

Después respondan:

1. ¿Qué dimensiones aparecen en todas las fuentes?
2. ¿Visualización, variabilidad y viabilidad describen el dato, el sistema o el uso?
3. ¿Por qué sería incorrecto presentar una lista de siete V como universal?
4. ¿Qué cuatro dimensiones usarían para analizar una plataforma de pagos y por qué?

### Evidencia a entregar

- Tabla comparativa con enlaces.
- Conclusión de 250 a 400 palabras.
- Una taxonomía propia, acompañada por su criterio de selección.

---

## Ejercicio 2. Auditoría documental de un dataset

**Tipo:** lectura académica y análisis de documentación. 60 minutos.

### Fuentes iniciales

- Gebru et al., [Datasheets for Datasets](https://arxiv.org/abs/1803.09010).
- Repositorio oficial de scikit-learn, [datasets incluidos](https://github.com/scikit-learn/scikit-learn/tree/main/sklearn/datasets).

### Consigna

1. Lean el resumen y las secciones que describen motivación, composición, recolección, usos y mantenimiento de un dataset.
2. Elijan un dataset pequeño incluido en scikit-learn.
3. Revisen su documentación y código de carga.
4. Redacten una ficha que responda:
   - ¿quién creó o mantiene el dataset?
   - ¿qué representa cada fila y cada variable?
   - ¿cómo se obtuvieron las etiquetas?
   - ¿qué usos son razonables?
   - ¿qué usos podrían causar daño o interpretaciones inválidas?
   - ¿qué información falta para reproducir su creación?

### Evidencia a entregar

- Ficha de dataset de una página.
- Tres preguntas que deberían responder sus responsables.
- Un párrafo que explique por qué la forma `(filas, columnas)` no basta para juzgar la calidad de un dataset.

---

## Ejercicio 3. Del diagrama de arquitectura a componentes verificables

**Tipo:** investigación de repositorios. 50 minutos.

### Repositorios oficiales

- [Apache Hadoop](https://github.com/apache/hadoop).
- [Apache Spark](https://github.com/apache/spark).

### Consigna

Inspeccionen el README, la documentación y la carpeta de ejemplos de ambos proyectos. No es necesario compilar los repositorios completos.

Completen una matriz:

| Necesidad | Hadoop/HDFS/MapReduce | Spark | Evidencia en el repositorio |
| --- | --- | --- | --- |
| Almacenamiento distribuido |  |  |  |
| Procesamiento por lotes |  |  |  |
| Procesamiento de flujos |  |  |  |
| SQL/DataFrames |  |  |  |
| Machine Learning |  |  |  |

Luego dibujen una arquitectura mínima para un sistema que:

- conserve transacciones históricas;
- calcule variables agregadas cada noche;
- evalúe una operación nueva antes de autorizarla;
- envíe casos dudosos a revisión humana.

### Preguntas

1. ¿Qué parte puede ejecutarse por lotes?
2. ¿Qué parte requiere baja latencia?
3. ¿Qué afirmaciones de la presentación no pueden atribuirse a “Hadoop” en general?
4. ¿Dónde ubicarían controles de calidad, seguridad y trazabilidad?

### Evidencia a entregar

- Matriz con enlaces a archivos o secciones concretas de los repositorios.
- Diagrama y explicación de hasta 500 palabras.

---

## Ejercicio 4. Accuracy engañosa y curva precision-recall

**Tipo:** reproducción y modificación de código. 60 minutos.

### Repositorio base

- Ejemplo oficial de scikit-learn: [`plot_precision_recall.py`](https://github.com/scikit-learn/scikit-learn/blob/main/examples/model_selection/plot_precision_recall.py).

### Consigna

1. Abran el ejemplo y ejecuten una versión equivalente en Colab o en un entorno local.
2. Construyan con `make_classification` tres datasets con proporciones aproximadas de clase positiva de 50 %, 10 % y 1 %.
3. Comparen dos baselines:
   - predecir siempre la clase mayoritaria;
   - una regresión logística.
4. Para cada dataset registren:
   - accuracy;
   - precision;
   - recall;
   - F1;
   - average precision;
   - matriz de confusión.
5. Dibujen la curva precision-recall del caso 1 %.

### Preguntas

1. ¿Cómo cambia la accuracy del baseline mayoritario cuando crece el desbalance?
2. ¿Por qué ese resultado no implica que el baseline sea útil?
3. ¿Qué información aporta la matriz de confusión que no aparece en una métrica única?
4. ¿Qué umbral elegirían si un falso negativo costara diez veces más que un falso positivo?

### Evidencia a entregar

- Notebook reproducible.
- Tabla de resultados.
- Interpretación de 300 a 500 palabras.

---

## Ejercicio 5. RUS, ROS y SMOTE bajo comparación controlada

**Tipo:** lectura y experimento. 90 minutos.

### Literatura y repositorio

- Chawla et al., [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/JAIR.953).
- Lemaître, Nogueira y Aridas, [Imbalanced-learn: A Python Toolbox](https://www.jmlr.org/papers/v18/16-365.html).
- Repositorio [imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn).

### Consigna

Construyan un dataset desbalanceado con `make_classification` y comparen:

1. regresión logística sin remuestreo;
2. `class_weight="balanced"`;
3. `RandomUnderSampler`;
4. `RandomOverSampler`;
5. `SMOTE`;
6. `BorderlineSMOTE`.

Usen `imblearn.pipeline.Pipeline` para que el remuestreo ocurra dentro de cada partición de entrenamiento durante la validación cruzada. Mantengan un test final intacto.

### Controles mínimos

- Misma partición y semilla para todas las variantes.
- Mismo clasificador base.
- Registro de precision, recall, F1 y average precision.
- Tiempo de ajuste de cada alternativa.

### Preguntas

1. ¿Algún método domina en todas las métricas?
2. ¿Qué información pierde RUS?
3. ¿Por qué ROS puede favorecer la memorización?
4. ¿En qué regiones crea puntos SMOTE?
5. ¿Qué riesgos tendría generar ejemplos sintéticos cuando existen variables categóricas o restricciones físicas?

### Evidencia a entregar

- Notebook o script.
- Tabla comparativa.
- Captura o gráfico de la frontera de decisión usando solo dos variables informativas.
- Recomendación argumentada, sin afirmar que existe un método universalmente mejor.

---

## Ejercicio 6. Experimento de fuga de información

**Tipo:** laboratorio de metodología. 60 minutos.

### Fuente técnica

- Ejemplos y documentación del repositorio [imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn/tree/master/examples).

### Consigna

Construyan dos experimentos sobre el mismo dataset:

**Experimento incorrecto**

1. Aplicar SMOTE a todo el dataset.
2. Separar entrenamiento y test después.
3. Entrenar y evaluar.

**Experimento correcto**

1. Separar primero el test.
2. Usar un `Pipeline` para aplicar SMOTE únicamente dentro del entrenamiento.
3. Evaluar sobre el test original.

Repitan ambos experimentos con al menos cinco semillas.

### Preguntas

1. ¿Cuál produce resultados más optimistas?
2. ¿Por qué ejemplos relacionados pueden quedar a ambos lados de la división incorrecta?
3. ¿La diferencia se mantiene con todas las semillas?
4. ¿Qué regla metodológica general se desprende del experimento?

### Evidencia a entregar

- Código completo.
- Resultados por semilla.
- Explicación causal de la fuga, no solo una comparación numérica.

---

## Ejercicio 7. Clasificación distribuida con Spark

**Tipo:** desafío técnico opcional. 90 a 120 minutos.

### Repositorio base

- [Apache Spark](https://github.com/apache/spark).
- Documentación del repositorio: [clasificación y regresión en MLlib](https://github.com/apache/spark/blob/master/docs/ml-classification-regression.md).

### Consigna

1. Ejecuten PySpark en modo local o utilicen un entorno que ya lo incluya.
2. Localicen el ejemplo oficial de regresión logística o árbol de decisión.
3. Ejecuten el ejemplo sin cambios y registren la salida.
4. Modifiquen al menos dos parámetros.
5. Expliquen qué partes del flujo son propias del algoritmo y cuáles pertenecen a la infraestructura distribuida.

### Preguntas

1. ¿Usar Spark mejora automáticamente un modelo?
2. ¿Cuándo el costo de distribuir supera el beneficio?
3. ¿Qué cambiaría al pasar de modo local a un clúster?
4. ¿Qué métrica agregarían para un caso de fraude desbalanceado?

### Evidencia a entregar

- Comando exacto de ejecución.
- Versión de Spark y Java.
- Cambios realizados.
- Comparación breve con scikit-learn.

---

## Ejercicio 8. Del notebook al sistema real

**Tipo:** lectura crítica y diseño. 60 minutos.

### Literatura

- Sculley et al., [Hidden Technical Debt in Machine Learning Systems](https://proceedings.neurips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html).

### Consigna

Lean el resumen y elijan tres riesgos descritos en el artículo. Aplíquenlos al caso de fraude de la clase.

Para cada riesgo indiquen:

- cómo podría aparecer;
- qué señal permitiría detectarlo;
- quién debería responder;
- qué control técnico u organizacional proponen.

Incluyan al menos uno de estos problemas:

- dependencia de datos;
- cambio en el comportamiento de usuarios o atacantes;
- consumidores no declarados de una variable o predicción;
- bucle de retroalimentación;
- configuración difícil de auditar.

### Evidencia a entregar

- Matriz de riesgos.
- Diagrama que ubique entrenamiento, inferencia, monitoreo y revisión humana.
- Conclusión: por qué un notebook con buenas métricas todavía no constituye un sistema confiable.

---

## Proyecto integrador opcional

En equipos de tres o cuatro, construyan una demostración reproducible que integre los ejercicios 2, 4 y 5:

1. ficha del dataset;
2. baseline mayoritario;
3. regresión logística;
4. comparación de dos estrategias de desbalance;
5. curva precision-recall;
6. elección justificada de umbral;
7. análisis de falsos positivos y falsos negativos;
8. limitaciones y riesgos de uso.

### Entrega

- Repositorio con README reproducible.
- Notebook o scripts.
- Archivo de dependencias con versiones.
- Informe de hasta cuatro páginas.
- Presentación oral de siete minutos.

### Criterios de evaluación

| Criterio | Peso |
| --- | ---: |
| Reproducibilidad y documentación | 20 % |
| Separación correcta de entrenamiento y prueba | 20 % |
| Elección e interpretación de métricas | 20 % |
| Uso crítico de literatura y repositorios | 20 % |
| Análisis de límites, riesgos y costo de errores | 20 % |

## Fuentes verificadas

- Scikit-learn, ejemplo de precision-recall: https://github.com/scikit-learn/scikit-learn/blob/main/examples/model_selection/plot_precision_recall.py
- Imbalanced-learn: https://github.com/scikit-learn-contrib/imbalanced-learn
- Apache Spark: https://github.com/apache/spark
- Apache Hadoop: https://github.com/apache/hadoop
- Gebru et al., *Datasheets for Datasets*: https://arxiv.org/abs/1803.09010
- Chawla et al., *SMOTE*: https://doi.org/10.1613/JAIR.953
- Lemaître et al., *Imbalanced-learn*: https://www.jmlr.org/papers/v18/16-365.html
- Sculley et al., *Hidden Technical Debt in Machine Learning Systems*: https://proceedings.neurips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html
