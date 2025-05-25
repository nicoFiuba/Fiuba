""" 
Ahora debemos validar que los datos ingresados por el usuario cumplan determinadas condiciones, para ello primero escibí una función que reciba una cadena y valide que la misma sólo esté formada por letras, y que no posee más de 25 caracteres. Esta función la utilizarás para validar el nombre y el apellido ingresado y en caso de no ser válidos alguno de ellos, le enviarás un mensaje al usuario mediante una ventana emergente.

También escribí otra función que reciba una cadena y valide que la cadena recibida es una dirección de email válida, para esto deberás controlar que en la cadena hay sólo una “@”, pero no debe estar ni en la primera, ni en la última posición de la cadena; y además la cadena a lo sumo debe tener 20 caracteres. En caso de no ser una dirección de email válida, deberás mostrar mediante una ventana emergente, un mensaje acorde.

Si los datos ingresados son válidos, entonces mediante una ventana emergente confirmá que los datos fueron recibidos. 
"""
from tkinter import *
from tkinter import messagebox

def crear_ventana():
    # Crear la ventana
    raiz = Tk()
    raiz.title("Ingreso de Datos")


    miFrame = Frame(raiz, width=500, height=300)
    miFrame.pack()

    
    
    # Crear etiquetas y cajas de texto

    # Función para validar nombre y apellido
    def validar_nombre_apellido(cadena):
        valido = True
        if len(cadena) > 25 or not cadena.isalpha():
            valido = False
            messagebox.showerror("Error", "El nombre o apellido debe contener solo letras y no más de 25 caracteres.")
        return valido
    
    # Función para validar email
    def validar_email(cadena):
        valido = True
        if cadena.count('@') != 1 or cadena.startswith('@') or cadena.endswith('@') or len(cadena) > 20:
            valido = False
            messagebox.showerror("Error", "El email no es válido.")
        return valido

    

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

        if validar_nombre_apellido(nombre) and validar_nombre_apellido(apellido) and validar_email(cuadroEmail.get()):
            messagebox.showinfo("Éxito", "Los datos fueron recibidos correctamente.")

    botonEnviar = Button(raiz, text="Enviar", command=enviar_datos)
    botonEnviar.pack()

    # Mostrar la ventana
    raiz.mainloop()
# Llamar a la función para crear la ventana
crear_ventana()

