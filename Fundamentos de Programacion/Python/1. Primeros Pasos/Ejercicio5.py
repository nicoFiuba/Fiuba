#1) Escribir un programa que solicite el ingreso del radio de un círculo y luego calcule e informe su diámetro, su perímetro y su superficie.
radio=int(input("Ingrese el radio del círculo: "))
diametro=radio*2
perimetro=2*3.14*radio
superficie=3.14*radio**2
print(f"El diámetro es: {diametro}.\nSu perímetro es: {perimetro}.\nSu superficie es: {superficie}")

#2) Solicitar el ingreso de tres palabras y luego mostrar todas las frases posibles, resultantes de combinar las 3 palabras ingresadas.
palabras=input("Ingrese tres palabras separadas por un espacio: ").split() #split() separa las palabras por el espacio
print(f"Las combinaciones posibles son: \n{palabras[0]} {palabras[1]} {palabras[2]}\n{palabras[0]} {palabras[2]} {palabras[1]}\n{palabras[1]} {palabras[0]} {palabras[2]}\n{palabras[1]} {palabras[2]} {palabras[0]}\n{palabras[2]} {palabras[0]} {palabras[1]}\n{palabras[2]} {palabras[1]} {palabras[0]}")

"""
Ejercicio 2 de manera optimizada (usa librería itertools para generar combinaciones de forma automatica):

import itertools
palabras=input("Ingrese tres palabras separadas por un espacio: ").split() #split() separa las palabras por el espacio
combinaciones=itertools.permutations(palabras) #Genera todas las combinaciones posibles de las palabras ingresadas
print ("Las combinaciones posibles son:")
for combinacion in combinaciones:
"""