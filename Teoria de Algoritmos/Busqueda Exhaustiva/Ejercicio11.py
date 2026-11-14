"""

EXPLICACIÓN: la estrategia consiste en aplicar una restricción y si no la cumple, volvemos para atrás y buscamos otra alternativa.

ESTRUCTURA DEL ÁRBOL DE ESTADOS

- NODO: nodo actual

- RAMAS: pintamos el nodo de un color dentro del rango de colores disponibles

- HOJA: evaluamos todo el grafo.

- PODA (Por factibilidad): si el nodo adyacente tiene el mismo color

PSEUDOCÓDIGO
"""

def backtracking(grafo, c, nodo_actual):

    if nodo_actual == len(grafo.nodos):
        return 1

    soluciones = 0

    for color in range(c):
        if color_valido(grafo, nodo_actual, color):
            grafo.nodos[nodo_actual].color = color
            soluciones += backtracking(grafo, c, nodo_actual + 1)
            grafo.nodos[nodo_actual].color = -1

    return soluciones

"""
ANÁLISIS DE COMPLEJIDAD

- TEMPORAL: en el peor de los casos, el algoritmo explora "k" colores para pintar el nodo, lo que toma O(K^N)

- ESPACIAL: O(N) ya que es el call stack de la recursión

EJEMPLO
- Entrada: grafo de 2 vértices (A y B) conectados por una arista. Límite de colores = 2
- Ejecución:
    - Si usamos un solo color, pongamosle blanco, entonces:
        Pintamos A de blanco. Para B solo está disponible el blanco, pero es adyacente. Se poda la rama. Soluciones = 0
    - Si usamos dos colores, blanco y rojo, entonces: 
        - Rama 1: pintamos A de blanco. Para B podemos usar blanco y rojo pero como blanco es adyacente, pintamos de rojo -> Llega a hoja. (1 solución)
        - Rama 2: pintamos A de rojo. Para B podemos usar blanco y rojo pero como rojo es adyacente, pintamos de blanco -> Llega a hoja. (Sumamos otra, total: 2 soluciones)
- Resultado: Retorna el arreglo [0, 2].
"""
