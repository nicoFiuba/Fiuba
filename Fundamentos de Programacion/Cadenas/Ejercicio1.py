"""
1) Escribir una función que reciba una cadena de caracteres. La función deberá evaluar si la cadena recibida
representa un número binario, y en ese caso devolver True, de lo contrario, deberá devolver False.
"""

def esBinario(cadena):
    bin= False
    for caracter in cadena:
        if caracter in "01":
            bin = True
    return bin

def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    if esBinario(cadena):
        print(f"La cadena '{cadena}' representa un número binario.")
    else:
        print(f"La cadena '{cadena}' no representa un número binario.")

main()

"""
2) Escribir una función que reciba una cadena de caracteres a validar, y un segundo parámetro, que
contenga una cadena con los caracteres válidos. La función debe devolver True, si la cadena a validar, está
formada sólo por caracteres válidos; en caso contrario, deberá devolver False.
"""

def esValida(cadena, caracteresValidos):
    cadenaValida = True
    for caracter in cadena:
        if caracter not in caracteresValidos:
            cadenaValida = False
    return cadenaValida

def main():
    cadena = input("Ingrese una cadena de caracteres: ")
    caracteresValidos = ("abcdefghijklmnopqrstuvwxyz")
    if esValida(cadena, caracteresValidos):
        print("Cadena válida.")
    else:
        print("Cadena inválida.")

main()

"""
3) Escribir una función que reciba una dirección de mail, y devuelva True ó False, en función de haber
evaluado que dicha dirección está bien formada. Escribir una función que reciba una cadena de caracteres que representa una dirección de mail. La
función deberá devolver True ó False, en función de haber evaluado que dicha dirección está bien formada. Se debe controla que:
    a. Que no contenga blancos
    b. Que sólo se utilicen letras y/o números para la parte del nombre, delante de la @
    c. Que haya exactamente una arroba
    d. Que los nombres de dominio sean: fi.uba.ar ó gmail.com
"""
def mailValido(mail):
    valido = True
    if " " in mail:
        valido = False
    
    if mail.count("@") != 1:  
        valido = False

    mailPartes = mail.split("@")
    if not mailPartes[0].isalnum():
        valido = False
    if mailPartes[1] != "fi.uba.ar" and mailPartes[1] != "gmail.com":
        valido = False
    return valido

def main():
    mail = input("Ingrese una dirección de mail: ")
    if mailValido(mail):
        print("La dirección de mail es válida.")
    else:
        print("La dirección de mail no es válida.")

main()

"""    
4) Escribir una función que reciba una palabra ó frase, y devuelva True, si es un palíndromo, ó False en caso contrario. Asumir que la cadena a recibir, sólo estará formada por caracteres alfabéticos y espacios en blanco. Un palíndromo es una palabra o frase que es igual si se lee de izquierda a derecha que de derecha a izquierda. Ejemplos: Ana, ala, Neuquén, Oro, seres, radar, Arriba la birra , Amar da drama, Luz azul, La ruta natural
"""

def esPalindromo(palabra):
    palindromo = False
    palabra = palabra.replace(" ", "").lower()
    palabraInvertida = palabra[::-1]
    if palabra == palabraInvertida:
        palindromo = True
    return palindromo

def main():
    palabra = input("Ingrese una palabra o frase: ")
    if esPalindromo(palabra):
        print("La palabra o frase es un palíndromo.")
    else:
        print("La palabra o frase no es un palíndromo.")
        
main()

"""
5) Escribir un programa que solicite el ingreso de palabras ó frases, y a medida que se ingresan informar si se
trata de un palíndromo. Validar que la palabra ó frase ingresada, sólo este formada por caracteres alfabéticos y por espacios en blanco. El ingreso de las palabras ó frases terminará cuando el usuario de enter, sin ingresar nada. La solución debe ser estructurada en funciones, que sigan los lineamientos de la programación estructurada. Reutilice el código de ejercicios anteriores.
"""
def esPalindromo(palabra):
    palindromo = False
    palabra = palabra.replace(" ", "").lower()
    palabraInvertida = palabra[::-1]
    if palabra == palabraInvertida:
        palindromo = True
    return palindromo

def validarPalindromo(palabra):
    valido = True
    while not palabra.isalnum() and palabra.isspace():
        valido = False
        print("La palabra o frase ingresada no es válida. Intente nuevamente.")
    return valido

def main():
    palabra = input("Ingrese una palabra o frase (o presione enter para salir): ")
    while not validarPalindromo(palabra):
        palabra = input("Ingrese una palabra o frase (o presione enter para salir): ")
        if esPalindromo(palabra):
            print("La palabra o frase es un palíndromo.")
        else:
            print("La palabra o frase no es un palíndromo.")

main()
    
"""
6) Escribir una función que reciba por parámetro un texto todo en mayúsculas. La función deberá devolver el texto pero respetando la regla que indica que luego de un punto la primer letra debe ser mayúscula, y el resto minúsculas.
"""


"""
7) Escribir una función que recibirá por parámetro, una palabra, que representa un sustantivo en singular. La función deberá devolver, el plural de dicho sustantivo, aplicando las siguientes reglas:
    a. Agregar una “s” al final, si la palabra termina en vocal sin acento.
    b. Agregar una “s” al final, si la palabra termina con una é (acentuada).
    c. Si la palabra termina en “z”, la reemplazamos por “ces”.
    d. Agregamos “es” al final, si la palabra termina en una consonante (a excepción de la “s”, la“z”, y la “x”), ó si la palabra termina con las vocales acentuadas: á, í, ó, ú
    e. Si el sustantivo termina en “s” ó “x”, entonces el plural es igual al singular, por lo tanto la función deberá devolver lo mismo que recibió. 
"""