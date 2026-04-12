% Definimos los 4 colores disponibles como hechos.
color(rojo).
color(azul).
color(verde).
color(amarillo).

colorear(A, B, C, D, E) :-
    % Asignamos colores a cada región
    color(A), color(B), color(C), color(D), color(E),

    % Restricciones de A (toca a todos)
    A \= B, A \= C, A \= D, A \= E,

    % Restricciones de B
    B \= C, B \= E,

    % Restricciones de C
    C \= D, C \= E,

    % Restricciones de D
    D \= E.

% La solucion anterior esta bien pero no es eficiente. 
% SOLUCION EFICIENTE:

colorear(A, B, C, D, E) :-
    color(A),
    color(B), A \= B,             % Si A y B son iguales, acá ya hace backtracking
    color(C), A \= C, B \= C,      % Si C no encaja, ni se gasta en D y E
    color(D), A \= D, C \= D,
    color(E), A \= E, B \= E, C \= E, D \= E.

