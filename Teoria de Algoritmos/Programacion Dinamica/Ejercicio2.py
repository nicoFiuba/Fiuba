"""

EXPLICACIÓN: voy a usar un arreglo unidimensional OPT de tamaño V, donde la celda OPT[v] guardará el peso máximo desde el origen "s" hasta el vértice "v". Como es un grafo dirigido acíclico, primero ordenamos los nodos topológicamente, luego iteramos los nodos en ese orden y nos fijamos que es mejor: mantener el peso máximo que ya tenía el vecino, o actualizarlo sumando el peso de la arista.

RELACION DE RECURRENCIA:

- Caso base: OPT[s] = 0, ir desde el origen hasta el origen no tiene peso.

- Caso recursivo: Si es vecino => OPT[vecino] = max(OPT[vecino], OPT[u] + peso(u, vecino))

PSEUDOCÓDIGO
"""

def camino_maximo(grafo, origen, destino):
    orden = orden_topologico(grafo)

    OPT = [float('-inf')] * len(grafo.nodos)
    OPT[origen] = 0

    for u in orden:
        if OPT[u] != float('-inf'):
            for vecino, peso in grafo.adyacentes(u):
                OPT[vecino] = max(OPT[vecino], OPT[u] + peso)

    return OPT[destino]

""" 
ANÁLISIS DE COMPLEJIDAD

- Temporal: ordenar y recorrer el grafo y sus adyacentes toma O(V + E). Por lo tanto, la complejidad es O(V + E).

- Espacial: O(V) para almacenar OPT y  el orden.

EJEMPLO: supongamos un DAC con 4 nodos (Origen, A, B, Destino)
y las siguientes aristas con pesos: 
Origen -> A = 3,
Origen -> B = 2,
A -> B = 4,
A -> Destino = 1,
B -> Destino = 5

OPT = [0, -inf, -inf, -inf]
OPT[A] = max(OPT[vecino], OPT[u] + peso) = max(OPT[A], OPT[Origen] + 3) = max(-inf, 0 + 3) = max(-inf, 3) = 3
OPT[B] = max(OPT[vecino], OPT[u] + peso) = max(OPT[B], OPT[Origen] + 2) = max(-inf, 0 + 2) = max(-inf, 2) = 2
OPT[B] = max(OPT[vecino], OPT[u] + peso) = max(OPT[B], OPT[A] + 4) = max(2, 3 + 4) = max(2, 7) = 7
OPT[Destino] = max(OPT[vecino], OPT[u] + peso) = max(OPT[Destino], OPT[A] + 1) = max(-inf, 3 + 1) = max(-inf, 4) = 4
OPT[Destino] = max(OPT[vecino], OPT[u] + peso) = max(OPT[Destino], OPT[B] + 5) = max(4, 7 + 5) = max(4, 12) = 12

Como Destino es el último nodo, el resultado final es OPT[Destino] = 12, que es el peso máximo desde Origen hasta Destino.

"""
