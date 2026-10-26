"""

EXPLICACIÓN: voy a usar un arreglo unidimensional OPT de tamaño N, la celda OPT[i] guardará la ganancia máxima posible de un bloque de terrenos que termina exactamente en i. Para calcular OPT[i] iteramos sobre todos los terrenos y nos fijamos qué es mejor: sumarle el terreno actual a la ganancia del bloque anterior (OPT[i-1]) o empezar un nuevo bloque de terrenos desde cero.

RELACION DE RECURRENCIA:
- Caso base: OPT[0] = terrenos[0], el primer terreno no tiene bloque anterior

- Caso recursivo: Si i > 0 => OPT[i] = max(terrenos[i], terrenos[i] + OPT[i-1])

PSEUDOCÓDIGO
"""

def max_ganancia(terrenos):

    n = len(terrenos)
    if n == 0:
        return 0
    
    OPT = [0] * n
    OPT[0] = terrenos[0]

    for i in range(1, n):
        OPT[i] = max(terrenos[i], terrenos[i] + OPT[i - 1])

    return max(OPT)

"""
ANÁLISIS DE COMPLEJIDAD
- Temporal: O(N) porque recorremos el arreglo de terrenos una sola vez.

- Espacial: O(N) porque usamos un arreglo adicional OPT de tamaño N.

EJEMPLO:

terrenos = [-2, 3, -3, 4, -1, 2]

OPT[0] = -2
OPT[1] = max(valor_actual, valor_actual + OPT[pos_actual - 1]) = max(3, 3 + OPT[1 - 1]) = max(3, 3 + OPT[0]) = max(3, 3 + (-2)) = max(3, 3 - 2) = max(3, 1) = 3
OPT[2] = max(valor_actual, valor_actual + OPT[pos_actual - 1]) = max(-3, -3 + OPT[2 - 1]) = max(-3, -3 + OPT[1]) = max(-3, -3 + 3) = max(-3, 0) = 0
OPT[3] = max(valor_actual, valor_actual + OPT[pos_actual - 1]) = max(4, 4 + OPT[3 - 1]) = max(4, 4 + OPT[2]) = max(4, 4 + 0) = max(4, 4) = 4
OPT[4] = max(valor_actual, valor_actual + OPT[pos_actual - 1]) = max(-1, -1 + OPT[4 - 1]) = max(-1, -1 + OPT[3]) = max(-1, -1 + 4) = max(-1, 3) = 3
OPT[5] = max(valor_actual, valor_actual + OPT[pos_actual - 1]) = max(2, 2 + OPT[5 - 1]) = max(2, 2 + OPT[4]) = max(2, 2 + 3) = max(2, 5) = 5

Vector resultante: OPT = [-2, 3, 0, 4, 3, 5].

El max(OPT) devuelve 5, que es la ganancia máxima.

"""
