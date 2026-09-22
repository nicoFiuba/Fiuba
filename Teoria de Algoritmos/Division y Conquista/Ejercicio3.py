"""

EXPLICACIÓN

- Divide: dividimos al vector a la mitad

- Conquista: ordenamos a cada mitad

- Combina: creamos una nueva lista vacía y comparamos al primer jugador de la mitad izquierda contra el de la derecha, al ganador lo sacamos de la lista original y lo agregamos a la lista vacía

PSEUDOCÓDIGO
"""

def ordenar_jugadores(jugadores, matriz_resultados):

    n = len(jugadores)
    if n == 1 or n == 0:
        return jugadores

    orden_final = []
    mitad = n // 2
    mitad_izquierda = ordenar_jugadores(jugadores[:mitad], matriz_resultados)
    mitad_derecha = ordenar_jugadores(jugadores[mitad:], matriz_resultados)

    while len(mitad_izquierda) > 0 and len(mitad_derecha) > 0:
        
        jugadorA = mitad_izquierda[0]
        jugadorB = mitad_derecha[0]
        
        if matriz_resultados[jugadorA][jugadorB] == "Victoria":
            orden_final.append(jugadorA)
            mitad_izquierda.popleft()
        else:
            orden_final.append(jugadorB)
            mitad_derecha.popleft()

    orden_final.extend(mitad_izquierda)
    orden_final.extend(mitad_derecha)

    return orden_final

"""
ECUACIÓN DE RECURRENCIA
T(N) = a * T(N/b) + c * f(N)

a = 2, son las llamadas recursivas
b = 2 porque dividimos al vector en dos
f(n) = O(N) para almacenar los resultados en la lista final

ANÁLISIS DE COMPLEJIDAD

- Temporal: T(N) = a * T(N/b) + c * f(N) = 2 * T(N/2) + O(N) = 2 * T(N/2) + O(N^1)
a vs b^k = 2 vs 2^1 = 2 vs 2 => 2 = 2 por lo tanto O(N^k * log(N)) = O(N^1 * log(N)) = O(N * log(N)) = O(N * log(N))

- Espacial: O(N) para almacenar el orden final
"""
