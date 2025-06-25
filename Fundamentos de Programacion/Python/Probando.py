"""
MANEJO DE ARCHIVOS EN PYTHON

1) Se tienen los resultados de la Eurocopa y la Copa America en dos archivos de texto con formato csv, llamados eurocopa.csv y copa_america.csv. Estos archivos tienen en cada linea, el resultado de un partido. Los campos son:
    dia,equipo_local,goles_local,equipo_visitante,goles_visitante
Los archivos se guardan en forma secuencial, comenzando desde el dia 1 del campeonato, por lo que estan ordenados por dia. Ejemplo:
    1,Alemania,5,Escocia,1
    2,Hungria,1,Suiza,3
    2,Espania,3,Croacia,0
    2,Italia,2,Albania,1
    etc...

Se pide realizar un programa modular (compuesto por funciones), en Python que:
    - Recorriendo una sola vez los dos archivos, y sin cargarlos completamente en memoria, los unifique (merge) en un unico archivo ordenado por dia, manteniendo el orden original y agregando un campo que indique de que archivo es la linea que se esta escribiendo (EUROCOPA o COPA AMERICA), ante igualdad de dia, guardar en primer lugar los partidos de la EUROCOPA.

2) El famoso torneo de tenis Roland Garros se disputa todos los años. Los resultados se guardan en el archivo resultados.csv. Este archivo tiene el siguiente formato:
    dia,participante1,puntos1_sets,participante2,puntos2_sets
El archivo se guarda en forma secuencial, comenzando desde el dia 1 del campeonato, por lo que queda ordenado por dia. Los partidos se juegan al mejor de cinco sets, en caso de ganar los tres primeros, no hace falta jugar los dos que le siguen, es por lo que hay partidos de tres, de cuatro y de cinco sets. Ejemplo:
    1,Jarry Nicolas,6-6-6,Dellien Hugo,4-4-2
    1,Purcel Max,7-1-6-6,Thompson Jordan,5-6-4-4
    2,Zapata Miralles,6-7-2-0-4,Schwartzman Diego,1-6-6-6-6
    etc...

Se pide realizar un programa modular (compuesto por funciones), en Python que:
    - Recorriendo una sola vez el archivo de resultados y sin cargarlo completamente en memoria, haga un corte por dia, indicando: dia, cantidad de partidos jugados, cantidad de sets jugados.
    Con nuestro ejemplo seria:
        Dia          Partidos          Sets
        1                   2                  7
        2                   1                  5
        Etc.

3) Durante el año 2023, la Facultad de Ingenieria ha dictado cursos para el plan Argentina Programa 4.0. En el segundo tramo del programa, se ofrecieron los cursos de: Python, Java, Programacion Front End, Programacion Back End y Testing. Cada uno de estos cursos tenia entre 2 y hasta 6 comisiones, con 120 alumnos en promedio por comisión. 
el archivo inscriptos_AP40.csv, posee los siguientes datos:
    Nro_Inscripto,Nivel_Educativo,Trabaja_Actualmente,Nombre_Curso,Codigo_Comision
Se encuentra ordenado por Curso y dentro de este por Comision.
Escribir un programa modular (compuesto por funciones), en Python, que en base a los datos que se encuentran en el archivo inscriptos_AP40.csv, genere:
    - Recorriendolo solo una vez el archivo, un informe indicando el nombre del curso, y para cada curso, las comisiones y la cantidad de alumnos inscriptos en cada una de las comisiones. Ademas por cada curso debe informar el total de alumnos inscriptos. Al final del listado se debe informar el total de alumnos inscriptos en todos los cursos, y que porcentaje de estos trabaja (este dato viene indicado con un "si", en el respectivo campo)
        
4) En una materia de un posgrado, se aplica evalucion continua. Esto consiste en pedir la entrega de actividades semanales. En una semana puede haber ninguna, una o varias actividades. Los resultados se guardan en un archivo notas.txt (CSV) con el siguiente formato (a excepcion de la primera linea, en donde figura la cantidad de trabaajos totales):
    semana,actividad,apellido_nombre,nota
Ejemplo:
5
1,cuestionario t1,Gonzalez Carlos,5
1,cuestionario t1,Rodriguez Rosa,8
1,trabajo practico t1,Rodiguez Rosa,10
3,cuestionario t2,Gonzalez Carlos,4
...

En el ejemplo anterior, el docente pidio 5 trabajos en total (primer linea). En la semana 1 se entregaron dos cuestionarios y un trabajo practico, con notas, 5, 8 y 10, etc.
Sabiendo que el archivo esta ordenado por semana y dentro de cada semana, por actividad, y que la aprobacion es con nota de 6 o superior, se pide realizar un programa modular en Pyhton que:
    - Recorriendo una sola vez el archivo notas.txt y sin cargarlo completamente en memoria, haga un corte de control por dia y por actividad, indicando: cantidad de actividades semanales entregadas y dentro de cada actividad, cantidad de entregados y aprobados. Tomando el ejemplo anterior seria:
        Semana 1:
        -- cuestionario t1: entregados: 2 - aprobados: 1
        -- trabajo practico t1: entregados: 1 - aprobados: 1
        - Total de actividades semanales entregadas: 3

5) Durante el año 2023, la Facultad de Ingenieria ha dictado cursos para el plan Argentina Programa 4.0. En el segundo tramo del programa, se ofrecieron los cursos de: Python, Java, Programacion Front End, Programacion Back End y Testing. Cada uno de estos cursos tenia entre 2 y hasta 6 comisiones, con 120 alumnos en promedio por comisión. El archivo inscriptos_AP40.csv, posee los siguientes datos:
    Nro_Inscripto,Nivel_Educativo,Trabaja_Actualmente,Nombre_Curso,Codigo_Comision
Se encuentra ordenado por Curso y dentro de este por Comision.
Escribir un programa modular (compuesto por funciones), en Python, que en base a los datos que se encuentran en el archivo inscriptos_AP40.csv, genere:
    - Recorriendo solo una vez el archivo y teniendo en cuenta que el mismo no entra completo en memoria, un informe indicando el nombre del curso, y para cada curso, las comisiones y la cantidad de alumnos inscriptos en cada una de las comisiones. Ademas por cada curso debe informar el total de alumnos inscriptos. Al final del listado se debe informar el total de alumnos inscriptos en todos los cursos, y que porcentaje de estos trabaja (este dato viene indicado con un "si", en el respectivo campo).
    Al mismo tiempo, genere el archivo trabajan.csv, con todos los datos de solo los que trabajan, omitiendo el campo Trabaja_Actualmente.
        

"""
"""
MAX = "zzz,zzz,zzz,zzz,zzz"

def leer(archivo):
    
    linea = archivo.readline()
    
    if linea:
        linea = linea.strip()
    else:
        linea = MAX
    
    campos = linea.split(",")

    return int(campos[0]), campos[1], campos[2], campos[3], campos[4]

def corte_de_control(archivo):

    _, _, Trabaja_Actualmente, Nombre_Curso, Codigo_Comision = leer(archivo)

    alumnos_totales = 0
    alumnos_que_trabajan = 0

    while Nombre_Curso != "zzz":
        curso_actual = Nombre_Curso
        alumnos_por_curso = 0

        print(f"Curso: {curso_actual}")

        while Nombre_Curso == curso_actual:
            comision_actual = Codigo_Comision
            alumnos_por_comision = 0

            while Nombre_Curso == curso_actual and Codigo_Comision == comision_actual:
                alumnos_por_comision += 1
                alumnos_por_curso += 1
                alumnos_totales += 1
                
                if Trabaja_Actualmente.lower() == "si":
                    alumnos_que_trabajan += 1

                _, _, Trabaja_Actualmente, Nombre_Curso, Codigo_Comision = leer(archivo)

            print(f" Comision: {comision_actual}, Alumnos inscriptos: {alumnos_por_comision}")

        print(f"Total alumnos inscriptos en {curso_actual}: {alumnos_por_curso}")
    
    if alumnos_totales > 0:
        porcentaje = (alumnos_que_trabajan/alumnos_totales) * 100
    else:
        porcentaje = 0

    print(f"Total alumnos inscriptos en todos los cursos: {alumnos_totales}")
    print(f"Porcentaje de alumnos que trabajan: {porcentaje:.2f}%")

def main():
    archivo = open("inscriptos_AP40.csv", "r")
    corte_de_control(archivo)
    archivo.close()
main()
"""

