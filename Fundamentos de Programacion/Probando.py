"""
1) Escribir una funcion que reciba una cadena de caracteres que representa un alias bancario. La funcion debera devolver True or False, en base a haber evaluado que dicho alias esta bien formado. Se debe controlar que:
    a. Que tenga entre 6 y 20 caracteres.
    b. Que solo se utilizan letras, numeros, guion del medio y punto.
    c. Que los puntos y el guion del medio no se encuentren en la primera, ni la ultima posicion.
    d. Que tenga al menos 4 letras
De los metodos de la clase cadena, solo se puede usar el metodo isalpha. Se deben evitar ciclos innecesarios
"""
def validar(alias):
    contador_letras = 0
    valido = True
    # a. Que tenga entre 6 y 20 caracteres.
    if len(alias) < 6 or len(alias) > 20:
        valido = False
    # c. Que los puntos y el guion del medio no se encuentren en la primera, ni la ultima posicion.
    elif alias[0] == "." or alias[-1] == "."  or  alias[0] == "-" or alias[-1] == "-":
        valido = False
    # b. Que solo se utilizan letras, numeros, guion del medio y punto.
    else:
        for caracter in alias:
            if not (caracter.isalpha() or caracter in "0123456789.-"):
                valido = False
            elif caracter.isalpha():
                contador_letras += 1
        # d. Que tenga al menos 4 letras
        if valido and contador_letras < 4:
            valido = False
    return valido

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
import doctest

def elegir_comidas(comidas, prohibidos):
    """ 
    >>> elegir_comidas(comidas, prohibidos_3)
    ['ravioles', 'pizza']
    >>> elegir_comidas(comidas, prohibidos_4)
    ['milanesa', 'pizza']
    """
    
    comidas_permitidas = []
    for comida in comidas:
        permitida = True
        for i in range(1, len(comida)):
            if comida[i] in prohibidos:
                permitida = False
        if permitida:
            comidas_permitidas.append(comida[0])
    return comidas_permitidas

comidas = [["milanesa", "bifes de nalga", "pan rallado", "huevo"], 
        ["ravioles", "harina", "espinaca", "ricota"],["pizza", "queso", "harina", "tomate", "aceitunas"]]
prohibidos_1 = ["huevo", "nueces", "aceitunas"]
prohibidos_2 = ["huevo", "nueces"]
prohibidos_3 = ["pan rallado"]
prohibidos_4 = ["ricota"]
print(elegir_comidas(comidas, prohibidos_1))
print(doctest.testmod())


"""
3) Se cuenta con una lista de votacion, ya cargada, que contiene sublistas. Cada una de esas sublistas tiene los siguientes valores: partido(string), nro. de mesa(entero), diputados(entero), senadores(entero). 
Ejemplo: [["PP", 2, 19, 35], ["PSOE", 13, 20, 30], ["PP", 5, 0, 15], ["VOX", 5, 10, 13], ["PP", 13, 9, 5], ...]
Los recuentos son de diferentes mesas por lo que los nombres de los partidos apareceran varias veces. Se pide que escribas un programa modular en Python(compuesto por funciones), que procese la lista de votacion una unica vez y:
    1. Obtenga la lista de votacion invocando a la funcion obtener_votos de la libreria votacion2024.
    2. Genere un diccionario con clave partido y valores total_diputados, total_senadores.
    3. Imprima un listado de los partidos con el respectivo total de votos obtenidos(diputados + senadores) y el porcentaje que representa el total de votos obtenidos sobre el total general, ordenados de mayor a menor por el total de votos obtenidos. El listado debe tener un formato de 3 columnas.
    4. Informe el total de mesas escrutadas.
"""

def cargar_alumnos():
    alumnos = {}
    continuar_legajos = True

    while continuar_legajos:
        legajo = int(input("Ingrese el padrón del alumno (0 para terminar): "))
        if legajo == 0:
            print("Fin de la carga de legajos")
            continuar_legajos = False
        elif legajo < 1 or legajo > 10000:
            print("Padrón inválido. Debe estar entre 1 y 10000.")
        else:
            if legajo not in alumnos:
                alumnos[legajo] = []

            continuar_notas = True
            while continuar_notas:
                nota = int(input("Ingrese la nota del alumno (0-10): "))
                if nota < 0 or nota > 10:
                    print("Nota inválida. Debe estar entre 0 y 10.")
                elif nota == 0:
                    print("Fin de la carga de notas para este alumno.")
                    continuar_notas = False
                else:
                    alumnos[legajo].append(nota)
                    mas_notas = input("¿Desea agregar otra nota? (s/n): ")
                    if mas_notas == "n":
                        print("Fin de la carga de notas para este alumno.")
                        continuar_notas = False

        if continuar_legajos: 
            mas_legajos = input("¿Desea agregar otro legajo? (s/n): ")
            if mas_legajos == "n":
                print("Fin de la carga de legajos")
                continuar_legajos = False

    return alumnos