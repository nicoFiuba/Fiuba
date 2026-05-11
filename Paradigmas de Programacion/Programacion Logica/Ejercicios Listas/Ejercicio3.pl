% Caso base 1: Una lista vacía trivialmente tiene "todos" sus elementos iguales.
todos_iguales([]).

% Caso base 2: Una lista con un solo elemento (no importa cuál sea, por eso el '_')
% también cumple la condición.
todos_iguales([_]).

% Caso recursivo: Extraemos los dos primeros elementos exigiendo que sean la 
% misma variable (X, X). Si lo son, verificamos que el resto de la lista 
% (empezando desde el segundo elemento para no perder la cadena) también cumpla.
todos_iguales([X, X | Cola]) :- 
    todos_iguales([X | Cola]).