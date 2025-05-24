""" 
Una funcion que reciba una cadena de caracteres que representa na direccion de mail. La funcion debera devolver True or false tras haber evaluado que dicha direccion de mail esta bien formada. Se debe controlar que:
    a. Que solo se utilicen letras (no acentuadas) y/o numeros para la parte del nomre,delante de la @
    b. Que haya exactamente una @ (no puede estar ni en la primera, ni en la ultima posicion)
    c. Que los nombres del dominio (lo que esta a continuacion de la @) se encuentre en la lista de dominios_validos que se obtiene invocando a la funcion obtener_dominios contenida en la libreriaa dominios.py. La lista es del tipo ["gmail.com", "fi.uba.ar"]
    d. Que tenga como maximo 30 caracteres totales
    De los metodos de la clase cadena, solo se pueden usar los metodos isalpha y find
    Se deben evitar ciclos innecesarios
    """

""" 
Escribir una funcion que reciba 3 listas que tendran mediciones diarias de valores para distintas personas. La 1ra lista es de temperauras corporales, la 2da es de presencia de tos seca y la 3ra es del nivel de cansancio (medidio del 1 al 10). La funcion tiene que devolver una lista con los indices (posiciones), que son los sospechosos de COVID-19 con temperaura mayor igual a 37 grados, presencia de tos y nivel de cancancio mayor a 6.
Ejemplos de Casos:
prueva_covid([35.6, 36.4, 35.2, 37.1], [True, False, True, True], [7, 2, 6, 8]) devuelve [3]
prueva_covid([38], [False], [9]) devuelve []
prueva_covid([40.2, 35.7, 38.4, 37.0], [True, False, True, True], [10, 2, 7, 8]) devuelve [0, 2, 3]
"""

""" 
Escribir un programa compuesto por funciones en Python que:
    1. Procese una lista de listas, condatos de partidos de futbol y genere un diccionario "campeonato". La lista "partidos" contiene sublistas con tres valores: el primer y segundo valor son los nombres de los equipos y el tercer valor podra ser: 0 o 1 para indicar la posicion del equipo ganador, o 2 para indicar empate. Los nombres de los equipos pueden repetirse. El diccionario "campeonato" debera tener por clave el nombre del equipo y como valor, una terna compuesta por: partidos ganados (primer valor), partidos perdidos (segundo valor) y partidos empatados (tercer valor).
    2. Informe el o los equipos con mas partidos jugados.
    3. Muestre por pantalla de mayor a menor, los equipos con sus puntajes, teniendo en cuenta que por cada partido ganado se obtienen 3 puntos, y un punto por cada partido empatado. Los datos deben mostrarse en dos columnas, una para el euipo y otra para el puntaje.
"""