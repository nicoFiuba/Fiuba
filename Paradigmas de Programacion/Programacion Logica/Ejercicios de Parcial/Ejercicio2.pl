% Si interpretas que N es el nombre del colectivo, entonces el código es:

subte(personaA).
subte(personaB).
subte(personaC).

colectivo(persona1).
colectivo(persona2).
colectivo(persona3).

viaja_acompanado(X, Y) :- subte(X), subte(Y), X \= Y.
viaja_acompanado(X, Y) :- colectivo(X), colectivo(Y), X \= Y.


% Si interpretas que N es la empresa del colectivo, entonces puede haber muchas lineas de colectivo, y el código es:

subte(personaA).
subte(personaB).

colectivo(persona1, 8).
colectivo(persona2, 2).
colectivo(persona3, 152).
colectivo(persona4, 8).
colectivo(persona5, 152).

viaja_acompanado(X, Y) :- colectivo(X, N), colectivo(Y, N), X \= Y.
viaja_acompanado(X, Y) :- subte(X), subte(Y), X \= Y.
