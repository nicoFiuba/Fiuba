# 113735 Nicolas Feldman

""" 
Requerimientos
Ahora nuestra interface necesita un botón para el envío de los datos ingresados por el alumno.
"""
from tkinter import *

def ventana_login():
    raiz = Tk()
    raiz.title("Login Grupo 24")
    raiz.geometry("300x130")
    raiz.resizable(False, False)
    raiz.iconbitmap("IMG_Grupo_24.ico")
    raiz.config(bg="lightblue")

    formularioFrame = Frame(raiz, bg="lightblue")   
    formularioFrame.pack(padx=5, pady=10, anchor="w")

    nombreLabel = Label(formularioFrame, text="Usuario Alumno:")
    nombreLabel.grid(row=0, column=0, sticky="w", padx=(5,2), pady=5)
    cuadroNombre = Entry(formularioFrame)
    cuadroNombre.grid(row=0, column=1, padx=(15,10), pady=5)

    passLabel = Label(formularioFrame, text="Clave:")
    passLabel.grid(row=1, column=0, sticky="w", padx=(5,2), pady=5)
    cuadroPass = Entry(formularioFrame)
    cuadroPass.grid(row=1, column=1, padx=(15,10), pady=5)
    cuadroPass.config(show="*")

    botonEnviar = Button(formularioFrame, text="Enviar")
    botonEnviar.grid(row=2, column=0, columnspan=2, pady=10)
    
    raiz.mainloop()

ventana_login()
