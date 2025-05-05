
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

