"""
Escribiendo progamas
Para cada uno de los siguientes ejercicios, deberás escribir un programa compuesto por una o más funciones. Recordá que lo adecuado es que una función realice sólo una tarea, por eso, antes de ponerte a programar cada una de las soluciones de los ejercicios, diseña la solución indicando cuáles serán las funciones que escribirás y compondrán tu programa. Es recomendable que hayas resuelto los ejercicios de las guías anteriores, ya que te encontrarás que podrás reutilizar funciones que ya has escrito.
"""

# 1) Escribir un programa que solicite el ingreso de 2 valores enteros y luego informe el resultado de multiplicarlos, pero mediante sumas sucesivas. Optimizar el cálculo, realizando la menor cantidad de ciclos posibles. Tener en cuenta que el usuario puede ingresar valores negativos. Para la solución NO utilices la función abs().
 
def solicitar_valores():
    numeros = map(
        int, input("Ingrese dos números enteros separados por un espacio: ").split()
    )
    return numeros

def multiplicar_por_sumas_sucesivas(num1, num2):

    resultado = 0
    resultadoSum = ""

    for num in range(num2):
        resultado += num1
        if num < num2 - 1:
            resultadoSum += f"{num1} + "
        else:
            resultadoSum += f"{num1}"
    return resultadoSum

def main():
    num1, num2 = solicitar_valores()
    suma_sucesiva = multiplicar_por_sumas_sucesivas(num1, num2)
    resultado = num1 * num2
    print(f"{num1} por {num2} = {suma_sucesiva} = {resultado}")

main()

# 2) Escribir un programa que solicite el ingreso de una serie de números. Por cada número ingresado se deberá informar si el mismo es ó no, un número capicúa. Se debe evaluar que lo ingresado, sea un número entero positivo; de lo contrario, se debe enviar el mensaje “Número Inválido”, y solicitar el siguiente. El ingreso de números, termina cuando en lugar de un número, el usuario ingresa “FIN”.

