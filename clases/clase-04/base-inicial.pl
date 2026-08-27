% Clase 4 - Programacion logica
% Base inicial para la actividad de orientacion academica.

% Individuos y propiedades.
estudiante(ana).
estudiante(bruno).
estudiante(carla).

inscripcion_activa(ana).
inscripcion_activa(bruno).
inscripcion_activa(carla).

% Materias aprobadas.
aprobo(ana, programacion_1).
aprobo(ana, programacion_2).
aprobo(ana, algoritmos).
aprobo(bruno, programacion_1).
aprobo(bruno, programacion_2).
aprobo(carla, programacion_1).

% Condiciones de cursada.
sin_superposicion(ana, inteligencia_artificial).
sin_superposicion(bruno, inteligencia_artificial).
sin_superposicion(carla, inteligencia_artificial).
hay_cupo(inteligencia_artificial).

% correlativa(Materia, RequisitoDirecto).
correlativa(inteligencia_artificial, algoritmos).
correlativa(algoritmos, programacion_2).
correlativa(programacion_2, programacion_1).

% Completar durante la actividad.
% puede_cursar(Estudiante, inteligencia_artificial) :- ... .

% Agregar luego una autorizacion excepcional para carla.
% autorizacion_excepcional(carla, inteligencia_artificial).

% Completar la relacion recursiva requisito/2.
