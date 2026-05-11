fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(N, X) :- 
    N > 1, 
    N1 is N - 1, 
    N2 is N - 2, 
    fibonacci(N1, X1), 
    fibonacci(N2, X2), 
    X is X1 + X2.


% --- VERSIÓN 2: Optimizada (Recursividad de cola con Acumuladores) ---
% Esta versión resuelve la matemática "hacia adelante" trasladando los valores.
% Evita desbordamientos de memoria porque no deja operaciones pausadas.

% 1. Regla "fachada": Inicializa los dos primeros números de la serie (0 y 1).
fibonacci(N, X) :- fibonacci(N, 0, 1, X).

% 2. Caso base: Cuando el contador N llega a 0, el resultado final es el primer acumulador (A).
fibonacci(0, A, _, A).

% 3. Caso recursivo: Calculo la suma de los anteriores y avanzo el contador.
fibonacci(N, A, B, X) :-
    N > 0,
    N1 is N - 1,
    Siguiente is A + B,
    fibonacci(N1, B, Siguiente, X).