MAX = "40,zzz,zzz,10000"

def leer(archivo):

    linea = archivo.readline()
    
    if linea:
        linea = linea.strip()
    else:
        linea = MAX
    
    campos = linea.split(",")
    
    return int(campos[0]), campos[1], campos[2], int(campos[3])

def guardar (dia,codigo_poductos,descripcion,cantidad_vendida,sucursal,union):
    union.write(f"{dia},{codigo_poductos},{descripcion},{cantidad_vendida},{sucursal}\n")

def merge (suc_1,suc_2,suc_3,union):

    dia1, codigo_poductos1, descripcion1, cantidad_vendida1 = leer(suc_1)
    dia2, codigo_poductos2, descripcion2, cantidad_vendida2 = leer(suc_2)
    dia3, codigo_poductos3, descripcion3, cantidad_vendida3 = leer(suc_3)

    while dia1 < 40 or dia2 < 40 or dia3 < 40:
        
        minimo = min(dia1, dia2, dia3)

        while minimo == dia1:
            guardar(dia1, codigo_poductos1, descripcion1, cantidad_vendida1, "Sucursal 1", union)
            dia1, codigo_poductos1, descripcion1, cantidad_vendida1 = leer(suc_1)
        
        while minimo == dia2:
            guardar(dia2, codigo_poductos2, descripcion2, cantidad_vendida2, "Sucursal 2", union)
            dia2, codigo_poductos2, descripcion2, cantidad_vendida2 = leer(suc_2)

        while minimo == dia3:
            guardar(dia3, codigo_poductos3, descripcion3, cantidad_vendida3, "Sucursal 3", union)
            dia3, codigo_poductos3, descripcion3, cantidad_vendida3 = leer(suc_3)
            
            if minimo == dia3 and minimo == dia2 and minimo == dia1:
                guardar(dia1, codigo_poductos1, descripcion1, cantidad_vendida1, "Sucursal 1", union)
                dia1, codigo_poductos1, descripcion1, cantidad_vendida1 = leer(suc_1)
            elif minimo == dia3 and minimo == dia2:
                guardar(dia2, codigo_poductos2, descripcion2, cantidad_vendida2, "Sucursal 2", union)
                dia2, codigo_poductos2, descripcion2, cantidad_vendida2 = leer(suc_2)
            else:
                guardar(dia1, codigo_poductos1, descripcion1, cantidad_vendida1, "Sucursal 1", union)
                dia1, codigo_poductos1, descripcion1, cantidad_vendida1 = leer(suc_1)
                
