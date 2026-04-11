% 1. Regla "fachada": Desarmamos la lista. Usamos el primer elemento (Cabeza) 
% como valor inicial de nuestro acumulador, y pasamos el resto (Cola) a la recursión.
max_lista([Cabeza | Cola], Maximo) :- 
    max_lista_acumulada(Cola, Cabeza, Maximo).

% 2. Caso base: Cuando terminamos de vaciar la lista ([]), 
% el resultado final es lo que nos quedó guardado en el acumulador.
max_lista_acumulada([], Acumulador, Acumulador).

% 3. Caso recursivo: Comparamos el primer elemento actual (Cabeza) con el acumulador.
% Guardamos el ganador usando 'max' y seguimos recorriendo la cola (Cola).
max_lista_acumulada([Cabeza | Cola], Acumulador, Maximo) :-
    NuevoAcumulador is max(Cabeza, Acumulador),
    max_lista_acumulada(Cola, NuevoAcumulador, Maximo).
