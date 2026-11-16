"""

EXPLICACIÓN: para probar que el problema es NP-Completo, tenemos que demostrar dos cosas:

1) Pertenece a NP: dado un certificado (un subconjunto de vértices), podemos verificar en tiempo polinomial que su longitud es al menos k y no hay dos clientes que compren el mismo producto.

2) Pertenece a NP-Hard: reducimos desde Conjunto Independiente (IS). Para eso, armamos una matriz de clientes y productos, donde cada cliente es un nodo y cada producto es una arista.

PSEUDOCÓDIGO
"""

def conjunto_independiente(grafo, k):
    
    clientes = grafo.nodos()
    productos = grafo.aristas()

    matriz = armar_matriz(clientes, productos)

    for cliente in clientes:
        for producto in productos:
            if cliente in producto:
                matriz[cliente][producto] = 1

    return caja_negra(matriz, k)

"""
ANÁLISIS DE COMPLEJIDAD

- Temporal: armar la matriz requiere iterar sobre todos productos de cada cliente, lo que toma O(V * E), lo cual es polinomial. Ademas como solo hay una llamada a la caja negra, la reduccion es polinomial, por lo tanto pertenece a NP y por ende queda demostrado formalmente que el problema es NP-Completo.

- Espacial: O(V * E) para construir y almacenar la matriz.

EJEMPLO
- Entrada Original: grafo G con 3 nodos (A, B, C), 2 aristas (A, B) y (B, C) y queremos saber si hay un IS de tamaño K = 2
- Reducción: armamos una matriz donde A compra (A, B), B compra (A, B) y (B, C), y C compra (B, C)
- Llamada: caja_negra(matriz, 2)
- Resultado: si la caja devuelve True, significa que el grafo original G tiene un Conjunto Independiente de tamaño K = 2
"""
