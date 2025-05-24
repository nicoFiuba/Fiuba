# 1) Escribir una función que reciba por parámetro un diccionario con el siguiente formato: { id_producto: [ stock_minimo, stock_actual ],..........}, donde el id_producto será la clave, de tipo cadena; y la lista asociada a cada clave id_producto, contendrá una dupla de valores, siendo el primero, el stock mínimo a mantener de dicho producto; y el segundo, el stock actual del producto; ambos de tipo entero positivo. La función debe imprimir un listado con los productos a reponer (cuyo stock_actual sea menor al stock_minimo), indicando el id_producto y la cantidad a reponer.

""" Se me borro lo que habia hecho"""

# 2) Escribir una función que reciba por parámetro un texto, y devuelva un diccionario, el cual tendrá como claves, cada una de las palabras que hay en el texto, y como valor, la cantidad de ocurrencias de dicha palabra en el texto. No distinguir entre mayúsculas y minúsculas. Considerar que las palabras del texto estarán separadas por blancos.

""" Se me borro lo que habia hecho"""

# 3) Dado el diccionario "dic_materias" que tiene cargados los nombre de las materias como clave, y como valor asociado, una lista con tres números enteros, que indican: la cantidad de alumnos anotados (como primer valor), cantidad de alumnos que rindieron el parcial (segundo valor), cantidad de alumnos que aprobaron el parcial (tercer valor). Se pide que escribas:
    # a) Una función que reciba el diccionario y devuelva una lista con las materias cuyo índice de deserción sea mayor al 50% (esto se calcula teniendo en cuenta la cantidad de alumnos que rindieron el parcial sobre la cantidad de anotados).
    # b) Una función que reciba el diccionario y que devuelva una lista de tuplas, formadas por pares (materia, porcentaje_aprobados), ordenada de mayor a menor por porcentaje de aprobados (en este caso, se calcula sobre la cantidad que rindieron).

""" Se me borro lo que habia hecho"""

# 4) Escribir un programa que solicite el ingreso de un texto y luego informe un ranking de las palabras que aparecen en el texto. El texto ingresado debe tener como mínimo 20 palabras. En caso de no tener las palabras suficientes, solicitar se ingrese más texto, que debe ser agregado al ya existente. Considere palabras que sólo estén formadas por letras. Tenga en cuenta que seguido a una palabra, pueden estar los siguientes signos de puntuación: “,;.:”, en este caso, se debe quitar el signo. No debe diferenciar entre mayúsculas y minúsculas, por ejemplo: si aparecen en el texto las siguientes palabras: “sol”, “Sol”, “SOL”; se deben contabilizar 3 ocurrencias de la palabra “sol” como clave. No utilice métodos tales como count, find, index. Imprima el ranking, ordenado descendentemente, por la cantidad de ocurrencias de la palabra. 

""" Se me borro lo que habia hecho"""

# 5) Escribir un programa que permita gestionar los datos de los alumnos de un curso. El programa deberá:
    # a) Permitir la carga de un diccionario, que tendrá por clave un número de padrón, y por valores asociados a la clave, una lista compuesta por valores numéricos, que serán las notas obtenidas por un alumno. En cada ingreso, se deberá solicitar el padrón y la nota a cargar. Si el padrón es existente, se agregará la nota a la lista de notas; sino, se creará la clave padrón correspondiente con la nota asociada. Validar que el padrón sea un número entero entre 1 y 10000; y la nota entre 0 y 10. El ingreso finaliza cuando el padrón ingresado sea igual a cero.
    # b) Informar mediante un listado, la nota promedio de cada alumno, ordenado por padrón.
    # c) Informar que alumnos aprobaron la materia y que porcentaje representan. Para aprobar la materia, es necesario que en la lista de notas, al menos, haya 2 notas mayores o iguales a 4. Informar asociado a cada padrón, la nota promedio resultante de sumar sólo los valores mayores ó iguales a 4.
    # d) En base al punto anterior, informar un ranking de notas, indicando la nota promedio de aprobación, y la cantidad de alumnos que la obtuvieron; ordenado por la cantidad de alumnos.

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

def calcular_promedio(alumnos):
    promedio = []
    for legajo, notas in alumnos.items():
        if len(notas) > 0:
            promedio.append((legajo, sum(notas) / len(notas)))
    return promedio

def alumnos_aprobados(alumnos):
    aprobados = []
    for legajo, notas in alumnos.items():
        if len(notas) >= 2:
            sum(notas)
            if sum(notas) >= 8:
                aprobados.append((legajo, sum(notas) / len(notas)))
    aprobados.sort(key=lambda x: x[1], reverse=True)
    return aprobados

def main():
    alumnos = cargar_alumnos()
    if len(alumnos) > 0:
        print("Promedio de cada alumno:")
        for legajo, promedio in calcular_promedio(alumnos):
            print(f"Legajo: {legajo}, Promedio: {promedio:.2f}")
        
        print("Alumnos aprobados:")
        for legajo, promedio in alumnos_aprobados(alumnos):
            print(f"Legajo: {legajo}, Promedio de aprobación: {promedio:.2f}")
    else:
        print("No se ingresaron alumnos.")
    return
main()

# 6) Escribir un programa, compuesto por funciones, que permita:
    # a) Ingresar en un diccionario, localidades (como clave) y dos datos: cantidad de habitantes y cantidad de hospitales públicos (HP). Los datos surgen de distintas planillas, por lo que una misma clave (localidad) se puede ingresar varias veces, debiendo sumarse los valores.
    # b) Listar el total de habitantes y HP para cada localidad.
    # c) Imprimir un listado ordenado de mayor a menor de las 5 localidades de mayor relación: (habitantes / HP). Indicar la Localidad y la relación resultante.

