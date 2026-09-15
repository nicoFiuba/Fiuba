"""

EXPLICACIÓN: 
- Divide: dividimos al vector a la mitad

- Conquista:
Si el valor en la mitad == índice + 1 => El vector no tiene desfase, por lo tanto descarto la parte izquierda.
Si el valor en la mitad != índice + 1 => El vector tiene un desfase, por lo tanto, descarto la parte derecha.

- Combina: el resultado está en el caso base.

PSEUDOCÓDIGO
"""

def encontrar_al_no_incluido(vector, inicio, final):

    if inicio == final:
        return inicio + 1

    mitad = (inicio + final) // 2

    if vector[mitad] == mitad + 1:
        return encontrar_al_no_incluido(vector, mitad + 1, final)
    else:
        return encontrar_al_no_incluido(vector, inicio, mitad)

"""
ECUACIÓN DE RECURRENCIA
T(N) = a * T(N/b) + c * f(N)

a = 1, es la llamada recursiva
b = 2 porque dividimos al vector en dos
f(n) = O(1) porque calcula los índices centrales y los compara

ANÁLISIS DE COMPLEJIDAD

- Temporal: T(N) = a * T(N/b) + c * f(N) = 1 * T(N/2) + O(1) = 1 * T(N/2) + O(N^0)
a vs b^k = 1 vs 2^0 = 1 vs 1 => 1 = 1 por lo tanto O(N^k * log(N)) = O(N^0 * log(N)) = O(1 * log(N)) = O(log(N))

- Espacial: O(log(N)) porque es el call stack de la recursión
"""
