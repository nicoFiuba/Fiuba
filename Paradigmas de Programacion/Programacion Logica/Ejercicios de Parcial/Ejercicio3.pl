padre(juan, ana).
padre(ana, pedro).
padre(pedro, lucia).
padre(lucia, carla).

ancestro(X, Y, N) :- 
    N >= 0,
    padre(X, Y).

ancestro(X, Y, N) :- 
    N > 0,
    padre(X, Z),
    N1 is N - 1,
    ancestro(Z, Y, N1).

