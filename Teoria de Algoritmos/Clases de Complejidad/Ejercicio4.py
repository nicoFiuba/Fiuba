"""
EXPLICACIÓN: para probar que el problema de la Publicidad Estratégica es NP-Completo, tenemos que demostrar dos cosas:

1) Pertenece a NP: dado un certificado (un subconjunto de vértices), podemos verificar en tiempo polinomial que su longitud es a lo sumo k y que cada recorrido de usuario pasa por al menos un vértice del conjunto.

2) Pertenece a NP-Hard: reducimos desde Vertex Cover (VC). Para eso, armamos un grafo web usando los mismos vértices y por cada arista original, creamos un recorrido que va desde el origen al destino. Si la caja negra nos devuelve un conjunto de vértices de tamaño a lo sumo k, entonces ese conjunto cubre todas las aristas del grafo original.

PSEUDOCÓDIGO
"""
def vertex_cover(grafo, k):
    
    grafo_web = GrafoDirigido()
    recorridos_usuarios = []

    for nodo in grafo.nodos():
        grafo_web.agregar_nodo(nodo)

    for origen, destino in grafo.aristas():
        grafo_web.agregar_arista(origen, destino)
        recorridos_usuarios.append([origen, destino])

    return caja_negra(grafo_web, recorridos_usuarios, k)

"""
ANÁLISIS DE COMPLEJIDAD

- Temporal: iterar los nodos toma O(V) y construir el recorrido toma O(E), por lo tanto la complejidad es O(V + E), lo cual es polinomial. Ademas como solo hay una llamada a la caja negra, la reduccion es polinomial, por lo tanto pertenece a NP y por ende queda demostrado formalmente que el problema es NP-Completo.

- Espacial: O(V + E) para construir y almacenar el grafo dirigido y la lista de recorridos.

EJEMPLO
- Entrada Original: grafo G con 3 nodos (A, B, C), 2 aristas (A, B) y (B, C) y queremos saber si hay un Vertex Cover de tamaño K = 1
- Reducción: armamos un grafo G' con nodos A, B, C y definimos 2 recorridos basados en las aristas: Arista1 = [A, B] y Arista2 = [B, C]
- Llamada: caja_negra(G', [Arista1, Arista2], 1)
- Resultado: si la caja devuelve True, entonces el grafo original G tiene un Vertex Cover de tamaño 1.
"""
