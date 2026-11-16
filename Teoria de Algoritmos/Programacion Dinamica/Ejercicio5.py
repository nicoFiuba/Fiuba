"""

EXPLICACIÓN_A: voy a usar un arreglo unidimensional OPT de tamaño N + 1, la celda OPT[i] guardará el valor booleano en base a si el bloque i se puede segmentar. Para calcular OPT[i] iteramos sobre todos los cortes y nos fijamos qué si: el corte es valido y si el resto del bloque es una palabra.

RELACION DE RECURRENCIA:
- Caso base: OPT[0] = True ya que un string vacio siempre se puede segmentar.

- Caso recursivo: Si i > 0 => OPT[i] = OR(OPT[j] and cadena[j:i] in palabras) para todo j en [0, i)

PSEUDOCÓDIGO
"""

def mensaje_valido(cadena, diccionario):

    n = len(cadena)
    if n == 0:
        return True

    OPT = [False] * (n + 1)
    OPT[0] = True

    for i in range(1, n + 1):
        j = 0
        while j < i and not OPT[i]:
            if OPT[j] and cadena[j:i] in diccionario:
                OPT[i] = True
            j += 1

    return OPT[n]

"""
ANÁLISIS DE COMPLEJIDAD
- Temporal: en el peor de los casos, el doble ciclo toma O(N²) y la verificación de la subcadena toma O(N). Por lo tanto, la complejidad temporal es O(N³).

- Espacial: O(N) para almacenar OPT .

EJEMPLO:
cadena = "osote", diccionario = ["te", "oso"]

OPT[0] = True
OPT[1] = OPT[j] and cadena[j:i] in diccionario = OPT[0] and cadena[0:1] in diccionario = True and "o" in ["te", "oso"] = True and False = False
OPT[2] = OPT[j] and cadena[j:i] in diccionario = OPT[0] and cadena[0:2] in diccionario = True and "os" in ["te", "oso"] = True and False = False
OPT[3] = OPT[j] and cadena[j:i] in diccionario = OPT[0] and cadena[0:3] in diccionario = True and "oso" in ["te", "oso"] = True and True = True
...
OPT[5] = OPT[j] and cadena[j:i] in diccionario = OPT[3] and cadena[3:5] in diccionario = True and "te" in ["te", "oso"] = True and True = True

El resultado final es OPT[5] = True, ya que "osote" se segmenta como "oso" + "te".
"""


""" 
EXPLICACIÓN_B: para que ahora el algoritmo evalue si la cadena corresponde a mas de un mensaje, tenemos que cambiar la definición de OPT[i] para que guarde una lista con todas las oraciones validas que se pueden formar en el corte. Para calcular OPT[i] iteramos sobre todos los cortes y nos fijamos si: el corte es valido y si el resto del bloque es una palabra, entonces agregamos la palabra a la lista de oraciones validas.

RELACION DE RECURRENCIA:
- Caso base: OPT[0] = [[]] ya que una lista con una lista vacia siempre se puede segmentar.

- Caso recursivo: Si i > 0 => para todo j en [0, i) si cadena[j:i] in diccionario => OPT[i] = OPT[i] + [oracion + cadena[j:i]] para cada oracion en OPT[j].

PSEUDOCÓDIGO
"""

def oraciones_validas(cadena, diccionario):

    n = len(cadena)
    if n == 0:
        return [[]]

    OPT = []
    for i in range(n + 1):
        OPT.append([])
    
    OPT[0] = [[]]

    for i in range(1, n + 1):
        for j in range(i):
            if cadena[j:i] in diccionario:
                for oracion in OPT[j]:
                    OPT[i].append(oracion + [cadena[j:i]])

    return OPT[n]

""" 
ANÁLISIS DE COMPLEJIDAD
- Temporal: en el peor de los casos, al haber multiples combinaciones de palabras, las posibles oraciones crecen exponencialmente. Por lo tanto, la complejidad temporal es O(2^N).

- Espacial: el arreglo OPT almacena una lista de listas, en donde cada lista puede tener hasta N elementos, por lo que la complejidad espacial es O(2^N * N).

EJEMPLO:
cadena = "ala", diccionario = ["a", "la", "ala"]

OPT[0] = [[]]
OPT[1] = cadena[j:i] in diccionario = cadena[0:1] in diccionario = "a" in ["a", "la", "ala"] = True => OPT[1] = OPT[1] + [oracion + [cadena[j:i]]] = [] + [[] + ["a"]] = [["a"]]
OPT[2] = cadena[j:i] in diccionario = cadena[0:2] in diccionario = "al" in ["a", "la", "ala"] = False => []
OPT[3] = cadena[j:i] in diccionario = cadena[0:3] in diccionario = "ala" in ["a", "la", "ala"] = True => OPT[3] = OPT[3] + [oracion + [cadena[j:i]]] = [] + [[] + ["ala"]] = [["ala"]]
OPT[3] = cadena[j:i] in diccionario = cadena[1:3] in diccionario = "la" in ["a", "la", "ala"] = True => OPT[3] = OPT[3] + [oracion + [cadena[j:i]]] = [["ala"]] + [["a"] + ["la"]] = [["ala"], ["a", "la"]]

El resultado final acumula todas las ramas exitosas: OPT[3] = [["ala"], ["a", "la"]].
"""
