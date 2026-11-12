""" 
EXPLICACIÓN: para probar que el problema es un NP-Completo, tenemos que demostrar dos cosas:

1) Pertenece a NP: dado un certificado (un subconjunto de vértices), podemos verificar en tiempo polinomial que su longitud es al menos k y que entre ellos no existen aristas ni caminos de tamaño 2.

2) Pertenece a NP-Hard: reducimos desde el Conjunto Independiente (IS). Para eso armamos un nuevo grafo G', en el cual subdividimos a cada arista original agregando un nuevo nodo en el medio.

PSEUDOCÓDIGO
"""

def conjunto_independiente(grafo, k):
    
    nuevo_grafo = GrafoNoDirigido()

    for nodo in grafo.nodos():
        nuevo_grafo.agregar_nodo(nodo)

    for origen, destino in grafo.aristas():
        nodo_intermedio = (origen, destino)

        nuevo_grafo.agregar_nodo(nodo_intermedio)
        nuevo_grafo.agregar_arista(origen, nodo_intermedio)
        nuevo_grafo.agregar_arista(nodo_intermedio, destino)

    return caja_negra(nuevo_grafo, k)

"""
ANÁLISIS DE COMPLEJIDAD

- Temporal: copiar los nodos toma O(V) y subdividir las aristas O(E), por lo tanto la complejidad es O(V + E), lo cual es polinomial. Ademas como solo hay una llamada a la caja negra, la reduccion es polinomial y por ultimo como CFI pertenece a NP, queda demostrado formalmente que el problema es NP-Completo.

- Espacial: O(V + E) para construir y almacenar el nuevo grafo.

EJEMPLO
- Entrada Original: grafo G con 2 nodos (A, B) conectados por una arista y buscamos un Independent Set (IS) de tamaño K
- Reducción: armamos G' copiando a G y agregamos un nodo intermedio en cada arista => (A, M) y (M, B)
- Llamada: caja_negra(G', K)
- Resultado: si la caja negra de Conjuntos Fuertemente Independientes devuelve True para G', significa que el grafo original G tiene un Conjunto Independiente de tamaño K.
"""
