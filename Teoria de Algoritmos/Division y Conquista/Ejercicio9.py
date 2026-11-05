"""

EXPLICACIÓN

- Divide: dividimos a la matriz en 4 submatrices de tamaño n/2

- Conquista: evaluamos el centro y descartamos la submatriz que no contiene el número buscado

- Combina: el resultado está en la unión de todos los casos conquistados

PSEUDOCÓDIGO
"""

def encontrar_posicion_numero(matriz, buscado, n):

    if n == 2:
        return resolver_con_fuerza_bruta(matriz, buscado)

    sub_matrices, centro = dividir_matriz_y_definir_centro(matriz, n/2)

    if centro > buscado:
        sub_matrices.delete(0)
    elif centro < buscado:
        sub_matrices.delete(1)
    else:
        return centro

    for sub_matriz in sub_matrices:
        resultado = encontrar_posicion_numero(sub_matriz, buscado, n/2)
        if resultado is not None:
            return resultado

    return None

"""
ECUACIÓN DE RECURRENCIA
T(N) = a * T(N/b) + c * f(N)

a = 3, son las llamadas recursivas
b = 2 porque dividimos la matriz en 2
f(n) = O(1) porque calcula los indices centrales

ANÁLISIS DE COMPLEJIDAD

-  Temporal: T(N) = a * T(N/b) + c * f(N) = 3 * T(N/2) + O(1) = 3 * T(N/2) + O(N^0)
a vs b^k = 3 vs 2^0 = 3 vs 1 => 3 > 1 por lo tanto O(N^log_b(a)) = O(N^log_2(3))

- Espacial: O(log (N)) porque es el call stack de la recursión
"""
