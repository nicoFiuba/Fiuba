# 113735 Nicolas Feldman

""" 
Deben agregar:
    1. Que la aplicación no hardcodee a los usuarios, sino que los guarde en un archivo CSV con el formato: nombre completo,usuario,clave 
    2. Cada vez que se abre la aplicación levante el archivo y lo guarde en un diccionario, ahí se actualizará mientras la aplicación esté abierta: altas, bajas y modificaciones, verificando que no haya usuarios duplicados y al momento de cerrar la aplicación, debe actualizar ese archivo.
    Para el manejo de todo esto, deben ofrecer un menú de opciones.
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
