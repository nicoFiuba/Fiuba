"""
Ejercicios - Listas y Tuplas
"""

# 1) Escribir una función que reciba por parámetro una tupla de números enteros. La función deberá devolver 1, si la tupla se encuentra ordenada en forma creciente; -1 si la tupla está ordenada en forma decreciente; ó 0 si la tupla está desordenada.

def ingresar_tupla():
    lista = []
    continuar = True
    while continuar:
        num = int(input("Ingrese un número entero (o 0 para terminar): "))
        if num == 0:
            continuar = False
        else:
            lista.append(num)
        tupla = tuple(lista)
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
    lista = []
    while len(lista) < 101:
        num = random.randint(0, 10000)
        if num not in lista:
            lista.append(num)
    tupla = tuple(lista)
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


def ingresar_numero():
    num = int(input("Ingrese un número natural: "))
    return num

def criba_eratostenes(num):
    naturales = list(range(2, num + 1))
    primos = []

    for i in range(2, int(num ** 0.5) + 1):
        if i in naturales:
            primos.append(i)
            for j in range(i * i, num + 1, i):
                if j in naturales:
                    naturales.remove(j)
    primos.extend(naturales)
    return primos

def no_primos(num, primos):
    no_primos = []
    for i in range(2, num + 1):
        if i not in primos:
            no_primos.append(i)
    return no_primos

def main():
    num = ingresar_numero()
    primos = criba_eratostenes(num)
    no_primos = [i for i in range(2, num + 1) if i not in primos]

    print("Números primos entre 0 y", num, ":", primos)
    print("Números no primos entre 0 y", num, ":", no_primos)
    return
main()

# 5) Escribir una función que indique si los 5 dados que han sido arrojados por un jugador, forman escalera. La función recibirá por parámetro, una tupla, con los 5 valores obtenidos al arrojar los dados. Deberá devolver True, si forman escalera, de lo contrario, deberá devolver, False. Para que se de escalera, hay 3 alternativas: (1,2,3,4,5); (2,3,4,5,6) ó (3,4,5,6,1), claro que el orden en el que aparecen los valores, no importa.

import random, doctest

def turno_jugador():
    dados = []

    while len(dados) < 5:
        dado = random.randint(1, 6)
        dados.append(dado)
    dados = tuple(dados)
    return dados

def es_escalera(tupla):
    """ 
    >>> es_escalera((1, 2, 3, 4, 5))
    True
    >>> es_escalera((2, 3, 4, 5, 6))
    True
    >>> es_escalera((3, 4, 5, 6, 1))
    True
    >>> es_escalera((1, 2, 3, 4, 6))
    False
    >>> es_escalera((1, 2, 3, 5, 6))
    False
    """

    escalera = None

    escalera1 = (1, 2, 3, 4, 5)
    escalera2 = (2, 3, 4, 5, 6)
    escalera3 = (3, 4, 5, 6, 1)

    if sorted(tupla) == sorted(escalera1) or sorted(tupla) == sorted(escalera2) or sorted(tupla) == sorted(escalera3):
        escalera = True
    else:
        escalera = False
    return escalera

# 6) De igual modo que el ejercicio anterior, escribir una función para cada uno de los posibles casos:
    # Generala: 5 dados de igual valor
    # Póker: 4 dados iguales y 1 distinto
    # Full: 3 dados iguales y otros 2 iguales

def es_generala(tupla):
    """
    >>> es_generala((1, 1, 1, 1, 1))
    True
    >>> es_generala((1, 2, 3, 4, 5))
    False
    >>> es_generala((1, 1, 1, 1, 2))
    False
    >>> es_generala((1, 2, 3, 4, 6))
    False
    >>> es_generala((4, 4, 4, 4, 4))
    True
    """ 
    generala = True

    for dado in tupla:
        if dado !=  tupla[0]:
            generala = False
    
    return generala

