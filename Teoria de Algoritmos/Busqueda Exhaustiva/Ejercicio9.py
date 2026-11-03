"""

EXPLICACIÓN: la estrategia consiste en aplicar una restricción y si no la cumple, volvemos para atrás y buscamos otra alternativa.

ESTRUCTURA DEL ÁRBOL DE ESTADOS

- NODO: posicion actual, representado por una tupla (fila, columna))

- RAMAS: pintamos la celda de negro o la pintamos de blanco

- HOJA: evaluamos toda la cuadricula.

- PODA (Por factibilidad): si incumplimos la restriccion

PSEUDOCÓDIGO
"""

def backtracking(fila, columna, cuadricula, limites, soluciones, N):

    if fila == N:
        if cumple_limites(cuadricula, limites):
            soluciones.append(cuadricula.copy())
        return

    siguiente_fila, siguiente_columna = calcular_siguiente_celda(fila, columna, N)

    for color in ["Negro", "Blanco"]:
        cuadricula[fila][columna] = color

        if es_valido(cuadricula, limites):

            backtracking(siguiente_fila, siguiente_columna, cuadricula, limites, soluciones, N)

        cuadricula[fila][columna] = "Sin pintar"

"""
ANÁLISIS DE COMPLEJIDAD

- TEMPORAL: en el peor de los casos, el algoritmo explora dos opciones por celda, lo que toma O(2^N); ademas la cuadricula es de N*N = N². Por lo tanto, la complejidad es O(2^N²)

- ESPACIAL: O(N²) ya que es el call stack de la recursión
"""
