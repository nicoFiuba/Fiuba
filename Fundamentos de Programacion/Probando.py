def contar_caracteres(cadena):
    caracteres = []
    cant_mayusculas = 0
    cant_minusculas = 0
    cant_simbolos = 0

    reemplazos = {
        "Á": "A",
        "É": "E",
        "Í": "I",
        "Ó": "O",
        "Ú": "U",
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
    }

    for caracter in cadena:
        if caracter in reemplazos:
            caracter = reemplazos[caracter]
        if caracter.isalpha() and caracter.isupper():
            cant_mayusculas += 1
        elif caracter.isalpha() and caracter.islower():
            cant_minusculas += 1
        elif not caracter.isalpha():
            cant_simbolos += 1
    caracteres.extend([cant_mayusculas, cant_minusculas, cant_simbolos])
    caracteres = tuple(caracteres)
    return caracteres
