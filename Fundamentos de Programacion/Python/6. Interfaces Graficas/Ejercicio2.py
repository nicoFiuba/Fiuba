""" 
Agregá a tu ventana del objetivo 1, cajas de texto y de ingreso de datos acordes, para solicitar a un usuario su Nombre, su Apellido y su  Email.
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






    # Mostrar la ventana
    raiz.mainloop()
# Llamar a la función para crear la ventana
crear_ventana()

