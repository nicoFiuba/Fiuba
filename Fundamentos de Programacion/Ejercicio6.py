#1) Escribir un programa que solicite el ingreso de dos números y luego informe cuál es el mayor de los número ingresados. Suponer que siempre los números ingresados serán distintos.
numeros = input("Ingrese dos números separados por un espacio: ").split()
numeros = [int(num) for num in numeros] # Convertir los números a enteros
mayor = max(numeros)

#2) Ahora, tomá el ejercicio anterior y considerá que el usuario podría ingresar dos veces el mismo número.
if numeros[0] == numeros[1]:
    print("Los números ingresados son iguales.")
else:
    print(f"El mayor de los números ingresados es: {mayor}")

#3) Escribir un programa que solicite el ingreso de un mes e informe el nombre del mes. Por ejemplo, si el usuario ingresa "1", se deberá mostrar: "Mes ingresado: Enero" En caso que el mes ingresado por el usuario no sea válido, deberá mostrar "Mes Ingresado: Inválido".
meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

mes = int(input("Ingrese un número de mes (1-12): "))

if mes in meses:
    print(f"Mes ingresado: {meses[mes]}")
else:
    print("Mes ingresado: Inválido")


#4) Solicitar el ingreso de un mes y un año e informar la cantidad de días del mes, considerando los años bisiestos. Tenga en cuenta que un año bisiesto es aquel dividible por 4, salvo que sea divisible por 100, en cuyo caso también debe ser divisible por 400.
añoBisiesto = False
if mes in meses:
    año = int(input("Ingrese un año: "))
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        añoBisiesto = True and print(f"El año {año} es bisiesto.")
    else:
        print(f"El año {año} no es bisiesto.")

    if mes == 2:
        dias = 29 if añoBisiesto else 28
    elif mes in [4, 6, 9, 11]:
        dias = 30
    else:
        dias = 31

    print(f"El mes {meses[mes]} del año {año} tiene {dias} días.")

#5) Escribir un programa que le solicite al usuario el ingreso de una temperatura y la unidad en la que se encuentra (F ó C). Luego el programa debe mostrar la temperatura ingresada, convertida en la otra unidad. La relación entre temperaturas (C) Celsius y (F) Fahrenheit, está dada por: C=5/9∗(F−32)
temperatura = {
    1: "grados",
    2: "unidad"
}
grados=float(input("Ingrese la temperatura: "))
unidad=input("Ingrese la unidad (C o F): ").upper()

if unidad == "C":
    temperatura_convertida = (grados * 9/5) + 32
    print(f"La temperatura ingresada es: {grados}°C, que equivale a {temperatura_convertida}°F")
elif unidad == "F":
    temperatura_convertida = (grados - 32) * 5/9
    print(f"La temperatura ingresada es: {grados}°F, que equivale a {temperatura_convertida}°C")