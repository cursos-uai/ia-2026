# Actividad registrada - Big Data y Machine Learning

## Resultado de aprendizaje

Evalúa los resultados de una tarea de Machine Learning para valorar la performance de un algoritmo particular, seleccionando e interpretando las métricas preestablecidas para la tarea.

## Actividad

Reflexione acerca del concepto de Big Data y su participación en Machine Learning. Para ello, resuelva los dos ejercicios que se presentan a continuación: uno de indagación conceptual y otro de experimentación técnica en Google Colab.

La entrega es única y debe presentarse en la [actividad registrada del portal Ultra](https://ultra.uaionline.edu.ar/ultra/courses/_166731_1/assessment/test/_17162900_1?gradeitemView=details) mediante una de estas opciones:

- un archivo PDF; o
- un enlace público a un PDF, con permiso de lectura habilitado.

El PDF debe integrar las respuestas de ambos ejercicios, incluir el enlace al notebook de Google Colab con permiso de lectura y consignar las fuentes utilizadas. No se aceptan el notebook solo, archivos editables ni enlaces que soliciten autorización de acceso.

---

## Ejercicio 1 - Indagación: de Big Data a Machine Learning

### Consigna

Seleccione un caso real en uno de estos ámbitos: detección de fraude, salud, educación, movilidad o comercio electrónico. A partir de al menos tres fuentes confiables, analice:

1. qué problema se intenta resolver y qué datos se utilizan;
2. qué características de Big Data aparecen en el caso —volumen, velocidad, variedad, veracidad o valor— y cuáles no resultan determinantes;
3. por qué se utiliza Machine Learning y qué resultado se espera del modelo;
4. si el problema requiere realmente tecnologías de Big Data o si podría resolverse con herramientas convencionales;
5. qué riesgos o limitaciones existen en relación con calidad de datos, privacidad, sesgo o interpretación de resultados.

Concluya con una reflexión propia de entre 250 y 400 palabras que responda: **¿qué aporta Big Data al proceso de Machine Learning en el caso elegido y qué no garantiza por sí mismo?**

### Fuentes y evidencia

- Utilice como mínimo una fuente académica y una fuente oficial o institucional.
- Registre autor u organización, título, año, URL o DOI y fecha de consulta.
- Compare las fuentes: no se limite a copiar definiciones.
- Puede comenzar con el [NIST Big Data Interoperability Framework](https://www.nist.gov/publications/nist-big-data-interoperability-framework-volume-1-big-data-definitions-version-2), pero debe sumar fuentes específicas del caso elegido.

### Evidencia que debe aparecer en el PDF

- descripción breve del caso;
- tabla que relacione características de Big Data, evidencia y efecto sobre Machine Learning;
- reflexión final;
- referencias completas.

---

## Ejercicio 2 - Google Colab: evaluación de un clasificador con datos desbalanceados

### Objetivo

Entrenar y evaluar un algoritmo de clasificación, comparar sus resultados con un baseline e interpretar métricas adecuadas para una tarea donde la clase positiva es poco frecuente.

### Preparación

1. Cree un notebook nuevo en Google Colab.
2. Use Python, `pandas`, `matplotlib` y `scikit-learn`. No necesita cargar datos externos: el conjunto se generará de forma sintética.
3. Fije `random_state=42` en la generación de datos, la partición y el modelo para que el experimento sea reproducible.

### Consigna técnica

1. Genere 10.000 observaciones con `make_classification`, usando 20 variables y aproximadamente 1 % de clase positiva.
2. Separe entrenamiento y prueba con `train_test_split`, reservando 25 % para test y utilizando `stratify=y`.
3. Entrene estos dos modelos:
   - un baseline que siempre prediga la clase mayoritaria con `DummyClassifier(strategy="most_frequent")`;
   - una regresión logística con `class_weight="balanced"` y `max_iter=2000`.
4. Evalúe ambos modelos sobre el mismo conjunto de prueba mediante:
   - accuracy;
   - precision;
   - recall;
   - F1;
   - average precision o PR-AUC;
   - matriz de confusión.
5. Para la regresión logística, obtenga `predict_proba` y compare el umbral predeterminado de 0,50 con un umbral de 0,20.
6. Presente una tabla con los resultados de los tres escenarios: baseline, regresión logística con umbral 0,50 y regresión logística con umbral 0,20.
7. Grafique la curva precision-recall de la regresión logística.

### Análisis obligatorio

Responda en el notebook y sintetice en el PDF:

1. ¿Por qué el baseline puede alcanzar una accuracy alta y, aun así, no resultar útil?
2. ¿Qué cambia en falsos positivos y falsos negativos al bajar el umbral?
3. ¿Qué métrica considera prioritaria para este problema y por qué?
4. Si un falso negativo costara diez veces más que revisar una falsa alarma, ¿qué modelo y umbral elegiría? Justifique con los resultados obtenidos.
5. ¿Qué limitaciones tiene evaluar con datos sintéticos y qué evidencia adicional necesitaría antes de usar el modelo en un caso real?

### Controles metodológicos

- El conjunto de prueba no debe intervenir en el entrenamiento ni en la selección de variables.
- Informe las versiones de Python y `scikit-learn` usadas por Colab.
- El notebook debe ejecutarse de principio a fin sin errores.
- No utilice datos personales, bancarios ni institucionales.

### Evidencia que debe aparecer en el PDF

- enlace público al notebook de Colab;
- explicación breve del procedimiento;
- tabla comparativa de métricas;
- matrices de confusión y curva precision-recall;
- interpretación de resultados y respuestas al análisis obligatorio;
- limitaciones y conclusión.

---

## Formato de la entrega

Organice el PDF con la [plantilla de entrega](plantilla-entrega.md). Extensión sugerida: entre 4 y 7 páginas, sin contar portada ni referencias.

Antes de entregar, verifique que:

- el PDF se abre correctamente;
- el enlace al PDF, si lo utiliza, no solicita acceso;
- el enlace a Colab permite leer el notebook;
- las dos actividades están completas;
- las tablas, gráficos y textos son legibles;
- todas las fuentes están citadas.

## Criterios de evaluación

| Criterio | Ponderación | Evidencia esperada |
|---|---:|---|
| Relación entre Big Data y Machine Learning | 20 % | Análisis del caso sustentado en fuentes y reflexión propia |
| Calidad y trazabilidad de las fuentes | 15 % | Referencias completas, confiables y comparadas |
| Implementación reproducible en Colab | 20 % | Notebook ejecutable, partición correcta y resultados verificables |
| Selección e interpretación de métricas | 30 % | Comparación de accuracy, precision, recall, F1, PR-AUC y matrices de confusión |
| Comunicación de resultados y limitaciones | 15 % | PDF claro, evidencia legible y conclusiones coherentes |
