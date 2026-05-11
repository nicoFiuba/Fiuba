#1) Escribir un programa que solicite el ingreso de un número y luego calcule e informe el factorial del número ingresado.

num = int(input("Ingrese un número: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i

print(f"El factorial de {num} es: {factorial}")

# 2) Escribir un programa que solicite el ingreso de valores numéricos. El ingreso finalizará cuando el usuario haya ingresado como último valor, un cero. Informar el total de los valores acumulados y cuantos valores fueron ingresados.

num = int(input("Ingrese un número o cero para finalizar: "))
total = 0
while num != 0:
    total += num
    num = int(input("Ingrese un número o cero para finalizar: "))
    
print(f"El total de los valores ingresados es: {total}")

# 3) Solicitar el ingreso de un número y luego informar si el número ingresado es un número primo.
num = int(input("Ingrese un número: "))
esPrimo = True
if num < 2:
    esPrimo = False
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            esPrimo = False
print(f"El número {num} {'es' if esPrimo else 'no es'} primo.")

# 4) Mostrar en forma descendente, los número pares entre 100 y 0 inclusive.
for i in range(100, -1, -2):
    print(i)
    
# 5) Si para resolver el ejercicio 4 no usaste el 3er. parámetro de la función range(), intenta resolver este ejercicio utilizando dicho parámetro, para así, evitar la evaluación de si el número es par.