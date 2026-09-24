# Ejercicios de indagación y experimentación

## Propósito

Estos ejercicios permiten contrastar las diapositivas con literatura técnica, inspeccionar proyectos reales y ejecutar pequeños experimentos reproducibles. El objetivo no es copiar definiciones ni obtener una métrica alta, sino producir evidencia y explicar decisiones.

## Reglas de trabajo

- Trabajen con datos públicos, sintéticos o anonimizados. No suban información personal, bancaria o institucional.
- Registren título, autor u organización, URL y fecha de consulta de cada fuente.
- Distingan una afirmación de una evidencia. Una captura sin explicación no alcanza.
- Antes de ejecutar un repositorio, lean `README`, licencia, dependencias y comandos.
- Usen un entorno aislado, como Colab, `venv` o un contenedor. No ejecuten scripts desconocidos con permisos administrativos.
- No presenten resultados del conjunto de entrenamiento como desempeño final.
- Si una instrucción ya no funciona, documenten el error, la versión y el cambio necesario. No oculten el problema.

## Roles del equipo

- **Investigador:** localiza y compara fuentes.
- **Ejecutor:** reproduce comandos y conserva evidencia.
- **Revisor:** intenta refutar las conclusiones, verifica citas y controla fugas de datos.

Los roles rotan en cada ejercicio.

---

## Ejercicio 1 - ¿Qué significa Big Data?

**Duración:** 35 minutos.  
**Modalidad:** indagación en parejas o tríos.  
**Producto:** tabla comparativa y definición propia.

### Fuentes iniciales

