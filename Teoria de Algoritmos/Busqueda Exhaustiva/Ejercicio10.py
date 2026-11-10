"""

EXPLICACIÓN: la estrategia consiste en aplicar una restricción y un record para que si no cumple la condicion o se supera a ese record, volvemos para atrás y buscamos otra alternativa.

ESTRUCTURA DEL ÁRBOL DE ESTADOS

- NODO: es el elemento actual

- RAMAS: agregamos el elemento a la mochila o no lo agregamos

- HOJA: se evaluaron los "n" elementos

- PODA: tenemos dos podas posibles:
    - PODA POR FACTIBILIDAD: si el elemento supera el peso máximo permitido o si este es incompatible con otro elemento ya agregado a la mochila

    - PODA POR COTA: como se busca maximizar, si el valor actual + valor restate es menor que nuestro record. En caso de empate, se elige la asignación que tenga menor peso

PSEUDOCÓDIGO
"""

RECORD_VALOR = float('-inf')
RECORD_PESO = float('inf')
MEJOR_ASIGNACION = []

def branch_and_bound(indice, peso_actual, valor_actual, agregados, elementos, k):

    global RECORD_VALOR, RECORD_PESO, MEJOR_ASIGNACION

    n = len(elementos)
    if indice == n:
        if valor_actual > RECORD_VALOR or (valor_actual == RECORD_VALOR and peso_actual < RECORD_PESO):
            RECORD_VALOR = valor_actual
            RECORD_PESO = peso_actual
            MEJOR_ASIGNACION = agregados.copy()
        return

    cota = valor_actual + estimar_valor_restante(indice, elementos)
    if cota < RECORD_VALOR or (cota == RECORD_VALOR and peso_actual >= RECORD_PESO):
        return

    elemento = elementos[indice]
    nuevo_peso = peso_actual + elemento.peso
    nuevo_valor = valor_actual + elemento.valor
    
    if nuevo_peso <= k and es_compatible(elemento, agregados):
        agregados.append(elemento)
        branch_and_bound(indice + 1, nuevo_peso, nuevo_valor, agregados, elementos, k)
        agregados.pop()

    branch_and_bound(indice + 1, peso_actual, valor_actual, agregados, elementos, k)

"""
ANÁLISIS DE COMPLEJIDAD

- Temporal: en el peor de los casos, evaluamos si agregar o no agregar a cada elemento, por lo tanto O(2^N). Ademas calcular la cota toma O(N), por lo tanto tenemos una complejidad de O(N * 2^N)

- Espacial: O(N) ya que es el call stack de la recursion
"""
