"""
Ejercicios - Listas y Tuplas
"""

# 1) Escribir una función que reciba por parámetro una tupla de números enteros. La función deberá devolver 1, si la tupla se encuentra ordenada en forma creciente; -1 si la tupla está ordenada en forma decreciente; ó 0 si la tupla está desordenada.

def ingresar_tupla():
    tupla = ()
    continuar = True
    while continuar:
        nro_tupla = int(input("Ingrese un número entero (o 0 para terminar): "))
        if nro_tupla == 0:
            continuar = False
        else:
            tupla += (nro_tupla,)
    return tupla

def validar(tupla):
    tiene_contenido = True
    if len(tupla) == 0:
        print("La tupla está vacía, saliendo...")
        tiene_contenido = False
    return tiene_contenido

def orden_creciente(tupla):
    creciente = True
    posicion = 0
    while posicion < len(tupla) - 1:
        if tupla[posicion] > tupla[posicion + 1]:
            creciente = False
        posicion += 1
    return creciente

def orden_decreciente(tupla):
    decreciente = True
    posicion = 0
    while posicion < len(tupla) - 1:
        if tupla[posicion] < tupla[posicion + 1]:
            decreciente = False
        posicion += 1
    return decreciente

def main():
    tupla = ingresar_tupla()
    if validar(tupla):
        if orden_creciente(tupla):
            print(1)
        elif orden_decreciente(tupla):
            print(-1)
        else:
            print(0)
    return

main()

# 2) Escribir un programa que genere una tupla de 100 valores aleatorios. Cada uno de los valores, debe ser entero, y estar entre 0 y 10000, inclusive; y sólo debe aparecer una vea. Luego, se deben listar por pantalla los números que sean primos e informar cuántos son, y la suma acumulada de los mismos.

import random

def generar_tupla():
    tupla = ()
    while len(tupla) < 101:
        nro_tupla = random.randint(0, 10000)
        if nro_tupla not in tupla:
            tupla += (nro_tupla,)
    return tupla

def es_primo(tupla):
    nros_primos = ()

    for nro in tupla:
        es_primo = True
        if nro < 2:
            es_primo = False
        else:
            for i in range(2, int(nro ** 0.5) + 1):
                if nro % i == 0:
                    es_primo = False
        if es_primo:
            nros_primos += (nro,)
    return nros_primos

def sumar_primos(nros_primos):
    suma = 0
    for nro in nros_primos:
        suma += nro
    return suma

def main():
    tupla = generar_tupla()
    nros_primos = es_primo(tupla)
    suma = sumar_primos(nros_primos)

    print("Tupla generada:", tupla)
    print("Números primos:", nros_primos)
    print("Cantidad de números primos:", len(nros_primos))
    print("Suma acumulada de números primos:", suma)
    return

main()

# 3) Escribir una función que reciba un entero y retorne una lista con los valores de la sucesión de Fibonacci desde la posición 0 y hasta la posición correspondiente al parámetro recibido. Recordemos que la sucesión comienza con los número 0 y 1; y a partir de estos, cada término es la suma de los dos anteriores.

def ingresar_numero():
    num = int(input("Ingrese un número entero: "))
    return num

def sucesion_fibonacci(num):
    fibonacci = []
    if num == 0:
        fibonacci.append(0)
    elif num == 1:
        fibonacci.extend([0, 1])
    else:
        fibonacci.extend([0, 1])
        for i in range(2, num+1):
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return fibonacci

def main():
    num = ingresar_numero()
    fibonacci = sucesion_fibonacci(num)
    print("Sucesión de Fibonacci hasta la posición", num, ":", fibonacci)
    return
main()

# 4) Escribir un programa que solicite al usuario el ingreso de un número natural N, y luego informe, primero los números primos que hay entre 0 y el número ingresado, y luego los números que no son primos. Para la solución, debe implementar el método de la Criba de Eratóstenes, que permite hallar los números primos menores que un número natural dado. En base a una lista con todos los números naturales comprendidos entre 2 y N, se descarta primero el 2 y todos sus múltiplos. Luego se repite el proceso para el primer número que aparece en la lista y todos sus múltiplos. Así sucesivamente hasta que el cuadrado del primer número que aparece como primero en la lista resultante, sea mayor a N.























