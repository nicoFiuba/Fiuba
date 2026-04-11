potencia(_, 0, 1). % Uso el _ para indicar que el valor de la base no importa cuando el exponente es 0 (ya que cualquier número elevado a 0 es 1).


% Caso recursivo: Base^Exponente = Base * Base^(Exponente-1)
potencia(Base, Exponente, Resultado) :- 
    Exponente > 0,
    Exponente1 is Exponente - 1,
    potencia(Base, Exponente1, ResultadoParcial), 
    Resultado is Base * ResultadoParcial. 

% --- VERSIÓN 2: Optimizada (Recursividad de cola con Acumulador) ---

% 1. Regla "fachada": Inicializa el acumulador en 1 (el elemento neutro de la multiplicación).
potencia(Base, Exponente, Resultado) :- potencia(Base, Exponente, 1, Resultado).

% 2. Caso base: Cuando el exponente llega a 0, devuelvo lo que junté en el acumulador.
potencia(_, 0, Acumulador, Acumulador).

% 3. Caso recursivo: Multiplico el acumulador por la base y bajo el exponente.
potencia(Base, Exponente, Acumulador, Resultado) :-
    Exponente > 0,
    Exponente1 is Exponente - 1,
    NuevoAcumulador is Acumulador * Base,
    potencia(Base, Exponente1, NuevoAcumulador, Resultado).
