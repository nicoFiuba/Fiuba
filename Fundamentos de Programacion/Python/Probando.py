"""
Se tienen los resultados de la Eurocopa y la Copa América en dos archivos de texto  con formato csv, llamados eurocopa.csv y copa_america.csv. Estos archivos tienen en cada linea, el resultado de un partido.
Los campos son:
    dia, equipo_local, goles_local, equipo_visitante, goles_visitante
Los archivos se guardaron en forma secuencial, comenzando desde el dia 1 del campeonato, por lo que están ordenados por dia.

Ejemplo

    1,Alemania,5,Escocia,1
    2,Hungria,1,Suiza,3
    2,Espania,3,Croacia,0
    2,Italia,2,Albania,2
    etc

1) Recorriendo una sola vez los dos archivos y sin cargarlos completamente en memoria, los unifique (merge con clave máxima) en un único archivo ordenado por dia, manteniendo el orden original y agregando un campo que indique de que archivo es la linea que se está escribiendo (EUROCOPA o COPA_AMERICA),  ante igualdad del dia, guardar en primer lugar los de Eurocopa.

2)	Realizando una lectura del archivo generado en el punto anterior, arme un diccionario en donde la clave será el país y el dato será una lista de longitud 3: partidos ganados, empatados y perdidos.

3)	En base al diccionario generado en el punto 2 armar un listado, ordenado de mayor a menor por cantidad de partidos ganados, indicando: país – partidos ganados. En este listado no deben figurar los países que no ganaron ningún partido.

"""

MAX_DIA = 100
MAX = str(MAX_DIA) + ",,,,"

def leer(archivo):
    linea = archivo.readline()
    if linea:
        linea = linea.strip()
    else:
        linea = MAX
    
    campos = linea.split(',')

    return (int(campos[0]), campos[1], campos[2], campos[3], campos[4])

def guardar(dia, equipo_local, goles_local, equipo_visitante, goles_visitante, torneo, archivo_salida):
    archivo_salida.write(f"{dia},{equipo_local},{goles_local},{equipo_visitante},{goles_visitante},{torneo}\n")

def merge(torneo1, torneo2, unificado):
    
    dia1, equipo_local1, goles_local1, equipo_visitante1, goles_visitante1 = leer(torneo1)
    dia2, equipo_local2, goles_local2, equipo_visitante2, goles_visitante2 = leer(torneo2)

    while dia1 < MAX_DIA or dia2 < MAX_DIA:
        minimo = min(dia1, dia2)

        while dia1 == minimo:
            guardar(dia1, equipo_local1, goles_local1, equipo_visitante1, goles_visitante1, 'EUROCOPA', unificado)
            dia1, equipo_local1, goles_local1, equipo_visitante1, goles_visitante1 = leer(torneo1)
        
        while dia2 == minimo:
            guardar(dia2, equipo_local2, goles_local2, equipo_visitante2, goles_visitante2, 'COPA_AMERICA', unificado)
            dia2, equipo_local2, goles_local2, equipo_visitante2, goles_visitante2 = leer(torneo2)
        
def unificar():
    eurocopa = open('eurocopa.csv', 'r')
    copa_america = open('copa_america.csv', 'r')
    union = open('unionx.csv', 'w')

    merge(eurocopa, copa_america, union)
    eurocopa.close()
    copa_america.close()
    union.close()

def crear_diccionario(archivo):
    diccionario = {}
    archivo = open('unionx.csv', 'r')
    linea = archivo.readline()
    while linea:
        campos = linea.strip().split(',')
        equipo_local = campos[1]
        goles_local = int(campos[2])
        equipo_visitante = campos[3]
        goles_visitante = int(campos[4])

        if equipo_local not in diccionario:
            diccionario[equipo_local] = [0, 0, 0]
        if equipo_visitante not in diccionario:
            diccionario[equipo_visitante] = [0, 0, 0]

        if goles_local > goles_visitante:
            diccionario[equipo_local][0] += 1
            diccionario[equipo_visitante][2] += 1
        elif goles_local < goles_visitante:
            diccionario[equipo_visitante][0] += 1
            diccionario[equipo_local][2] += 1
        else:
            diccionario[equipo_local][1] += 1
            diccionario[equipo_visitante][1] += 1

        linea = archivo.readline()
    archivo.close()
    return diccionario

def ordenar_diccionario(diccionario):
    lista_a_ordenar = []

    for equipo, resultados in diccionario.items():
        if resultados[0] >= 1:
            lista_a_ordenar.append((equipo, resultados[0]))
    
    diccionario_ordenado = sorted(lista_a_ordenar, key=lambda x: x[1], reverse=True)
    return diccionario_ordenado            


def imprimir_diccionario(diccionario_ordenado):
    print("Pais - Partidos Ganados")
    for equipo, ganados in diccionario_ordenado:
        print(f"{equipo} - {ganados}")


def main():
    unificar()
    diccionario = crear_diccionario('unionx.csv')
    diccionario_ordenado = ordenar_diccionario(diccionario)
    imprimir_diccionario(diccionario_ordenado)

main()