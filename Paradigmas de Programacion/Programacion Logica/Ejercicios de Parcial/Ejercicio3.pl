% Base conocimientos original
padre(juan, ana).
padre(ana, pedro).
padre(pedro, lucia).
padre(lucia, carla).

% Base de conocimientos adicional
padre(mario, ana).
padre(sofia, mario).
padre(diego, pedro).

% Reglas
ancestroConLimite(Y, X, N) :-
    personasEnElMedio(Y, X, Cantidad), % Verifico cuántas personas hay entre el ancestro y el descendiente
    Cantidad =< N. % Verifico que la cantidad no exceda el límite N.

personasEnElMedio(Y, X, 0) :-
    padre(X, Y). % Verifico que Y sea el padre de X, lo que significa que es progenitor directo

personasEnElMedio(Y, X, Cantidad) :-
    padre(Z, Y), % Verifico que Y sea progenitor de un hijo intermedio Z
    personasEnElMedio(Z, X, CantidadAnterior), % Verifico cuántas personas hay entre Z y el descendiente final X
    Cantidad is CantidadAnterior + 1. % Calculo la cantidad sumando 1 a la cantidadAnterior
