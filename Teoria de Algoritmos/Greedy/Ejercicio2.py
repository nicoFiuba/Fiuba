"""

EXPLICACIÓN: la estrategia consiste en ordenar las aristas de mayor a menor según su peso. Esta estrategia es Greedy porque en cada iteración opta por evaluar a la arista más pesada, realizando una elección que es localmente óptima, factible (si al eliminarla, no se desconecta) e irrevocable (una vez eliminada, no se considera para posteriores elecciones del algoritmo).

PSEUDOCÓDIGO
"""

def mst_reverse_delete(grafo):

    aristas_ordenadas = sorted(grafo.aristas, key=lambda x: x.peso, reverse=True)

    for arista in aristas_ordenadas:
        grafo.remover_arista(arista)

        if no_es_conexo(grafo):
            grafo.agregar_arista(arista)

    return grafo

"""
ANÁLISIS DE COMPLEJIDAD

- TEMPORAL: ordenar las aristas toma O(E * log(E)) y recorrerlas toma O(V + E). Por lo tanto, la complejidad es O(E * log(E) + E * (V + E)).

- ESPACIAL: O(V + E) para almacenar el grafo.

ANÁLISIS DE OPTIMALIDAD: se demuestra mediante el absurdo, ya que si la arista más pesada del ciclo analizado formara parte del MST, significa que podríamos reemplazarla por otra más barata para abaratar costos. Por lo tanto, al eliminar siempre la arista más pesada sin que se rompa la conexión, nos asegura que vamos a alcanzar la solución óptima global.
"""
