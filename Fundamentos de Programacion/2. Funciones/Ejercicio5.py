"""
Escribir una función potencia que reciba dos enteros: a y b. Debe retornar a^b sin utilizar funciones de potencia o el operador **, solo con sumas, productos y divisiones. 
"""

def potencia(a, b):
    resultado = 1
    if b < 0:
        for i in range(-b):
            resultado *= 1/a
    else:
        for i in range(b):
            resultado *= a
    return resultado

def main():
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese otro numero: "))
    resultado = potencia(a, b)
    print(f"El resultado de {a} elevado a {b} es: {resultado}")

main()