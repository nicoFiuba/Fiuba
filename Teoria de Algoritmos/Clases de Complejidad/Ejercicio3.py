""" 
EXPLICACIÓN: para probar que el problema es un NP-Completo, tenemos que demostrar dos cosas:

1) Pertenece a NP: dado un certificado (un subconjunto de vértices), podemos verificar en tiempo polinomial que su longitud es al menos k y que no hay caminos de tamaño 2.

2) Pertenece a NP-Hard: reducimos desde el Conjunto Independiente (IS). Para eso armamos un nuevo grafo G', en el cual subdividimos a cada arista original agregando un nuevo nodo en el medio.

PSEUDOCÓDIGO
"""

def existe_conjunto_independiente(grafo, k):
    
    nuevo_grafo = GrafoNoDirigido()

    for nodo in grafo.nodos():
        nuevo_grafo.agregar_nodo(nodo)

    for origen, destino in grafo.aristas():
        nodo_intermedio = (origen, destino)

        nuevo_grafo.agregar_nodo(nodo_intermedio)
        nuevo_grafo.agregar_arista(origen, nodo_intermedio)
        nuevo_grafo.agregar_arista(nodo_intermedio, destino)

    return caja_negra_CFI(nuevo_grafo, k)

"""
ANÁLISIS DE COMPLEJIDAD

- Temporal: copiar los nodos toma O(V) y subdividir las aristas O(E), por lo tanto la complejidad es O(V + E), lo cual es polinomial. Ademas como solo hay una llamada a la caja negra, la reduccion es polinomial y por ultimo como CFI pertenece a NP, queda demostrado formalmente que el problema es NP-Completo.

- Espacial: O(V + E) para construir y almacenar el nuevo grafo.

"""
