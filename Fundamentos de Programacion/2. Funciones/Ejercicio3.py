"""
Escribir una función que reciba un valor y calcule el factorial del mismo. Si no se puede calcular el factorial del valor recibido, la función deberá devolver 0, de lo contrario deberá devolver el valor calculado. No debe imprimir el valor, debe solamente devolverlo. Probá la función invoncándola desde el bloque principal, con al menos 3 valores.
"""

def factorial():
    num = int(input("Ingrese un número: "))
    factorial = 1
    if num < 0:
        print(0)
    else:
        for i in range(1, num + 1):
            factorial *= i

        print(f"El factorial de {num} es: {factorial}")

def main():
    factorial()

main()