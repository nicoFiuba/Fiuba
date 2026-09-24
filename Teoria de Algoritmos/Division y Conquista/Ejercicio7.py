"""

EXPLICACIÓN

- Divide: dividimos al vector a la mitad

- Conquista: resolvemos un único subproblema recursivamente

- Combina: el resultado está en el caso base.

PSEUDOCÓDIGO
"""

def contornear(edificios, inicio, final):

    if (final -inicio) <= 2:
        return usar_fuerza_bruta(edificios, inicio, final)
    
    mitad = (inicio + final) // 2
    inicio_edificio = edificios[mitad - 1].valor
    altura_edificio = edificios[mitad].valor
    fin_edificio = edificios[mitad + 1].valor

    if es_pico(inicio_edificio, altura_edificio, fin_edificio):
            return altura_edificio
    elif inicio_edificio < altura_edificio < fin_edificio:
        return contornear(edificios, mitad, final)
    else:
        return contornear(edificios, inicio, mitad)

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
