# 113735 Nicolas Feldman

""" 
Requerimientos
Nuestra ventana se utilizará para solicitar el ingreso del usuario del alumno y la clave
correspondiente. Entonces ahora deberemos agregar a lo realizado:
    1. Dos mensajes (label), uno que diga “Usuario Alumno: “ y otro que diga “Clave:”
    2. Dos cajas de ingreso (Entry box) que permitan tipear el usuario y la clave respectivamente. El ingreso de la clave debe estar enmascarado por asteriscos.
Nota: Por la simplicidad de lo pedido, se podría evitar si quisieran, el uso del método grid.
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
    
    raiz.mainloop()

ventana_login()
