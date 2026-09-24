"""Experimento mínimo y reproducible para la clase 08.

Compara un baseline constante con regresión logística sobre un dataset
sintético desbalanceado. No descarga datos externos.
"""

from sklearn.datasets import make_classification
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    balanced_accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def evaluar(nombre, modelo, x_train, x_test, y_train, y_test):
    modelo.fit(x_train, y_train)
    prediccion = modelo.predict(x_test)
    if hasattr(modelo, "predict_proba"):
        puntaje = modelo.predict_proba(x_test)[:, 1]
    else:
        puntaje = prediccion

    print(f"\n{nombre}")
    print("Matriz de confusión:")
    print(confusion_matrix(y_test, prediccion))
    print(f"accuracy:          {accuracy_score(y_test, prediccion):.3f}")
    print(f"balanced_accuracy: {balanced_accuracy_score(y_test, prediccion):.3f}")
    print(f"precision:         {precision_score(y_test, prediccion, zero_division=0):.3f}")
    print(f"recall:            {recall_score(y_test, prediccion, zero_division=0):.3f}")
    print(f"f1:                {f1_score(y_test, prediccion, zero_division=0):.3f}")
    print(f"average_precision: {average_precision_score(y_test, puntaje):.3f}")


def main():
    x, y = make_classification(
        n_samples=10_000,
        n_features=20,
        n_informative=8,
        n_redundant=4,
        weights=[0.99, 0.01],
        class_sep=1.2,
        flip_y=0.002,
        random_state=42,
    )
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, stratify=y, random_state=42
    )

    evaluar(
        "Baseline: predecir siempre la clase mayoritaria",
        DummyClassifier(strategy="most_frequent"),
        x_train,
        x_test,
        y_train,
        y_test,
    )
    evaluar(
        "Regresión logística con pesos balanceados",
        make_pipeline(
            StandardScaler(),
            LogisticRegression(
                class_weight="balanced",
                max_iter=2_000,
                solver="liblinear",
                random_state=42,
            ),
        ),
        x_train,
        x_test,
        y_train,
        y_test,
    )


if __name__ == "__main__":
    main()
