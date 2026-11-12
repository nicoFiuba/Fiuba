"""

EXPLICACIÓN: para probar que el problema es un NP-Completo, tenemos que demostrar dos cosas:

1) Pertenece a NP: dado un certificado, podemos verificar en tiempo polinomial que su longitud es al menos k, que use aristas válidas del grafo y que no repita vértices.

2) Pertenece a NP-Hard: reducimos desde el camino Hamiltoniano (lo pide asi el enunciado) que ya sabemos que es un NP-Completo. Como el camino Hamiltoniano busca un camino simple que visite todos los nodos, su longitud es |V| - 1 => usamos el mismo grafo y decimos que K = |V| - 1

PSEUDOCÓDIGO
"""

def existe_camino_hamiltoniano(grafo):
    k = len(grafo.nodos()) - 1
    return existe_camino_mas_largo(grafo, k)

"""
ANÁLISIS DE COMPLEJIDAD
- Temporal: la transformación toma O(1) ya que solo calculamos k = |V| - 1. Traducir la respuesta de la única llamada a la caja negra toma O(1). Como la reducción toma tiempo estrictamente polinomial y CML pertenece a NP, queda demostrado formalmente que el problema es NP-Completo.

- Espacial: O(1) ya que no se crean estructuras adicionales.

EJEMPLO
- Entrada Original: grafo G con 4 nodos y queremos saber si tiene Camino Hamiltoniano
- Reducción: K = |V| - 1 = 4 - 1 = 3.
- Llamada: existe_camino_mas_largo(G, 3)
- Resultado: si la caja negra devuelve True, significa que existe un camino simple de longitud 3 que visita los 4 nodos (Camino Hamiltoniano).
"""
