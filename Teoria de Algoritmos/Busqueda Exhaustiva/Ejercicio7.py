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

EJEMPLO
- Entrada: 3 escenas con duraciones [10, 20, 30] y 2 servidores (S0 y S1). RECORD inicial = infinito.
- Ejecución:
    - Rama 1 (Solución inicial): asignamos las 3 escenas al S0. Las cargas quedan: S0 = 60, S1 = 0. Llegamos a la hoja, el tiempo máximo es 60. Actualizamos RECORD = 60.
    - Rama 2 (Nueva mejor solución): asignamos Escena 1 y 2 al S0 (carga = 30) y Escena 3 al S1 (carga = 30). Llegamos a la hoja, el tiempo máximo es 30. Actualizamos RECORD = 30.
    - Rama 3 (Poda por cota): en otra exploración, intentamos asignar la Escena 1 y 2 al S1 (carga = 30). Al intentar sumarle la Escena 3 a S1, su carga pasaría a ser 60 (30 + 30). Como esta carga proyectada (60) es mayor o igual a nuestro RECORD actual (30), se poda la rama inmediatamente.
- Resultado: finaliza la exploración y retorna la asignación más equilibrada con un tiempo máximo de 30.
"""
