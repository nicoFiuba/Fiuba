"""
Escribiendo progamas
Para cada uno de los siguientes ejercicios, deberás escribir un programa compuesto por una o más funciones. Recordá que lo adecuado es que una función realice sólo una tarea, por eso, antes de ponerte a programar cada una de las soluciones de los ejercicios, diseña la solución indicando cuáles serán las funciones que escribirás y compondrán tu programa. Es recomendable que hayas resuelto los ejercicios de las guías anteriores, ya que te
encontrarás que podrás reutilizar funciones que ya has escrito.
"""


# 1) Escribir un programa que solicite el ingreso de 2 valores enteros y luego informe el resultado de multiplicarlos, pero mediante sumas sucesivas. Optimizar el cálculo, realizando la menor cantidad de ciclos posibles. Tener en cuenta que el usuario puede ingresar valores negativos. Para la solución NO utilices la función abs().

def solicitar_valores():
    numeros = map(int, input("Ingrese dos números enteros separados por un espacio: ").split())
    return numeros

def multiplicar_por_sumas_sucesivas(num1, num2):

    resultado = 0
    resultadoSum = ""

    for num in range (num2):
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

"""
2. Escribir un programa que solicite el ingreso de una serie de números. Por cada número ingresado se deberá informar si el mismo es ó no, un número capicúa. Se debe evaluar que lo ingresado, sea un número entero positivo; de lo contrario, se debe enviar el mensaje “Número Inválido”, y solicitar el siguiente. El ingreso de números, termina cuando en lugar de un número, el usuario ingresa “FIN”.



3. Escribir un programa que solicite el ingreso de valores, que representarán una cantidad de segundos. El programa deberá informar al usuario, el equivalente en días, horas, minutos y segundos. Se debe validar que el valor ingresado sea entero y positivo, de lo contrario, deberá mostrarse el mensaje: “Valor ingresado inválido”.
El ingreso de valores finaliza cuando el usuario ingrese como valor, 0.

4. Escribir un programa que solicite el ingreso de dos números, y luego informe los números primos que hay entre esos dos números. Se debe validar que los números ingresados sean enteros y además que el primer número sea menor o igual que el segundo.

5. Escribir un programa que solicite el ingreso de valores que representarán una cantidad de azúcar (sacarosa), en gramos. El programa deberá informar a cuántos átomos de Carbono, Hidrógeno y Oxígeno, equivale. Se debe validar que el valor ingresado sea un número entero positivo, de lo contrario se debe indicar que el valor ingresado no es válido y solicitar un nuevo valor. El ingreso de valores finaliza cuando la cantidad ingresada es igual a 0.

6. Escribir un programa que solicite el ingreso de una cantidad de átomos de Carbono, una cantidad de átomos de Hidrógeno y una cantidad de átomos de Oxígeno. Validar a medida que se ingresan las cantidades, que se trate de un número entero y positivo, de lo contrario se deberá enviar el mensaje de “Valor Inválido” y solicitar un nuevo valor. Teniendo en cuenta que la composición del azúcar (sacarosa), es Carbono 12, Hidrógeno 22 y Oxígeno 11; el programa deberá informar la cantidad de moléculas de azúcar (sacarosa) a las que equivalen los valores ingresados, ó indicar que las cantidades ingresadas no corresponden a moléculas de sacarosa.

7. Escribir un programa que solicite el ingreso de un texto que será enviado mediante un telegrama. Luego de ingresado, se deberá informar la cantidad de palabras que lo componen y el importe a abonar por el solicitante. El texto sólo puede contener, letras, números y los siguientes signos de puntuación: . , ; : () Para el cálculo de las palabras, considerar que una palabra estará separada de otra, por uno ó más blancos. Para el cálculo del importe a abonar, deberá considerar que cada palabra pagará $10 por cada 3 caracteres. Por las fracciones menores a los 3 caracteres, pagará $8.

8. Escribir un programa que solicite al usuario el ingreso de una serie de palabras de a una por vez. El ingreso termina cuando el usuario, en lugar de ingresar una palabra, sólo presione la tecla Enter. Controlar que las palabras ingresadas tengan al menos 5 caracteres y que estén formadas solo por la combinación de las vocales y las letras consonantes utilizadas en el sistema de numeración romano (I, V, X, L, C, D, M). Dar aviso al usuario cuando una palabra no cumpla con esta condición, y luego solicitar el ingreso de la siguiente.

"""