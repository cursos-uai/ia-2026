# Clase 08 - Big Data, Machine Learning y detección de fraude

Material complementario para acompañar la presentación de la Unidad 4.

## Objetivos

Al finalizar la clase, los estudiantes deberían poder:

- distinguir Big Data, análisis predictivo y Machine Learning;
- explicar el recorrido de los datos desde la ingesta hasta una decisión;
- reconocer clasificación, regresión y aprendizaje no supervisado;
- analizar el desbalance de clases en detección de fraude;
- interpretar matriz de confusión, precision, recall, F1 y PR-AUC;
- detectar por qué regresión lineal y R² no validan un clasificador binario.

## Materiales

- [Guion completo para alumnos](guion-alumnos-big-data-ml.md): diccionario ampliado, explicación de las 36 diapositivas y autoevaluación.
- [Guion y diccionario resumidos](guion-y-diccionario.md): versión breve para consulta durante la clase.
- [Ejercicios ampliados de indagación y repositorios](ejercicios-indagacion-y-repositorios.md): seis recorridos con literatura, auditoría de GitHub, métricas, SMOTE, fraude reproducible y Spark.
- [Ejercicios de investigación y laboratorio](ejercicios-investigacion-y-laboratorio.md): actividades adicionales y consignas de profundización.
- [Experimento reproducible sobre clases desbalanceadas](laboratorio_desbalance.py)
- [Dependencias mínimas](requirements.txt)
- [Plantilla de entrega](plantilla-entrega.md): registro de fuentes, entorno, evidencia, límites y riesgos.

## Ejecución rápida

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python laboratorio_desbalance.py
```

El laboratorio usa datos sintéticos y no descarga información privada ni financiera.

## Recorrido sugerido

- Antes de clase: investigación sobre Big Data y auditoría de un repositorio.
- Durante la clase: laboratorio de métricas y ejercicio de SMOTE sin fuga de datos.
- Después de clase: reproducción de una sección del Fraud Detection Handbook.
- Profundización opcional: arquitectura batch/streaming y prueba local con Spark.

Los equipos pueden trabajar en roles rotativos de investigador, ejecutor y revisor. Toda entrega debe citar fuentes, registrar versiones y distinguir resultados observados de conclusiones generales.
