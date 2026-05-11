# 1) Escribir un programa que solicite el ingreso de números, y a medida que se ingresan, calcule e informe el factorial de cada número. Para saber si el programa debe seguir solicitando ingresos, se le debe preguntar al usuario si desea ingresar otro número. En caso que no se pueda calcular el factorial del número ingresado, se debe informar que no es posible calcular el factorial para dicho número.

num = int(input("Ingrese un número entero positivo para calcular su factorial o 0 para terminar: "))

while num != 0:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"El factorial de {num} es: {factorial}")
    num = int(input("Ingrese otro número entero positivo para calcular su factorial o 0 para terminar: "))
    if num < 0: print("No es posible calcular el factorial para números negativos")
    else:
        print("Fin del programa")

# 2) Solicitar el ingreso de 2 valores enteros y luego informar el resultado de multiplicarlos, pero mediante sumas sucesivas. Optimizar el algoritmo, realizando la menor cantidad de ciclos posibles. Tener en cuenta que el usuario puede ingresar valores negativos. Para la solución NO PUEDE utilizar la función abs().

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
resultado = 0
resultadoSum = ""

for num in range (num2):
    resultado += num1
    if num < num2 - 1:
        resultadoSum += f"{num1} + "
    else:
        resultadoSum += f"{num1}"

print(f"{num1} por {num2} = {resultadoSum} = {resultado}")

"""
3) Escribir un programa que simule el proceso de control de peso y cantidad de personas que puede transportar un ascensor. Vamos a suponer que nuestro ascensor puede soportar un máximo de 400 kg y hasta 6 personas. Nuestra simulación debe proceder del siguiente modo:
    a) A medida que las personas ingresan al ascensor de a una a la vez, se registra el peso de la persona. Supondremos que el ingreso de 0 kg, indica que no hay más personas por subir al ascensor.
    b) Si en un determinado momento del ingreso de las personas, se supera el peso máximo, el ascensor, advertirá mediante un mensaje, que indique que se ha excedido el peso máximo y nuestra simulación terminará.
    c) De igual modo, si el ascensor detecta que ha subido una séptima persona al ascensor, deberá advertir de esto, y nuestra simulación terminará.
    d) Por último, si habiéndose indicado que todas las personas están abordo del ascensor y las condiciones establecidas se cumplen, el ascensor anunciará "ascensor en movimiento".
"""
ascensor = {"peso": 0, "personas": 0}
cantPersonas = 0
cantPersonasMax = 6
pesoMax = 400
valido = True
while valido and ascensor["peso"] <= pesoMax and ascensor["personas"] <= cantPersonasMax:
    ingresoPersonas = input("Desea ingresar una persona al ascensor? (Responde por si o por no) ")
    if ingresoPersonas == "si":
        cantPersonas += 1
        if cantPersonas <= cantPersonasMax:
            ascensor["personas"] += 1
            if ascensor["personas"] <= cantPersonasMax:
                print("Ingreso valido")
            else:
                print("El limite es de 6 personas")
                valido = False
            pesoPersona = float(input("Ingrese el peso de la persona o 0 para terminar: "))
            if pesoPersona == 0:
                print("Fin del programa")
            elif pesoPersona > 0:
                ascensor["peso"] += pesoPersona
                if ascensor["peso"] <= 400:
                    print("Inreso valido")
                else:
                    print("El peso maximo sportado es de 400 kg")
                    valido = False
        else:
            print("El limite es de 6 personas")
            valido = False
    else:
        print("No ingreso ninguna persona")
        valido = False