def es_capicua(numero):
    numero = str(numero)
    longitud = len(numero)
    capicua = True
    for i in range(longitud // 2):
        if numero[i] != numero[longitud - i - 1]:
            capicua = False
    return capicua

def solicitar_numero():
    ingreso = input("Ingrese un número entero positivo (o 'FIN' para terminar): ")
    if ingreso.upper() == "FIN" or not ingreso.isdigit():
        ingreso = None
        # Si el ingreso no es un numero entero positivo tendria que devolver "Numero invalido, intentar nuevamente"
    return ingreso

def es_positivo():
    numero = -1

    while numero < 0:
        ingreso = solicitar_numero()
        if ingreso is None:
            numero = None
        elif ingreso.isdigit():
            numero = int(ingreso)
        else:
            print("Número inválido. Intente nuevamente.")
    return numero

def main():
    continuar = True
    while continuar:
        numero = solicitar_numero()
        if numero is None:
            continuar = False
        else:
            capicua = es_capicua(numero)
            print(f"El número {numero} {'es' if capicua else 'no es'} capicúa.")
    print("Fin del programa.")

main()

# 3) Escribir un programa que solicite el ingreso de valores, que representarán una cantidad de segundos. El programa deberá informar al usuario, el equivalente en días, horas, minutos y segundos. Se debe validar que el valor ingresado sea entero y positivo, de lo contrario, deberá mostrarse el mensaje: “Valor ingresado inválido”.El ingreso de valores finaliza cuando el usuario ingrese como valor, 0.

def solicitar_segundos():
    ingreso = float(input("Ingrese la cantidad de segundos: (0 para salir): "))
    return ingreso

def validar_segundos(ingreso):
    valido = False
    while not valido:
        if ingreso < 0 or not ingreso.is_integer():
            print("Valor ingresado inválido. Intente nuevamente.")
            solicitar_segundos()
        elif ingreso == 0:
            print("Fin del programa.")
            valido = None
        else:
            valido = True
    return valido

def calcular_fecha(ingreso):
    segundos = ingreso
    minuto = 60
    hora = 60 * minuto
    dia = 24 * hora

    dias = segundos // dia
    segundos %= dia
    horas = segundos // hora
    segundos %= hora
    minutos = segundos // minuto
    segundos %= minuto

    fecha = [dias, horas, minutos, segundos]
    return fecha

def main():
    ingreso = solicitar_segundos()
    segundos_validos = validar_segundos(ingreso)
    if segundos_validos:
        dias, horas, minutos, segundos = calcular_fecha(ingreso)
        print(f"{ingreso} segundos equivalen a {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos."
        )

main()

# 4) Escribir un programa que solicite el ingreso de dos números, y luego informe los números primos que hay entre esos dos números. Se debe validar que los números ingresados sean enteros y además que el primer número sea menor o igual que el segundo.

def solicitar_numeros():
    num1, num2 = map(
        int, input("Ingrese dos números enteros separados por un espacio: ").split()
    )
    numeros = (num1, num2)
    return numeros

def validar_numeros(num1, num2):
    valido = False
    while not valido:
        if num1 > num2:
            print(
                "El primer número debe ser menor o igual que el segundo. Intente nuevamente."
            )
            num1, num2 = solicitar_numeros()
        elif num1 < 0 or num2 < 0:
            print("Los números deben ser enteros positivos. Intente nuevamente.")
            num1, num2 = solicitar_numeros()
        else:
            valido = True
    return valido

def es_primo(num):
    primo = True
    if num < 2:
        primo = False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                primo = False
    return primo

def obtener_numeros_primos(num1, num2):
    numeros_primos = []
    for num in range(num1, num2 + 1):
        if es_primo(num):
            numeros_primos.append(num)
    return numeros_primos

def main():
    num1, num2 = solicitar_numeros()
    numeros_primos = obtener_numeros_primos(num1, num2)
    print(f"Los números primos entre {num1} y {num2} son: {numeros_primos}")

main()

# 5) Escribir un programa que solicite el ingreso de valores que representarán una cantidad de azúcar (sacarosa), en gramos. El programa deberá informar a cuántos átomos de Carbono, Hidrógeno y Oxígeno, equivale. Se debe validar que el valor ingresado sea un número entero positivo, de lo contrario se debe indicar que el valor ingresado no es válido y solicitar un nuevo valor. El ingreso de valores finaliza cuando la cantidad ingresada es igual a 0.

def solicitar_azucar():
    azucar = float(input("Ingrese la cantidad de azúcar (sacarosa) en gramos: (0 para salir): "))
    return azucar

def validar_azucar(azucar):
    valido = False
    while not valido:
        if azucar < 0 or not azucar.is_integer():
            print("Valor ingresado inválido. Intente nuevamente.")
            solicitar_azucar()
        elif azucar == 0:
            print("Fin del programa.")
            valido = None
        else:
            valido = True
    return valido

def calcular_atomos(azucar):
    gramos_por_molecula = 342.3  # gramos por mol de sacarosa
    moles = azucar / gramos_por_molecula

    atomos_carbono = moles * 12
    atomos_hidrogeno = moles * 22
    atomos_oxigeno = moles * 11

    atomos = (atomos_carbono, atomos_hidrogeno, atomos_oxigeno) 

    return atomos

def main():
    azucar = solicitar_azucar()
    azucar_validos = validar_azucar(azucar)
    if azucar_validos:
        atomos_carbono, atomos_hidrogeno, atomos_oxigeno = calcular_atomos(azucar)
        print(
            f"{azucar} gramos de azúcar (sacarosa) equivalen a {atomos_carbono} átomos de Carbono, {atomos_hidrogeno} átomos de Hidrógeno y {atomos_oxigeno} átomos de Oxígeno."
        )
        
main()

# 6) Escribir un programa que solicite el ingreso de una cantidad de átomos de Carbono, una cantidad de átomos de Hidrógeno y una cantidad de átomos de Oxígeno. Validar a medida que se ingresan las cantidades, que se trate de un número entero y positivo, de lo contrario se deberá enviar el mensaje de “Valor Inválido” y solicitar un nuevo valor. Teniendo en cuenta que la composición del azúcar (sacarosa), es Carbono 12, Hidrógeno 22 y Oxígeno 11; el programa deberá informar la cantidad de moléculas de azúcar (sacarosa) a las que equivalen los valores ingresados, ó indicar que las cantidades ingresadas no corresponden a moléculas de sacarosa.

def solicitar_atomos():
    atomos = map(int, input("Ingrese la cantidad de átomos de Carbono, Hidrógeno y Oxígeno separados por un espacio: ").split())
    return atomos

def validar_atomos(atomos_carbono, atomos_hidrogeno, atomos_oxigeno):
    atomos = (atomos_carbono, atomos_hidrogeno, atomos_oxigeno)
    valido = False
    while not valido:
        for atomo in atomos:
            if atomo < 0 or not isinstance(atomo, int):
                print("Valor ingresado inválido. Intente nuevamente.")
                solicitar_atomos()
        else:
            valido = True
    return valido

def calcular_moleculas(atomos_carbono, atomos_hidrogeno, atomos_oxigeno):
    comp_carbono = 12
    comp_hidrogeno = 22
    comp_oxigeno = 11

    moleculas = min(
        atomos_carbono // comp_carbono,
        atomos_hidrogeno // comp_hidrogeno,
        atomos_oxigeno // comp_oxigeno,
    )

    return moleculas

def main():
    atomos_carbono, atomos_hidrogeno, atomos_oxigeno = solicitar_atomos()
    atomos_validos = validar_atomos(atomos_carbono, atomos_hidrogeno, atomos_oxigeno)
    if atomos_validos:
        moleculas = calcular_moleculas(atomos_carbono, atomos_hidrogeno, atomos_oxigeno)
        if moleculas > 0:
            print(f"Los átomos ingresados equivalen a {moleculas} moléculas de azúcar (sacarosa).")
        else:
            print("Las cantidades ingresadas no corresponden a moléculas de sacarosa.")

main()

# 7) Escribir un programa que solicite el ingreso de un texto que será enviado mediante un telegrama. Luego de ingresado, se deberá informar la cantidad de palabras que lo componen y el importe a abonar por el solicitante. El texto sólo puede contener, letras, números y los siguientes signos de puntuación: . , ; : () Para el cálculo de las palabras, considerar que una palabra estará separada de otra, por uno ó más blancos. Para el cálculo del importe a abonar, deberá considerar que cada palabra pagará $10 por cada 3 caracteres. Por las fracciones menores a los 3 caracteres, pagará $8.

def solicitar_texto():
    texto = input("Ingrese el texto del telegrama: ")
    return texto

def validar_texto(texto):
    valido = False
    while not valido:
        if not all(caracter.isalnum() or caracter in ".,;:() " for caracter in texto):
            print("El texto contiene caracteres inválidos. Intente nuevamente.")
            solicitar_texto()
        else:
            valido = True
    return valido

def calcular_importe(texto):
    palabras = texto.split()
    cantidad_palabras = len(palabras)
    importe = 0

    for palabra in palabras:
        longitud = len(palabra)
        if longitud % 3 == 0:
            importe += (longitud // 3) * 10
        else:
            importe += (longitud // 3) * 10 + 8

    calculo_final = (cantidad_palabras, importe)
    return calculo_final

def main():
    texto = solicitar_texto()
    texto_validos = validar_texto(texto)
    if texto_validos:
        cantidad_palabras, importe = calcular_importe(texto)
        print(f"El texto contiene {cantidad_palabras} palabras y el importe a abonar es: ${importe}.")
main()

# 8) Escribir un programa que solicite al usuario el ingreso de una serie de palabras de a una por vez. El ingreso termina cuando el usuario, en lugar de ingresar una palabra, sólo presione la tecla Enter. Controlar que las palabras ingresadas tengan al menos 5 caracteres y que estén formadas solo por la combinación de las vocales y las letras consonantes utilizadas en el sistema de numeración romano (I, V, X, L, C, D, M). Dar aviso al usuario cuando una palabra no cumpla con esta condición, y luego solicitar el ingreso de la siguiente.

def solicitar_palabra():
    palabra = input("Ingrese una palabra (o presione Enter para salir): ")
    if palabra == "":
        palabra = None
    return palabra

def validar_palabra(palabra):
    valido = True
    if len(palabra) < 5:
        print("La palabra debe tener al menos 5 caracteres. Intente nuevamente.")
        valido = False
    if not all(caracter in "IVXLCDM" for caracter in palabra):
            print("La palabra contiene caracteres inválidos. Intente nuevamente.")
            valido = False
    
    return valido

def main():
    palabra = solicitar_palabra()
    while palabra is not None:
        if validar_palabra(palabra):
            print(f"La palabra '{palabra}' es válida.")
        palabra = solicitar_palabra()
main()
