"""

EXPLICACIÓN Y MODELADO: estamos ante un problema de asignacion, el cual lo vamos a resolver mediante el algoritmo de flujo maximo. Para ello, vamos a modelar el problema como un grafo dirigido, en donde:

- NODOS: una fuente S, un sumidero T, un nodo para cada medico y un nodo para cada feriado

- ARISTAS: 
S -> nodo medico (capacidad = 1) porque cada medico puede trabajar un solo feriado
nodo medico -> nodo feriado (capacidad = 1) porque el medico puede trabajar ese feriado
nodo feriado -> T (capacidad = 1) porque cada feriado se cubre con un solo medico

PSEUDOCÓDIGO
"""

def cubrir_feriados(medicos, feriados, disponibilidad):

    grafo = GrafoDirigido()

    for medico in medicos:
        grafo.agregar_arista('S', medico, 1)

    for feriado in feriados:
        grafo.agregar_arista(feriado, 'T', 1)

    for medico, feriado in disponibilidad:
        grafo.agregar_arista(medico, feriado, 1)

    flujo_maximo, grafo_residual = ford_fulkerson(grafo, 'S', 'T')

    return flujo_maximo == len(feriados)

"""
ANÁLISIS DE COMPLEJIDAD

- Temporal:
    - Armar la red toma O(M + F) donde M es el número de médicos y F es el número de feriados.
    - V' tiene 2 (fuente y sumidero) + M + F nodos, por lo tanto, O(M + F)
    - E' tiene M + F + M * F (disponibilidad) aristas, por lo tanto, O(M * F)
    - Al usar Edmonds-Karp, la complejidad teorica es O(V' * E'^2), aunque en ese caso como todas las capacidades son 1, la complejidad se reduce a O(E' * Raiz(V')) por lo tanto trayendolo a nuestra red, nos queda O((M * F * Raiz(M + F)))

- Espacial: O(V' + E') para almacenar el grafo, por lo tanto O(M + F + M * F) = O(M * F)

EJEMPLO

Medicos = ['M1', 'M2']
Feriados = ['F1', 'F2']
Disponibilidad = [('M1', 'F1'), ('M1', 'F2'), ('M2', 'F1')]

Red
S -> M1 (capacidad 1)
S -> M2 (capacidad 1)
M1 -> F1 (capacidad 1)
M1 -> F2 (capacidad 1)
M2 -> F1 (capacidad 1)
F1 -> T (capacidad 1)
F2 -> T (capacidad 1)

Camino
1) S -> M2 -> F1 -> T
2) S -> M1 -> F2 -> T

Como el flujo máximo es 2, y la cantidad de feriados es 2, entonces se puede cubrir todos los feriados.

"""
