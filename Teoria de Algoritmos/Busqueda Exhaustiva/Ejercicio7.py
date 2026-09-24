"""

EXPLICACIÓN: la estrategia consiste en aplicar una restricción y un record para que si no cumple la condicion o se supera a ese record, volvemos para atrás y buscamos otra alternativa.

ESTRUCTURA DEL ÁRBOL DE ESTADOS

- NODO: es la escena actual

- RAMAS: son los posibles servidores para la escena actual

- HOJA: se asignaron las "m" escenas a los "n" servidores

- PODA (POR COTA): como se busca minimizar, si la carga actual + duracion de la escena es mayor igual que nuestro record

PSEUDOCÓDIGO
"""

RECORD = float('inf')
MEJOR_ASIGNACION = []

def branch_and_bound(indice_escena, asignaciones, cargas, duraciones):

    global RECORD, MEJOR_ASIGNACION

    n = len(duraciones)
    if indice_escena == n:
        tiempo_maximo = max(cargas)

        if tiempo_maximo < RECORD:
            RECORD = tiempo_maximo
            MEJOR_ASIGNACION = asignaciones.copy()

        return

    duracion_actual = duraciones[indice_escena]
    
    for servidor in range(len(cargas)):

        if cargas[servidor] + duracion_actual < RECORD:

            asignaciones.append(servidor)
            cargas[servidor] += duracion_actual

            branch_and_bound(indice_escena + 1, asignaciones, cargas, duraciones)

            cargas[servidor] -= duracion_actual
            asignaciones.pop()

"""
ANÁLISIS DE COMPLEJIDAD

- Temporal: en el peor de los casos, la cota no logra podar ninguna rama, es decir que podemos agregar "m" escenas a "n" servidores. Por lo tanto O(N^M). Ademas calcular el maximo de las cargas toma O(N), por lo tanto tenemos una complejidad de O(N * N^M)

- Espacial: el call stack de la recursion toma O(M) pero ademas necesitamos almacenar las cargas de los servidores, lo que toma O(N). Por lo tanto, la complejidad es O(M + N) 
"""
