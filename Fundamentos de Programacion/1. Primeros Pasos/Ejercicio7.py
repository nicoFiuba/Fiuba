# 1) Escribir un programa que solicite el ingreso de dos números y luego informe cuál es el mayor de los números ingresados. Suponer que siempre los números ingresados serán distintos.

numeros = input("Ingrese dos números separados por un espacio: ").split()
numeros = [int(num) for num in numeros] # Convertir los números a enteros
mayor = max(numeros)

#2) Ahora, tomá el ejercicio anterior y considerá que el usuario podría ingresar dos veces el mismo número.
if numeros[0] == numeros[1]:
    print("Los números ingresados son iguales.")
else:
    print(f"El mayor de los números ingresados es: {mayor}")

#3) Escribir un programa que solicite el ingreso de un número, y luego indique si el número ingresado es par ó impar. Suponer que el número ingresado será un número entero.

numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

#4) Escribir un programa que solicite el ingreso de un número, y luego informe si el mismo es positivo, negativo ó neutro.
nuumero = int(input("Ingrese un número: "))
if nuumero > 0:
    print(f"El número {nuumero} es positivo.")
elif nuumero < 0:
    print(f"El número {nuumero} es negativo.")
else:
    print(f"El número {nuumero} es neutro.")

#5) Escribir un programa que solicite el ingreso de tres palabras, y luego las muestre en orden alfabético. Suponer que las palabras ingresadas sólo contendrán letras minúsculas.
palabras = input("Ingrese tres palabras separadas por un espacio: ").split()
palabras.sort()
print(f"Palabras en orden alfabético:  {palabras}")
