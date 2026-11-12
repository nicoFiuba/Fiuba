"""

EXPLICACIÓN

- Divide: dividimos a los jugadores a la mitad

- Conquista: ordenamos las sublistas sgun el ranking pasado

- Combina: mezclamos las sublistas ordenadas y contamos cuantos jugadores fueron superados por cada jugador

PSEUDOCÓDIGO
"""

def contar_superados(jugadores):

    n = len(jugadores)
    if n <= 1:
        return jugadores

    orden_final = []
    mitad = n // 2
    mitad_izquierda = contar_superados(jugadores[:mitad])
    mitad_derecha = contar_superados(jugadores[mitad:])

    pasaron_a = 0
    while len(mitad_izquierda) > 0 and len(mitad_derecha) > 0:
        jugadorA = mitad_izquierda[0]
        jugadorB = mitad_derecha[0]

        if jugadorA.ranking_pasado > jugadorB.ranking_pasado:
            pasaron_a += 1
            orden_final.append(jugadorB)
            mitad_derecha.pop(0)
        else:
            jugadorA.superados += pasaron_a
            orden_final.append(jugadorA)
            mitad_izquierda.pop(0)

    for jugador in mitad_izquierda:
        jugador.superados += pasaron_a
        orden_final.append(jugador)

    orden_final.extend(mitad_derecha)

    return orden_final


"""
ECUACIÓN DE RECURRENCIA
T(N) = a * T(N/b) + c * f(N)

a = 2, son las llamadas recursivas
b = 2 porque dividimos al vector en dos
f(n) = O(N) para mezclar las listas

ANÁLISIS DE COMPLEJIDAD

- Temporal: T(N) = a * T(N/b) + c * f(N) = 2 * T(N/2) + O(N) = 2 * T(N/2) + O(N^1)
a vs b^k = 2 vs 2^1 = 2 vs 2 => 2 = 2 por lo tanto O(N^k * log(N)) = O(N^1 * log(N)) = O(N * log(N)) = O(N * log(N))

- Espacial: O(N) ya que si bien el call stack de la recursión toma O(log(N)), almacenar las listas ordenadas toma O(N)
"""
