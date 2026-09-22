"""

EXPLICACIÓN: la estrategia consiste en aplicar una restricción y un record para que si no cumple la condicion o no se supera a ese record, volvemos para atrás y buscamos otra alternativa.

ESTRUCTURA DEL ÁRBOL DE ESTADOS

- NODO: es la actividad actual

- RAMAS: son las opciones posibles (inlcuir o no a la actividad actual)

- HOJA: se evaluaron las "n" actividades

- PODA: tenemos dos podas posibles:
    - PODA POR VALIDEZ: si la acividad se superpone con otra

    - PODA POR COTA: como se busca maximizar, si la ganancia actual + ganancia actividades restantes es menor o igual que nuestro record

PSEUDOCÓDIGO
"""

RECORD = float('-inf')
MEJORES_INCLUSIONES = []

def branch_and_bound(indice_actividad, actividades, ganancia_actual,inclusiones):

    global RECORD, MEJORES_INCLUSIONES

    n = len(actividades)

    cota = ganancia_actual + estimar_ganancias(indice_actividad, actividades)

    if cota <= RECORD:
        return

    if indice_actividad == n:

        RECORD = ganancia_actual
        MEJORES_INCLUSIONES = inclusiones.copy()

        return

    actividad_actual = actividades[indice_actividad]

    if es_compatible(actividad_actual, inclusiones):


        inclusiones.append(actividad_actual)
        nueva_ganancia = ganancia_actual + actividad_actual.ganancia

        branch_and_bound(indice_actividad + 1, actividades, nueva_ganancia,inclusiones)

        inclusiones.pop()

    branch_and_bound(indice_actividad + 1, actividades, ganancia_actual,inclusiones)

"""
ANÁLISIS DE COMPLEJIDAD

- Temporal: en el peor de los casos, la cota no logra podar ninguna rama, por lo tanto O(2^N). Ademas por cada nodo tenemos que calcular la cota que toma O(N), por lo tanto tenemos una complejidad de O(N * 2^N)

- Espacial: O(N) ya que es el call stack de la recursion
"""
