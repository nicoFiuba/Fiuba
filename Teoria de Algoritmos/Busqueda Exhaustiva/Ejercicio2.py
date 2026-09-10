"""

EXPLICACIÓN: Como se pide determinar si existe una solución, significa que el problema se resuelve mediante backtracking, es decir que aplicamos una restricción y si no la cumple, volvemos para atrás y buscamos otra alternativa.

ESTRUCTURA DEL ÁRBOL DE ESTADOS
- NODO: es el estado de la orilla representado con la tupla (Caníbales, Vegetarianos, Bote).

- RAMAS: son las combinaciones posibles de viaje

- HOJAS: tenemos dos casos posibles:
    - Éxito: Llegaron todos sanos y salvos al destino.
    - Fracaso: No llegaron todos al destino.

PSEUDOCÓDIGO
"""

def backtracking(estado_actual, viajes_realizados):

    if estado_actual == (0, 0, 0):
        return "Exito"

    if murio_un_vegetariano(estado_actual) or estado_actual in viajes_realizados:
        return "Fracaso"

    viajes_realizados.add(estado_actual)

    posibles_viajes = [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1)]

    for viaje in posibles_viajes:
        nuevo_estado = mover_bote(estado_actual, posibles_viajes)

        resultado = backtracking(nuevo_estado, viajes_realizados)

        if resultado != "Fracaso":
            return resultado

    viajes_realizados.remove(estado_actual)

    return "Fracaso"

"""
ANÁLISIS DE COMPLEJIDAD

- TEMPORAL: En el peor de los casos, gracias a que llevábamos un registro, el algoritmo explora cada estado y sus cambios una única vez. Por lo tanto, la complejidad es O(V + E). A su vez, como nuestro problema tiene 4 estados posibles para los caníbales y vegetarianos (0, 1, 2 o 3) y el bote tiene 2 posibles estados (origen o destino), te queda un total de 4 * 4 * 2 = 32 estados posibles; por lo tanto, la complejidad es O(1).

- ESPACIAL: O(V), ya que es el call stack de la recursión. Pero como la temporal es O(1), la espacial también es O(1).
"""
    