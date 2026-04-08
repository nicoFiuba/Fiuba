"""
TEORÍA DE ALGORITMOS - EJERCICIO 2: Estrategia Destructiva para MST (Reverse-Delete)

1. ESTRATEGIA Y RESOLUCIÓN
El enunciado propone un algoritmo "destructivo" (inverso a Kruskal). 
- ¿Corresponde a un algoritmo óptimo?
SÍ, es un algoritmo óptimo y generará correctamente un Árbol Recubridor Mínimo (MST).

-¿Con qué estructuras implementarlo eficientemente?
Para encontrar ciclos y aristas pesadas de forma eficiente, la mejor estrategia no es buscar ciclos ciegamente en el grafo, sino ordenar TODAS las aristas de mayor a menor peso. Luego, iteramos sobre esta lista intentando eliminar cada arista. Para saber si esa arista formaba parte de un ciclo (y por ende, se puede borrar) o si era vital para mantener el grafo unido (un "puente"), utilizamos un recorrido estándar como BFS o DFS (Búsqueda en Anchura o Profundidad) para verificar la conectividad.
"""


def reverse_delete_mst(nodos, aristas):

    # nodos: lista de nodos [1, 2, 3...]
    # aristas: lista de tuplas (nodo_origen, nodo_destino, peso)

    # 1. Ordenar las aristas de MAYOR a MENOR peso
    aristas.sort(key=lambda x: x[2], reverse=True)

    # Iniciamos nuestro MST con el grafo completo
    mst = aristas.copy()

    for arista in aristas:

        # Intentamos remover la arista más pesada actual
        mst.remove(arista)

        # Verificamos si el grafo sigue siendo conexo sin esta arista
        # (Usaríamos una función auxiliar BFS o DFS)
        if not es_conexo(nodos, mst):
            # Si se desconectó, significa que no había un ciclo que ofreciera un camino alternativo. Esta arista es puente. La volvemos a agregar.
            mst.append(arista)

    return mst


# Función auxiliar abstracta (BFS/DFS) para revisar conectividad
def es_conexo(nodos, aristas_actuales):
    # Retorna True si desde un nodo inicial se pueden visitar todos los demás
    pass


"""
2. ANÁLISIS DE COMPLEJIDAD

Sea V la cantidad de vértices y E la cantidad de aristas.

Complejidad Temporal: O(E^2)
- Ordenar las aristas de mayor a menor peso toma O(E log E).
- Iteramos sobre las E aristas. En cada iteración, llamamos a la función `es_conexo`.
- La función `es_conexo` implementada con un BFS o DFS toma tiempo O(V + E).
- Por lo tanto, el ciclo for tiene una complejidad de O(E * (V + E)). 
- Como en un grafo conexo V <= E + 1, la complejidad domina en O(E^2).
(Nota: Existen estructuras avanzadas como Link-Cut Trees para optimizar esto, 
pero con estructuras estándar como DFS/BFS, esta es la cota esperada).

Complejidad Espacial: O(V + E)
- Guardamos la lista de aristas originales y la lista del MST actual, O(E).
- El recorrido BFS/DFS para verificar conectividad requerirá armar listas de adyacencia y estructuras auxiliares (visitados, colas/pilas) que toman O(V + E).
- La complejidad espacial total es O(V + E).


3. JUSTIFICACIÓN DE OPTIMALIDAD (Propiedad del Ciclo)

La correctitud y optimalidad de este algoritmo se basan matemáticamente en la "Propiedad del Ciclo" de los árboles recubridores mínimos, la cual establece que:

"Para cualquier ciclo C en un grafo G, la arista de mayor peso en ese ciclo NUNCA pertenecerá al MST".

Demostración por el absurdo: supongamos que armamos un árbol recubridor T que SÍ incluye la arista más pesada (llamémosla Ep) de un ciclo C. Si quitamos Ep de T, el árbol se divide en dos componentes desconectadas. Sin embargo, como Ep pertenecía a un ciclo C original, existe obligatoriamente al menos otra arista alternativa en ese ciclo (llamémosla El) que puede volver a unir estas dos mitades. Como Ep era estrictamente la arista más pesada del ciclo, sabemos que peso(El) < peso(Ep).  Si reemplazamos Ep por El, el grafo vuelve a ser un árbol conexo, pero su peso total ahora es estrictamente menor. Por lo tanto, T no podía ser un Árbol Recubridor Mínimo.

Conclusión: al ordenar de mayor a menor, el algoritmo evalúa primero las aristas más pesadas de todo el grafo. Si al borrar una de estas aristas el grafo no se desconecta, es la prueba de que existía un camino alternativo (es decir, la arista formaba parte de un ciclo). Por la Propiedad del Ciclo, es 100% seguro eliminarla. Al finalizar, nos queda un árbol conexo sin ciclos, que obligatoriamente es el MST.
"""
