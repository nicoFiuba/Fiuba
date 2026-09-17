"""

EXPLICACIÓN: la estrategia consiste en aplicar una restricción y si no la cumple, volvemos para atrás y buscamos otra alternativa.

ESTRUCTURA DEL ÁRBOL DE ESTADOS
- NODO: Es el estado del tablero, representado por un vector donde el índice es la fila y el valor es la columna elegida.

- RAMAS: son las columnas posibles para colocar a la reina en la siguiente fila

- HOJA: todas las reinas están ubicadas en el tablero sin atacarse entre sí.

- PODA: no se puede ubicar una reina en el tablero sin que se ataque con otra

PSEUDOCÓDIGO
"""

def backtracking(tablero, fila_actual, N):

    if fila_actual <= N:
        return "EXITO"

    for columna in range(N):

        tablero.append(columna)

        if es_valido(tablero):

            resultado = backtracking(fila_actual + 1, tablero, N)

            if resultado == "EXITO":
                return "EXITO"

        tablero.pop()

    return "FRACASO"

"""
ANÁLISIS DE COMPLEJIDAD

- TEMPORAL: al modelear el problema como permutaciones, en el peor de los casos, el algoritmo explora todas las cambinaciones posiles. Por lo tanto, la complejidad es O(N!)

- ESPACIAL: O(N) ya que es el call stack de la recursión
"""
