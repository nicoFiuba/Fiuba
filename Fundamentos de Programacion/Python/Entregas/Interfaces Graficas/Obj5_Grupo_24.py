# 113735 Nicolas Feldman

""" 
Ahora, te proponemos agregues debajo del botón que tiene la ventana, un nuevo botón que permita registrar un nuevo usuario. Si el usuario aprieta ese botón, debería abrirle una nueva ventana de registración, que le solicite el usuario y una clave, y que incorpore dicho par de valores al diccionario existente. Se debe controlar que el usuario ingresado no exista previamente en el diccionario.
"""

from tkinter import *
from tkinter import messagebox

usuarios ={"Nicolas": "123", "Agustin": "456", "Feldman": "789"}


def ventana_registro():
    registro = Toplevel()
    registro.title("Registro Grupo 24")
    registro.geometry("300x180")
    registro.resizable(False, False)
    registro.iconbitmap("IMG_Grupo_24.ico")
    registro.config(bg="lightblue")

    formularioFrame = Frame(registro, bg="lightblue")   
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

    def registrar_usuario():
        nuevo_usuario = cuadroNombre.get()
        nueva_clave = cuadroPass.get()

        if nuevo_usuario in usuarios:
            messagebox.showerror("","El usuario ya existe.")
        else:
            usuarios[nuevo_usuario] = nueva_clave
            messagebox.showinfo("","Usuario registrado correctamente.")
            registro.destroy()

    botonRegistrar = Button(formularioFrame, text="Registrar Usuario", command=registrar_usuario)
    botonRegistrar.grid(row=3, column=0, columnspan=2, pady=10)

def ventana_login():
    raiz = Tk()
    raiz.title("Login Grupo 24")
    raiz.geometry("300x180")
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
    
    def validar_ingreso():
        nombre = cuadroNombre.get()
        clave = cuadroPass.get()

        if nombre in usuarios and clave == usuarios[nombre]:
            messagebox.showinfo("","Usuario y Clave Correctos.")  
        else:
            messagebox.showerror("","Alguno de los datos ingresados es Incorrecto")
            
    botonEnviar = Button(formularioFrame, text="Enviar", command=validar_ingreso)
    botonEnviar.grid(row=2, column=0, columnspan=2, pady=10)
    
    botonRegistrar = Button(formularioFrame, text="Registrar Usuario", command=ventana_registro)
    botonRegistrar.grid(row=3, column=0, columnspan=2, pady=10)
    
    raiz.mainloop()

ventana_login()
