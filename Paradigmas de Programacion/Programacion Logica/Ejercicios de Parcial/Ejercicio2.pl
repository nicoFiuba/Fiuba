% Base de conocimientos
subte(personaA).
subte(personaB).

colectivo(persona1, 8). 
colectivo(persona2, 2).
colectivo(persona3, 152).
colectivo(persona4, 8).
colectivo(persona5, 152).

viaja_acompanado(X, Y) :-
    colectivo(X, N), % Verifico que X viaje en colectivo y obtengo el número de colectivo N
    colectivo(Y, N), % Verifico que Y viaje en colectivo y obtengo el número de colectivo N
    X \= Y. % Verifico que X e Y sean personas distintas

viaja_acompanado(X, Y) :-
    subte(X), % Verifico que X viaje en subte
    subte(Y), % Verifico que Y viaje en subte
    X \= Y. % Verifico que X e Y sean personas distintas
