"""
Declaración de Funciones Simples (Sin uso de condicionales y ciclos)
Para la solución de los siguientes ejercicios, no debes imprimir resultados dentro de las funciones que escribas. Los resultados deben ser devueltos mediante el return de la función. Luego de escribir cada función, probala, invocándola desde el bloque principal del programa, pasándole distintos valores para que la prueba tenga en cuenta varias alternativas y así estar seguro que funciona adecuadamente.
"""

# 1) Escribir una función que reciba a través de un parámetro, el radio de una circunferencia y retorne su longitud.
""" 
def calcular_longitud(radio):
    pi=3.141
    longitud = 2*pi*radio
    return longitud

def main():
    radio = float(input("Ingrese el radio de la circunferencia: "))
    longitud = calcular_longitud(radio)
    print(f"La longitud de la circunferencia con radio {radio} es: {longitud}")

main()

# 2) Escribir una función que reciba por medio de un parámetro, el radio de un círculo y retorne su área.

def calcular_area(radio):
    pi=3.141
    area = pi * (radio ** 2)
    return area

def main():
    radio = float(input("Ingrese el radio del círculo: "))
    area = calcular_area(radio)
    print(f"El área del círculo con radio {radio} es: {area}")

main()

# 3) Escribir una función que reciba un valor en centímetros y devuelva el equivalente en pulgadas. Tener en cuenta que 1 cm equivale a 0,393701 pulgadas.

def convertir_medida(medida):
    pulgadas = 0.393701 * medida
    return pulgadas

def main():
    medida = float(input("Ingrese la medida en centímetros: "))
    pulgadas = convertir_medida(medida)
    print(f"{medida} cm equivalen a {pulgadas} pulgadas")

main()

# 4) Escribir una función que reciba a través de sus parámetros, la base y la altura de un rectángulo y devuelva, el perímetro y la superficie, respetando este orden.

def calcular_perimetro_y_superficie(base, altura):
    perimetro = 2 * (base + altura)
    superficie = base * altura
    calculos = (perimetro, superficie)
    return calculos

def main():
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    perimetro, superficie = calcular_perimetro_y_superficie(base, altura)
    print(f"El perímetro del rectángulo es: {perimetro}")
    print(f"La superficie del rectángulo es: {superficie}")

main()

# 5) Escribir una función que reciba como parámetro una temperatura en grados Fahrenheit y devuelva el valor en Celsius. Tener en cuenta que: F = (C * 1,8) + 32.

def convertir_a_celcius(farenheit):
    celsius = (farenheit - 32) / 1.8
    return celsius

def main():
    farenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    celsius = convertir_a_celcius(farenheit)
    print(f"{farenheit}°F equivalen a {celsius}°C")

main()

# 6) Escribir una función que reciba como primer parámetro, la velocidad de desplazamiento de un objeto; y como segundo parámetro, el tiempo durante el cual se desplazó. La función debe devolver la distancia recorrida. Tener en cuenta que: velocidad = distancia / tiempo.

def calcular_distancia_recorridad(velocidad,tiemplo):
    distancia = velocidad * tiemplo
    return distancia

def main():
    velocidad = float(input("Ingrese la velocidad de desplazamiento en metros sobre segundo (m/s): "))
    tiempo = float(input("Ingrese el tiempo de desplazamiento en segundos (s): "))
    distancia = calcular_distancia_recorridad(velocidad, tiempo)
    print(f"La distancia recorrida es: {distancia} m")

main()

# 7) Escribir una función que reciba una cantidad de segundos, y devuelva el equivalente en días, horas, minutos, segundos. Devolver los valores en el orden indicado.

def calcular_fecha(segundos):
    minuto = 60
    hora= 60*minuto
    dia = 24*hora

    dias = segundos//dia
    segundos %= dia
    horas = segundos//hora
    segundos %= hora
    minutos = segundos//minuto
    segundos %= minuto

    fecha = [dias, horas, minutos, segundos]
    return fecha

def main():
    segundos_ingresados = float(input("Ingrese la cantidad de segundos: "))
    dias, horas, minutos, segundos = calcular_fecha(segundos_ingresados)
    print(f"{segundos_ingresados} segundos equivalen a {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos.")

main()

# 8) Escribir una función que reciba a través de sus parámetros, dos valores numéricos, y devuelva True (verdadero), si el primer parámetro es mayor que el segundo, de lo contrario debe devolver False (falso). Dale a la función el nombre es_mayor.

def es_mayor(num1,num2):
    mayor = num1>num2
    return mayor

def main():
    numeros = input("Ingrese dos números separados por un espacio: ").split()
    num1 = float(numeros[0])
    num2 = float(numeros[1])
    resultado = es_mayor(num1, num2)
    print(f"La siguiente afirmacion: {num1} es mayor que {num2} es {resultado}")

main() """

# 9) Escribir una función que reciba por parámetro, un valor entero, y devuelva True si el valor recibido es impar; de lo contrario debe devolver False. Dale a la función el nombre es_impar.

def es_impar(num):
    impar = num % 2 != 0
    return impar

def main():
    num = int(input("Ingrese un número entero: "))
    resultado = es_impar(num)
    print(f"La siguiente afirmacion: {num} ES IMPAR. Es {resultado}")

main()










# 10) Escribir una función que reciba a través de sus parámetros, dos valores enteros, y devuelva True, si el primer parámetro es múltiplo del segundo, de lo contrario debe devolver False. No te preocupes por el caso que uno ó ambos valores recibidos sea igual a cero. Dale a la función el es_multiplo_de.
# 11) Sabiendo que el peso de un mol de agua es igual a 18 g, escriba una función que reciba el valor en gramos de agua, y devuelva el valor en moles.
# 12) Un mol de una sustancia es igual a 6,022 × 10²³ unidades (moléculas) de esa sustancia, el valor resultante se conoce como Número de Avogadro. Escribir una función que dado el valor en moles del agua, retorne la cantidad de moléculas que la componen.
# 13) Por cada molécula de agua, hay 2 átomos de hidrógeno y 1 de oxígeno. Escribir una función que reciba la cantidad de moléculas de agua y devuelva; la cantidad de átomos de hidrógeno y la cantidad de átomos de oxígeno, que componen la cantidad de moléculas de agua recibida.
# 14) Ahora toma las funciones escritas en los ejercicios 8, 9 y 10, y utilizalas en una nueva función, que reciba la cantidad de gramos de agua, y retorne la cantidad de átomos de hidrógeno y de átomos de oxígeno, que hay en la cantidad de gramos de agua recibida.


