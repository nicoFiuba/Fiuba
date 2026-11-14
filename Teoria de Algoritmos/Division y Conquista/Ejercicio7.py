"""

EXPLICACIÓN
- Divide: dividimos la lista de N edificios a la mitad.
- Conquista: resolvemos de forma recursiva el contorno de la mitad izquierda y el de la mitad derecha.
- Combina: fusionamos ambos subcontornos avanzando de izquierda a derecha. En cada coordenada X, evaluamos la altura de ambos contornos y agregamos al resultado final la altura máxima vigente, omitiendo los puntos redundantes si la altura del cielo no cambia.

PSEUDOCÓDIGO
def skyline(edificios, inicio, final):
    
    if inicio == final:
        izquierda, altura, derecha = edificios[inicio]
        return [(izquierda, altura), (derecha, 0)]
    
    mitad = (inicio + final) // 2
    contorno_izquierda = skyline(edificios, inicio, mitad)
    contorno_derecha = skyline(edificios, mitad + 1, final)
    
    return combinar_contornos(contorno_izquierda, contorno_derecha)

ECUACIÓN DE RECURRENCIA
T(N) = a * T(N/b) + c * f(N)
a = 2, son las llamadas recursivas para resolver cada mitad de los edificios.
b = 2, porque dividimos la lista de edificios en dos partes iguales.
f(N) = O(N) porque el proceso de combinar (barrer ambos contornos de izquierda a derecha) toma tiempo lineal respecto a la cantidad de puntos.

ANÁLISIS DE COMPLEJIDAD
- Temporal: T(N) = a * T(N/b) + c * f(N) = 2 * T(N/2) + O(N) = 2 * T(N/2) + O(N^1) 
a vs b^k = 2 vs 2^1 = 2 vs 2 => 2 = 2, por lo tanto O(N^k * log(N)) = O(N^1 * log(N)) = O(N * log(N))

- Espacial: almacenar los contornos toma O(N) mientras que el call stack de la recursión toma O(log N). Por lo tanto, la complejidad espacial es O(N).

EJEMPLO
- Entrada: edificios = [(1, 11, 5), (2, 6, 7)].
- Ejecución:
    1. Divide y Conquista: el subproblema izquierdo retorna [(1, 11), (5, 0)]. El derecho retorna [(2, 6), (7, 0)].
    2. Combina (barrido de X):
        - En x = 1: sube el izquierdo. Máximo = 11. Agrega (1, 11).
        - En x = 2: sube el derecho a 6. El máximo global sigue siendo 11. No hay cambio visible en la silueta.
        - En x = 5: el izquierdo baja a 0. El derecho sigue aportando 6. El máximo pasa a 6. Agrega (5, 6).
        - En x = 7: el derecho baja a 0. Máximo = 0. Agrega (7, 0).
- Resultado: [(1, 11), (5, 6), (7, 0)].
"""