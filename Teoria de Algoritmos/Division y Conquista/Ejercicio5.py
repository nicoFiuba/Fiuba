"""

EXPLICACIÓN ACTUAL: la estrategia consiste en usar la fuerza bruta, es decir, recorrer el lote comparando paquete a paquete, para que al final comparemos los paquetes del mismo volumen contra los paquetes totales para ver si el lote es válido o no

PSEUDOCÓDIGO

def procesoA(lote):

    n = len(lote)

    for i in range(n):
        
        mismo_volumen = 0
        
        for j in range(n):
            if lote[i].volumen == lote[j].volumen:
                mismo_volumen += 1
            
        if mismo_volumen > n // 2:
            return "Lote válido"
    
    return "Lote inválido"

ANÁLISIS DE COMPLEJIDAD

- Temporal: O(N²) por el doble for

- Espacial: O(1) porque solamente comparamos


EXPLICACIÓN B: la estrategia consiste en ordenar el lote de mayor a menor según su volumen para que, en vez de comparar paquete a paquete, comparemos solamente el paquete actual vs el que se encuentra a una mitad de distancia, ya que al estar ordenados por volumen, si el paquete de esa mitad tiene el mismo volumen que el actual, significa que los del medio también tienen el mismo volumen

PSEUDOCÓDIGO

def procesoB(lote):

    n = len(lote)

    if n == 0:
        return "Lote inválido"
    elif n == 1:
        return "Lote válido"

    lote.sort(key=lambda x: x.volumen, reverse = True)    
    mitad = n // 2

    i = 0
    while i + mitad < n:
        if lote[i].volumen == lote[i + mitad].volumen:
            return "Lote válido"
        
        i += 1

    return "Lote inválido"

ANÁLISIS DE COMPLEJIDAD

- Temporal: Ordenar la lista toma O(N * log(n)) mientras que recorrerla toma O(N). Por lo tanto, la complejidad es O(N * log(N))

- Espacial: O(1) porque solamente comparamos


EXPLICACIÓN C

- Divide: dividimos al vector a la mitad

- Conquista: resolvemos los subproblemas recursivamente

- Combina: si alguno de los subproblemas supera a la mitad estricta del lote, significa que el lote es válido. En caso contrario, el lote es inválido

PSEUDOCÓDIGO

def procesoC(lote):

    n = len(lote)

    if n == 0:
        return "Lote inválido"
    elif n == 1:
        return lote[0]

    mitad = n // 2

    candidato_izquierdo = procesoC(lote[:mitad])
    candidato_derecho= procesoC(lote[mitad:])

    for candidato in [candidato_izquierdo, candidato_derecho]:
        if candidato != "Lote inválido" and contar(lote, candidato) > n // 2:
            return candidato

    return "Lote inválido"

ECUACIÓN DE RECURRENCIA
T(N) = a * T(N/b) + c * f(N)

a = 2, son las llamadas recursivas
b = 2 porque dividimos al vector en dos
f(n) = O(N) porque recorre el vector para contar los paquetes

ANÁLISIS DE COMPLEJIDAD

- Temporal: T(N) = a * T(N/b) + c * f(N) = 2 * T(N/2) + O(N) = 2 * T(N/2) + O(N^1)
a vs b^k = 2 vs 2^1 = 2 vs 2 => 2 = 2 por lo tanto O(N^k * log(N)) = O(N^1 * log(N)) = O(N * log(N))

- Espacial: O(log(N)) porque es el call stack de la recursión
"""
