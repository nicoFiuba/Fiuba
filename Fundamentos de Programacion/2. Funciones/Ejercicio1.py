"""
Escribir una función como la descripta en el video, pero que evalúe si el número recibido es impar, y en ese caso debe devolver True, de lo contrario debe devolver False. Probá la función invoncándola desde el bloque principal, con dos casos:
    a) Con tu número de tu legajo/padrón
    b) Con tu número de DNI
"""
def esPar(num):
    esPar = False
    if num %2 == 0:
        esPar = True
        return esPar

def main():
    legajo = int(input("Ingrese su legajo: "))
    dni = int(input("Ingrese su dni: "))
    print("El legajo es par" if esPar(legajo) else "El legajo no es par")
    print("El dni es par" if esPar(dni) else "El dni no es par")

main()