def unificar():
    suc_1 = open("ventas1.csv", "r")
    suc_2 = open("ventas2.csv", "r")
    suc_3 = open("ventas3.csv", "r")
    union = open("union.csv", "w")
    merge(suc_1, suc_2, suc_3, union)
    suc_1.close()
    suc_2.close()
    suc_3.close()
    union.close()

def main():
    unificar()
main()


MAX = "40,zzz,zzz,10000"

def leer(archivo):

    linea = archivo.readline()
    
    if linea:
        linea = linea.strip()
    else:
        linea = MAX
    
    campos = linea.split(",")
    
    return int(campos[0]), campos[1], campos[2], int(campos[3])

def guardar (dia,codigo_poductos,descripcion,cantidad_vendida,sucursal,union):
    union.write(f"{dia},{codigo_poductos},{descripcion},{cantidad_vendida},{sucursal}\n")

def merge (suc_1,suc_2,suc_3,union):

    dia1, codigo_poductos1, descripcion1, cantidad_vendida1 = leer(suc_1)
    dia2, codigo_poductos2, descripcion2, cantidad_vendida2 = leer(suc_2)
    dia3, codigo_poductos3, descripcion3, cantidad_vendida3 = leer(suc_3)

    while dia1 < 40 or dia2 < 40 or dia3 < 40:
        
        minimo = min(dia1, dia2, dia3)

        while minimo == dia1:
            guardar(dia1, codigo_poductos1, descripcion1, cantidad_vendida1, "Sucursal 1", union)
            dia1, codigo_poductos1, descripcion1, cantidad_vendida1 = leer(suc_1)
        
        while minimo == dia2:
            guardar(dia2, codigo_poductos2, descripcion2, cantidad_vendida2, "Sucursal 2", union)
            dia2, codigo_poductos2, descripcion2, cantidad_vendida2 = leer(suc_2)

        while minimo == dia3:
            guardar(dia3, codigo_poductos3, descripcion3, cantidad_vendida3, "Sucursal 3", union)
            dia3, codigo_poductos3, descripcion3, cantidad_vendida3 = leer(suc_3)
            
def unificar():
    suc_1 = open("ventas1.csv", "r")
    suc_2 = open("ventas2.csv", "r")
    suc_3 = open("ventas3.csv", "r")
    union = open("union.csv", "w")
    merge(suc_1, suc_2, suc_3, union)
    suc_1.close()
    suc_2.close()
    suc_3.close()
    union.close()

def main():
    unificar()
main()