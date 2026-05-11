byCar(auckland,hamilton).
byCar(hamilton,raglan).
byCar(valmont,saarbruecken).
byCar(valmont,metz).

byTrain(metz,frankfurt).
byTrain(saarbruecken,frankfurt).
byTrain(metz,paris).
byTrain(saarbruecken,paris).

byPlane(frankfurt,bangkok).
byPlane(frankfurt,singapore).
byPlane(paris,losAngeles).
byPlane(bangkok,auckland).
byPlane(singapore,auckland).
byPlane(losAngeles,auckland).

% Para no estar llamando a la base de datos cada vez, se puede crear una regla que unifique los tres medios de transporte.
sinEscalas(X,Y) :- byCar(X,Y).
sinEscalas(X, Y) :- byTrain(X,Y).
sinEscalas(X, Y) :- byPlane(X,Y).

% Armo el viaje con o sin escalas. Si no hay escalas, se llama a la regla sinEscalas. Si hay escalas, se llama a la regla sinEscalas para el primer tramo del viaje y luego se llama a la regla travel para el resto del viaje.
travel(X, Y) :- sinEscalas(X, Y). % Caso base: si no hay escalas, el viaje es directo.
travel(X, Y) :- sinEscalas(X, Z), travel(Z, Y). % Caso recursivo: si hay escalas, se busca un punto intermedio Z y se llama a travel para el resto del viaje, pueden haber infinidad de escalas, por eso se llama a travel y no a sinEscalas.
