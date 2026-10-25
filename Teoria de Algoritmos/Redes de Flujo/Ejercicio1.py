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
    - V' tiene 2 + M + F nodos, por lo tanto, O(M + F)
    - E' tiene M + F + (M * F) aristas, por lo tanto, O(M * F)
    - Al usar Edmonds-Karp, la complejidad teorica es O(V' * E'^2), aunque en ese caso como todas las capacidades son 1, la complejidad se reduce a O(E' * Raiz(V')) por lo tanto trayendolo a nuestra red, nos queda O((M * F * Raiz(M + F)))

- Espacial: O(V' + E') para almacenar el grafo, por lo tanto O(M + F + M * F) = O(M * F)

ANÁLISIS DE OPTIMALIDAD: el algortimo es optimo gracias al teorema de flujo máximo - corte mínimo, el cual asegura que, al terminar el algoritmo, la cantidad de emparejamientos encontrada es matemáticamente insuperable. Y al teorema de integralidad el cual, como las capacidades son enteras, garantiza que no se asignen "fracciones de médicos" a un feriado

"""