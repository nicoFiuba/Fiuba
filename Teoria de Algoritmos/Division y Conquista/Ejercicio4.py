"""

EXPLICACIÓN: 
- Divide: dividimos al exponente "n" a la mitad

- Conquista: resolvemos un único subproblema recursivamente

- Combina:
Si "n" es par => multiplicamos el resultado del subproblema por sí mismo
Si "n" es impar => multiplicamos el resultado del subproblema por sí mismo y por la base "a"

PSEUDOCÓDIGO
"""

def primoFermat(a, n):

    if n == 0:
        return 1

    sub_potencia = primoFermat(a, n // 2)

    if n % 2 == 0:
        return sub_potencia * sub_potencia
    else:
        return a * sub_potencia * sub_potencia

"""
ECUACIÓN DE RECURRENCIA
T(N) = a * T(N/b) + c * f(N)

a = 1, es la llamada recursiva
b = 2 porque dividimos a "n" en dos
f(n) = O(1) porque verifica paridad y multiplica

ANÁLISIS DE COMPLEJIDAD

- Temporal: T(N) = a * T(N/b) + c * f(N) = 1 * T(N/2) + O(1) = 1 * T(N/2) + O(N^0)
a vs b^k = 1 vs 2^0 = 1 vs 1 => 1 = 1 por lo tanto O(N^k * log(N)) = O(N^0 * log(N)) = O(1 * log(N)) = O(log(N))

- Espacial: O(log(N)) porque es el call stack de la recursión
"""
