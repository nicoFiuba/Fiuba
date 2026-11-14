"""

EXPLICACIÓN: la estrategia consiste en ordenar las aristas de mayor a menor según su peso y, en cada iteración, evaluar la arista más pesada para decidir si se la descarta o no. Esta estrategia es Greedy porque realiza una elección:
    - Localmente óptima porque en cada iteración opta por evaluar a la arista más pesada
    - Factible ya que cumple con las restricciones del problema
    - Irrevocable ya que una vez tomada la decisión, no permite ser removida en posteriores elecciones del algoritmo.

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

EJEMPLO
- Entrada: Grafo triangular con nodos A, B, C. Aristas: (A,B) peso 5, (B,C) peso 3, (A,C) peso 1.
- Ejecución:
    - Ordenamos descendentemente: (A,B), (B,C), (A,C).
    - Evaluamos (A,B) peso 5: la removemos. El grafo sigue conexo (A llega a B vía C). Se descarta definitivamente.
    - Evaluamos (B,C) y (A,C): al intentar remover cualquiera de las dos, un nodo queda aislado (no conexo), por lo que se mantienen en el grafo.
- Resultado: MST compuesto por las aristas (B,C) y (A,C) con peso total 4.
"""
