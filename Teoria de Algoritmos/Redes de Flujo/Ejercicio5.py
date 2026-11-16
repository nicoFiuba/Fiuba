"""

EXPLICACIÓN Y MODELADO: estamos ante un problema de corte minimo. Para ello, vamos a basarnos en el Teorema de Menger, es decir el flujo máximo es igual al corte mínimo. 

- Caso 1 (Cables de datos):
    - NODOS: un nodo para cada organismo
    - ARISTAS: son los cables de datos, y como usamos el teorema de Menger, la capacidad de estos es de 1.

- Caso 2 (Organismos):
    - NODOS: dos nodos para cada organismo (uno de entrada y otro de salida)
    - ARISTAS:
        entrada_nodo -> salida_nodo (capacidad 1)
        salida_nodo -> entrada_vecino (capacidad infinita)

PSEUDOCÓDIGO
"""
def analizar_conectividad(organismos, cables):

    red_cables = GrafoDirigido()
    
    for origen, destino in cables:
        red_cables.agregar_arista(origen, destino, 1)
        red_cables.agregar_arista(destino, origen, 1)

    cortes_minimos_cables = float('inf')
    origen = organismos[0]
    for destino in organismos[1:]:
        flujo_maximo, _ = ford_fulkerson(red_cables, origen, destino)
        cortes_minimos_cables = min(cortes_minimos_cables, flujo_maximo)

    red_organismos = GrafoDirigido()

    for organismo in organismos:
        red_organismos.agregar_arista(("entrada", organismo), ("salida", organismo), 1)

    for origen, destino in cables:
        red_organismos.agregar_arista(("salida", origen), ("entrada", destino), float('inf'))
        red_organismos.agregar_arista(("salida", destino), ("entrada", origen), float('inf'))

    cortes_minimos_organismos = float('inf')
    origen = organismos[0]
    for destino in organismos[1:]:
        flujo_maximo, _ = ford_fulkerson(red_organismos, ("salida", origen), ("entrada", destino))
        cortes_minimos_organismos = min(cortes_minimos_organismos, flujo_maximo)

    return cortes_minimos_cables, cortes_minimos_organismos

"""
ANÁLISIS DE COMPLEJIDAD

- Temporal:
    - Armar cada red toma O(N + C) donde N es el número de organismos y C es el número de cables.
    - V' tiene 2N (entrada y salida) + N nodos, por lo tanto, O(N)
    - E' tiene N + 2C aristas, por lo tanto, O(N + C)
    - Al usar Edmonds-Karp, la complejidad teorica es O(V' * E'^2), aunque en este caso como todas las capacidades son 1, la complejidad se reduce a O(E' * Raiz(V')) por lo tanto trayendolo a nuestra red, nos queda O((N + C) * Raiz(N))
    - Además, como calculamos el flujo maximo para N - 1 organismos, la complejidad final es O((N + C) * Raiz(N) * N)

- Espacial: O(V' + E') para almacenar el grafo y las redes residuales, por lo tanto O(N + C)

EJEMPLO

Organismos = ['A', 'B', 'C', 'D']
Cables = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]

- Caso 1 (Cables): Origen = 'A', Destino = 'C'
Caminos disjuntos: 
1) A -> B -> C (Flujo = 1)
2) A -> D -> C (Flujo = 1)
Flujo máximo = 2. Al evaluar todos los destinos, el mínimo global es 2.

- Caso 2 (Organismos): Origen = 'A' (salida_A), Destino = 'C' (entrada_C)
Caminos por nodos desdoblados:
1) salida_A -> entrada_B -> salida_B -> entrada_C (cuello de botella: B)
2) salida_A -> entrada_D -> salida_D -> entrada_C (cuello de botella: D)
Flujo máximo = 2. Al evaluar todos los destinos, el mínimo global es 2.

Resultado: (2, 2). Se deben romper mínimo 2 cables o 2 organismos para desconectar la red.

"""
