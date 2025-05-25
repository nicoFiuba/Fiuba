# 113735 Nicolas Feldman

""" 
Ahora que logramos nuestra ventana de Login, deberemos validar el ingreso del usuario y la clave. Primero escribiremos la función obtener_usuarios_claves(), que genere y devuelva un diccionario del tipo {clave: valor}, siendo la clave el “usuario alumno”, y el valor, la clave de ingreso correspondiente. Generar un diccionario con cada uno de los integrantes del grupo. No debe solicitar que se ingresen los datos por teclado, simplemente genérenlo dentro del código de la función. A continuación debemos validar el ingreso que se haga contra el diccionario que devuelve la función, si el usuario y la clave son correctos, mostrar el mensaje: “Usuario y Clave Correctos”, de lo contrario, mostrar el mensaje “Algunos de los datos ingresados es Incorrecto”.
"""

from tkinter import *
from tkinter import messagebox

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

    def obtener_usuarios_claves():
        usuarios ={"Nicolas": "123", "Agustin": "456", "Feldman": "789"}
        return usuarios
    
    def validar_ingreso(usuarios):
        nombre = cuadroNombre.get()
        clave = cuadroPass.get()

        if nombre in usuarios and clave == usuarios[nombre]:
            messagebox.showinfo("","Usuario y Clave Correctos.")  
        else:
            messagebox.showerror("","Alguno de los datos ingresados es Incorrecto")
            
    botonEnviar = Button(formularioFrame, text="Enviar", command=lambda: validar_ingreso(obtener_usuarios_claves()))
    botonEnviar.grid(row=2, column=0, columnspan=2, pady=10)
    
    raiz.mainloop()

ventana_login()
