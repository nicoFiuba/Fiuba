"""
TEORÍA DE ALGORITMOS - EJERCICIO 13: Centro de Distribución Ferroviario (Camino de Máximo Cuello de Botella)

1. ESTRATEGIA (Elección Golosa)
El problema requiere encontrar un camino desde un origen hacia todos los demás nodos tal que se maximice el "cuello de botella" (el valor mínimo de las aristas del camino). Se resuelve con una variante del Algoritmo de Dijkstra.

Estrategia greedy:
1. Mantenemos un registro de la `capacidad_maxima` conocida para llegar a cada estación. Inicializamos el origen en Infinito y el resto en 0.
2. Usamos una Cola de Prioridad (Max-Heap) para procesar siempre la estación que actualmente tiene el mayor cuello de botella garantizado.
3. Al procesar una estación U, evaluamos a sus vecinos V. La capacidad para llegar a V pasando por U será: min(capacidad_para_llegar_a_U, limite_kilos_arista_UV).
4. Si esta nueva capacidad calculada es MAYOR que la capacidad que V tenía registrada, actualizamos a V con este nuevo valor óptimo y lo metemos al Max-Heap.
"""

import heapq

def maximo_cuello_botella(n_estaciones, red_ferroviaria, origen):
    # n_estaciones: cantidad de nodos (0 a n-1)
    # red_ferroviaria: lista de tuplas (estacion_A, estacion_B, limite_kilos)
    
    # 1. Armamos el grafo bidireccional
    grafo = {i: [] for i in range(n_estaciones)}
    for u, v, kilos in red_ferroviaria:
        grafo[u].append((v, kilos))
        grafo[v].append((u, kilos))
        
    # 2. Estructuras de datos
    capacidades = {i: 0 for i in range(n_estaciones)}
    capacidades[origen] = float('inf') # En el origen la capacidad es ilimitada
    
    padres = {i: None for i in range(n_estaciones)} # Para reconstruir el camino
    visitados = set()
    
    # Max-Heap: Python solo tiene Min-Heap nativo (heapq). 
    # TRUCO: Guardamos los valores multiplicados por -1 para simular un Max-Heap.
    # Formato tupla: (-capacidad, nodo)
    max_heap = [(-float('inf'), origen)]
    
    # 3. Proceso Greedy (Dijkstra modificado)
    while max_heap:
        cap_negativa, u = heapq.heappop(max_heap)
        cap_actual_u = -cap_negativa
        
        # Si ya lo visitamos definitivamente, lo ignoramos
        if u in visitados:
            continue
        visitados.add(u)
        
        # Analizamos vecinos
        for v, limite_via in grafo[u]:
            # El cuello de botella del camino hacia V será el "caño más estrecho" 
            # entre lo que traíamos hasta U y la vía directa U-V.
            cuello_botella_posible = min(cap_actual_u, limite_via)
            
            # Si encontramos una forma de mandar MÁS kilos a V, actualizamos
            if cuello_botella_posible > capacidades[v]:
                capacidades[v] = cuello_botella_posible
                padres[v] = u
                heapq.heappush(max_heap, (-cuello_botella_posible, v))
                
    return capacidades, padres

def reconstruir_camino(padres, destino):
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = padres[actual]
    return camino[::-1] # Invertimos para que quede Origen -> Destino

"""
2. ANÁLISIS DE COMPLEJIDAD

Sea V la cantidad de estaciones (nodos) y E la cantidad de vías (aristas).

Complejidad Temporal: O((V + E) log V)
- La inicialización del grafo toma O(V + E).
- Cada vértice se extrae del Heap como máximo una vez: O(V log V).
- Cada arista se evalúa como máximo dos veces (una de ida y una de vuelta). Si la capacidad mejora, hacemos un `heappush` que toma O(log V). En el peor caso esto ocurre E veces, tomando O(E log V).
- La complejidad total queda idéntica a la de Dijkstra clásico: O((V + E) log V).

Complejidad Espacial: O(V + E)
- La lista de adyacencia (grafo) ocupa O(V + E).
- El Heap, el conjunto de visitados, el diccionario de capacidades y padres ocupan O(V).
- Complejidad total: O(V + E).


3. JUSTIFICACIÓN DE OPTIMALIDAD (Inducción / Paso Seguro)

Demostramos que cuando el algoritmo extrae un nodo 'u' del Max-Heap, la `capacidad_actual_u` es verdaderamente el máximo cuello de botella posible desde el origen.

Supongamos por el absurdo que existiera un camino alternativo hacia 'u' que permita un cuello de botella ESTRICTAMENTE MAYOR al que calculó nuestro algoritmo. Para que este camino alternativo exista, en algún punto debe abandonar el conjunto de nodos ya `visitados` y cruzar por un nodo 'x' que aún está en el Max-Heap (no procesado).

Como nuestro algoritmo Greedy utiliza un Max-Heap, siempre extrae el nodo con la mayor capacidad conocida. Si extrajo a 'u' antes que a 'x', significa obligatoriamente que:
Capacidad_Conocida(u) >= Capacidad_Conocida(x).

Cualquier camino que pase a través de 'x' hacia 'u' tendrá su cuello de botella limitado, como máximo, por la capacidad para llegar al propio 'x'. Por lo tanto, el cuello de botella final de ese camino alternativo será:
Cuello_Alternativo <= Capacidad_Conocida(x) <= Capacidad_Conocida(u).

Esto demuestra que es matemáticamente imposible que un camino que pase por 'x' ofrezca una capacidad mayor a la que ya descubrimos para 'u'. La decisión Greedy de fijar el valor de 'u' al extraerlo es segura e irrevocable, garantizando la optimalidad global.
"""

# Bloque de prueba
if __name__ == "__main__":
    n = 6
    # (origen, destino, max_kilos_soportados)
    red = [
        (0, 1, 10), # Ruta directa a 1, soporta 10k
        (0, 2, 50), # Ruta a 2, muy gruesa (50k)
        (2, 1, 40), # Ruta de 2 a 1, soporta 40k
        (1, 3, 20),
        (2, 4, 15),
        (3, 5, 30),
        (4, 5, 60)
    ]
    centro_distribucion = 0
    
    caps, pads = maximo_cuello_botella(n, red, centro_distribucion)
    
    print("--- Ejercicio 13: Distribución Ferroviaria ---")
    print(f"Desde el Centro de Distribución (Nodo {centro_distribucion}):\n")
    
    for estacion in range(1, n):
        camino = reconstruir_camino(pads, estacion)
        print(f"Hacia la Estación {estacion}:")
        print(f"  - Kilos máximos posibles por viaje: {caps[estacion]} kg")
        print(f"  - Ruta elegida: {' -> '.join(map(str, camino))}\n")