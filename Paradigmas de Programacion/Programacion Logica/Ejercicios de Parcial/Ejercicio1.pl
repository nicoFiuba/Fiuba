% Base de conocimientos
viaje(buenosAires, rosario, 100).
viaje(buenosAires, bariloche, 300).
viaje(rosario, misiones, 200).
viaje(bariloche, antartida, 500).

% Caso base: Viaje directo. El costo total es el costo del tramo.
puedo_viajar(X, Y, CostoTotal) :- 
    viaje(X, Y, CostoTotal).

% Caso recursivo: Viaje con escala en 'Z'.
puedo_viajar(X, Y, CostoTotal) :- 
    viaje(X, Z, CostoTramo1),           % Averiguo a dónde puedo ir directo y cuánto sale (Tramo 1)
    puedo_viajar(Z, Y, CostoRestante),  % Calculo mágicamente el costo de todo el resto del viaje
    CostoTotal is CostoTramo1 + CostoRestante. % Sumo ambos costos

% Este codigo no soluciona si el destino es el origen, o sea, si quiero viajar de Buenos Aires a Z y de Z a Buenos Aires, aca dejo la solucion al problema:

% 1. Base de conocimientos
viaje(buenosAires, rosario, 100).
viaje(buenosAires, bariloche, 300).
viaje(rosario, misiones, 200).
viaje(bariloche, antartida, 500).
viaje(misiones, buenosAires, 150). % <- Agregamos la trampa (un ciclo) para probar que funciona.

% 2. Regla "Fachada" (La que usa el usuario)
% El usuario solo pone Origen y Destino. Nosotros le iniciamos la lista
% de Visitados poniendo el Origen como el primer lugar pisado.
puedo_viajar(Origen, Destino, CostoTotal) :-
    viaje_aux(Origen, Destino, CostoTotal, [Origen]).

% 3. Caso Base de la regla auxiliar
% Si hay viaje directo, el costo es el del tramo. 
% No nos importa la lista de visitados acá (por eso el guión bajo).
viaje_aux(X, Y, CostoTotal, _Visitados) :- 
    viaje(X, Y, CostoTotal).

% 4. Caso Recursivo de la regla auxiliar (El corazón del algoritmo)
viaje_aux(X, Y, CostoTotal, Visitados) :- 
    viaje(X, Z, CostoTramo1),               % 1. Busco una escala 'Z' y su costo.
    \+ member(Z, Visitados),                % 2. SEGURIDAD: Verifico que 'Z' NO esté en la lista de visitados.
    viaje_aux(Z, Y, CostoRestante, [Z | Visitados]), % 3. Recursión: viajo desde 'Z', agregando 'Z' a la lista.
    CostoTotal is CostoTramo1 + CostoRestante. % 4. Sumo los costos a la vuelta.

