"""

EXPLICACIÓN

- Divide: dividimos al vector a la mitad

- Conquista: resolvemos un único subproblema recursivamente

- Combina: el resultado está en el caso base.

PSEUDOCÓDIGO
"""

def buscar_extremo(coordenadas):

    n = len(coordenadas)

    if n <= 2:
        return usar_fuerza_bruta(coordenadas)
    
    mitad = n // 2
    punto_izquierdo = coordenadas[mitad - 1].punto
    punto_medio = coordenadas[mitad].punto
    punto_derecho = coordenadas[mitad + 1].punto

    if es_extremo(punto_izquierdo, punto_medio, punto_derecho):
        return punto_medio
    elif punto_izquierdo < punto_medio < punto_derecho:
        return buscar_extremo(coordenadas[mitad:])
    else:
        return buscar_extremo(coordenadas[:mitad])

"""
ECUACIÓN DE RECURRENCIA
T(N) = a * T(N/b) + c * f(N)

a = 1, es la llamada recursiva
b = 2 porque dividimos al vector en dos
f(n) = O(1) porque calcula los indices centrales y los compara

ANÁLISIS DE COMPLEJIDAD

- Temporal: T(N) = a * T(N/b) + c * f(N) = 1 * T(N/2) + O(1) = 1 * T(N/2) + O(N^0)
a vs b^k = 1 vs 2^0 = 1 vs 1 => 1 = 1 por lo tanto O(N^k * log(N)) = O(N^0 * log(N)) = O(1 * log(N)) = O(log(N))

- Espacial: O(log(N)) porque es el call stack de la recursión
"""
