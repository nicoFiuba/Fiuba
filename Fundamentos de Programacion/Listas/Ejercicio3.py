"""
Ejercicio: Operaciones varias sobre una lista de valores
Escribir un programa modular (compuesto por funciones), que haciendo uso de listas:
1. Solicite el ingreso de una secuencia de valores, que termina con el valor 0.
A medida que solicita y se ingresa una valor se debe almacenar en una lista.
El valor 0 no debe almacenarse.
2. Muestre los valores ingresados.
3. Muestre los valores hasta encontrar el 3er. valor par ingresado inclusive.
En caso de haber ninguno o menos de 3 valores pares en la lista, se mostrarán
todos los valores.
4. Muestre los elementos que se encuentren en posiciones pares.
5. Muestre los elementos ordenados de mayor a menor, sin repetirlos.
"""

def ingresar_valores():
    valores = []
    continuar = True
    while continuar:
        valor = int(input("Ingrese un valor (0 para terminar): "))
        if valor == 0:
            continuar = False
        else:
            valores.append(valor)
    return valores

def validar(valores):
    tiene_valores = True
    if not valores:
        print("Fin del programa")
        tiene_valores = False
    return tiene_valores

def mostrar_valores(mensaje, valores):
    print(mensaje)
    for valor in valores:
        print(valor)
    return None

def mostrar_hasta_tercer_par(valores):
    valores_pares = []
    for valor in valores:
        if valor % 2 == 0:
            valores_pares.append(valor)
    return valores_pares if len(valores_pares) == 3 else valores

def mostrar_posiciones_pares(valores):
    posiciones_pares = []
    for i in range(0, len(valores), 2):
        posiciones_pares.append(valores[i])
    return posiciones_pares

def mostrar_ordenados_sin_repetir(valores):
    valores_sin_repetir = []
    for valor in valores:
        if valor not in valores_sin_repetir:
            valores_sin_repetir.append(valor)
    valores_sin_repetir.sort()
    return valores_sin_repetir

def main():
    valores = ingresar_valores()
    if validar(valores):
        mostrar_valores("Valores ingresados:", valores)
        valores_pares = mostrar_hasta_tercer_par(valores)
        if valores_pares == valores:
            mostrar_valores("Como no se encontraron 3 valores pares, se muestran todos los valores: ", mostrar_hasta_tercer_par(valores))
        posiciones_pares = mostrar_posiciones_pares(valores)
        mostrar_valores("Valores en posiciones pares: ", posiciones_pares)
        sin_repetir = mostrar_ordenados_sin_repetir(valores)
        mostrar_valores("Valores ordenados sin repetir: ", sin_repetir)
    return

main()