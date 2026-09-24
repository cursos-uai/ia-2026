# Ejercicios de indagación y laboratorio

Las actividades priorizan lectura crítica, código reproducible y contraste entre afirmaciones y evidencia. Cada equipo debe registrar fuentes, versión del software, comandos utilizados, resultados y limitaciones.

## Entrega mínima común

Para cada ejercicio entregar:

1. pregunta investigada;
2. fuentes consultadas y criterio de selección;
3. procedimiento reproducible;
4. evidencia obtenida;
5. conclusión y una limitación.

## 1. Las V de Big Data: taxonomías en conflicto

**Objetivo:** comprender que no existe una única lista universal.

1. Buscar tres fuentes académicas o institucionales que definan las V.
2. Registrar año, autor, propósito y lista propuesta.
3. Comparar coincidencias y diferencias.
4. Elegir un sistema real y justificar qué cinco dimensiones son más relevantes.

**Producto:** tabla comparativa de una página y una conclusión de hasta 200 palabras.

**Criterio:** no aceptar blogs sin autor o textos que no indiquen su fuente original.

## 2. Reproducir el error de accuracy

**Objetivo:** demostrar por qué una métrica alta puede ocultar un clasificador inútil.

Usar `sklearn.datasets.make_classification` para crear 10.000 casos con 1 % de positivos. Comparar:

- clasificador que siempre predice la clase mayoritaria;
- regresión logística con `class_weight="balanced"`;
- árbol de decisión.

Calcular accuracy, precision, recall, F1, matriz de confusión y average precision.

**Preguntas:**

1. ¿Cuál modelo obtiene mayor accuracy?
2. ¿Cuál detecta más positivos?
3. ¿Qué métrica usarían si el falso negativo cuesta diez veces más?

