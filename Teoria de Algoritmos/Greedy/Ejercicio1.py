"""

EXPLICACIÓN: la estrategia consiste en ordenar los pueblos de menor a mayor según su kilómetro. Nos paramos en el primer pueblo sin cobertura y le sumamos 50 km para determinar el alcance máximo. Luego, buscamos el último pueblo cuya ubicación sea menor o igual a ese límite y colocamos la patrulla allí. Esta estrategia es Greedy porque en cada iteración opta por estirar lo máximo posible la cobertura, realizando una elección que es localmente óptima, factible (cumple con las restricciones del problema) e irrevocable (una vez tomada no permite ser removida en posteriores elecciones del algoritmo).

PSEUDOCÓDIGO
"""

def ubicar_patrullas(bifurcaciones):

    bifurcaciones.sort(key=lambda x: x.kilometro)

    n = len(bifurcaciones)
    patrulleros = []
    
    i = 0
    while i < n:
        alcance_patrulla = bifurcaciones[i].kilometro + 50
        posicion_patrullero = bifurcaciones[i]

        while i + 1 < n and bifurcaciones[i + 1].kilometro <= alcance_patrulla:
            i += 1
            posicion_patrullero = bifurcaciones[i]

        patrulleros.append(posicion_patrullero)
        cobertura_patrulla = posicion_patrullero.kilometro + 50

        while i + 1 < n and bifurcaciones[i + 1].kilometro <= cobertura_patrulla:
            i += 1

        i += 1

    return patrulleros, len(patrulleros)

"""
ANÁLISIS DE COMPLEJIDAD

- TEMPORAL: ordenar la lista toma O(N * log(N)) y recorrerla toma O(N). Por lo tanto, la complejidad es O(N * log(N)).

- ESPACIAL: O(N) para almacenar a las patrullas.

ANÁLISIS DE OPTIMALIDAD: se demuestra mediante el argumento de stays ahead, ya que al poner la patrulla lo más a la derecha posible en cada iteración, Greedy cubre la misma o mayor distancia que cualquier otra alternativa. Por lo tanto, por inducción, podemos decir que al nunca quedarse atrás en la cobertura, garantiza usar la menor cantidad de patrullas en total.
"""