# 5) Escribir una función que indique si los 5 dados que han sido arrojados por un jugador, forman escalera. La función recibirá por parámetro, una tupla, con los 5 valores obtenidos al arrojar los dados. Deberá devolver True, si forman escalera, de lo contrario, deberá devolver, False. Para que se de escalera, hay 3 alternativas: (1,2,3,4,5); (2,3,4,5,6) ó (3,4,5,6,1), claro que el orden en el que aparecen los valores, no importa.


# 6) De igual modo que el ejercicio anterior, escribir una función para cada uno de los posibles casos:
    # Generala: 5 dados de igual valor
    # Póker: 4 dados iguales y 1 distinto
    # Full: 3 dados iguales y otros 2 iguales

    
# 7) Ahora vamos a escribir un programa que simule una situación de juego, utilizando las funciones escritas en los puntos 3 y 4; y sumando nuevas funciones para lo que se solicite en este punto específicamente. Escribir un programa que genere 1000 tiradas aleatorias, de los 5 dados. Por cada tirada, se debe clasificar si corresponde a alguna de las categorías para las que hemos escrito las funciones, ó a ninguna de ellas. El programa deberá emitir un informe que indique la cantidad de tiradas coincidentes con cada categoría (incluída que no coincide con ninguna categoría), y el % que representa cada una.


# 8) Escribir un programa que genere una lista anidada, con 50 sublistas de pares de valores aleatorios. Los valores deben estar entre -1000 y 1000, inclusive. Luego, agregar a cada sublista de pares, un tercer elemento, que sea el MCD de los otros dos. Por último, suprimir de la lista, las ternas cuyo MCD sea igual a 1. Listar las ternas resultantes.


# 9) Escribir una función que reciba una tupla de N números enteros. La función deberá devolver una lista formada por pares de elementos, donde el primer elemento, será uno de los valores que venía en la tupla, y el segundo elemento, la cantidad de veces que dicho valor aparecía en la tupla. La lista debe estar ordenada por el primer elemento del par. Los valores sólo deben aparecer una única vez en la lista. Pruebe su función, con tuplas generadas aleatoriamente:
    # a. Con 100 elementos, con valores entre 0 y 10.
    # b. Con 1000 elementos, con valores entre -10 y 10.
    # c. Con 5000 elementos, con valores pares entre 2 y 20.

# 10) Si para el ejercicio anterior, usaste el método count; y eliminaste a través del método pop ó con la función del(), los valores que aparecían más de una vez; reescribí la función pero sin utilizar ninguna de estas alternativas.


# 11) Necesitamos elegir al azar una persona, dentro de un grupo de personas. Por ello escribiremos un programa que nos permita realizar esta operación. El programa deberá solicitar el ingreso de los nombres y apellidos de cada uno de los integrantes de este grupo. El ingreso de nombres finalizará cuando el usuario en lugar de ingresar un nombre y apellido, simplemente, de enter. A medida que se ingresan los nombres y apellidos, se debe controlar que el que se está ingresando, no haya sido ingresado. Una vez finalizada la carga, el programa deberá informar cual es el elegido.

# 12) Escribir un programa que solicite el ingreso de un texto formado sólo por sustantivos en singular, separados uno del otro, por un blanco. El usuario ingresará por ejemplo: “casa canción río bebé pez paraguas tórax” El programa deberá mostrar cada una de las palabras ingresadas, seguida por su palabra en plural, un par por línea (singular - plural), en orden alfabético. Validar que las palabras ingresadas por el usuario, sólo contengan letras; caso contrario, enviar un mensaje acorde y volver a solicitar el ingreso. Las reglas a cumplir para pasar un sustantivo en singular a su plural son:
    # a. Agregar una “s” al final, si la palabra termina en vocal sin acento.
    # b. Agregar una “s” al final, si la palabra termina con una é (acentuada).
    # c. Si la palabra termina en “z”, la reemplazamos por “ces”.
    # d. Agregamos “es” al final, si la palabra termina en una consonante (a excepción de la “s”, la “z”, y la “x”), ó si la palabra termina con las vocales acentuadas: á, í, ó, ú.
    # e. Si el sustantivo termina en “s” ó “x”, consideramos que el plural es igual al singular, por lo tanto la función deberá devolver lo mismo que recibió.
