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

EJEMPLO
- Entrada: jugadores con ranking_pasado = [3, 1, 4, 2]. Todos inician con superados = 0.
- Ejecución (foco en el Merge final):
    1. Las llamadas recursivas retornan las mitades ordenadas: izquierda = [1, 3], derecha = [2, 4]. (El 3 ya sumó 1 superado al mezclarse con el 1).
    2. Compara 1 vs 2: se agrega el 1 a orden_final. superados de 1 += pasaron_a => 0 += 0 = 0.
    3. Compara 3 vs 2: se agrega el 2 a orden_final. Como 3 > 2, pasaron_a += 1 => 0 += 1 = 1. 
    4. Compara 3 vs 4: se agrega el 3 a orden_final. superados de 3 += pasaron_a => 1 += 1 = 2.
    5. Se vacía la izquierda. Se agrega el 4 de la derecha con extend().
- Resultado: Lista ordenada [1, 2, 3, 4]. Los "superados" finales son: Jugador 1 con 0, Jugador 2 con 0, Jugador 3 con 2 y Jugador 4 con 1.
"""
