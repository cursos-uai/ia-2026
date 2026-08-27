# Actividad en clase - Diseñamos y auditamos un sistema experto

## Propósito

Aplicar los conceptos de símbolo, hecho, regla e inferencia mediante el diseño de un sistema experto pequeño. La actividad también busca reconocer excepciones, riesgos y límites del modelo construido.

## Modalidad y duración

- Grupos de 3 o 4 estudiantes.
- Duración total: 45 minutos.
- Entrega: una hoja o archivo por grupo.

## Situación

La universidad quiere una herramienta de orientación inicial que indique si un estudiante está en condiciones de inscribirse a una materia. El sistema no decide formalmente ni reemplaza al personal académico: solo produce una recomendación que debe poder explicar.

Para esta actividad, supongan que pueden ser relevantes estos datos:

- materias correlativas aprobadas;
- inscripción administrativa activa;
- superposición horaria;
- cupo disponible;
- autorización excepcional de la dirección de carrera.

## Parte 1 - Construcción del modelo (15 minutos)

Definan:

1. al menos cinco símbolos o predicados;
2. cuatro hechos para un estudiante ficticio;
3. tres reglas del tipo “SI... ENTONCES...”;
4. una consulta que el sistema debería responder.

Pueden usar lenguaje natural estructurado o una notación como esta:

```text
correlativas_aprobadas(lucia)
inscripcion_activa(lucia)
hay_cupo(inteligencia_artificial)

SI correlativas_aprobadas(X)
Y inscripcion_activa(X)
Y hay_cupo(inteligencia_artificial)
ENTONCES puede_inscribirse(X, inteligencia_artificial)
```

## Parte 2 - Inferencia explicada (10 minutos)

Respondan la consulta para el caso creado y escriban la cadena de razonamiento:

```text
Hechos utilizados → regla aplicada → conclusión
```

La conclusión debe derivarse realmente de las reglas. No puede aparecer como un hecho inicial.

Luego escriban una explicación destinada al estudiante, sin jerga técnica y en no más de tres oraciones.

## Parte 3 - Auditoría cruzada (10 minutos)

Intercambien el modelo con otro grupo. El grupo revisor debe encontrar:

- una excepción no contemplada;
- una regla ambigua o incompleta;
- dos reglas que podrían producir recomendaciones incompatibles, si las hubiera;
- un dato innecesario o sensible que no debería usarse;
- una decisión que debe conservar supervisión humana.

Registren las observaciones recibidas y modifiquen al menos una regla.

## Parte 4 - Comparación de enfoques (5 minutos)

Respondan:

1. ¿Qué parte del problema resolverían con reglas explícitas?
2. ¿Hay alguna parte que podría beneficiarse de aprender patrones a partir de datos?
3. Si combinaran ambos enfoques, ¿qué restricciones deberían seguir siendo explícitas?

## Parte 5 - Cierre (5 minutos)

Cada grupo comparte:

- una regla;
- una conclusión derivada;
- la excepción más importante detectada durante la auditoría.

## Entregable

El archivo o la hoja debe contener:

- integrantes;
- símbolos o predicados;
- hechos;
- reglas;
- consulta;
- cadena de inferencia;
- explicación para el estudiante;
- hallazgos de la auditoría;
- regla corregida;
- respuesta sobre un posible enfoque híbrido.

## Criterios de evaluación

| Criterio | Logrado | En proceso | A revisar |
|---|---|---|---|
| Representación | Símbolos y hechos son claros y pertinentes | Hay pequeñas ambigüedades | Confunde símbolos, hechos y conclusiones |
| Reglas | Las reglas permiten derivar la conclusión | Alguna regla está incompleta | La conclusión no se sigue de las reglas |
| Explicación | El recorrido es trazable y comprensible | Se entiende parcialmente | No identifica hechos o reglas usados |
| Auditoría | Detecta excepciones, riesgos y datos sensibles | Detecta solo parte de los problemas | Asume que una regla explícita siempre es correcta |
| Revisión | Corrige una regla justificadamente | Corrige sin justificar | No incorpora la revisión |
| Comparación | Distingue con fundamento lo simbólico, aprendido e híbrido | La distinción es general | Confunde los enfoques |

## Pregunta individual de salida

En no más de cinco líneas:

> ¿Por qué un sistema capaz de explicar qué regla aplicó puede seguir tomando una mala decisión?

## Orientaciones para el docente

- Verificar que los grupos no escriban la conclusión como un hecho inicial.
- Preguntar qué ocurre si faltan datos o si dos reglas se contradicen.
- Recordar que “explicable” no significa automáticamente “correcto”, “justo” o “seguro”.
- No permitir que se usen atributos sensibles sin una justificación legítima y explícita.
- Cerrar conectando hechos, reglas y consultas con la próxima clase de programación lógica y Prolog.
