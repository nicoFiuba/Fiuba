"""
1) Escribir una funcion que reciba una cadena de caracteres que representa un alias bancario. La funcion debera devolver True or False, en base a haber evaluado que dicho alias esta bien formado. Se debe controlar que:
    a. Que tenga entre 6 y 20 caracteres.
    b. Que solo se utilizan letras, numeros, guion del medio y punto.
    c. Que los puntos y el guion del medio no se encuentren en la primera, ni la ultima posicion.
    d. Que tenga al menos 4 letras
De los metodos de la clase cadena, solo se puede usar el metodo isalpha. Se deben evitar ciclos innecesarios
"""

""" 
def alias_valido(cadena):
    valido = True
    while valido and (len(cadena) < 6 or len(cadena) > 20):
        valido = False
        if ("." or "-") in (cadena[0] or cadena[19]): #No funciona asi IN No necesarioamente la cadena tiene largo 19
            valido = False
        if cadena.isalpha():
            for caracter in cadena: #No! Por cada caracter del while se ejecuta este for que vuelve a recorrer la cadena mal
                letras += 1
                if letras <= 4:
                    valido = False
        else:
            valido = False
    return valido

def main():
    cadena = input("Ingrese un alias: ")
    if alias_valido(cadena):
        print("El alias es valido")
    else:
        print("El alias no es valido")
main()
"""

"""
2) Escribir una funcion elegir_comidas en Python que reciba una lista de listas, cada sublista es una comida, en donde el primer elemento es el nombre de la comida y los siguientes elementos los respectivos ingredientes. Tambien recibe una lista de ingredientes prohibidos. Debe devolver una lista con los nombres de las comidas permitidas (no deben contener ingredientes prohibidos).
    Ejemplo:
        comidas = ["milanesa", "bifes de nalga", "pan rallado", "huevo"], 
        ["ravioles", "harina", "espinaca", "ricota"],["pizza", "queso", "harina", "tomate", "aceitunas"]]
    prohibidos_1 = ["huevo", "nueces", "aceitunas"]
    prohibidos_2 = ["huevo", "nueces"]
    elegir_comidas(comidas, prohibidos_1) => ["ravioles"]
    elegir_comidas(comidas, prohibidos_2) => ["ravioles", "pizza"]
Testea la funcion con DOS casos usando doctest, con 2 listas de prohibidos distintas a las del ejemplo.
"""

"""
import doctest

def elegir_comidas(comidas, prohibidos_1, prohibidos_2):
    comida_valida = True
    while comida_valida: #Este while no hace nada
        for com in comidas: #Falta un while interno para recorrer los ingredientes de la comida
            if com in prohibidos_1:
                comida_valida = False
            elif com in prohibidos_2:
                comida_valida = False
            else:
                comidas_validas = []
                comidas_validas.append(com)
    return comidas_validas

def prueba_elegir_comidas(): # El doctest va dentro de la funcion que se prueba
    """
    #>>> elegir_comidas(comidas, prohibidos_1)
    #["ravioles"]
    #>>> elegir_comidas(comidas, prohibidos_2)
    #["ravioles", "pizza"]
"""

def main():
    comidas = [["milanesa", "bifes de nalga", "pan rallado", "huevo"], ["ravioles", "harina", "espinaca", "ricota"], ["pizza", "queso", "harina", "tomate", "aceitunas"]]
    prohibidos_1 = ["huevo", "nueces", "aceitunas"]
    prohibidos_2 = ["huevo", "nueces"]
    print(doctest.testmod())
    print(elegir_comidas(comidas, prohibidos_1))
    print(elegir_comidas(comidas, prohibidos_2))
main()
 """

"""
3) Se cuenta con una lista de votacion, ya cargada, que contiene sublistas. Cada una de esas sublistas tiene los siguientes valores: partido(string), nro. de mesa(entero), diputados(entero), senadores(entero). 
Ejemplo: [["PP", 2, 19, 35], ["PSOE", 13, 20, 30], ["PP", 5, 0, 15], ["VOX", 5, 10, 13], ["PP", 13, 9, 5], ...]
Los recuentos son de diferentes mesas por lo que los nombres de los partidos apareceran varias veces. Se pide que escribas un programa modular en Python(compuesto por funciones), que procese la lista de votacion una unica vez y:
    1. Obtenga la lista de votacion invocando a la funcion obtener_votos de la libreria votacion2024.
    2. Genere un diccionario con clave partido y valores total_diputados, total_senadores.
    3. Imprima un listado de los partidos con el respectivo total de votos obtenidos(diputados + senadores) y el porcentaje que representa el total de votos obtenidos sobre el total general, ordenados de mayor a menor por el total de votos obtenidos. El listado debe tener un formato de 3 columnas.
    4. Informe el total de mesas escrutadas.
"""

""" 
import obtener_votos from votacion2024 #Falta modularizar

elecciones = {"clave partido": , "total_diputados": , "total_senadores": }

def partidos_con_votos(elecciones):
    for partido in lista_votaciones: # Mal, Solo se podia recorrer la lista inicial una unica vez
        if partido != " ":
            elecciones["clave partido"] += "partido"
    for diputados in lista_votaciones:
        if diputados > 0: # No se entiende la estructura del codigo
            elecciones["total_diputados"] += "diputados"
    for senadores in lista_votaciones:
        if senadores > 0:
            elecciones["total_senadores"] += "senadores"
    for elecciones["clave partido"] in elecciones:
        print(f"El nombre del partido es: {elecciones['clave partido']} y sus votos obtenidos son {elecciones['total_diputados'] + elecciones['total_senadores']}")
        #Falta ordenar e imprimir en el formato pedido
        # Es innecesario tantos for
#Falta codigo xd pero bue
"""
