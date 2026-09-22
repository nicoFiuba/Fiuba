"""

EXPLICACIÓN: la estrategia consiste en ordenar a los competidores de mayor a menor según su tiempo en paralelo (ciclismo y carrera), para que estos solapen su tiempo. Esta estrategia es Greedy porque realiza una elección:
    - Localmente óptima ya que en cada iteración elige al competidor mas lento
    - Factible ya que solo permite una persona en la pileta
    - Irrevocable ya que una vez tomada la decision, no se la puede remover.

PSEUDOCÓDIGO
"""

def minimizar_tiempos(competidores):

    competidores.sort(key=lambda x: x.tiempo_ciclismo + x.tiempo_carrera, reverse = True)

    orden_final = []
    tiempo_pileta = 0
    duracion_triatlon = 0

    for competidor in competidores:

        tiempo_pileta += competidor.tiempo_natacion
        tiempo_competidor = tiempo_pileta + competidor.tiempo_ciclismo + competidor.tiempo_carrera

        if tiempo_competidor > duracion_triatlon:
            duracion_triatlon = tiempo_competidor

        orden_final.append(competidor)

    return orden_final, duracion_triatlon

"""
ANÁLISIS DE COMPLEJIDAD

- TEMPORAL: ordenar la lista toma O(N * log(N)) mientras que  recorrerla toma O(N). Por lo tanto, la complejidad es O(N * log(N)).

- ESPACIAL: O(N) para almacenar el orden.

ANÁLISIS DE OPTIMALIDAD: se demuestra mediante el argumento de la sustitución, ya que si una solución ordena diferente a la de Greedy, significa que un competidor va a tardar más en terminar la carrera y por ende se va a alargar la duración del triatlón. Por lo tanto, tendríamos que cambiar el orden para poder minimizar la duración del torneo (es lo que hace Greedy).
"""
