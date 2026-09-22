"""

EXPLICACIÓN

- Divide: dividimos a las matrices en bloques de tamaño n/4

- Conquista: resolvemos los S subproblemas recursivamente

- Combina: el resultado está en la unión de todos los casos conquistados

PSEUDOCÓDIGO
"""

def nueva_multiplicacion_de_matrices(A, B, n):

    if n <= LIMITE:
        return multiplicar_matrices(A, B)
    
    sub_A, sub_B = dividir_matrices(A, B, n/4)
    subMatrices = []

    for i in range(48): # 48 es el a de la ecuacion de recurrencia.
        matrices = nueva_multiplicacion_de_matrices(sub_A[i], sub_B[i], n/4)
        subMatrices.append(matrices)

    matriz_final = combinar_matrices(subMatrices)

    return matriz_final

"""
ECUACIÓN DE RECURRENCIA
T(N) = a * T(N/b) + c * f(N) = a * T(N/4) + O(N²) => log_b(a) = log_4(a) y como tiene que ser mejor => log_4(a) < log_2(7) y por propiedad de logaritmo digo que log_4(b) = log_baseBuscada(a)/log_baseBuscada(baseActual) = log_2(a)/log_2(4) = log_2(a)/log_2(2²) = log_2(a)/2 * log_2(2) = log_2(a)/2 * 1 = log_2(a)/2 por lo tanto log_4(a) < log_2(7) = log_2(a)/2 < log_2(7) = log_2(a) < log_2(7) * 2
= log_2(a) < log_2(7²) = log_2(a) < log_2(49) = a < 49. La cantidad maxima de subproblemas es 48, entonces:

a = 48, son las llamadas recursivas
b = 4 porque dividimos las matrices en 4
f(n) = O(N²) porque multiplicamos matrices

ANÁLISIS DE COMPLEJIDAD

- Temporal: T(N) = 48 * T(N/4) + O(N²) => O(N^log_b(a)) = O(N^log_4(48))

- Espacial: O(N²) porque es el call stack de la recursión
"""
