"""

EXPLICACIÓN Y MODELADO: estamos ante un problema corte minimo. Para ello, vamos a modelar el problema como un grafo dirigido, en donde:

- NODOS: una fuente S, un sumidero T, un nodo para subestacion

- ARISTAS: son los cables de alta tension, y como usamos el teorema de Menger, la capacidad de estos es de 1.

PSEUDOCÓDIGO
"""

def analizar_robustez(red, generadora, capital):

    for origen, destino in red.cables:
        red.asignar_capacidad(origen, destino, 1)

    flujo_maximo, red_residual = ford_fulkerson(red, generadora, capital)

    nodos_alcanzables = bfs(red_residual, generadora)
    cables_a_cortar = []

    for nodo_actual in nodos_alcanzables:
        for vecino in red.vecinos(nodo_actual):
            if vecino not in nodos_alcanzables:
                cables_a_cortar.append((nodo_actual, vecino))

    return flujo_maximo, cables_a_cortar

"""
ANÁLISIS DE COMPLEJIDAD

- Temporal:
    - Asignar la capacidades toma O(C) donde C son los cables.
    - V' tiene S nodos, por lo tanto, O(S)
    - E' tiene C aristas, por lo tanto, O(C)
    - El recorrido BFS toma O(V' + E'), por lo tanto trayendolo a nuestra red, nos queda O(S + C)
    - Al usar Edmonds-Karp, la complejidad teorica es O(V' * E'^2), aunque en este caso como todas las capacidades son 1, la complejidad se reduce a O(E' * Raiz(V')) por lo tanto trayendolo a nuestra red, nos queda O(C * Raiz(S))

- Espacial: O(V' + E') para almacenar el grafo y la red residual, por lo tanto O(S + C)

EJEMPLO

Nodos = ['Generadora', 'A', 'B', 'Capital']
Cables = [('Generadora', 'A'), ('Generadora', 'B'), ('A', 'Capital'), ('B', 'Capital')]

Red
'Generadora' -> 'A' (capacidad 1)
'Generadora' -> 'B' (capacidad 1)
'A' -> 'Capital' (capacidad 1)
'B' -> 'Capital' (capacidad 1)

Caminos
1) 'Generadora' -> 'A' -> 'Capital' (Flujo = 1)
2) 'Generadora' -> 'B' -> 'Capital' (Flujo = 1)

Como hay dos caminos que van de la generadora al capital, el flujo maximo es 2. Para cortar el flujo, debemos cortar los dos cables que van de la generadora a A y B ya que si bien podriamos cortar los cables que van de A y B se acostumbra a cortar los mas cercanos a la fuente. Por lo tanto, los cables a cortar son [('Generadora', 'A'), ('Generadora', 'B')].
"""
