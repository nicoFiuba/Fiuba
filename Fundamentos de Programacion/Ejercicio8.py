#1) Escribir un programa que solicite el ingreso de un número y luego calcule e informe el factorial del número ingresado.

num = int(input("Ingrese un número: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i

print(f"El factorial de {num} es: {factorial}")

# 2) Solicitar el ingreso de un número y luego informar si el número ingresado es un número primo.
num = int(input("Ingrese un número: "))
esPrimo = True
if num < 2:
    esPrimo = False
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            esPrimo = False
print(f"El número {num} {'es' if esPrimo else 'no es'} primo.")

# 3) Tomá la solución del ejercicio anterior y preguntate sí elegiste el cliclo adecuado, y si estás evitando realizar ciclos innecesarios. Por ejemplo, algunas preguntas que nos podríamos hacer son: a) Si con sólo encontrar un divisor del número a evaluar, ya puedo afirmar que el número no es primo, tiene sentido seguir evaluando divisores? b) Teniendo en cuenta que todo número par a excepción del 2, no es primo, tiene sentido seguir en un ciclo si al calcular el resto de la división del número a evaluar por 2, el resultado es cero?  c) Puedo encontrar un divisor del número a evaluar que sea mayor al número a evaluar dividido 2? Seguramente, si tengo en cuenta estás cuestiones en mi programa, podré lograr que el  mismo sea más eficiente.

# 4) Solicitar el ingreso de dos valores enteros, y calcular e informar el máximo común divisor entre ambos números.  Recordemos que se define el máximo común divisor (MCD) de dos o más números enteros al mayor número entero que los divide sin dejar resto alguno. Te sugerimos que antes de programar la solución te hagas preguntas del tipo a las planteadas en en el ejercicio 3

def recibirNumeros():
    numeros = input("Ingrese dos números enteros separados por un espacio: ").split()
    numeros = [int(num) for num in numeros] # Convertir los números a enteros
    return numeros

def mcm (x,y):
    resultado = max(x,y)
    while resultado % x != 0 or resultado % y != 0:
        resultado += 1
    return resultado

def mcd (x,y):
    resultado = max(x,y)
    while x % resultado != 0 or y % resultado != 0:
        resultado -= 1
    return resultado

def main():
    numeros = recibirNumeros()
    mcm_resultado = mcm(numeros[0], numeros[1])
    mcd_resultado = mcd(numeros[0], numeros[1])
    print(f"El MCM de los dos primeros números es: {mcm_resultado} y el MCD es: {mcd_resultado}.")

main()

# 5) Hacer el ejercicio 4 pero usando el metodo de Euclides
def recibirNumeros():
    numeros = input("Ingrese dos números enteros separados por un espacio: ").split()
    numeros = [int(num) for num in numeros] # Convertir los números a enteros
    return numeros

def mcdEuclides(x,y):
    while y != 0: #Mientras que Y != 0 => el MCD es el último valor de X
        x, y = y, x % y #Divide a X entre Y, guarda el resto, transforma el valor de Y a X, asigna el resto a Y, Divide a X ente Y y asi sucecivamente hasta que Y sea 0. 
    return x

def mcmEuclides(x,y):
    mcm = (x*y)//mcdEuclides(x,y)
    return mcm

def main():
    numeros = recibirNumeros()
    mcm = mcmEuclides(numeros[0], numeros[1])
    mcd = mcdEuclides(numeros[0], numeros[1])
    print(f"El MCM de los dos primeros números es: {mcm} y el MCD es: {mcd}.")

main()