"""

EXPLICACIÓN Y MODELADO: estamos ante un problema de flujo maximo con capacidades en los nodos. Para poder resolverlo, vamos a modelar el problema como un grafo dirigido, en donde:

- NODOS: una fuente S, un sumidero T, y a cada nodo intermedio lo dividimos en dos, entrada y salida del nodo

- ARISTAS: 
entrada_planeta -> salida_planeta (capacidad = limite) porque el puesto de control es el que controla eso.
salida_planeta -> entrada_nuevo_planeta (capacidad = infinita) porque las rutas no tienen limite de capacidad

PSEUDOCÓDIGO
"""

def max_naves_ayuda(planetas, rutas, origen, destino):

    grafo = GrafoDirigido()

    for planeta, limite in planetas:
        grafo.agregar_arista(('entrada_', planeta), ('salida_', planeta), limite)

    for u, v in rutas:
        grafo.agregar_arista(('salida_', u), ('entrada_', v), float('inf'))

    flujo_maximo, grafo_residual = ford_fulkerson(grafo, ('salida_', origen), ('entrada_', destino))

    return flujo_maximo

"""
ANÁLISIS DE COMPLEJIDAD

- Temporal:
    - Armar la red toma O(P + R) donde P es el número de planetas y R es el número de rutas.
    - V' tiene 2 (entrada y salida)*P nodos, por lo tanto, O(P)
    - E' tiene P (limite) + R (rutas) aristas, por lo tanto, O(P + R)
    - Al usar Edmonds-Karp, la complejidad teorica es O(V' * E'^2), por lo tanto trayendolo a nuestra red, nos queda O(P * (P + R)²)

- Espacial: O(V' + E') para almacenar el grafo, por lo tanto O(P + R)

EJEMPLO

Planetas = [('P1', limite = 2)]
Rutas = [('P0', 'P1'), ('P1', 'PF')]
Origen = 'P0'
Destino = 'PF'

Red
('entrada_', 'P0') -> ('salida_', 'P0') con capacidad infinita
('entrada_', 'P1') -> ('salida_', 'P1') con capacidad 2
('entrada_', 'PF') -> ('salida_', 'PF') con capacidad infinita
('salida_', 'P0') -> ('entrada_', 'P1') con capacidad infinita
('salida_', 'P1') -> ('entrada_', 'PF') con capacidad infinita

Camino
('salida_', 'P0') -> ('entrada_', 'P1') -> ('salida_', 'P1') -> ('entrada_', 'PF')

Como el cuello de botella es P1 con capacidad 2, el flujo máximo es 2. Por lo tanto, se pueden enviar 2 naves de ayuda desde el origen al destino.

"""
