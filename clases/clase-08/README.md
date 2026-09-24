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
- [Actividad registrada: dos ejercicios y entrega](ejercicios-indagacion-y-repositorios.md): una indagación sobre Big Data y Machine Learning y un experimento técnico reproducible en Google Colab.
- [Experimento reproducible sobre clases desbalanceadas](laboratorio_desbalance.py)
- [Dependencias mínimas](requirements.txt)
- [Plantilla de entrega](plantilla-entrega.md): estructura sugerida para el único PDF que integra ambos ejercicios.

## Ejecución rápida

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python laboratorio_desbalance.py
```

El laboratorio usa datos sintéticos y no descarga información privada ni financiera.

## Recorrido sugerido

- Antes de clase: lectura del enunciado y elección de un caso real para investigar.
- Durante la clase: desarrollo del experimento de clasificación en Google Colab.
- Después de clase: integración de la indagación y los resultados técnicos en un único PDF.

Toda entrega debe citar fuentes, registrar versiones y distinguir resultados observados de conclusiones generales. La actividad se entrega en Ultra como archivo PDF o enlace público a un PDF e incluye un enlace de lectura al notebook de Google Colab.
