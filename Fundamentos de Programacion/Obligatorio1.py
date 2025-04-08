"""
Escribir una función que reciba por parámetro cuatro valores enteros. Debe calcular él mínimo común múltiplo entre los dos primeros parámetros y verificar si el valor está comprendido en el rango que generan los últimos dos parámetros, inclusive.  En caso afirmativo, la función devolverá el mcm. En caso negativo, debe devolver 0.
"""
import doctest

def recibirNumeros():
    numeros = input("Ingrese cuatro números enteros separados por un espacio: ").split()
    numeros = [int(num) for num in numeros] # Convertir los números a enteros
    return numeros

def mcm (x,y):
    resultado = max(x,y)
    while resultado % x != 0 or resultado % y != 0:
        resultado += 1
    return resultado

def test_mcm():
    """
    >>> mcm(1,2)
    2
    >>> mcm(3,2)
    6
    >>> mcm(4,5)
    20
    >>> mcm(3,10)
    30
    >>> mcm(6,8)
    24
    """

def verificarRango(numeros):
    valor_mcm= mcm(numeros[0], numeros[1])
    if numeros[2]<= valor_mcm <= numeros[3]:
        return valor_mcm
    else:
        return 0



def main():
    numeros = recibirNumeros()
    verificado = verificarRango(numeros)
    if verificado != 0:
        print(f"El MCM de los dos primeros números es: {verificado} y esta en el rango de los dos últimos números.")
    else:
        print("El MCM no está en el rango de los dos últimos números.")
    
    print(doctest.testmod())

main()