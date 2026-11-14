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

- TEMPORAL: O(N²) por el doble for

- ESPACIAL: O(1) ya que no importa cuántos puntos tenga, se almacenan únicamente 3 pares depuntos

EJEMPLO
- Entrada: 4 puntos sobre una línea: A=(0,0), B=(1,0), C=(3,0), D=(6,0).
- Ejecución:
    - Se evalúan los primeros pares y se llena la lista: (A,B)=1, (A,C)=3, (A,D)=6.
    - Al calcular (B,C)=2, el algoritmo detecta que 2 es menor que el peor guardado (6). Por lo tanto, (B,C) reemplaza a (A,D) y la lista se reordena.
    - La lista actual queda: (A,B)=1, (B,C)=2, (A,C)=3.
    - Los pares restantes, como (B,D)=5, se ignoran por no ser menores que 3.
- Resultado: Retorna el top 3 de pares más cercanos: (A,B), (B,C) y (A,C).
"""
