% Base de conocimientos
viaje(buenosAires, rosario, 100).
viaje(buenosAires, bariloche, 300).
viaje(rosario, misiones, 200).
viaje(bariloche, antartida, 500).

puedo_viajar(V1, V2, X) :- 
    viaje(V1, V2, Costo), % Verifico que exista un viaje directo entre V1 y V2 con un costo
    Costo =< X. % Verifico que el costo del viaje no exceda el presupuesto X.

puedo_viajar(V1, V2, X) :- 
    viaje(V1, Tramo, CostoTramo), % Viajo a un punto intermedio con un costo
    CostoTramo =< X, % Verifico que el costo del tramo no exceda el presupuesto X.
    XRestante is X - CostoTramo, % Calculo el presupuesto restante.
    puedo_viajar(Tramo, V2, XRestante). % Verifico si puedo viajar desde el punto intermedio hasta el destino con el presupuesto restante.
