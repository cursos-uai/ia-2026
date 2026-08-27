% Clase 4 - Programacion logica con Prolog
% Base inicial para la actividad "Rutas inteligentes".

conexion(campus, centro, colectivo).
conexion(centro, terminal, subte).
conexion(campus, parque, bicicleta).
conexion(parque, centro, bicicleta).
conexion(terminal, aeropuerto, colectivo).
conexion(centro, aeropuerto, tren).

habilitado(ana, colectivo).
habilitado(ana, subte).
habilitado(ana, tren).
habilitado(bruno, bicicleta).
habilitado(bruno, colectivo).

% Parte 2: reemplazar fail por las condiciones necesarias.
puede_viajar_directo(_Persona, _Origen, _Destino) :-
    fail.

% Parte 3: reemplazar fail por las condiciones necesarias.
puede_viajar_con_una_escala(_Persona, _Origen, _Escala, _Destino) :-
    fail.

% Parte 4: agregar hechos o reglas para los casos pendientes de revision.
