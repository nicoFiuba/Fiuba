"""
TEORÍA DE ALGORITMOS - EJERCICIO 15: Viaje Familiar (Dijkstra con Pesos Dinámicos)

1. ESTRATEGIA (Elección Golosa)
El problema busca encontrar el camino de menor tiempo desde un origen a un destino, sabiendo que el peso (tiempo) de las aristas es dinámico y depende del tiempo acumulado al momento de iniciar el trayecto.

Estrategia greedy: Algoritmo de Dijkstra.
1. Utilizamos una Cola de Prioridad (Min-Heap) para ordenar los nodos explorados según su `tiempo_de_llegada`.
2. Iniciamos en el origen con `tiempo_de_llegada = hora_salida`.
3. En cada paso, la decisión localmente óptima es extraer del Min-Heap el nodo al que podemos llegar MÁS TEMPRANO.
4. Para cada vecino de este nodo, calculamos el costo de transitar la ruta: Costo = Tiempo_Base + Trafico(tiempo_llegada_actual).
5. Si `tiempo_llegada_actual + Costo` es menor al mejor tiempo conocido para ese vecino, lo actualizamos y lo metemos al Min-Heap.
"""

import heapq

def calcular_mejor_ruta(grafo, origen, destino, hora_salida, funcion_trafico):
    # grafo: diccionario {nodo: [(vecino, tiempo_base_ruta), ...]}
    # funcion_trafico: funcion(nodo_u, nodo_v, hora_actual) que retorna el delay
    
    # Inicializamos tiempos con infinito
    tiempos = {nodo: float('inf') for nodo in grafo}
    tiempos[origen] = hora_salida
    
    padres = {nodo: None for nodo in grafo}
    visitados = set()
    
    # Min-Heap para elegir siempre el nodo con menor tiempo de llegada: (hora_llegada, nodo)
    min_heap = [(hora_salida, origen)]
    
    while min_heap:
        hora_actual, u = heapq.heappop(min_heap)
        
        # Si ya extrajimos el destino, encontramos el camino óptimo total
        if u == destino:
            break
            
        if u in visitados:
            continue
        visitados.add(u)
        
        for v, tiempo_base in grafo[u]:
            # El "peso" de la arista se calcula en el momento exacto en que llegamos a 'u'
            delay_trafico = funcion_trafico(u, v, hora_actual)
            tiempo_transito = tiempo_base + delay_trafico
            hora_llegada_v = hora_actual + tiempo_transito
            
            # Si llegamos más rápido que antes, actualizamos
            if hora_llegada_v < tiempos[v]:
                tiempos[v] = hora_llegada_v
                padres[v] = u
                heapq.heappush(min_heap, (hora_llegada_v, v))
                
    # Reconstrucción del camino
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = padres[actual]
        
    return tiempos[destino], camino[::-1]

"""
2. ANÁLISIS DE COMPLEJIDAD

Sea V la cantidad de pueblos (nodos) y E la cantidad de rutas (aristas).

Complejidad Temporal: O((V + E) log V)
- El uso del Min-Heap para extraer el pueblo más cercano toma O(log V) por extracción.
- En el peor caso, extraemos V veces y actualizamos las distancias E veces.
- El cálculo de la función de tráfico se asume O(1).
- La complejidad queda dominada por las operaciones del Heap, siendo idéntica al Dijkstra estándar: O((V + E) log V).

Complejidad Espacial: O(V + E)
- El grafo ocupa O(V + E) de memoria.
- El Min-Heap, el diccionario de tiempos, padres y el Set de visitados ocupan O(V).
- Complejidad total: O(V + E).


3. JUSTIFICACIÓN DE OPTIMALIDAD (Inducción y Pesos Positivos)

El algoritmo de Dijkstra garantiza optimalidad basándose en la premisa de que los pesos de las aristas son estrictamente positivos (el tiempo no retrocede).

Supongamos por el absurdo que, al extraer un nodo 'u' del Min-Heap, el `tiempo_llegada(u)` no es el óptimo, y existe un camino alternativo aún no descubierto que llega más temprano a 'u'. Para que ese camino exista, debe pasar por algún nodo 'x' que actualmente está en la frontera (adentro del Min-Heap). 

Sin embargo, como el algoritmo eligió extraer a 'u' antes que a 'x', sabemos obligatoriamente que `tiempo_llegada(u) <= tiempo_llegada(x)`. Dado que viajar de 'x' hacia 'u' consumirá un tiempo estrictamente mayor a cero (tiempo base + tráfico >= 0), el tiempo de llegada por esa ruta alternativa será:
Tiempo_Alternativo = tiempo_llegada(x) + Costo(x -> ... -> u) 
Por lo tanto: Tiempo_Alternativo > tiempo_llegada(x) >= tiempo_llegada(u).

Esto demuestra que es matemáticamente imposible encontrar un camino más rápido a 'u' después de haberlo extraído del Heap. La decisión Greedy es local y globalmente óptima. 
(Nota: Esta demostración asume la condición lógica de no-adelantamiento (FIFO): salir más tarde de un nodo 'A' nunca te hará llegar más temprano a un nodo 'B').
"""

# Bloque de prueba
if __name__ == "__main__":
    # Grafo: {Ciudad: [(Destino, tiempo_base_horas)]}
    mapa = {
        'A': [('B', 2), ('C', 5)],
        'B': [('C', 2), ('D', 4)],
        'C': [('D', 1)],
        'D': []
    }
    
    # Simulamos el tráfico: Si es hora pico (hora >= 10), hay 2 horas de demora.
    def trafico_simulado(origen, destino, hora_actual):
        if hora_actual >= 10:
            return 2 
        return 0
        
    origen_viaje = 'A'
    destino_viaje = 'D'
    hora_salida_viaje = 8 # Salen a las 8 AM
    
    mejor_tiempo, ruta = calcular_mejor_ruta(mapa, origen_viaje, destino_viaje, hora_salida_viaje, trafico_simulado)
    
    print("--- Ejercicio 15: Viaje Familiar ---")
    print(f"Ruta óptima: {' -> '.join(ruta)}")
    print(f"Hora de llegada estimada: {mejor_tiempo} hs")