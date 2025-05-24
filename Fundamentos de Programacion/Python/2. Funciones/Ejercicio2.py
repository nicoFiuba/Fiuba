"""
Escribir una función que reciba el número de un mes, y devuelva el nombre del mes. Por ejemplo, si la función recibe un "1", deberá devolver: "Enero"; si recibe un "2", deberá devolver: "Febrero"; y así con el resto de los valores. En caso que el mes recibido no sea válido, deberá devolver "Mes Inválido". No debe imprimir el nombre del mes, sólo devolver la cadena correspondiente.
Probá la función invoncándola desde el bloque principal, con al menos 3 valores.
"""
import doctest

def mesDelAño(mes):
    meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
            7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
    
    if mes in meses:
        print(f"Mes ingresado: {meses[mes]}")
    else:
        print("Mes ingresado: Inválido")
    
def test_mesesDelAño():
    """
    >>> mesDelAño(1)
    Mes ingresado: Enero
    >>> mesDelAño(2)
    Mes ingresado: Febrero
    >>> mesDelAño(13)
    Mes ingresado: Inválido
    """
def main():
    mes = int(input("Ingrese el número del mes: "))
    mesDelAño(mes)
    print(doctest.testmod())

main()