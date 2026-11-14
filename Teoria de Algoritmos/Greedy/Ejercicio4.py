"""

EXPLICACIÓN: la estrategia consiste en ordenar las charlas de menor a mayor según su inicio, para que, si una sala está ocupada, se habilite una nueva sala. Esta estrategia es Greedy porque realiza una elección:
    - Localmente óptima ya que en cada iteración evalúa si la sala está libre para poder evitar el uso de una nueva sala
    - Factible ya que solo asigna la charla si la sala está libre
    - Irrevocable ya que una vez asignada la charla, no se puede desasignar

PSEUDOCÓDIGO
"""

import heapq

def asignar_salas(charlas):

    charlas.sort(key=lambda x: x.inicio)
    horarios_salas_libres = []
    cantidad_salas = 0

    for charla in charlas:

        if len(horarios_salas_libres) > 0 and horarios_salas_libres[0] <= charla.inicio:
                heapq.heappop(horarios_salas_libres)
                heapq.heappush(horarios_salas_libres, charla.fin)
        else:
            cantidad_salas += 1
            heapq.heappush(horarios_salas_libres, charla.fin)

    return cantidad_salas

"""
ANÁLISIS DE COMPLEJIDAD

- TEMPORAL: ordenar la lista toma O(N * log(N)) mientras que insertar y extraer del Heap toma O(N * log(N)). Por lo tanto, la complejidad es O(N * log(N)).

- ESPACIAL: O(N) para almacenar a las salas.

ANÁLISIS DE OPTIMALIDAD: se demuestra mediante el absurdo, ya que si el algoritmo se ve obligado a habilitar K salas, es porque en determinado momento hay K charlas ocurriendo a la vez. Por lo tanto, como es imposible dar K charlas en menos de K salas, el algoritmo es óptimo.

EJEMPLO
- Entrada: Charlas con (inicio, fin): Charla 1 = (1, 4), Charla 2 = (2, 5), Charla 3 = (4, 6). (Ya ordenadas por inicio).
- Ejecución:
    - C1(1, 4): heap vacío. Se habilita sala 1. Heap = [4].
    - C2(2, 5): inicio (2) < Heap[0] (4). Sala ocupada. Se habilita sala 2. Heap = [4, 5].
    - C3(4, 6): inicio (4) >= Heap[0] (4). Hay sala libre. Se extrae el 4 y se inserta el 6. Heap = [5, 6].
- Resultado: Se utilizan 2 salas en total.
"""
