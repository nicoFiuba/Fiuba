""" 
Ahora necesitamos poder enviar los datos que ingrese un usuario, para ello agregá a tu ventana del objetivo 2 un botón de envío.
Además, situa en algún lugar de la ventana que quede conveniente, el texto "Hecho por: NOMBRE APELLIDO", reemplazando NOMBRE por tu nombre, y APELLIDO por tu apellido.
"""
from tkinter import *

def crear_ventana():
    # Crear la ventana
    raiz = Tk()
    raiz.title("Ingreso de Datos")


    miFrame = Frame(raiz, width=500, height=300)
    miFrame.pack()

    
    
    # Crear etiquetas y cajas de texto
    nombreLabel = Label(miFrame, text="Nombre:")
    nombreLabel.grid(row=0, column=0)
    cuadroNombre = Entry(miFrame)
    cuadroNombre.grid(row=0, column=1)

    apellidoLabel = Label(miFrame, text="Apellido:")
    apellidoLabel.grid(row=1, column=0)
    cuadroApellido = Entry(miFrame)
    cuadroApellido.grid(row=1, column=1)

    emailLabel = Label(miFrame, text="Email:")
    emailLabel.grid(row=2, column=0)
    cuadroEmail = Entry(miFrame)
    cuadroEmail.grid(row=2, column=1)
    
    # Crear botón de envío
    def enviar_datos():
        nombre = cuadroNombre.get()
        apellido = cuadroApellido.get()
        cuadroHechoPor = Label(miFrame, text=f"Hecho por: {nombre} {apellido}")
        cuadroHechoPor.grid(row=4, column=0)

    botonEnviar = Button(raiz, text="Enviar", command=enviar_datos)
    botonEnviar.pack()

    # Mostrar la ventana
    raiz.mainloop()
# Llamar a la función para crear la ventana
crear_ventana()

