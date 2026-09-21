"""

EXPLICACIÓN: la estrategia consiste en aplicar una restricción y un record para que si no cumple la condicion o se supera a ese record, volvemos para atrás y buscamos otra alternativa.

ESTRUCTURA DEL ÁRBOL DE ESTADOS

- NODO: es el trabajo actual

- RAMAS: son los posibles contratistas para el trabajo actual

- HOJA: se asignaron los "n" trabajos a los "n" contratistas

- PODA: tenemos dos podas posibles:
    - PODA POR VALIDEZ: si el contratista ya fue asignado a un trabajo

    - PODA POR COTA: como se busca minimizar, si el costo actual + costo minimo de los trabajos restates es mayor igual que nuestro record

PSEUDOCÓDIGO
"""

RECORD = float('inf')
MEJOR_ASIGNACION = []

def branch_and_bound(indice_trabajo, asignaciones, costo_actual, matriz_costos):

    global RECORD, MEJOR_ASIGNACION

    n = len(matriz_costos)

    cota = costo_actual + estimar_costo(indice_trabajo, matriz_costos)
    if cota >= RECORD:
        return

    if indice_trabajo == n:

        RECORD = costo_actual
        MEJOR_ASIGNACION = asignaciones.copy()

        return

    for contratista in range(n):

        if contratista not in asignaciones:

            asignaciones.append(contratista)
            nuevo_costo = costo_actual + matriz_costos[indice_trabajo][contratista]

            branch_and_bound(indice_trabajo + 1, asignaciones, nuevo_costo, matriz_costos)

            asignaciones.pop()

"""
ANÁLISIS DE COMPLEJIDAD

- Temporal: en el peor de los casos, la cota no logra podar ninguna rama, por lo tanto O(N!). Ademas por cada nodo tenemos que calcular la cota que toma O(N), por lo tanto tenemos una complejidad de O(N * N!)

- Espacial: O(N) ya que es el call stack de la recursion
"""
