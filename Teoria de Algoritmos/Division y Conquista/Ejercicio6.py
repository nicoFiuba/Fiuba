"""

EXPLICACIÓN

- Divide: dividimos al vector a la mitad

- Conquista: resolvemos un único subproblema recursivamente

- Combina: el resultado está en el caso base.

PSEUDOCÓDIGO
"""

def buscar_extremo(coordenadas, indice_izquierdo, indice_derecho):

    if (indice_derecho - indice_izquierdo) <= 2:
        return usar_fuerza_bruta(coordenadas, indice_izquierdo, indice_derecho)
    
    mitad = (indice_izquierdo + indice_derecho) // 2
    punto_izquierdo = coordenadas[mitad - 1].punto
    punto_medio = coordenadas[mitad].punto
    punto_derecho = coordenadas[mitad + 1].punto

    if es_extremo(punto_izquierdo, punto_medio, punto_derecho):
        return punto_medio
    elif punto_izquierdo < punto_medio < punto_derecho:
        return buscar_extremo(coordenadas, mitad, indice_derecho)
    else:
        return buscar_extremo(coordenadas, indice_izquierdo, mitad)

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

EJEMPLO
- Entrada: coordenadas con valores = [2, 4, 6, 8, 10, 9, 7]. indices: izq = 0, der = 6.
- Ejecución:
    1. mitad =  (0 + 6) // 2 = 6 // 2 = 3 => valor_mitad = 8. Valor_vecinos = 6 y 10. Como 6 < 8 < 10 (subiendo), el pico está a la derecha. Llamamos recursivamente con izq = 3 y der = 6.
    2. Nueva llamada: mitad = (3 + 6) // 2 =  9 // 2 = 4 => valor_mitad = 10. Valor_vecinos = 8 y 9. Como 8 < 10 y 10 > 9, es_extremo() da verdadero.
- Resultado: Retorna el punto con valor 10.
"""
