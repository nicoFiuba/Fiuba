"""
Escribir una función que reciba un valor y calcule el factorial del mismo.
Si no se puede calcular el factorial del valor recibido, la función deberá devolver 0, de lo contrario deberá devolver el valor calculado.
No debe imprimir el valor, debe solamente devolverlo.
La función debe ser testeada, usando el módulo doctest, y se deben incluir al menos 5 casos de prueba que sean significativos.
"""
import doctest

def calcularFactorial(num):
    factorial = 1
    if num < 0:
        factorial = 0
    else:
        for i in range(1, num + 1):
            factorial *= i
    return factorial

def test_calcularFactorial():
    """
    >>> calcularFactorial(0)
    1
    >>> calcularFactorial(1)
    1
    >>> calcularFactorial(5)
    120
    >>> calcularFactorial(10)
    3628800
    >>> calcularFactorial(-3)
    0
    """

def main():
    num = int(input("Ingrese un número: "))
    print(calcularFactorial(num))
    print(doctest.testmod())
main()
