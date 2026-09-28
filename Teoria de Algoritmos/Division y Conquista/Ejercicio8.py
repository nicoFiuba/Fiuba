"""

EXPLICACIÓN

- Divide: dividimos el patio en 4 cuadrantes de tamaño n/2

- Conquista: colocamos la baldosa en "L" en el centro y resolvemos los 4 subproblemas recursivamente

- Combina: el resultado está en la unión de todos los casos conquistados

PSEUDOCÓDIGO
"""

def ubicar_baldosas(patio, sumidero, n):

    if n == 2:
        return colocar_baldosa_en_L(patio, sumidero)

    sub_patios, centros = dividir_patio_y_definir_centro(patio, sumidero, n/2)
    patios_resueltos = []

    for i in range(4):
        cuadrante = ubicar_baldosas(sub_patios[i], centros[i], n/2)
        patios_resueltos.append(cuadrante)

    patio_final = combinar_patios(patios_resueltos)

    return patio_final


"""
ECUACIÓN DE RECURRENCIA
T(N) = a * T(N/b) + c * f(N)

a = 4, son las llamadas recursivas
b = 2 porque dividimos el patio en 2
f(n) = O(1) porque calcula los indices centrales

ANÁLISIS DE COMPLEJIDAD

-  Temporal: T(N) = a * T(N/b) + c * f(N) = 4 * T(N/2) + O(1) = 4 * T(N/2) + O(N^0)
a vs b^k = 4 vs 2^0 = 4 vs 1 => 4 > 1 por lo tanto O(N^log_b(a)) = O(N^log_2(4)) = O(N^log_2(2^2)) = O(N^(2 * log_2(2))) = O(N^(2 * 1)) = O(N^2)

- Espacial: O(log (N)) porque es el call stack de la recursión
"""