**Referencias:** [ejemplo precision-recall de scikit-learn](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html) y [repositorio oficial de scikit-learn](https://github.com/scikit-learn/scikit-learn).

## 3. SMOTE bajo auditoría

**Objetivo:** comparar estrategias de desbalance sin contaminar el test.

Clonar o explorar [imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn) y localizar sus ejemplos. Construir pipelines para comparar:

- sin remuestreo;
- `class_weight="balanced"`;
- `RandomUnderSampler`;
- `RandomOverSampler`;
- `SMOTE`;
- `BorderlineSMOTE`.

Repetir la evaluación con cinco particiones estratificadas y reportar promedio y dispersión de F1 y average precision.

**Indagación literaria:** leer el artículo original [SMOTE: Synthetic Minority Over-sampling Technique](https://arxiv.org/abs/1106.1813) y contrastar su evaluación con las métricas utilizadas actualmente.

**Pregunta crítica:** ¿en qué condiciones los ejemplos sintéticos podrían ser poco realistas?

## 4. Fuga de información deliberada

**Objetivo:** observar cómo una práctica incorrecta infla resultados.

Implementar dos experimentos:

- A: aplicar SMOTE antes de dividir train/test;
- B: dividir primero y aplicar SMOTE sólo dentro del entrenamiento mediante un pipeline.

Comparar resultados y explicar por qué A produce evidencia inválida. Dibujar el flujo de información de ambos experimentos.

**Producto:** notebook más un párrafo titulado “Qué información vio el modelo”.

## 5. Explorar un repositorio científico

**Objetivo:** aprender a evaluar software más allá de sus estrellas.

Auditar [imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn):

1. identificar licencia, versiones de Python y dependencias;
2. encontrar documentación, ejemplos y tests;
3. elegir un ejemplo ejecutable y reproducirlo;
4. registrar versión o commit utilizado;
5. revisar dos issues abiertos y decidir si afectan el ejercicio.

**Producto:** ficha de auditoría de repositorio con enlaces permanentes al commit o archivo usado.

## 6. Spark local: de una colección a un cálculo distribuido

**Objetivo:** observar particiones y ejecución local sin requerir un clúster.

Explorar el [repositorio oficial de Apache Spark](https://github.com/apache/spark), especialmente `examples`. Ejecutar Spark en modo local y:

1. crear un DataFrame de transacciones sintéticas;
2. agrupar por comercio y calcular cantidad y monto total;
3. inspeccionar el plan con `explain()`;
4. cambiar el número de particiones;
5. explicar qué parte del ejercicio simula distribución y qué parte sigue ocurriendo en una sola máquina.

**Extensión:** ejecutar uno de los ejemplos oficiales con `spark-submit` y documentar las diferencias entre el código del repositorio y el entorno usado.

## 7. Clasificación con Spark MLlib

**Objetivo:** conectar el concepto de pipeline con una implementación distribuida.

Partir de los ejemplos oficiales de clasificación en `apache/spark`. Construir un pipeline con ensamblado de variables, clasificador y evaluación. Comparar su interfaz conceptual con un pipeline de scikit-learn.

**Preguntas:**

1. ¿Qué transformaciones se ajustan con `fit`?
2. ¿Qué objeto conserva el modelo entrenado?
3. ¿Qué métrica disponible elegirían para datos desbalanceados y cuál falta?

## 8. MapReduce en la literatura y en el código

**Objetivo:** relacionar la arquitectura con su fuente académica.

Leer [“MapReduce: Simplified Data Processing on Large Clusters”](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/) de Dean y Ghemawat. Localizar el repositorio oficial [Apache Hadoop](https://github.com/apache/hadoop) y el módulo de ejemplos MapReduce.

Entregar:

- definición de `map`, `shuffle` y `reduce` con un ejemplo propio;
- diagrama del flujo de `wordcount`;
- comparación entre la promesa del artículo y una ejecución actual;
- explicación de por qué este patrón no equivale a inferencia antifraude en milisegundos.

## 9. Reglas contra modelos

**Objetivo:** comparar desempeño y explicabilidad.

Diseñar tres reglas de fraude sobre un dataset sintético. Compararlas con regresión logística y árbol de decisión usando el mismo test.

Medir métricas, tiempo de inferencia y cantidad de decisiones que el equipo puede explicar correctamente. Proponer un sistema híbrido con tres bandas: aprobar, revisar y bloquear.

**Pregunta ética:** ¿qué explicación recibiría una persona cuya compra fue bloqueada?

## 10. Revisión de literatura sobre fraude desbalanceado

**Objetivo:** desarrollar lectura comparativa.

Seleccionar un survey y dos trabajos empíricos. Para cada uno registrar:

- dataset y prevalencia de fraude;
- partición temporal o aleatoria;
- técnica de balanceo;
- baseline;
- métricas;
- disponibilidad de código y datos;
- amenazas a la validez.

Como punto de partida puede utilizarse [A Survey of Predictive Modelling under Imbalanced Distributions](https://arxiv.org/abs/1505.01658).

**Producto:** matriz de evidencia. La conclusión debe separar “lo que afirma el artículo” de “lo que el equipo pudo reproducir”.

## 11. Desafío integrador reproducible

**Objetivo:** unir datos, modelo, métricas y decisión.

Construir un repositorio pequeño que incluya:

- `README.md` con la pregunta y decisiones de diseño;
- archivo de dependencias con versiones;
- notebook o script ejecutable;
- partición estratificada;
- baseline mayoritario y regresión logística;
- una estrategia de desbalance;
- matriz de confusión y curva precision-recall;
- elección justificada del umbral;
- sección de limitaciones, privacidad y sesgo.

No subir datos sensibles ni archivos cuya licencia no permita redistribución.

## Rúbrica breve

| Dimensión | 0 | 1 | 2 |
|---|---|---|---|
| Fuentes | Sin fuentes | Fuentes débiles o incompletas | Fuentes académicas/oficiales bien citadas |
| Reproducibilidad | No ejecuta | Ejecuta con pasos faltantes | Versiones, comandos y semilla documentados |
| Evaluación | Sólo accuracy | Varias métricas sin interpretación | Métricas conectadas con costos de error |
| Pensamiento crítico | Repite afirmaciones | Señala alguna limitación | Contrasta evidencia, código y límites |
| Comunicación | Resultado confuso | Comprensible | Claro, conciso y verificable |

## Recursos de referencia

- [Scikit-learn: precision-recall](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)
- [Scikit-learn en GitHub](https://github.com/scikit-learn/scikit-learn)
- [Imbalanced-learn en GitHub](https://github.com/scikit-learn-contrib/imbalanced-learn)
- [Artículo original de SMOTE](https://arxiv.org/abs/1106.1813)
- [Apache Spark en GitHub](https://github.com/apache/spark)
- [Apache Hadoop en GitHub](https://github.com/apache/hadoop)
- [Artículo original de MapReduce](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/)
- [Survey sobre distribuciones desbalanceadas](https://arxiv.org/abs/1505.01658)
