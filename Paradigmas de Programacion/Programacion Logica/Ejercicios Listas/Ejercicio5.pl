% Caso base: El elemento en la posición 1 es la Cabeza de la lista.
% Usamos '_' para la Cola porque no nos interesa el resto de la lista.
elemento_en(1, [Cabeza | _], Cabeza).

% Caso recursivo: Si K > 1, el elemento que busco está en la posición K-1 de la Cola.
% Usamos '_' para la Cabeza actual porque la descartamos, no es el que buscamos.
elemento_en(K, [_ | Cola], X) :-
    K > 1,
    K1 is K - 1,
    elemento_en(K1, Cola, X).
    