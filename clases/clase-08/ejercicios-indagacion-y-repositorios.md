# Actividad registrada - Big Data y Machine Learning

## Resultado de aprendizaje

Evalúa los resultados de una tarea de Machine Learning para valorar la performance de un algoritmo particular, seleccionando e interpretando las métricas preestablecidas para la tarea.

## Actividad

Reflexione acerca del concepto de Big Data y su participación en Machine Learning. Para ello, resuelva los dos ejercicios siguientes. El primero propone una indagación fundamentada y el segundo, una experiencia técnica en Google Colab. Ambos ejercicios son obligatorios y forman una única entrega.

Trabaje con datos públicos, sintéticos o anonimizados. No incluya información personal, bancaria o institucional.

## Ejercicio 1 - Indagación: de Big Data a Machine Learning

Investigue qué relación existe entre Big Data y Machine Learning. Utilice al menos tres fuentes confiables: una publicación académica o universitaria y dos fuentes técnicas u oficiales. Puede comenzar por:

- [NIST Big Data Interoperability Framework, volumen 1](https://www.nist.gov/publications/nist-big-data-interoperability-framework-volume-1-big-data-definitions-version-2);
- [documentación oficial de Apache Hadoop](https://hadoop.apache.org/);
- [documentación oficial de Apache Spark](https://spark.apache.org/).

En el informe:

1. Explique con sus palabras qué caracteriza a Big Data y por qué no significa solamente “muchos datos”.
2. Distinga Big Data de Machine Learning: indique qué problema aborda cada concepto y cómo pueden complementarse.
3. Elija un caso real o verosímil —por ejemplo fraude, salud, educación, movilidad o redes sociales— y analice si necesita una arquitectura de Big Data para entrenar o utilizar un modelo de Machine Learning. Justifique la decisión considerando volumen, velocidad, variedad, latencia y costo.
4. Incluya una conclusión de entre 250 y 400 palabras que responda: ¿disponer de más datos garantiza un mejor modelo? Fundamente la respuesta.

La respuesta debe citar las fuentes dentro del texto y consignar autor u organización, título, enlace y fecha de consulta. No se evaluará la copia de definiciones, sino la comparación y la argumentación propia.

## Ejercicio 2 - Google Colab: evaluar un clasificador desbalanceado

Cree un notebook nuevo en Google Colab y desarrolle una tarea de clasificación binaria con datos sintéticos. El propósito es demostrar por qué una accuracy alta puede ser insuficiente y elegir métricas coherentes con el problema.

### Procedimiento mínimo

1. Genere 10.000 observaciones con `make_classification`, usando 1 % de clase positiva y `random_state=42`.
2. Separe entrenamiento y prueba con `train_test_split`, `stratify=y` y `random_state=42`. Mantenga el conjunto de prueba fuera del entrenamiento.
3. Compare estos tres modelos:
   - un clasificador constante que siempre prediga la clase mayoritaria;
   - una regresión logística sin balanceo;
   - una regresión logística con `class_weight="balanced"`.
4. Para cada modelo informe matriz de confusión, accuracy, precision, recall, F1 y average precision (PR-AUC).
5. Para el modelo balanceado compare los umbrales 0,50 y 0,20 mediante `predict_proba`. Registre cómo cambian los falsos positivos y falsos negativos.
6. Presente una tabla comparativa y al menos un gráfico propio.
7. Interprete los resultados en entre 300 y 500 palabras. Indique qué modelo y umbral elegiría si un falso negativo costara diez veces más que una revisión innecesaria. Justifique la decisión con métricas y tipos de error; no alcanza con señalar qué número es mayor.

Puede adaptar el archivo [`laboratorio_desbalance.py`](laboratorio_desbalance.py) al notebook, pero debe ejecutar todas las celdas y explicar los resultados con sus propias palabras.

## Entrega en Ultra

Entregue la actividad en el [portal Ultra](https://ultra.uaionline.edu.ar/ultra/courses/_166731_1/assessment/test/_17162900_1?gradeitemView=details) mediante una de estas dos modalidades:

- un único archivo PDF; o
- un enlace público o institucional a un único PDF con permiso de lectura.

El PDF debe reunir, en este orden:

1. carátula con nombre, materia, comisión y fecha;
2. resolución del ejercicio de indagación;
3. resolución del ejercicio técnico, con enlace de lectura al Colab;
4. tabla de métricas, gráfico e interpretación;
5. referencias bibliográficas.

Antes de enviar, compruebe que el PDF y el enlace al Colab puedan abrirse sin solicitar permisos. No se acepta el notebook como sustituto del PDF.

## Criterios de evaluación

| Criterio | Ponderación | Evidencia esperada |
|---|---:|---|
| Indagación y fuentes | 25 % | Compara fuentes confiables y argumenta la relación entre Big Data y Machine Learning. |
| Procedimiento técnico | 25 % | Colab ejecutable, separación correcta de datos y comparación de los tres modelos. |
| Selección e interpretación de métricas | 30 % | Relaciona accuracy, precision, recall, F1 y PR-AUC con errores y costos. |
| Análisis crítico | 10 % | Reconoce límites de los datos sintéticos y evita conclusiones no respaldadas. |
| Comunicación y entrega | 10 % | PDF ordenado, citas completas y enlaces accesibles. |

Una métrica alta, por sí sola, no demuestra que el modelo sea adecuado. La evaluación debe explicar qué errores comete, qué costo tendrían y qué evidencia no aporta el experimento.
