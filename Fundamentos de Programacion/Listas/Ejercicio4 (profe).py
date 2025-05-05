"""
SON LAS SOLUCIONES DEL PROFE, NO SON LAS UNICAS POSIBLES
Ejercicio 1
Escribir una función que reciba una palabra, y devuelva True, si la palabra tiene diptongo, y False, en caso contrario. Asumir que la palabra recibida, solo esta formada por letras. En español dos vocales en contacto se articulan como diptongo cuando:
    1. una es cerrada (i u) átona (no acentuada) y la otra es abierta (a e o) y viceversa.
    2. ambas son cerradas, excepto si son iguales (como en chiita), donde forman un hiato
"""
import doctest

def hay_diptongo(palabra):
    """
    Funcion que recibe una palabra y retorna True si la misma tiene diptongo, o False, si no lo tiene.
    >>> hay_diptongo("ciudad")
    True
    >>> hay_diptongo("autódromo")
    True
    >>> hay_diptongo("ruido")
    True
    >>> hay_diptongo("audiovisual")
    True
    >>> hay_diptongo("cual")
    True
    >>> hay_diptongo("renuncia")
    True
    >>> hay_diptongo("renunciá")
    True
    >>> hay_diptongo("renuncié")
    True
    >>> hay_diptongo("renunció")
    True
    >>> hay_diptongo("manual")
    True
    >>> hay_diptongo("ruiseñor")
    True
    >>> hay_diptongo("ansioso")
    True
    >>> hay_diptongo("ansiedad")
    True
    >>> hay_diptongo("estación")
    True
    >>> hay_diptongo("silla")
    False
    >>> hay_diptongo("mesa")
    False
    >>> hay_diptongo("búho")
    False
    """

    # Armado de la lista de posibles diptongos segun definicion
    l_diptongo = []
    for letra_1 in ["u", "i"]:
        for letra_2 in ["a", "e", "o", "á", "é", "ó"]:
            l_diptongo.append( letra_1 + letra_2 )
            l_diptongo.append( letra_2 + letra_1)
    l_diptongo.extend(["ui", "iu"])

    # Control de si alguno de los diptongos forma parte de la palabra
    devolver = True
    posicion = 0
    while posicion < len(l_diptongo) and l_diptongo[posicion] not in palabra:
        posicion += 1
    if posicion == len(l_diptongo):
        devolver = False
    return devolver

#----------------------- Bloque Principal ---------------------------#
import doctest
doctest.testmod()

"""
Ejercicio 2
Escribir una función que reciba un texto y devuelva una lista anidada que representa un ranking de palabras. El texto puede tener gran cantidad de palabras.
La función deberá devolver una lista anidada, en la que cada sublista, esté formada por un par [palabra, cantidad de veces en el texto], ordenada por la cantidad de veces que aparece la palabra. Las palabras sólo deben aparecer una vez en la lista.
"""

def generar_ranking_palabras(texto):
    l_palabras = texto.split()
    if l_palabras:
        # Inicializo el ranking con la 1er. palabra del texto
        l_ranking = [[l_palabras[0].lower(), 0]]
    else:
            # Si el texto no tiene palabras, el ranking se devuelve vacio
            l_ranking = []
    for palabra in l_palabras:
        pos = 0
        while pos < len(l_ranking) and l_ranking[pos][0] != palabra.lower():
            pos += 1
        if pos == len(l_ranking):
            l_ranking.append([palabra.lower(), 1])
        else:
            l_ranking[pos][1] += 1
        l_ranking.sort(key = lambda dupla : dupla[1])
    return l_ranking

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

def generar_lista():
    print("Ingreso de Valores - Finalice ingresando 0", end ="\n\n")
    lista = []
    valor = int(input("Valor: "))
    while (valor != 0):
        lista.append(valor)
        valor = int(input("Valor: "))
    return lista

def mostrar(titulo, lista):
    print("\n", titulo)
    for elemento in lista:
        print("\t", elemento)

def generar_3er_impar(lista):
    lista_3er_impar = []
    cant_imp = 0
    posicion = 0
    while ((cant_imp < 3) and (posicion < len(lista))):
        lista_3er_impar.append(lista[posicion])
        if (lista[posicion]%2 == 1):
            cant_imp += 1
        posicion += 1
    return lista_3er_impar

def generar_pos_pares(lista):
    lista_pos_pares = []
    for posicion in range(0, len(lista), 2):
        lista_pos_pares.append(lista[posicion])
    return lista_pos_pares

def generar_ord_sin_dup(lista):
    lista_ord = sorted(lista)
    lista_ord_sin_dup = []
    anterior = 0
    for elemento in lista_ord:
        if elemento != anterior:
            lista_ord_sin_dup.append(elemento)
            anterior = elemento
    return lista_ord_sin_dup

#-------------------------- Bloque Principal --------------------------#
l_original = generar_lista() #Punto 1
mostrar("Datos Ingresados", l_original) #Punto 2
l_3er_impar = generar_3er_impar(l_original) #Punto 3
mostrar("Datos hasta 3er. Valor Impar", l_3er_impar)
l_pos_pares = generar_pos_pares(l_original) #Punto 4
mostrar("Datos en posiciones pares", l_pos_pares)
l_ord_sin_dup = generar_ord_sin_dup(l_original) #Punto 5
mostrar("Datos ordenados sin duplicados", l_ord_sin_dup) 