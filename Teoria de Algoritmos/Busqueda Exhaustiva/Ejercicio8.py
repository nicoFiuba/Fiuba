"""

EXPLICACIÓN: como se pide determinar si existe una solución, significa que el problema se resuelve mediante backtracking, es decir que aplicamos una restricción y si no la cumple, volvemos para atrás y buscamos otra alternativa.

ESTRUCTURA DEL ÁRBOL DE ESTADOS

- NODO: es el estado de la orilla representado con la tupla (Lobo, Cabra, Zanahoria, Bote).

- RAMAS: son las combinaciones posibles de pasajeros por viaje

- HOJAS: llegaron todos sanos y salvos al destino.

- PODA: si murio la cabra, se comieron la zanahoria o ya hicimos ese viaje

PSEUDOCÓDIGO
"""

def backtracking(estado_actual, viajes_realizados):

    if estado_actual == (0, 0, 0, 0):
        return True

    if murio_la_cabra(estado_actual) or comieron_la_zanahoria(estado_actual) or estado_actual in viajes_realizados:
        return False

    viajes_realizados.add(estado_actual)

    posibles_viajes = [(1, 0,0), (0, 1, 0), (0, 0, 1), (0, 0, 0)]

    for viaje in posibles_viajes:
        nuevo_estado = mover_bote(estado_actual, viaje)

        resultado = backtracking(nuevo_estado, viajes_realizados)

        if resultado == True:
            return True

    viajes_realizados.remove(estado_actual)

    return False

"""
ANÁLISIS DE COMPLEJIDAD

- TEMPORAL: en el peor de los casos, gracias a que llevábamos un registro, el algoritmo explora cada estado y sus cambios una única vez. Por lo tanto, la complejidad es O(V + E). A su vez, como nuestro problema tiene 2 estados posibles para el lobo, la cabra y la zanahoria (0, 1) y el bote tiene 2 posibles estados (origen o destino), te queda un total de 2 * 2 * 2 * 2 = 16 estados posibles; por lo tanto, la complejidad es O(1).

- ESPACIAL: O(V) ya que es el call stack de la recursión. Pero como la temporal es O(1), la espacial también es O(1).
"""
