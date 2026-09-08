"""

EXPLICACIÓN: como se habla de naive, significa que el problema se resuelve mediante fuerza bruta, es decir que tenemos que generar y probar todas las posibles soluciones.

PSEUDOCÓDIGO
"""

def naive (puntos):

    n = len(puntos)
    top3_distancias = []

    for i in range(n):
        for j in range(i + 1, n):

            distancia_actual = calcular_distancia(puntos[i], puntos[j])

            if len(top3_distancias) < 3:
                top3_distancias.append((distancia_actual, puntos[i], puntos[j]))

                top3_distancias.sort(key=lambda x: x[0])

            elif distancia_actual < top3_distancias[2][0]:
                top3_distancias[2] = (distancia_actual, puntos[i], puntos[j])

                top3_distancias.sort(key=lambda x: x[0])

    return top3_distancias

"""
ANÁLISIS DE COMPLEJIDAD
- TEMPORAL: O(N²) ya que estamos en fuerza bruta
- ESPACIAL: O(1) ya que no importa cuántos puntos tenga, se almacenan únicamente 3 puntos
"""
