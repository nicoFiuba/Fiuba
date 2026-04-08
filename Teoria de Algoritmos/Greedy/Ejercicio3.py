"""
TEORÍA DE ALGORITMOS - EJERCICIO 3: Dijkstra y Árboles Recubridores

ENUNCIADO: 
Sea C el conjunto de ejes seleccionados por el algoritmo de Dijkstra para un 
grafo G=(V,E) pesado no dirigido.


a) C corresponde a un árbol recubridor.
Respuesta: VERDADERO (asumiendo que el grafo G original es conexo).
Justificación: el algoritmo de Dijkstra, partiendo desde un nodo origen 's', visita todos los vértices del grafo buscando el camino de menor costo hacia cada uno de ellos. Para registrar estos caminos, el algoritmo guarda para cada vértice (distinto del origen) un único nodo "predecesor" o "padre". Dado un grafo conexo de V vértices, este proceso seleccionará exactamente V-1 aristas (una por cada vértice destino que se conecta a su predecesor). Un subgrafo conexo que contiene a todos los V vértices del grafo original y tiene exactamente V-1 aristas no puede contener ciclos. Por definición matemática, un grafo conexo, sin ciclos y que incluye a todos los vértices es un árbol recubridor (específicamente, se lo denomina Árbol de Caminos Mínimos o Shortest Path Tree).

b) C corresponde a un árbol recubridor mínimo.
Respuesta: FALSO.
Justificación por contraejemplo: para demostrar que el árbol de caminos mínimos de Dijkstra no siempre es un Árbol Recubridor Mínimo (MST), proponemos el siguiente contraejemplo con un grafo G de 3 vértices: V = {A, B, C}. Definimos los pesos de las aristas de la siguiente manera:
- Arista (A, B) con peso 5.
- Arista (A, C) con peso 5.
- Arista (B, C) con peso 1.

1. Ejecución de Dijkstra (Árbol de Caminos Mínimos): si tomamos como nodo origen al vértice A, el algoritmo de Dijkstra buscará las rutas más cortas hacia B y C:
- El camino más corto desde A hacia B es la arista directa (A, B) con un costo de 5.
- El camino más corto desde A hacia C es la arista directa (A, C) con un costo de 5.
(Nota: Si intentara ir a C pasando por B, el costo sería 5 + 1 = 6, que es mayor).
El conjunto C de aristas seleccionadas por Dijkstra es: {(A, B), (A, C)}.
El peso total de este árbol recubridor es 5 + 5 = 10.

2. Ejecución de Kruskal / Prim (Árbol Recubridor Mínimo): si queremos encontrar el MST real del grafo, debemos conectar todos los nodos minimizando el peso total:
- Seleccionamos la arista más barata de todo el grafo: (B, C) con peso 1.
- Para conectar el nodo A sin formar ciclos, elegimos una de las otras dos aristas: por ejemplo, (A, B) con peso 5.
Las aristas del MST son: {(B, C), (A, B)}.
El peso total de este árbol recubridor mínimo es 1 + 5 = 6.

Conclusión: como el peso del árbol generado por Dijkstra (10) es estrictamente mayor al peso del Árbol Recubridor Mínimo (6) para el mismo grafo, queda demostrado que el conjunto C seleccionado por Dijkstra NO corresponde obligatoriamente a un árbol recubridor mínimo.
"""

def imprimir_contraejemplo():
    print("--- Ejercicio 3: Contraejemplo Dijkstra vs MST ---")
    print("Grafo: Triángulo con vértices A, B, C")
    print("Pesos: A-B (5), A-C (5), B-C (1)\n")

    # Simulación del resultado de Dijkstra desde el nodo A
    aristas_dijkstra = [("A", "B", 5), ("A", "C", 5)]
    costo_dijkstra = sum(peso for origen, destino, peso in aristas_dijkstra)

    print("1. Resultado de Dijkstra (partiendo desde A):")
    print(f"   Aristas seleccionadas: {aristas_dijkstra}")
    print(f"   Costo Total del Árbol: {costo_dijkstra}\n")

    # Simulación del resultado de Kruskal/Prim
    aristas_mst = [("B", "C", 1), ("A", "B", 5)]
    costo_mst = sum(peso for origen, destino, peso in aristas_mst)

    print("2. Resultado del Árbol Recubridor Mínimo (Kruskal/Prim):")
    print(f"   Aristas seleccionadas: {aristas_mst}")
    print(f"   Costo Total del Árbol: {costo_mst}\n")

    print("CONCLUSIÓN:")
    print(f"Como {costo_dijkstra} > {costo_mst}, el árbol de Dijkstra NO es un MST.")


if __name__ == "__main__":
    imprimir_contraejemplo()