def cargar_localidades():
    localidades = {}
    continuar = True

    while continuar:
        localidad = input("Ingrese la localidad (FIN para terminar): ")
        if localidad == "FIN":
            continuar = False
        else:
            habitantes = int(input("Ingrese la cantidad de habitantes: "))
            hospitales = int(input("Ingrese la cantidad de hospitales públicos: "))
            if localidad in localidades:
                localidades[localidad]["habitantes"] += habitantes
                localidades[localidad]["hospitales"] += hospitales
            else:
                localidades[localidad] = {"habitantes": 0, "hospitales": 0}

    return localidades

def ordenar_localidades(localidades):
    localidades_ordenadas = sorted(localidades.items(), key=lambda x: (x[1]["habitantes"] / x[1]["hospitales"]), reverse=True)
    return localidades_ordenadas[:5]

def main():
    localidades = cargar_localidades()
    localidades_ordenadas = ordenar_localidades(localidades)
    print(" Localidades - Habitantes - Hospitales")
    for localidad, datos in localidades.items():
        print(f"{localidad} - {datos['habitantes']} - {datos['hospitales']}")
    print("Top 5 localidades por relación habitantes/hospitales:")
    for localidad, datos in localidades_ordenadas:
        relacion = datos["habitantes"] / datos["hospitales"]
        print(f"{localidad} - Relación: {relacion:.2f}")
        print (f"{localidad}")
main()  

# 7) Escribir un programa que permita administrar los datos de una votación electoral. Para ello, será necesario que nuestro programa cumpla los siguiente requerimientos:
    # a) Gestionar la carga de datos de la votación, almacenando los datos en un diccionario de diccionarios, que tendrá el siguiente formato: { provincia: { partido_politico: votos_obtenidos ,,,,,} ,,,,} Por cada una de las provincias, tendremos la cantidad de votos obtenidos por cada uno de los partidos políticos. La carga de datos debe solicitar, la Provincia, el Partido Político, y la cantidad de votos. Puede haber más de un ingreso de cantidad de votos, para una misma Provincia y Partido Político, en ese caso se deben acumular a los ya existentes. La carga finaliza cuando se ingrese como nombre de Provincia, la palabra FIN.
    # b) Informar para cada Provincia que Partido obtuvo más votos, indicando la cantidad de votos y el porcentaje que representan sobre el total de las votaciones de la provincia. El listado debe estar ordenado por el nombre de la Provincia.
    # c) Informar el ranking de votos a nivel Nacional por Partido Político. El listado debe estar ordenado de mayor a menor por la cantidad de votos obtenidos, y debe figurar el Partido Político, la cantidad de votos obtenidos, y el porcentaje respecto del total de votos. 


def cargar_votacion():
    votacion = {}
    continuar = True

    while continuar:
        provincia = input("Ingrese la provincia (FIN para terminar): ")
        if provincia == "FIN":
            continuar = False
        else:
            partido = input("Ingrese el partido político: ")
            votos = int(input("Ingrese la cantidad de votos: "))
            if provincia not in votacion:
                votacion[provincia] = {}
            if partido not in votacion[provincia]:
                votacion[provincia][partido] = {"votos": 0}
            votacion[provincia][partido]["votos"] += votos
    return votacion

def ordenar_por_votos(votacion):
    votos_totales = {}
    for provincia, partidos in votacion.items():
        total_votos = sum(partido["votos"] for partido in partidos.values())
        votos_totales[provincia] = total_votos
    return votos_totales

def calcular_porcentaje(votacion, votos_totales):
    resultados = {}
    for provincia, partidos in votacion.items():
        total_votos = votos_totales[provincia]
        for partido, datos in partidos.items():
            votos = datos["votos"]
            porcentaje = (votos / total_votos) * 100
            if provincia not in resultados:
                resultados[provincia] = []
            resultados[provincia].append((partido, votos, porcentaje))
    return resultados

def main():
    votacion = cargar_votacion()
    votos_totales = ordenar_por_votos(votacion)
    resultados = calcular_porcentaje(votacion, votos_totales)

    # Ordenar provincias alfabéticamente
    print("Resultados por provincia:")
    for provincia in sorted(resultados.keys(), key=lambda x: x):
        partidos = resultados[provincia]
        partidos.sort(key=lambda x: x[1], reverse=True)  # Ordenar partidos por votos
        partido_ganador = partidos[0]
        print(f"Provincia: {provincia}, Partido: {partido_ganador[0]}, Votos: {partido_ganador[1]}, Porcentaje: {partido_ganador[2]:.2f}%")
    
    # Calcular ranking nacional
    print("Ranking Nacional por Partido Político:")
    ranking_nacional = {}
    for provincia, partidos in votacion.items():
        for partido, datos in partidos.items():
            if partido not in ranking_nacional:
                ranking_nacional[partido] = {"votos": 0}
            ranking_nacional[partido]["votos"] += datos["votos"]
    
    total_votos_nacional = sum(datos["votos"] for datos in ranking_nacional.values())
    ranking = sorted(ranking_nacional.items(), key=lambda x: x[1]["votos"], reverse=True)  # Ordenar por votos

    for partido, datos in ranking:
        porcentaje = (datos["votos"] / total_votos_nacional) * 100
        print(f"Partido: {partido}, Votos: {datos['votos']}, Porcentaje: {porcentaje:.2f}%")
