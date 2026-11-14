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

EJEMPLO
- Entrada: Cuadrícula de 2x2 (N=2). Límite: exactamente 1 celda negra por fila y columna.
- Ejecución:
    - Celda (0, 0) - Rama 1: pintamos de "Negro". Como es válido (llevamos 1 negra en la fila 0 y columna 0), avanzamos a la celda (0, 1).
    - Celda (0, 1) - Rama 1.a: pintamos de "Negro". Se incumple la restricción (habría 2 negras en la fila 0), por ende se poda la rama.
    - Celda (0, 1) - Rama 1.b: pintamos de "Blanco". La restricción se mantiene intacta, seguimos explorando hacia la fila siguiente.
- Resultado: El algoritmo avanza y retrocede hasta completar la cuadrícula con una configuración válida y la guarda en soluciones.
"""
