"""
Ejercicio 1
Escribir una función que reciba una palabra, y devuelva True, si la palabra tiene diptongo, y False, en caso contrario. Asumir que la palabra recibida, solo esta formada por letras. En español dos vocales en contacto se articulan como diptongo cuando:
    1. una es cerrada (i u) átona (no acentuada) y la otra es abierta (a e o) y viceversa.
    2. ambas son cerradas, excepto si son iguales (como en chiita), donde forman un hiato
"""

def ingrese_palabra():
    palabra = input("Ingrese una palabra: ")
    return palabra

def tiene_diptongo(palabra):
    palabra = palabra.lower()
    vocales_abiertas = "aeo"
    vocales_cerradas = "iu"
    diptongo = []

    for letra in vocales_cerradas:
        for letra2 in vocales_abiertas:
            diptongo.append(letra + letra2)
            diptongo.append(letra2 + letra)
    diptongo.extend(["iu", "ui"])

    es_diptongo = True
    posicion = 0

    while posicion < len(diptongo) and diptongo[posicion] not in palabra:
        posicion += 1
    if posicion == len(diptongo):
        es_diptongo = False
    return es_diptongo


"""
Ejercicio 2
Escribir una función que reciba un texto y devuelva una lista anidada que representa un ranking de palabras. El texto puede tener gran cantidad de palabras.
La función deberá devolver una lista anidada, en la que cada sublista, esté formada por un par [palabra, cantidad de veces en el texto], ordenada por la cantidad de veces que aparece la palabra. Las palabras sólo deben aparecer una vez en la lista.
"""
def ingrese_texto():
    texto = input("Ingrese un texto: ")
    return texto

def ranking(texto):
    palabras = texto.lower().split()
    if palabras:
        # Inicializo el ranking con la 1er. palabra del texto
        ranking = [[palabras[0], 0]]
    else:
        ranking = []
    for palabra in palabras:
        posicicion = 0
        while posicicion < len(ranking) and ranking[posicicion][0] != palabra:
            posicicion += 1
        if posicicion == len(ranking):
            ranking.append([palabra, 1])
        else:
            ranking[posicicion][1] += 1
    ranking.sort(key=lambda x: x[1], reverse=True)
        
    return ranking

def main():
    texto = ingrese_texto()
    ranking_palabras = ranking(texto)
    print("Ranking de palabras:", ranking_palabras)

    return
main()
"""
Ejercicio 3:
Escribir un programa modular que haciendo uso de listas, permita:
1. El ingreso de una secuencia de valores, que termina con el valor 0.
2. Muestre los valores ingresados.
3. Muestre los valores hasta encontrar el 3er. valor impar ingresado inclusive.
4. Muestre los elementos que se encuentren en posiciones pares.
5. Muestre los elementos ordenados de menor a mayor, sin repetirlos.
En todos los casos, las salidas deben contener un título que indique lo que se está mostrando
y mostrar un valor por línea.
"""
def ingresar_valores():
    valores = []
    continuar = True
    while continuar:
        valor = int(input("Ingrese un valor (0 para terminar): "))
        if valor == 0:
            continuar = False
        else:
            valores.append(valor)
    return valores

def validar(valores):
    tiene_valores = True
    if not valores:
        print("Fin del programa")
        tiene_valores = False
    return tiene_valores

def mostrar_valores(mensaje, valores):
    print(mensaje)
    for valor in valores:
        print(valor)
    return None

def mostrar_hasta_tercer_impar(valores):
    valores_impares = []
    impares = 0
    posicion = 0
    while len(valores_impares) < 3 and posicion < len(valores):
        if valores[posicion] % 2 != 0:
            valores_impares.append(valores[posicion])
            impares += 1
        posicion += 1
    return valores_impares


def mostrar_posiciones_pares(valores):
    posiciones_pares = []
    for i in range(0, len(valores), 2):
        posiciones_pares.append(valores[i])
    return posiciones_pares

def mostrar_ordenados_sin_repetir(valores):
    valores_sin_repetir = []
    for valor in valores:
        if valor not in valores_sin_repetir:
            valores_sin_repetir.append(valor)
    valores_sin_repetir.sort()
    return valores_sin_repetir

def main():
    valores = ingresar_valores()
    if validar(valores):
        mostrar_valores("Valores ingresados:", valores)
        valores_pares = mostrar_hasta_tercer_impar(valores)
        if valores_pares == valores:
            mostrar_valores("Como no se encontraron 3 valores pares, se muestran todos los valores: ", mostrar_hasta_tercer_impar(valores))
        posiciones_pares = mostrar_posiciones_pares(valores)
        mostrar_valores("Valores en posiciones pares: ", posiciones_pares)
        sin_repetir = mostrar_ordenados_sin_repetir(valores)
        mostrar_valores("Valores ordenados sin repetir: ", sin_repetir)
    return

main()
