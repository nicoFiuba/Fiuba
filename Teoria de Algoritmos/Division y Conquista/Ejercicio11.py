"""

EXPLICACIÓN

- Divide: ordenamos a los agentes segun su posicion en X y dividimos en dos grupos

- Conquista: resolvemos dos subproblemas recursivamente

- Combina: calculamos la distancia minima entre los dos grupos y revisamos la frontera para encontrar la distancia minima global.

PSEUDOCÓDIGO
"""

def buscar_agentes(agentes_ordenados):

    n = len(agentes_ordenados)
    if n <= 3:
        return usar_fuerza_bruta(agentes_ordenados)
    
    mitad = n // 2
    distancia_izquierda, agentes_izquierda = buscar_agentes(agentes_ordenados[:mitad])
    distancia_derecha, agentes_derecha = buscar_agentes(agentes_ordenados[mitad:])

    distancia_minima, minimos_agentes = calcular_minimo(distancia_izquierda, agentes_izquierda, distancia_derecha, agentes_derecha)

    frontera = evaluar_limite(agentes_ordenados, mitad, distancia_minima)

    return revisar_frontera(frontera, distancia_minima, minimos_agentes)

"""
ECUACIÓN DE RECURRENCIA
T(N) = a * T(N/b) + c * f(N)

a = 2, son las llamadas recursivas
b = 2 porque dividimos a los agentes en dos grupos
f(n) = O(N) para almacenar y revisar la frontera

ANÁLISIS DE COMPLEJIDAD

- Temporal: T(N) = a * T(N/b) + c * f(N) = 2 * T(N/2) + O(N) = 2 * T(N/2) + O(N^1)
a vs b^k = 2 vs 2^1 = 2 vs 2 => 2 = 2 por lo tanto O(N^k * log(N)) = O(N^1 * log(N)) = O(N * log(N))

- Espacial: la creacion de las sublistas y la frontera toma O(N) mientras que el call stack de la recursión toma O(log(N)). Por lo tanto, la complejidad es O(N)

EJEMPLO
- Entrada: 4 agentes: A(0,0), B(0,1), C(10,0), D(10,2).
- Ejecución:
    - Divide y Conquista: la mitad izquierda retorna distancia = 1 (A,B). La mitad derecha retorna distancia = 2 (C,D).
    - Combina: la distancia_minima es 1. Al evaluar el límite en el centro del mapa, la frontera queda vacía porque no hay agentes cerca del medio.
- Resultado: Retorna distancia 1 con los agentes (A, B).
"""
