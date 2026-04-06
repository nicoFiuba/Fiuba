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

travel(X,Y) :- byCar(X,Y).
travel(X, Y) :- byTrain(X,Y).
travel(X, Y) :- byPlane(X,Y).

% FALTA DEFINIR travel(X,Y) PARA QUE INCLUYA LOS VIAJES CON ESCALAS
