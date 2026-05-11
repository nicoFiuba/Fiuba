""" 
Ejercicio 1
Utilice un for para ir a través del diccionario libros e imprimir todas las autores. libros = {
" El Aleph.": "Borges" ,
"Sobre Heroes y Tumbas.":"E.Sabato",
"La Gesta del Marrano":" M. AGUINIS",
"Misteriosa Buenos Aires.": "Mujica Laines",
"Fundacion":"I.Asimov"
}
"""
libros = {
    "El Aleph.": "Borges",
    "Sobre Heroes y Tumbas.": "E.Sabato",
    "La Gesta del Marrano": "M. AGUINIS",
    "Misteriosa Buenos Aires.": "Mujica Laines",
    "Fundacion": "I.Asimov"
}

for titulo in libros:
    print(libros[titulo])

""" 
Ejercicio 2
Programar una función que dada una palabra, calcule la
cantidad de veces que esta cada una de las letras que
contiene
"""
def contar_letras(palabra):
    contador = {}
    for letra in palabra:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    #for letra in contador:
        #print(f"La letra {letra} aparece {contador[letra]} veces")
    return contador

def main():
    palabra = input("Ingrese una palabra: ")
    resultado = contar_letras(palabra)
    print(resultado)
    return

main()

""" 
Ejercicio 3
Se tiene cargado en memoria un diccionario llamado Stock con clave Producto y valores cantidad y precio. Se pide calcular el valor total del inventario stock={1:[2,300],2:[5000,3],5:[60,400]}
"""
def calcular_valor_total(stock):
    valor_total = 0
    for producto in stock:
        cantidad = stock[producto][0]
        precio = stock[producto][1]
        valor_total += cantidad * precio
    return valor_total

def main():
    stock = {1: [2, 300], 2: [5000, 3], 5: [60, 400]}
    valor_total = calcular_valor_total(stock)
    print(f"El valor total del inventario es: {valor_total}")
    return
main()