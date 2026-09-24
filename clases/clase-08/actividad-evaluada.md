# Actividad evaluada - Big Data y Machine Learning

## Resultado de aprendizaje

**Evalúa los resultados de una tarea de Machine Learning para valorar la performance de un algoritmo particular, seleccionando e interpretando las métricas preestablecidas para la tarea.**

## Actividad

Reflexione acerca del concepto de Big Data y su participación en Machine Learning a partir de una indagación con fuentes confiables y de un experimento técnico reproducible en Google Colab. Integre ambos ejercicios en una conclusión que relacione las características de los datos, la elección del algoritmo y la interpretación de las métricas.

La actividad consta solamente de los dos ejercicios siguientes. Ambos son obligatorios.

## Ejercicio 1 - Indagación: Big Data y Machine Learning

Investigue cómo las características de Big Data influyen en el desarrollo y la evaluación de una solución de Machine Learning.

1. Consulte al menos tres fuentes confiables: una fuente académica y dos fuentes institucionales, documentación oficial o publicaciones científicas.
2. Compare las definiciones de Big Data y determine qué características resultan relevantes para Machine Learning. Considere, como mínimo, volumen, velocidad, variedad y veracidad.
3. Seleccione un caso real o plausible, por ejemplo detección de fraude, salud, movilidad o redes sociales.
4. Explique qué problema se intenta resolver, qué datos se necesitarían y por qué su escala o complejidad podría requerir tecnologías de Big Data.
5. Identifique un algoritmo de Machine Learning adecuado para el caso y justifique la elección.
6. Proponga al menos tres métricas para evaluarlo y explique qué información aporta cada una. No se limite a enumerarlas.
7. Cierre con una reflexión de entre 300 y 500 palabras sobre esta pregunta: **¿tener más datos garantiza un mejor modelo?**

### Evidencia esperada

- tabla comparativa de las fuentes;
- descripción y justificación del caso seleccionado;
- relación razonada entre datos, algoritmo y métricas;
- citas y referencias completas con enlaces verificables.

## Ejercicio 2 - Laboratorio técnico en Google Colab

Construya y evalúe en Google Colab un clasificador para un conjunto de datos desbalanceado. El objetivo no es alcanzar la métrica más alta, sino demostrar que puede seleccionar e interpretar medidas adecuadas para comparar algoritmos.

### Procedimiento obligatorio

1. Cree un notebook en Google Colab.
2. Genere un conjunto sintético de 10.000 observaciones con aproximadamente 1 % de casos positivos mediante `sklearn.datasets.make_classification`.
3. Separe entrenamiento y prueba con `train_test_split`, utilizando `stratify=y` y `random_state=42`.
4. Entrene y compare estos tres modelos:
   - un clasificador que siempre prediga la clase mayoritaria;
   - regresión logística sin balanceo;
   - regresión logística con `class_weight="balanced"`.
5. Para cada modelo calcule y presente:
   - matriz de confusión;
   - accuracy;
   - precision;
   - recall;
   - F1;
   - average precision o PR-AUC.
6. Para la regresión logística balanceada compare los umbrales `0.50` y `0.20`. Explique cómo cambian los falsos positivos, los falsos negativos, precision y recall.
7. Interprete los resultados y responda:
   - ¿por qué el clasificador mayoritario puede tener accuracy alta y ser inútil?;
   - ¿qué modelo elegiría si un falso negativo costara diez veces más que una revisión innecesaria?;
   - ¿qué métrica priorizaría y por qué?;
   - ¿qué limitaciones tiene experimentar con datos sintéticos?

### Requisitos de reproducibilidad

- todo el código debe ejecutarse desde el inicio en Colab sin pasos ocultos;
- el conjunto de prueba no puede intervenir en el entrenamiento;
- el notebook debe indicar versiones de Python y bibliotecas, semilla y fecha de ejecución;
- los gráficos y tablas deben incluir título, rótulos y una interpretación propia;
- no se deben incluir datos personales, credenciales ni información sensible.

## Entrega

Entregue **un único PDF o un enlace directo y accesible a ese PDF** en la actividad registrada del portal UAI Ultra:

<https://ultra.uaionline.edu.ar/ultra/courses/_166731_1/assessment/test/_17162900_1?gradeitemView=details>

El PDF debe integrar los dos ejercicios y contener:

1. carátula con integrantes, comisión y fecha;
2. desarrollo del ejercicio de indagación;
3. enlace al notebook de Google Colab con permiso de lectura;
4. fragmentos relevantes del código, tablas, matrices de confusión y resultados;
5. interpretación y conclusión integradora;
6. bibliografía y enlaces consultados.

Antes de entregar, verifique que el enlace al PDF y el enlace a Colab puedan abrirse sin solicitar permisos. **No se aceptará el notebook de Colab como única entrega:** la entrega formal es el PDF o el enlace al PDF.

## Criterios de evaluación

| Criterio | Ponderación | Evidencia esperada |
|---|---:|---|
| Indagación y calidad de fuentes | 20 % | Fuentes académicas u oficiales comparadas y correctamente citadas |
| Implementación y reproducibilidad | 25 % | Notebook completo, ejecutable y sin fuga entre entrenamiento y prueba |
| Selección e interpretación de métricas | 30 % | Comparación razonada de accuracy, precision, recall, F1 y PR-AUC |
| Análisis crítico | 15 % | Decisión vinculada con costos de error y limitaciones de la evidencia |
| Comunicación y entrega | 10 % | PDF claro, ordenado, con enlaces accesibles y referencias completas |

No alcanza con presentar código ni con informar una métrica alta: deben explicar qué significan los resultados para el problema elegido.

## Recursos de inicio

- [NIST Big Data Interoperability Framework, volumen 1](https://www.nist.gov/publications/nist-big-data-interoperability-framework-volume-1-big-data-definitions-version-2)
- [Scikit-learn: `make_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html)
- [Scikit-learn: Precision-Recall](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)
- [Scikit-learn: métricas de clasificación](https://scikit-learn.org/stable/api/sklearn.metrics.html)
