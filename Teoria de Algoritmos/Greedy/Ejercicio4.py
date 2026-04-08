"""
TEORÍA DE ALGORITMOS - EJERCICIO 4: Asignación de Salas de Exposición

1. ESTRATEGIA (Elección Golosa)
El problema consiste en minimizar la cantidad de recursos (salas) para acomodar 
un conjunto de intervalos de tiempo superpuestos (charlas + 15 min de descanso).

Estrategia greedy:
1. Calculamos el "horario de liberación" de cada charla (inicio + duración + 15 min).
2. Ordenamos todas las charlas cronológicamente según su HORARIO DE INICIO.
3. Utilizamos una Cola de Prioridad (Min-Heap) para llevar el registro de las salas activas. El Heap ordenará las salas basándose en qué momento se liberan.
4. Iteramos sobre las charlas ordenadas:
- Miramos la cima del Heap (la sala que se libera más temprano).
- Si esa sala se libera ANTES o en el mismo momento en que empieza la charla actual, sacamos esa sala del Heap, le asignamos la charla actual, actualizamos su nuevo horario de liberación y la volvemos a insertar.
- Si la sala en la cima del Heap todavía está ocupada, significa que TODAS las salas actuales están ocupadas. Abrimos una sala nueva (si no superamos el límite 'm') y la metemos al Heap.
"""

import heapq

def planificar_congreso(charlas, m_max_salas):
    # charlas es una lista de tuplas: (id_charla, inicio, duracion)
    
    # 1. Preprocesar las charlas para tener: (inicio, fin_con_descanso, id_charla)
    charlas_procesadas = []
    for id_charla, inicio, duracion in charlas:
        fin_real = inicio + duracion + 15
        charlas_procesadas.append((inicio, fin_real, id_charla))
        
    # 2. Ordenar por horario de inicio (de menor a mayor)
    charlas_procesadas.sort(key=lambda x: x[0])
    
    # Heap de mínmos para las salas. 
    # Guardará tuplas: (tiempo_liberacion, id_sala)
    salas_activas_heap = []
    
    # Diccionario para guardar qué charlas van en qué sala
    asignacion_salas = {}
    contador_salas = 0
    
    for inicio, fin_real, id_charla in charlas_procesadas:
        
        # Verificamos si podemos reusar la sala que se libera más temprano
        # salas_activas_heap[0] nos da el elemento en la cima sin sacarlo
        if salas_activas_heap and salas_activas_heap[0][0] <= inicio:
            # La sala está libre! La sacamos del heap
            tiempo_lib, id_sala = heapq.heappop(salas_activas_heap)
            
            # Asignamos la charla a esta sala
            asignacion_salas[id_sala].append(id_charla)
            
            # Volvemos a meter la sala al heap con su nuevo horario de liberación
            heapq.heappush(salas_activas_heap, (fin_real, id_sala))
            
        else:
            # No hay salas libres o es la primera charla. Necesitamos una sala nueva.
            contador_salas += 1
            if contador_salas > m_max_salas:
                return f"ERROR: Se sobrepasó el máximo de {m_max_salas} salas disponibles."
            
            id_sala_nueva = f"Sala_{contador_salas}"
            asignacion_salas[id_sala_nueva] = [id_charla]
            
            # Metemos la sala nueva al heap
            heapq.heappush(salas_activas_heap, (fin_real, id_sala_nueva))
            
    return asignacion_salas, contador_salas


"""
2. ANÁLISIS DE COMPLEJIDAD

Sea N la cantidad total de charlas.

Complejidad Temporal: O(N log N)
- El preprocesamiento para sumar los 15 minutos toma O(N).
- Ordenar las N charlas por su horario de inicio toma O(N log N).
- Iterar sobre la lista ordenada toma N pasos. En cada paso, podemos hacer operaciones de Heap (heappop y heappush). El tamaño máximo del Heap es N (si todas las charlas se superponen). Las operaciones de Heap cuestan O(log N). Por lo tanto, el ciclo toma
O(N log N).
- Complejidad total: O(N log N) + O(N log N) = O(N log N).

Complejidad Espacial: O(N)
- La lista procesada y el diccionario de asignaciones ocupan O(N).
- El Heap ocupará en el peor de los casos un espacio proporcional a N (o a 'm', la cantidad máxima de salas). 
- Complejidad total: O(N).


3. JUSTIFICACIÓN DE OPTIMALIDAD

Demostraremos que el algoritmo utiliza la cantidad mínima posible de salas utilizando el argumento de la "profundidad" de los intervalos.

Definimos la "profundidad" (d) de un conjunto de intervalos como la cantidad máxima de intervalos que se superponen en un mismo instante de tiempo. Es evidente que, como regla general, cualquier planificación válida necesitará AL MENOS 'd' salas para evitar  superposiciones.

Supongamos que nuestro algoritmo Greedy termina abriendo 'k' salas. El algoritmo únicamente decide abrir la sala número 'k' cuando está procesando una charla 'C' y descubre que no puede ubicarla en ninguna de las 'k-1' salas ya abiertas. Esto significa que en el instante de inicio de la charla 'C', las 'k-1' charlas que están actualmente en las otras salas comenzaron en el mismo instante o ANTES (porque ordenamos por inicio), y todavía NO han terminado. Por lo tanto, en el instante exacto en que comienza la charla 'C', existen exactamente 'k' charlas superponiéndose simultáneamente (las 'k-1' previas + la charla 'C').

Esto demuestra que la profundidad del conjunto de charlas en ese instante es 'k'. Si la profundidad es 'k', matemáticamente es imposible resolver el problema con menos de 'k' salas. Como nuestro algoritmo Greedy utiliza exactamente 'k' salas, queda demostrado que encuentra la solución óptima.
"""

# Bloque de prueba
if __name__ == "__main__":
    # Formato: (Nombre, inicio en minutos, duracion en minutos)
    # Ejemplo: Una charla a las 10:00 (600 mins) que dura 45 mins.
    charlas_prueba = [
        ("Charla_A", 600, 45), # Termina 645. Libre: 660
        ("Charla_B", 630, 30), # Se pisa con A. Necesita Sala 2.
        ("Charla_C", 660, 60), # Entra justo en la Sala 1 que dejó A.
        ("Charla_D", 700, 30)  # Entra en la Sala 2 que dejó B (B se liberaba a las 675).
    ]
    
    m_maximo = 3
    resultado = planificar_congreso(charlas_prueba, m_maximo)
    
    print("--- Ejercicio 4: Asignación de Salas ---")
    if isinstance(resultado, str):
        print(resultado)
    else:
        asignaciones, total_salas = resultado
        print(f"Total de salas utilizadas: {total_salas}")
        for sala, lista_charlas in asignaciones.items():
            print(f"{sala}: {lista_charlas}")