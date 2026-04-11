factorial(X, Y) :- X = 0, Y = 1.
factorial(X, Y) :- X > 0, X1 is X - 1, factorial(X1, Y1), Y is X * Y1. 

% Para mas facilidad se puede escribir como:
factorial(0, 1).
factorial(X, Y) :- X > 0, X1 is X - 1, factorial(X1, Y1), Y is X * Y1.

% Estas dos formas son equivalentes. La primera es una forma más explícita, mientras que la segunda es más concisa y comúnmente utilizada en Prolog. Ambas definen la función factorial de manera recursiva, donde el caso base es cuando X es 0, y el caso recursivo se aplica para valores mayores que 0.

% El problema es que no es optima ya que se hacen muchas llamadas recursivas, lo que puede llevar a un desbordamiento de pila para valores grandes de X. Para optimizarla, se puede usar una técnica llamada "tail recursion" o recursión de cola, que evita la necesidad de mantener múltiples llamadas en la pila. Aquí hay una versión optimizada:

% 1. Regla "fachada": Es la que vos llamás. Inicializa la "mochila" (el acumulador) en 1.
factorial(X, Y) :- factorial(X, 1, Y).

% 2. Caso base: Cuando X llega a 0, el resultado final (Y) es lo que juntamos en el Acumulador.
factorial(0, Acumulador, Acumulador).

% 3. Caso recursivo: Voy multiplicando paso a paso y pasándolo al siguiente.
factorial(X, Acumulador, Y) :-
    X > 0,
    X1 is X - 1,
    NuevoAcumulador is Acumulador * X,
    factorial(X1, NuevoAcumulador, Y).

% En esta versión optimizada, la función factorial/3 es la que hace el trabajo real. El primer argumento es el número del cual queremos calcular el factorial, el segundo es un acumulador que va guardando el resultado parcial, y el tercero es el resultado final. La función factorial/2 simplemente llama a factorial/3 con el acumulador inicializado en 1. Esta técnica evita la necesidad de mantener múltiples llamadas en la pila, lo que hace que sea más eficiente para valores grandes de X.