- [NIST Big Data Interoperability Framework, volumen 1](https://www.nist.gov/publications/nist-big-data-interoperability-framework-volume-1-big-data-definitions-version-2)
- [Repositorio oficial de Apache Hadoop](https://github.com/apache/hadoop)
- [Sitio oficial de Apache Spark](https://spark.apache.org/)

### Consigna

1. Lean la definición y las características de Big Data propuestas por NIST.
2. Revisen cómo Hadoop y Spark describen su propio propósito.
3. Construyan una tabla con estas columnas:

| Fuente | Problema que intenta resolver | Características de los datos | Tecnología mencionada | Qué no afirma |
|---|---|---|---|---|
| NIST | | | | |
| Hadoop | | | | |
| Spark | | | | |

4. Redacten una definición propia de entre 60 y 90 palabras.
5. Analicen uno de estos casos y decidan si requiere Big Data: historial académico de una comisión, telemetría de una flota o eventos de una red social.

### Preguntas de indagación

- ¿Las V forman una definición universal o una herramienta de caracterización?
- ¿Qué requisito vuelve insuficiente una solución convencional?
- ¿Qué diferencia existe entre gran volumen y procesamiento distribuido?

### Criterios de logro

- La definición propia integra al menos dos fuentes y no se limita a “muchos datos”.
- La decisión sobre el caso incluye volumen, velocidad, variedad, latencia y costo.
- El equipo identifica al menos una afirmación que la fuente no permite sostener.

---

## Ejercicio 2 - Auditoría de un repositorio técnico

**Duración:** 40 minutos.  
**Modalidad:** equipos de tres.  
**Producto:** ficha de auditoría de un repositorio.

### Repositorios para elegir

- [Apache Hadoop](https://github.com/apache/hadoop)
- [Apache Spark](https://github.com/apache/spark)
- [imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn)
- [Fraud Detection Handbook](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook)

### Consigna

Sin clonar todavía, inspeccionen el repositorio desde GitHub y respondan:

1. ¿Cuál es el propósito declarado?
2. ¿Quién mantiene el proyecto?
3. ¿Qué licencia posee?
4. ¿Qué lenguajes predominan?
5. ¿Cuándo fue la última modificación visible?
6. ¿Existen pruebas automatizadas o integración continua?
7. ¿Hay ejemplos ejecutables?
8. ¿Qué dependencias o requisitos aparecen?
9. ¿Qué issue o pull request abierto muestra una limitación actual?
10. ¿Qué parte concreta podría utilizar un estudiante sin desplegar toda la plataforma?

### Evidencia mínima

- enlaces permanentes a dos archivos del repositorio;
- enlace a un issue o pull request;
- captura o transcripción breve del comando de instalación propuesto;
- una recomendación: usar, usar con precaución o descartar para esta clase.

### Criterios de logro

- La recomendación distingue popularidad de adecuación pedagógica.
- El equipo revisa licencia, mantenimiento y reproducibilidad.
- Las conclusiones citan archivos o discusiones concretas.

---

## Ejercicio 3 - Del baseline a una evaluación honesta

**Duración:** 55 minutos.  
**Modalidad:** laboratorio en Colab o entorno virtual.  
**Producto:** notebook ejecutado y comentario de resultados.

### Lecturas y código de referencia

- [Precision-Recall en scikit-learn](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)
- [Ejemplo oficial de reporte para datos desbalanceados](https://github.com/scikit-learn-contrib/imbalanced-learn/blob/master/examples/evaluation/plot_classification_report.py)
- [Artículo de imbalanced-learn en JMLR](https://www.jmlr.org/papers/v18/16-365.html)

### Preparación

Instalen dependencias en un entorno aislado:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install scikit-learn imbalanced-learn matplotlib
```

En Colab alcanza con:

```python
%pip install -q imbalanced-learn
```

### Consigna

1. Generen un dataset sintético con 10.000 casos y 1% de clase positiva mediante `make_classification`.
2. Dividan con `train_test_split(..., stratify=y, random_state=42)`.
3. Construyan tres modelos:
   - predictor constante de la clase mayoritaria;
   - regresión logística sin balanceo;
   - regresión logística con `class_weight="balanced"`.
4. Para cada uno calculen accuracy, precision, recall, F1, average precision y matriz de confusión.
5. Expliquen por qué el modelo constante puede obtener una accuracy alta y resultar inútil.
6. Modifiquen el umbral de 0,50 a 0,20. Registren qué ocurre con falsos positivos y falsos negativos.

### Preguntas

- ¿Qué métrica cambió más entre modelos?
- ¿Qué modelo elegirían si un fraude no detectado costara diez veces más que una revisión innecesaria?
- ¿La probabilidad estimada está calibrada? ¿Qué evidencia adicional necesitarían?

### Criterios de logro

- El test no interviene en el entrenamiento.
- La comparación incluye un baseline trivial.
- La recomendación utiliza costos y tipos de error, no solo una métrica aislada.

---

## Ejercicio 4 - SMOTE sin fuga de datos

**Duración:** 50 minutos.  
**Modalidad:** laboratorio con revisión cruzada.  
**Producto:** dos pipelines comparados y explicación de la fuga.

### Recursos

- [Documentación y repositorio de imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn)
- [Ejemplo oficial con pipeline, SMOTE y regresión logística](https://github.com/scikit-learn-contrib/imbalanced-learn/blob/master/examples/evaluation/plot_classification_report.py)
- [Fraud Detection Handbook, introducción al aprendizaje desbalanceado](https://fraud-detection-handbook.github.io/fraud-detection-handbook/Chapter_6_ImbalancedLearning/Introduction.html)

### Consigna

1. Reutilicen el dataset del ejercicio anterior.
2. Construyan un `imblearn.pipeline.Pipeline` con escalado, SMOTE y regresión logística.
3. Evalúen con validación cruzada estratificada.
4. Construyan deliberadamente una variante incorrecta que aplique SMOTE antes de separar o validar.
5. Comparen ambos resultados y expliquen por qué la variante incorrecta puede parecer mejor.
6. Revisen cinco ejemplos sintéticos generados. ¿Son necesariamente casos realistas?

### Código de inicio

```python
from imblearn.pipeline import make_pipeline
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = make_pipeline(
    StandardScaler(),
    SMOTE(random_state=42),
    LogisticRegression(max_iter=2000, random_state=42),
)
```

### Revisión entre pares

Otro equipo debe localizar dónde ocurre el remuestreo y comprobar que el conjunto de prueba conserva su distribución original.

### Criterios de logro

- El flujo correcto encapsula SMOTE dentro del pipeline.
- El equipo explica la fuga con sus propias palabras.
- La conclusión reconoce que SMOTE no garantiza una mejora.

---

## Ejercicio 5 - Reproducir y cuestionar un caso de fraude

**Duración:** 90 minutos más trabajo fuera de clase.  
**Modalidad:** equipos de tres.  
**Producto:** informe reproducible de dos páginas y notebook.

### Repositorio principal

- [Reproducible Machine Learning for Credit Card Fraud Detection](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook)

El repositorio reúne capítulos y notebooks ejecutables en Jupyter, Colab o Binder. Antes de comenzar, lean su README y observen las versiones declaradas: algunas dependencias son antiguas y pueden requerir adaptación.

### Consigna

1. Clonen el repositorio o abran un notebook mediante el enlace ofrecido por el proyecto.
2. Elijan una sección de los capítulos sobre métricas, selección de modelos o aprendizaje desbalanceado.
3. Ejecuten un fragmento reproducible.
4. Registren versión de Python, dependencias, commit o fecha del material y tiempo de ejecución.
5. Cambien una sola decisión experimental: métrica, umbral, modelo o estrategia de balanceo.
6. Comparen el resultado original y el modificado.
7. Identifiquen una limitación del experimento: dataset simulado, cambio temporal, costo no modelado, calibración, explicabilidad u otra.

### Preguntas de literatura

- ¿Por qué los autores consideran insuficiente comparar trabajos sin un protocolo común?
- ¿Qué diferencia existe entre una partición aleatoria y una evaluación temporal en fraude?
- ¿Qué métricas relacionan mejor el modelo con la carga de trabajo de los investigadores humanos?

### Criterios de logro

- Otra persona puede repetir los pasos con la información entregada.
- El equipo modifica una sola variable experimental y compara evidencia.
- La conclusión distingue resultado computacional de validez externa.

---

## Ejercicio 6 - Batch, streaming y arquitectura mínima

**Duración:** 60 minutos.  
**Modalidad:** desafío opcional.  
**Producto:** mapa de arquitectura y pequeña prueba de Spark.

### Recursos

- [Quick Start oficial de Apache Spark](https://github.com/apache/spark/blob/master/docs/quick-start.md)
- [Repositorio oficial de Apache Spark](https://github.com/apache/spark)
- [Apache Hadoop](https://hadoop.apache.org/)

### Consigna

1. Lean el Quick Start y distingan transformación de acción.
2. Ejecuten Spark localmente mediante una instalación de PySpark o la imagen oficial indicada en el sitio de Spark.
3. Carguen un archivo de texto o CSV pequeño, filtren registros y calculen un conteo.
4. Expliquen por qué este experimento local no demuestra escalabilidad distribuida.
5. Diseñen dos arquitecturas para fraude:
   - entrenamiento histórico por lotes;
   - inferencia de baja latencia para una transacción nueva.
6. Marquen fuentes, ingesta, almacenamiento, transformación, modelo, salida, monitoreo y revisión humana.

### Preguntas

- ¿Qué parte puede resolverse por lotes?
- ¿Qué parte exige baja latencia?
- ¿Dónde se almacenan las variables históricas?
- ¿Cómo se registra la decisión para una auditoría posterior?

### Criterios de logro

- El equipo no confunde ejecutar Spark localmente con operar un clúster.
- La arquitectura separa entrenamiento e inferencia.
- El diagrama incluye seguridad, trazabilidad y supervisión humana.

---

## Entrega integradora

Cada equipo selecciona tres ejercicios, con al menos uno experimental, y entrega:

- la [plantilla completa](plantilla-entrega.md);
- enlaces permanentes a las fuentes y repositorios;
- notebook o comandos ejecutados;
- evidencia de resultados;
- una comparación entre expectativa y observación;
- una limitación técnica;
- un riesgo de privacidad, sesgo o uso indebido;
- una propuesta de siguiente experimento.

## Rúbrica

| Criterio | Logrado | En proceso | A revisar |
|---|---|---|---|
| Indagación | Contrasta fuentes primarias y explica diferencias | Reúne fuentes sin compararlas | Usa afirmaciones sin fuente |
| Reproducibilidad | Registra entorno, versiones, pasos y evidencia | Faltan uno o dos datos del entorno | No puede repetirse el experimento |
| Evaluación | Interpreta métricas según errores y costos | Informa métricas con explicación parcial | Confunde métricas o usa solo accuracy |
| Fuga de datos | Separa test y encapsula remuestreo correctamente | El flujo es correcto pero no lo justifica | Remuestrea antes de separar o usa test al entrenar |
| Pensamiento crítico | Identifica límites y propone una prueba siguiente | Menciona límites generales | Presenta el resultado como definitivo |
| Uso responsable | Protege datos y contempla supervisión humana | Reconoce el riesgo sin mitigarlo | Usa datos sensibles o automatiza decisiones sin control |

## Señales de aprendizaje

- El estudiante puede explicar por qué Big Data no significa solamente volumen.
- Inspecciona un repositorio antes de ejecutar código.
- Usa un baseline y reserva un test intacto.
- Relaciona precision y recall con consecuencias reales.
- Detecta una fuga de datos en un procedimiento de remuestreo.
- Distingue una demostración local de una arquitectura distribuida.
- Comunica límites, versiones y fuentes de manera trazable.
