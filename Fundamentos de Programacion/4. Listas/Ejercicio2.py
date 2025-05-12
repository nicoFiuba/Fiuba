"""
Ejercicio
Generar en la consola las siguientes listas utilizando el mcanismo de comprensión de listas:
    1. Una lista que contenga los cuadrados de los múltiplos de 4, entre 4 y 20 inclusive. La lista a obtener será: [16, 64, 144, 256, 400]
    2. En base a la siguiente lista de notas: l_notas = [2, 2, 4, 9, 7, 10, 2, 5, 7] genere la lista l_aprobados con aquellos valores que sean superiores o iguales a 7.
    La lista a obtener será: [9, 7, 10, 7]
    3. En base a la siguiente lista de apellidos: l_apellidos = ['Perez', 'Alvarez', 'Rodriguez', 'Alonso', 'García', 'Fernandez', 'Arias']
    Genere una lista de apellidos que comiencen con la letra “A”. La lista a obtener será: ['Alvarez', 'Alonso', 'Arias']
"""

lista = [i**2 for i in range(4, 21) if i % 4 == 0]
print("Lista de cuadrados de los múltiplos de 4 entre 4 y 20:", lista)

l_notas = [2, 2, 4, 9, 7, 10, 2, 5, 7]
l_aprobados = [nota for nota in l_notas if nota >= 7]
print("Lista de aprobados:", l_aprobados)
l_apellidos = ['Perez', 'Alvarez', 'Rodriguez', 'Alonso', 'García', 'Fernandez', 'Arias']
l_apellidos_a = [apellido for apellido in l_apellidos if apellido.startswith('A')]
print("Lista de apellidos que comienzan con 'A':", l_apellidos_a)

