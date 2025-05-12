"""
Escribir una función que reciba un valor y si el valor recibido no es mayor a 0, envíe un mensaje de error diciendo "ERROR: El valor a ingresar debe ser mayor a 0", y vuelva a solicitar el ingreso de un valor y evaluar si cumple con la condición. Debe repetirse hasta que el usuario haya ingresado un valor mayor a 0. La función debe devolver un valor válido.Es importante que te detengas a pensar con que estructura de control se resuelve adecuadamente este problema.
"""

def valorPositivo():
    valido = False
    while not valido:
        valor = int(input("Ingrese un valor: "))
        if valor > 0:
            print(f"El valor ingresado es: {valor}")
            valido = True
        else:
            print("ERROR: El valor a ingresar debe ser mayor a 0")

def main():
    valorPositivo()

main()