# Actividad evaluativa - Big Data y Machine Learning

## Resultados de aprendizaje

Evalúa los resultados de una tarea de Machine Learning para valorar la performance de un algoritmo particular, seleccionando e interpretando las métricas preestablecidas para la tarea.

## Actividad

Reflexione acerca del concepto de Big Data y su participación en Machine Learning. Para ello, resuelva los dos ejercicios obligatorios que se presentan a continuación: uno de indagación y otro de aplicación técnica en Google Colab.

Trabaje con datos públicos, sintéticos o anonimizados. No incluya información personal, bancaria o institucional. Distinga las afirmaciones tomadas de fuentes de los resultados observados en su propia ejecución.

## Ejercicio 1 - Indagación: de Big Data a Machine Learning

Investigue y explique cómo las características asociadas a Big Data influyen en el desarrollo de una solución de Machine Learning.

1. Compare al menos tres fuentes confiables: una fuente académica o institucional, la documentación de una tecnología de procesamiento de datos y una fuente sobre Machine Learning.
2. Defina con sus propias palabras Big Data y Machine Learning, y explique la relación entre ambos conceptos. Aclare por qué no son sinónimos y por qué no todo problema de Machine Learning requiere Big Data.
3. Seleccione un caso real o verosímil —por ejemplo fraude, recomendación, mantenimiento predictivo o abandono de clientes— y analice:
   - qué datos utilizaría;
   - qué características de volumen, velocidad, variedad, veracidad o valor aparecen;
   - qué tarea de Machine Learning corresponde;
   - qué algoritmo podría emplearse;
   - qué métricas permitirían evaluar su desempeño;
   - qué riesgo, sesgo o limitación debería controlarse.
4. Cierre con una reflexión fundamentada de entre 200 y 300 palabras sobre el aporte concreto de Big Data al caso elegido.

### Evidencia requerida

- Tabla comparativa de las tres fuentes.
- Citas y referencias con autor u organización, título, URL y fecha de consulta.
- Justificación del algoritmo y de las métricas elegidas.
- Reflexión final propia.

## Ejercicio 2 - Aplicación técnica en Google Colab

Construya y evalúe en Google Colab un modelo de clasificación sobre un conjunto de datos desbalanceado. El objetivo es comprobar por qué una accuracy alta no siempre representa un buen modelo y cómo cambia la interpretación al considerar precision, recall, F1 y PR-AUC.

### Procedimiento mínimo

1. Cree un notebook nuevo en Google Colab.
2. Genere un conjunto sintético de 10.000 casos con aproximadamente 1 % de clase positiva mediante `sklearn.datasets.make_classification`.
3. Separe entrenamiento y prueba con `train_test_split`, usando `stratify=y` y `random_state=42`.
4. Entrene y compare:
   - un predictor constante de la clase mayoritaria;
   - una regresión logística sin balanceo;
   - una regresión logística con `class_weight="balanced"`.
5. Para cada modelo informe accuracy, precision, recall, F1, PR-AUC y matriz de confusión.
6. Para el modelo balanceado compare el umbral predeterminado de 0,50 con un umbral de 0,20. Explique qué ocurre con los falsos positivos y falsos negativos.
7. Seleccione el modelo y el umbral que usaría si un caso positivo no detectado costara diez veces más que una revisión innecesaria. Fundamente la decisión con las métricas obtenidas.
8. Incluya una conclusión que diferencie el resultado del experimento de lo que podría esperarse en un sistema real.

### Condiciones técnicas

- El conjunto de prueba debe permanecer separado del entrenamiento y de cualquier ajuste de preprocesamiento.
- Deben fijarse las semillas aleatorias para facilitar la reproducción.
- El notebook debe ejecutar de principio a fin sin errores.
- Cada bloque de código debe incluir una breve explicación de su propósito y cada resultado debe ser interpretado.

### Evidencia requerida

- Enlace al Google Colab con permiso de lectura.
- Fragmentos de código relevantes, tablas o gráficos y matrices de confusión.
- Tabla comparativa de métricas.
- Interpretación de los errores y justificación de la decisión final.

## Entrega en Ultra

Entregue **un único archivo PDF o un enlace directo y accesible a un PDF** en la [actividad registrada en Ultra](https://ultra.uaionline.edu.ar/ultra/courses/_166731_1/assessment/test/_17162900_1?gradeitemView=details). El PDF debe integrar los dos ejercicios y contener:

1. Carátula con materia, actividad, integrantes y fecha.
2. Desarrollo completo del ejercicio de indagación.
3. Desarrollo y resultados del ejercicio técnico.
4. Enlace de solo lectura al notebook de Google Colab.
5. Conclusiones integradoras.
6. Referencias bibliográficas y técnicas.

Si entrega un enlace, verifique en una ventana privada que el PDF pueda abrirse sin solicitar permisos. El notebook de Colab acompaña la evidencia, pero no reemplaza el PDF.

## Criterios de evaluación

| Criterio | Evidencia esperada |
|---|---|
| Comprensión conceptual | Relaciona Big Data y Machine Learning sin confundirlos. |
| Calidad de indagación | Contrasta fuentes confiables y formula una reflexión propia. |
| Corrección técnica | El notebook es reproducible y conserva el conjunto de prueba. |
| Selección de métricas | Elige e interpreta métricas adecuadas para datos desbalanceados. |
| Análisis de resultados | Vincula las métricas y los tipos de error con el costo del caso. |
| Comunicación y trazabilidad | Presenta evidencia clara, referencias completas y enlaces accesibles. |

No se evaluará únicamente la obtención de una métrica alta. Se evaluará especialmente la capacidad de interpretar los resultados, justificar decisiones y reconocer limitaciones.
