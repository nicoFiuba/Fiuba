"""
Definiendo Funciones propias
Para la solución de los siguientes ejercicios, no debes imprimir resultados dentro de las funciones que escribas. Los resultados deben ser devueltos mediante el return de la función. Luego de escribir cada función, probala, invocándola desde el bloque principal del programa, pasándole distintos valores para que la prueba contemple varias alternativas y así estar seguro que funciona adecuadamente.
"""

# 1) Escribir una función que reciba el número de un mes, y devuelva el nombre del mes. Por ejemplo, si la función recibe un "1", deberá devolver: "Enero" En caso que el mes recibido no sea válido, deberá devolver "Mes Inválido". No debe imprimir el nombre, sólo devolver la cadena correspondiente.
""" 
def obtener_nombre_mes(mes):
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
    return meses.get(mes, "Mes Inválido") #El método get devuelve el valor de la clave especificada, o un valor predeterminado si la clave no se encuentra en el diccionario.

def main():
    mes = int(input("Ingrese el número del mes (1-12): "))
    nombre_mes = obtener_nombre_mes(mes)
    print({nombre_mes})

main() """

# 2) Escribir una función que reciba un mes y un año; y devuelva la cantidad de días del mes, considerando los años bisiestos. Tenga en cuenta que un año bisiesto es aquel divisible por 4, salvo que sea divisible por 100, en cuyo caso también debe ser divisible por 400.

def calcular_dias_mes(mes, año):
    año_bisiesto = False

    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        año_bisiesto = True
    print(f"El año {año} {'es bisiesto.' if año_bisiesto else 'no es bisiesto.'}")    

    if  1 <= mes <= 12: 
        if mes == 2:
            dias = 29 if año_bisiesto else 28
        elif mes == [4, 6, 9, 11]:
            dias = 30
        else:
            dias = 31
    else:
        print("Mes inválido.")
    return dias

def main():
    mes = int(input("Ingrese el número del mes (1-12): "))
    año = int(input("Ingrese el año: "))
    dias = calcular_dias_mes(mes, año)
    print(f"El mes {mes} del año {año} tiene {dias} días.")
main()








"""
3. Escribir una función que reciba un valor y calcule el factorial del mismo. Si no se
puede calcular el factorial del valor recibido, la función deberá devolver 0, de lo
contrario deberá devolver el valor calculado.
4. Escribir una función que reciba un valor n, entero, y devuelva la suma de los
valores entre 0 y n.
5. Escribir una función que reciba las coordenadas de dos puntos en una recta, y
devuelva la pendiente de la misma. Tener en cuenta que: la pendiente ó m =
(y2 – y1)/(x2 - x1), donde (x1, y1) y (x2, y2), serán las coordenadas del primer
y segundo punto, respectivamente.
6. Escribir una función que reciba un número y devuelva un valor booleano
indicando si el número recibido es ó no primo.
7. Tomá la solución del ejercicio anterior y analizá si elegiste el cliclo adecuado, y si
estás evitando realizar ciclos innecesarios.
Por ejemplo, algunas preguntas que te podrías hacer son:
a) Con sólo encontrar un divisor del número a evaluar distinto a uno y a sí
mismo, ya puedo afirmar que el número no es primo, tiene sentido seguir
evaluando más divisores?
b) Teniendo en cuenta que todo número par a excepción del 2, no es primo,
tiene sentido seguir en un ciclo, si al calcular el resto de la división del número a
evaluar por 2, el resultado es cero?
c) Puedo encontrar un divisor del número a evaluar que sea mayor al número a
evaluar dividido 2?
Modificá la función escrita en el punto anterior, para que tenga en cuenta las
situaciones planteadas.
______________________________________________________________________________________
Lic. Gustavo Bianchi Página 1
Ejercicios Prácticos - Versión Preliminar Introducción a la Programación - FIUBA
______________________________________________________________________________________
8. Escribir una función que reciba dos valores enteros, y devuelva el máximo
común divisor entre ambos números.
Recordemos que se define el máximo común divisor (MCD) de dos o más
números enteros al mayor número entero que los divide sin dejar resto alguno.
Te sugerimos que antes de programar la solución te hagas preguntas del tipo a
las planteadas en en el ejercicio anterior
9. Ahora toma el ejercicio anterior, pero intenta resolverlo aplicando el método de
Euclides.
Para poder escribir el algoritmo, quizás te ayude ver el siguiente video:
https://www.youtube.com/watch?v=x6qFMSRpgpM ó consultar en el siguiente
link: https://es.wikipedia.org/wiki/Algoritmo_de_Euclides
10. El producto de Wallis es una expresión matemática, utilizada para representar el
valor del número Pi, que fue descubierta por John Wallis en 1655 y que
establece que:
Escribir una función, que reciba por parámetro, el valor más alto a utilizar en el
cálculo (n). La función debe calcular el valor de Pi utilizando la fórmula de Wallis
y devolver el valor de Pi obtenido.
Proba la función, utilizando al menos, como valor de n, 100, 1000 y 10000.
Fuente de consulta: https://es.wikipedia.org/wiki/Producto_de_Wallis
11. Un palíndromo es una palabra o frase que se puede leer de igual modo en ambos
sentidos. Por ejemplo: Oso - Ana - Oso baboso - Arriba la birra
Escribir una función que reciba una frase que podría estar compuesta por una o
más palabras; y devuelva True, si se trata de un palíndromo, de lo contrario,
deberá devolver False.
Fuente de conulta: https://es.wikipedia.org/wiki/Palíndromo
12. Tome la solución del ejercicio anterior y proceda según lo descripto a
continuación:
a) Si en su solución no utiliza un ciclo, entonces, intente resolver el ejercicio
utilizando uno y sólo uno, y luego siga con los puntos b) y c).
b) Si decidió utilizar un ciclo para la solución, responda lo siguiente:
1) Cualquiera sea la cadena recibida, el algoritmo recorrerá siempre toda la
cadena?
2) Si la respuesta de la pregunta anterior es afirmativa, entonces, evalúe si
realmente es necesario recorrer siempre toda la cadena ó podemos evitar
continuar con la evaluación, si detectamos en algún momento que no es posible
que la cadena sea un palíndromo.
Genere un nuevo algoritmo teniendo en cuenta esto.
______________________________________________________________________________________
Lic. Gustavo Bianchi Página 2
Ejercicios Prácticos - Versión Preliminar Introducción a la Programación - FIUBA
______________________________________________________________________________________
13. Escribir una función que reciba por parámetro un texto todo en mayúsculas.
La función deberá devolver el texto pero respetando la regla que indica que
luego de un punto la primer letra debe ser mayúscula, y el resto minúsculas.
14. Escribir una función que recibirá por parámetro, una palabra, que representa un
sustantivo en singular.
La función deberá devolver, el plural de dicho sustantivo, aplicando las
siguientes reglas:
a. Agregar una “s” al final, si la palabra termina en vocal sin acento.
b. Agregar una “s” al final, si la palabra termina con una é (acentuada).
c. Si la palabra termina en “z”, la reemplazamos por “ces”.
d. Agregamos “es” al final, si la palabra termina en una consonante (a excepción
de la “s”, la “z”, y la “x”), ó si la palabra termina con las vocales acentuadas: á,
í, ó, ú.
e. Si el sustantivo termina en “s” ó “x”, entonces el plural es igual al singular,
por lo tanto la función deberá devolver lo mismo que recibió.
"""