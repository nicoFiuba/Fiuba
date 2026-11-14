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

EJEMPLO
- Entrada: 3 clases para dar. Clase 1 = (8 a 9hs, $10), Clase 2 = (8 a 10hs, $50), Clase 3 = (10 a 11hs, $20). RECORD inicial = -infinito.
- Ejecución:
    - Rama 1 (Solución inicial): Incluimos a la Clase 1 = $10. Intentamos incluir a la Clase 2, pero se superponen los horarios y por ende se poda. Incluimos a la Clase 3 = $20. Llegamos a la hoja con ganancia total = 30. Actualizamos RECORD = 30.
    - Rama 2 (Nueva mejor solución): excluimos a la Clase 1 (ganancia = 0). Incluimos a la Clase 2 y  3 ya que no se pisan, entonces 50 + 20. Llegamos a la hoja con ganancia = 70. Actualizamos RECORD = 70.
    - Rama 3 (Poda por cota): Intentamos una rama excluyendo a la Clase 1 y 2 (ganancia actual = $0). Solo queda la Clase 3. Calculamos la cota: ganancia actual (0) + ganancia máxima restante (20) = 20. Como nuestra cota de 20 es menor que el RECORD actual (70), podamos la rama inmediatamente porque es imposible mejorar.
- Resultado: finaliza la exploración y retorna la inclusión de Clase 2 y 3 con una ganancia máxima de $70.
"""
