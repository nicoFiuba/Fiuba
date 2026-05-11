"""
Ejercicio 1 (20m)
Pedir al usuario el ingreso de una frase. Contabilizar cuántos acentos por cada tipo de letra tiene la frase y mostrarlos por pantalla al usuario. Los posibles acentos son á, é, í, ó, ú (pasar toda la frase a minúsculas).
"""
def contar_acentos(frase):
    
    acentos = {
        'á': 0,
        'é': 0,
        'í': 0,
        'ó': 0,
        'ú': 0
    }
    
    frase = frase.lower()
    
    for letra in frase:
        if letra in acentos:
            acentos[letra] += 1
    
    return acentos

def main():
    frase = input("Ingrese una frase: ")
    resultado = contar_acentos(frase)
    
    print("Cantidad de acentos por letra:")
    for letra, cantidad in resultado.items():
        print(f"{letra}: {cantidad}")
    return
main()

"""
Ejercicio 2 (30m)
Pedir al usuario el ingreso de una frase. Contabilizar cuantas apariciones hay de cada letra en cada palabra en la frase. Si hay más de una aparición de una palabra en la frase, no volver a contabilizar las apariciones de sus letras.
Ej: casa, linda casa → resultado: {
    “casa”: {“c”: 1, “a”: 2, “s”: 1} ,
    “linda”: {“l”: 1, “i”: 1, “n”: 1, “d”: 1, “a”: 1}
}
"""

def contar_letras(frase):
    
    palabras = frase.split()
    resultado = {}
    
    for palabra in palabras:
        if palabra not in resultado:
            contador = {}
            for letra in palabra:
                if letra in contador:
                    contador[letra] += 1
                else:
                    contador[letra] = 1
            resultado[palabra] = contador
    
    return resultado

def main():
    frase = input("Ingrese una frase: ")
    resultado = contar_letras(frase)
    
    print("Cantidad de letras por palabra:")
    for palabra, letras in resultado.items():
        print(f"{palabra}: {letras}")
    return
main()

""" 
Ejercicio 3 (50m)
Pedir al usuario campo por campo el ingreso de personas, el mismo usuario debe poder decidir cuando parar de ingresar personas. Cada persona tiene un nombre, una edad, un dni y una o más comidas preferidas (el usuario ingresa cada comida una por una). El nombre de cada persona se asume único para este ejercicio. Luego de decidir parar de ingresar personas, el usuario debe elegir un campo por el cual ordenar las personas, estos pueden ser: por nombre alfabéticamente, por edad, por dni o por la cantidad de letras que tiene la primera comida preferida que ingresó el usuario. Luego de elegir el campo, el usuario debe indicar si el ordenamiento es ascendentemente o descendentemente, el resultado final debe tener formato de diccionario
"""

def ingresar_personas():
    personas = {}
    continuar = True

    while continuar:
        nombre = input("Ingrese el nombre de la persona: ").capitalize() 
        edad = int(input("Ingrese la edad de la persona: "))
        dni = int(input("Ingrese el DNI de la persona: "))
        comidas = []

        mas_comidas = True
        while mas_comidas:
            comida = input("Ingrese una comida preferida (o 'fin' para terminar): ").lower()
            if comida != 'fin':
                comidas.append(comida)
            else:
                mas_comidas = False

        personas[nombre] = {
            "edad": edad,
            "dni": dni,
            "comidas": comidas
        }
            
        ingresar_nueva_persona = (input("Desea ingresar otra persona? (s/n)")).lower()
        if ingresar_nueva_persona == 'n':
            continuar = False
    return personas

def ordenar_personas(personas, campo, orden):
    lista_personas = list(personas.items())
    if campo == "nombre":
        lista_personas.sort(key=lambda x: x[0], reverse=(orden == "descendente"))
    elif campo == "edad":
        lista_personas.sort(key=lambda x: x[1]["edad"], reverse=(orden == "descendente"))
    elif campo == "dni":
        lista_personas.sort(key=lambda x: x[1]["dni"], reverse=(orden == "descendente"))
    elif campo == "comida":
        lista_personas.sort(key=lambda x: len(x[1]["comidas"][0]) if x[1]["comidas"] else 0, reverse=(orden == "descendente"))
    personas = dict(lista_personas)
    return personas

def main():
    personas = ingresar_personas()
    campo = input("Ingrese el campo por el cual desea ordenar (nombre, edad, dni, comida): ")
    orden = input("Ingrese el orden (asc o desc): ").lower()
    if orden == "asc":
        orden = "ascendente"
    elif orden == "desc":
        orden = "descendente"
    else:
        print("Orden no válido. Se usará ascendente por defecto.")
        orden = "ascendente"
    personas_ordenadas = ordenar_personas(personas, campo, orden)
    print("Personas ordenadas:", personas_ordenadas)
    return
main()