def es_poker(tupla):
    """
    >>> es_poker((1, 1, 1, 1, 2))
    True
    >>> es_poker((1, 2, 3, 4, 5))
    False
    >>> es_poker((1, 1, 1, 2, 2))
    False
    >>> es_poker((1, 1, 1, 1, 1))
    False
    >>> es_poker((4, 4, 4, 4, 2))
    True
    """
    poker = False

    for dado in tupla:
        if tupla.count(dado) ==  4:
            poker = True

    return poker

def es_full(tupla):
    """
    >>> es_full((1, 1, 1, 2, 2))
    True
    >>> es_full((1, 2, 3, 4, 5))
    False
    >>> es_full((1, 1, 1, 1, 2))
    False
    >>> es_full((1, 2, 3, 4, 6))
    False
    >>> es_full((4, 4, 4, 2, 2))
    True
    """
    full = False
    valores = ()
    for dado in tupla:
        if dado not in valores:
            valores += (dado,)

    if len(valores) == 2:
        valor1 = tupla.count(valores[0])
        valor2 = tupla.count(valores[1])
        if (valor1 == 3 and valor2 == 2) or (valor1 == 2 and valor2 == 3):
            full = True
    return full

def main():
    tupla = turno_jugador()
    print("Dados arrojados:", tupla)
    print("¿Es escalera?", es_escalera(tupla))
    print("¿Es generala?", es_generala(tupla))
    print("¿Es póker?", es_poker(tupla))
    print("¿Es full?", es_full(tupla))
    print(doctest.testmod())
    return

main()

# 7) Ahora vamos a escribir un programa que simule una situación de juego, utilizando las funciones escritas en los puntos 3 y 4; y sumando nuevas funciones para lo que se solicite en este punto específicamente. Escribir un programa que genere 1000 tiradas aleatorias, de los 5 dados. Por cada tirada, se debe clasificar si corresponde a alguna de las categorías para las que hemos escrito las funciones, ó a ninguna de ellas. El programa deberá emitir un informe que indique la cantidad de tiradas coincidentes con cada categoría (incluída que no coincide con ninguna categoría), y el % que representa cada una.

def clasificar_tiradas(tiradas):
    clasificaciones = [
        ["escalera", 0],
        ["generala", 0],
        ["poker", 0],
        ["full", 0],
        ["ninguna", 0]
    ]

    for tirada in tiradas:
        if es_escalera(tirada):
            clasificaciones[0][1] += 1
        elif es_generala(tirada):
            clasificaciones[1][1] += 1
        elif es_poker(tirada):
            clasificaciones[2][1] += 1
        elif es_full(tirada):
            clasificaciones[3][1] += 1
        else:
            clasificaciones[4][1] += 1
    total_tiradas = len(tiradas)
    for clasificacion in clasificaciones:
        clasificacion[1] = (clasificacion[1] / total_tiradas) * 100
    return clasificaciones

def main():
    tiradas = []
    for i in range(1000):
        tiradas.append(turno_jugador())
    
    clasificaciones = clasificar_tiradas(tiradas)
    
    print("Clasificación de tiradas:")
    for clasificacion in clasificaciones:
        print(f"{clasificacion[0]}: {clasificacion[1]:.2f}%")
    return
main()

# 8) Escribir un programa que genere una lista anidada, con 50 sublistas de pares de valores aleatorios. Los valores deben estar entre -1000 y 1000, inclusive. Luego, agregar a cada sublista de pares, un tercer elemento, que sea el MCD de los otros dos. Por último, suprimir de la lista, las ternas cuyo MCD sea igual a 1. Listar las ternas resultantes.

import random

def generar_lista_anidada():
    lista_anidada = []
    for i in range(50):
        pares = [random.randint(-1000, 1000), random.randint(-1000, 1000)]
        lista_anidada.append(pares)
    return lista_anidada

def mcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def agregar_mcd(lista_anidada):
    for i in range(len(lista_anidada)):
        mcd_valor = mcd(lista_anidada[i][0], lista_anidada[i][1])
        lista_anidada[i].append(mcd_valor)
    return lista_anidada

def eliminar_mcd_igual_a_uno(lista_anidada):
    lista_filtrada = []
    for sublista in lista_anidada:
        if sublista[2] != 1:
            lista_filtrada.append(sublista)
    return lista_filtrada

def main():
    lista_anidada = generar_lista_anidada()
    print("Se ha generado la lista correctamente.")
    lista_anidada = agregar_mcd(lista_anidada)
    lista_filtrada = eliminar_mcd_igual_a_uno(lista_anidada)
    print(f"Se eliminaron las ternas cuyo MCD es igual a 1. De 50 pasamos a {len(lista_filtrada)}")
    print("Lista resultante:")
    for sublista in lista_filtrada:
        print(sublista)
    return
main()

# 9) Escribir una función que reciba una tupla de N números enteros. La función deberá devolver una lista formada por pares de elementos, donde el primer elemento, será uno de los valores que venía en la tupla, y el segundo elemento, la cantidad de veces que dicho valor aparecía en la tupla. La lista debe estar ordenada por el primer elemento del par. Los valores sólo deben aparecer una única vez en la lista. Pruebe su función, con tuplas generadas aleatoriamente:
    # a. Con 100 elementos, con valores entre 0 y 10.
    # b. Con 1000 elementos, con valores entre -10 y 10.
    # c. Con 5000 elementos, con valores pares entre 2 y 20.

import random

def generar_tupla_aleatoria():
    lista = []
    continuar = True
    while continuar:
        num = random.randint(0, 10)
        
        lista.append(num)
        if len(lista) == 100:
            continuar = False
    tupla = tuple(lista)
    return tupla

def generar_tupla_aleatoria_2():
    lista = []
    continuar = True
    while continuar:
        num = random.randint(-10, 10)
        
        lista.append(num)
        if len(lista) == 1000:
            continuar = False
    tupla = tuple(lista)
    return tupla

def generar_tupla_aleatoria_3():
    lista = []
    continuar = True
    while continuar:
        num = random.randint(2, 20)
        if num % 2 == 0:
            lista.append(num)
        if len(lista) == 5000:
            continuar = False
    tupla = tuple(lista)
    return tupla

def contar(tupla):
    lista = []
    
    for valor in tupla:
        esta_en_lista = False
        for cantidad in lista:
            if cantidad[0] == valor:
                cantidad[1] += 1
                esta_en_lista = True
        if not esta_en_lista:
            lista.append([valor, 1])
    return lista

def ordenar_lista(lista):
    lista.sort(key=lambda x: x[0])
    return lista

def main():
    tupla1 = generar_tupla_aleatoria()
    tupla2 = generar_tupla_aleatoria_2()
    tupla3 = generar_tupla_aleatoria_3()

    lista1 = contar(tupla1)
    lista2 = contar(tupla2)
    lista3 = contar(tupla3)

    lista1 = ordenar_lista(lista1)
    lista2 = ordenar_lista(lista2)
    lista3 = ordenar_lista(lista3)

    print("Lista 1: ")
    for sublista in lista1:
        print(sublista)
    print("Lista 2: ")
    for sublista in lista2:
        print(sublista)
    print("Lista 3: ")
    for sublista in lista3:
        print(sublista)
    return
main()

# 10) Si para el ejercicio anterior, usaste el método count; y eliminaste a través del método pop ó con la función del(), los valores que aparecían más de una vez; reescribí la función pero sin utilizar ninguna de estas alternativas.

#RTA: no se utilizó el método count, ni el pop o del().

