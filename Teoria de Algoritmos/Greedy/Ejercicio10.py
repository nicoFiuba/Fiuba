"""

EXPLICACIÓN: la estrategia consiste en poner la cantidad minima de cada fragancia y luego como nos piden minimizar, ordenar de menor a mayor segun su ratio (costo/volumen). Esta estrategia es Greedy porque realiza una elección:
    - Localmente óptima porque en cada iteración, elige lo mas barato posible.
    - Factible ya que cumple con las restricciones del problema
    - Irrevocable ya que una vez tomada la decisión, no permite ser removida en posteriores elecciones del algoritmo.

PSEUDOCÓDIGO
"""

def minimizar_costo(fragancias, volumen_maximo):

    volumen_perfume = 0
    costo_total = 0

    for fragancia in fragancias:
        volumen_perfume += fragancia.minimo
        costo_total += fragancia.minimo * fragancia.costo_por_m3

    fragancias.sort(key=lambda x: x.costo_por_m3)

    i = 0
    while volumen_perfume < volumen_maximo and i < len(fragancias):
        fragancia_actual = fragancias[i]
        volumen_disponible = volumen_maximo - volumen_perfume
        posible_agregado = fragancia_actual.maximo - fragancia_actual.minimo

        if posible_agregado > 0:
            cantidad_a_agregar = min(posible_agregado, volumen_disponible)
            volumen_perfume += cantidad_a_agregar
            costo_total += cantidad_a_agregar * fragancia_actual.costo_por_m3
        
        i += 1

    return costo_total

"""
ANÁLISIS DE COMPLEJIDAD

- TEMPORAL: Ordenar las fragancias toma O(N log N) y recorrerlas O(N), por lo tanto la complejidad es O(n log n).

- ESPACIAL: O(1) para almacenar el costo y el volumen total

ANÁLISIS DE OPTIMALIDAD: se demuestra mediante el argumento de la sustitución, ya que si una solución ordena diferente a la de Greedy, significa que en algún momento se va a poner más cantidad de una fragancia más cara. Por lo tanto, tendríamos que cambiar el orden para poder evitar que esto suceda y así minimizar el costo (es lo que hace Greedy).

EJEMPLO
- Entrada: Volumen máximo = 10. Dos fragancias: F1(min 2, max 5, costo 10) y F2(min 1, max 6, costo 20).
- Ejecución:
    - Fase inicial (Mínimos): Agregamos 2 de F1 y 1 de F2. Volumen = 3. Costo = 40. Faltan 7.
    - Fase greedy: Ordenamos por costo de menor a mayor (F1 primero, luego F2).
    - Evaluamos F1: Podemos sumar 3 más (máx 5 - mín 2). Agregamos 3. Volumen = 6. Costo = 40 + 30 = 70. Faltan 4.
    - Evaluamos F2: Podemos sumar hasta 5 más (máx 6 - mín 1). Agregamos solo los 4 que faltan. Volumen = 10. Costo = 70 + 80 = 150.
- Resultado: Retorna un costo total de 150.
"""
