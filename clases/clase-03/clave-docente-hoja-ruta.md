# Clave docente - Hoja de ruta de lectura de IA simbólica

Este documento acompaña la [hoja de ruta de lectura](hoja-ruta-lectura-russell-norvig.md).

## Respuestas del cuestionario

| Pregunta | Respuesta | Justificación breve | Tramo a revisar |
|---:|:---:|---|---|
| 1 | B | El enfoque representa conocimiento explícito y realiza inferencias sobre símbolos. | Tramo 1 y apunte de clase |
| 2 | A | El *Advice Taker* ejemplifica la incorporación declarativa de conocimiento para razonar. | Tramo 1 |
| 3 | B | El avance de sistemas expertos mostró el valor del conocimiento específico del dominio. | Tramo 2 |
| 4 | B | DENDRAL y MYCIN fueron diseñados alrededor de conocimiento especializado, no de inteligencia general. | Tramo 2 |
| 5 | A | Extraer, formalizar, validar y mantener conocimiento experto requiere mucho trabajo. | Tramo 2 |
| 6 | B | La trazabilidad permite auditar el recorrido, pero no corrige datos falsos ni reglas incompletas. | Tramo 2 y Clase 3 |
| 7 | B | Una base de conocimiento reúne afirmaciones representadas sobre el mundo o el dominio. | Tramo 3 |
| 8 | B | `TELL` incorpora una nueva afirmación a la base. | Tramo 3 |
| 9 | C | `ASK` consulta qué puede inferirse a partir del conocimiento disponible. | Tramo 3 |
| 10 | A | El nivel de conocimiento describe qué sabe el agente; la implementación explica cómo se representa y procesa. | Tramo 3 |
| 11 | B | La construcción declarativa agrega conocimiento y deja que el agente derive la acción. | Tramo 3 |
| 12 | C | No poder demostrar una conclusión puede revelar información faltante; requiere verificación humana. | Integración |

## Matriz de contenidos

| Contenido | Preguntas |
|---|---|
| Sistema simbólico y representación | 1, 2 |
| Historia y conocimiento de dominio | 3, 4, 5 |
| Trazabilidad y límites | 6, 12 |
| Base de conocimiento | 7 |
| `TELL` y `ASK` | 8, 9 |
| Niveles y construcción declarativa | 10, 11 |

## Criterio de validación

Puntaje sugerido: un punto por respuesta correcta, máximo 12.

- **10-12:** lectura comprendida.
- **7-9:** comprensión parcial; pedir revisión dirigida y una nueva justificación.
- **0-6:** lectura insuficiente; solicitar nuevamente la hoja de ruta antes de avanzar.

Para reducir respuestas por adivinación, seleccionar dos preguntas al azar y pedir una justificación oral o escrita. La respuesta debería:

1. explicar la idea con palabras propias;
2. vincularla con una sección concreta;
3. aplicarla a un ejemplo distinto del libro.

## Evidencias esperadas en las actividades

### Tramo 1

El estudiante debería reconocer que la tradición simbólica plantea representar y manipular símbolos, y que las primeras expectativas sobre métodos generales fueron muy altas.

### Tramo 2

Debería explicar que DENDRAL y MYCIN se apoyaron en conocimiento especializado, y que formalizar y mantener ese conocimiento genera un cuello de botella.

### Tramo 3

Debería reconstruir un ciclo equivalente a:

```text
percibir → TELL(percepción) → ASK(acción) → actuar → TELL(acción)
```

El orden conceptual esperado en el ejercicio es:

1. recibir una percepción;
2. incorporar la percepción a la base;
3. consultar qué acción se sigue;
4. ejecutar una acción;
5. registrar la acción realizada.

## Retroalimentación ante errores frecuentes

- **“La base de conocimiento es solo una base de datos”:** pedir que identifique una conclusión que deba inferirse y no esté almacenada explícitamente.
- **“Si se explica, es correcto”:** presentar una regla transparente pero basada en un supuesto falso.
- **“`ASK` busca información en Internet”:** recordar que consulta qué se deriva de la base de conocimiento del agente.
- **“`TELL` enseña automáticamente una regla verdadera”:** distinguir incorporar una afirmación de validar que sea correcta.
- **“Más reglas solucionan todo”:** discutir contradicciones, excepciones, mantenimiento e información ausente.

## Uso sugerido

- Aplicar las doce preguntas en un formulario con orden aleatorio de opciones.
- Conservar las preguntas 6 y 12 como validación conceptual obligatoria.
- Usar las preguntas 8 y 9 como control mínimo del vocabulario de la sección 7.1.
- No entregar esta clave junto con el cuestionario si la actividad será evaluada.