# 11) Necesitamos elegir al azar una persona, dentro de un grupo de personas. Por ello escribiremos un programa que nos permita realizar esta operación. El programa deberá solicitar el ingreso de los nombres y apellidos de cada uno de los integrantes de este grupo. El ingreso de nombres finalizará cuando el usuario en lugar de ingresar un nombre y apellido, simplemente, de enter. A medida que se ingresan los nombres y apellidos, se debe controlar que el que se está ingresando, no haya sido ingresado. Una vez finalizada la carga, el programa deberá informar cual es el elegido.

import random

def ingresar_personas():
    personas = []
    continuar = True
    while continuar:
        persona = input("Ingrese un nombre y apellido (o presione enter para terminar): ")
        if persona == "":
            continuar = False
        elif persona not in personas:
            personas.append(persona)
        else:
            print("El nombre ya fue ingresado.")
    return personas

def validar(personas):
    tiene_contenido = True
    if len(personas) == 0:
        print("No se ingresaron personas, saliendo...")
        tiene_contenido = False
    return tiene_contenido

def elegir_persona(personas):
    if validar(personas):
        elegido = random.choice(personas)
        print("La persona elegida es:", elegido)
    return

def main():
    personas = ingresar_personas()
    elegir_persona(personas)
    return
main()

# 12) Escribir un programa que solicite el ingreso de un texto formado sólo por sustantivos en singular, separados uno del otro, por un blanco. El usuario ingresará por ejemplo: “casa canción río bebé pez paraguas tórax” El programa deberá mostrar cada una de las palabras ingresadas, seguida por su palabra en plural, un par por línea (singular - plural), en orden alfabético. Validar que las palabras ingresadas por el usuario, sólo contengan letras; caso contrario, enviar un mensaje acorde y volver a solicitar el ingreso. Las reglas a cumplir para pasar un sustantivo en singular a su plural son:
    # a. Agregar una “s” al final, si la palabra termina en vocal sin acento.
    # b. Agregar una “s” al final, si la palabra termina con una é (acentuada).
    # c. Si la palabra termina en “z”, la reemplazamos por “ces”.
    # d. Agregamos “es” al final, si la palabra termina en una consonante (a excepción de la “s”, la “z”, y la “x”), ó si la palabra termina con las vocales acentuadas: á, í, ó, ú.
    # e. Si el sustantivo termina en “s” ó “x”, consideramos que el plural es igual al singular, por lo tanto la función deberá devolver lo mismo que recibió.

def ingresar_texto():
    texto = input("Ingrese un texto con sustantivos en singular, separados por espacios: ")
    palabras = texto.split()
    return palabras

def validar_palabra(palabra):
    es_valida = True
    for letra in palabra:
        if not letra.isalpha():
            es_valida = False
    return es_valida

def convertir_a_plural(palabra):
    palabra = palabra.lower()
    if palabra.endswith(("s", "x")): # Regla e
        palabra = palabra
    elif palabra.endswith(("a", "e", "i", "o", "u")):
        palabra += "s"  # Regla a
    elif palabra.endswith("é"):
        palabra += "s"  # Regla b
    elif palabra.endswith("z"):
        palabra = palabra[:-1] + "ces"  # Regla c
    elif not palabra[-1].lower() in ("s", "z", "x"):
        palabra += "es"  # Regla d
    else:
        palabra = palabra 
    return palabra

def generar_lista_plural(palabras):
    lista_plural = []
    for palabra in palabras:
        if validar_palabra(palabra):
            plural = convertir_a_plural(palabra)
            lista_plural.append((palabra, plural))
        else:
            print(f"La palabra '{palabra}' no es válida. Debe contener solo letras.")
    return lista_plural

def ordenar_lista(lista):
    lista.sort(key=lambda x: x[0])
    return lista

def main():
    palabras = ingresar_texto()
    lista_plural = generar_lista_plural(palabras)
    lista_plural = ordenar_lista(lista_plural)

    print("Palabras en singular y plural:")
    for singular, plural in lista_plural:
        print(f"{singular} - {plural}")
    return
main()