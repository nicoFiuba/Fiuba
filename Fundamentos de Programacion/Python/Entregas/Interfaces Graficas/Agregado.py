# 113735 Nicolas Feldman

""" 
Deben agregar:
    1. Que la aplicación no hardcodee a los usuarios, sino que los guarde en un archivo CSV con el formato: nombre completo,usuario,clave 
    2. Cada vez que se abre la aplicación levante el archivo y lo guarde en un diccionario, ahí se actualizará mientras la aplicación esté abierta: altas, bajas y modificaciones, verificando que no haya usuarios duplicados y al momento de cerrar la aplicación, debe actualizar ese archivo.
    Para el manejo de todo esto, deben ofrecer un menú de opciones.
"""

from tkinter import *
from tkinter import messagebox

RUTA_CSV = "usuarios.csv"

def cargar_usuarios():
    usuarios = {}
    archivo = open(RUTA_CSV, "r")
    linea = archivo.readline()
    while linea:
        datos = linea.strip().split(",")
        if len(datos) == 3:
            nombre_completo, usuario, clave = datos
            usuarios[usuario] ={"nombre_completo": nombre_completo, "clave": clave}
            linea = archivo.readline()
    archivo.close()
    return usuarios

def guardar_usuarios(usuarios):
    archivo = open(RUTA_CSV, "w")
    for usuario, datos in usuarios.items():
        archivo.write(f"{datos['nombre_completo']},{usuario},{datos['clave']}\n")
    archivo.close()
    return

def ventana_registro(usuarios):
    registro = Toplevel()
    registro.title("Registro Grupo 24")
    registro.geometry("300x180")
    registro.resizable(False, False)
    registro.iconbitmap("IMG_Grupo_24.ico")
    registro.config(bg="lightblue")

    formularioFrame = Frame(registro, bg="lightblue")   
    formularioFrame.pack(padx=5, pady=10, anchor="w")

    nombreCompletoLabel = Label(formularioFrame, text="Nombre y Apellido:")
    nombreCompletoLabel.grid(row=0, column=0, sticky="w", padx=(5,2), pady=5)
    cuadroNombreCompleto = Entry(formularioFrame)
    cuadroNombreCompleto.grid(row=0, column=1, padx=(15,10), pady=5)

    nombreLabel = Label(formularioFrame, text="Usuario Alumno:")
    nombreLabel.grid(row=1, column=0, sticky="w", padx=(5,2), pady=5)
    cuadroNombre = Entry(formularioFrame)
    cuadroNombre.grid(row=1, column=1, padx=(15,10), pady=5)

    passLabel = Label(formularioFrame, text="Clave:")
    passLabel.grid(row=2, column=0, sticky="w", padx=(5,2), pady=5)
    cuadroPass = Entry(formularioFrame)
    cuadroPass.grid(row=2, column=1, padx=(15,10), pady=5)
    cuadroPass.config(show="*")

    def registrar_usuario():
        nombre_completo = cuadroNombreCompleto.get() 
        usuario = cuadroNombre.get()
        clave = cuadroPass.get()

        if not nombre_completo or not usuario or not clave:
            messagebox.showerror("","Todos los campos son obligatorios.")
        elif usuario in usuarios:
            messagebox.showerror("","El usuario ya existe.")
        else:
            usuarios[usuario] = {"nombre_completo": nombre_completo, "clave": clave}
            guardar_usuarios(usuarios)
            messagebox.showinfo("","Usuario registrado correctamente.")
            registro.destroy()
        return
    botonRegistrar = Button(formularioFrame, text="Registrar Usuario", command=registrar_usuario)
    botonRegistrar.grid(row=3, column=0, columnspan=2, pady=10)

def ventana_login(usuarios):
    raiz = Toplevel()
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
        usuario = cuadroNombre.get()
        clave = cuadroPass.get()

        if usuario in usuarios and clave == usuarios[usuario]["clave"]:
            messagebox.showinfo("","Usuario y Clave Correctos.")
            raiz.destroy()
        else:
            messagebox.showerror("","Alguno de los datos ingresados es Incorrecto")
        
    botonEnviar = Button(formularioFrame, text="Enviar", command=validar_ingreso)
    botonEnviar.grid(row=2, column=0, columnspan=2, pady=10)
    
    botonRegistrar = Button(formularioFrame, text="Registrar Usuario", command=lambda: ventana_registro(usuarios))
    botonRegistrar.grid(row=3, column=0, columnspan=2, pady=10)

def ventana_baja(usuarios):
    baja = Toplevel()
    baja.title("Baja Usuario")
    baja.geometry("300x180")
    baja.resizable(False, False)
    baja.iconbitmap("IMG_Grupo_24.ico")
    baja.config(bg="lightblue")

    formularioFrame = Frame(baja, bg="lightblue")   
    formularioFrame.pack(padx=5, pady=10, anchor="w")

    eliminarUsuarioLabel = Label(formularioFrame, text="Usuario a Eliminar:")
    eliminarUsuarioLabel.grid(row=0, column=0, sticky="w", padx=(5,2), pady=5)
    cuadroEliminarUsuario = Entry(formularioFrame)
    cuadroEliminarUsuario.grid(row=0, column=1, padx=(15,10), pady=5)

    def eliminar_usuario():
        usuario = cuadroEliminarUsuario.get()

        if usuario in usuarios:
            del usuarios[usuario]
            guardar_usuarios(usuarios)
            messagebox.showinfo("","Usuario eliminado correctamente.")
            baja.destroy()
        else:
            messagebox.showerror("","El usuario no existe.")
        return
    botonEliminar = Button(formularioFrame, text="Eliminar Usuario", command=eliminar_usuario)
    botonEliminar.grid(row=1, column=0, columnspan=2, pady=10)

def ventana_modificacion(usuarios):
    modificar = Toplevel()
    modificar.title("Modificar Usuario")
    modificar.geometry("300x200")
    modificar.resizable(False, False)
    modificar.iconbitmap("IMG_Grupo_24.ico")
    modificar.config(bg="lightblue")

    formularioFrame = Frame(modificar, bg="lightblue")
    formularioFrame.pack(padx=5, pady=10, anchor="w")

    usuarioLabel = Label(formularioFrame, text="Usuario a Modificar:")
    usuarioLabel.grid(row=0, column=0, sticky="w", padx=(5,2), pady=5)
    cuadroUsuario = Entry(formularioFrame)
    cuadroUsuario.grid(row=0, column=1, padx=(15,10), pady=5)

    nombreCompletoLabel = Label(formularioFrame, text="Nombre y Apellido:")
    nombreCompletoLabel.grid(row=1, column=0, sticky="w", padx=(5,2), pady=5)
    cuadroNombreCompleto = Entry(formularioFrame)
    cuadroNombreCompleto.grid(row=1, column=1, padx=(15,10), pady=5)

    claveLabel = Label(formularioFrame, text="Nueva Clave:")
    claveLabel.grid(row=2, column=0, sticky="w", padx=(5,2), pady=5)
    cuadroClave = Entry(formularioFrame)
    cuadroClave.grid(row=2, column=1, padx=(15,10), pady=5)
    cuadroClave.config(show="*")

    def modificar_usuario():
        usuario = cuadroUsuario.get()
        nueva_clave = cuadroClave.get()
        nuevo_nombre_completo = cuadroNombreCompleto.get()

        if usuario not in usuarios:
            messagebox.showerror("","El usuario no existe.")
        elif not nuevo_nombre_completo and not nueva_clave:
            messagebox.showerror("","Debe ingresar al menos un campo para modificar.")
        else:
            if nuevo_nombre_completo:
                usuarios[usuario]["nombre_completo"] = nuevo_nombre_completo
            if nueva_clave:
                usuarios[usuario]["clave"] = nueva_clave
            guardar_usuarios(usuarios)
            messagebox.showinfo("","Usuario modificado correctamente.")
            modificar.destroy()
        return
    
    botonModificar = Button(formularioFrame, text="Modificar Usuario", command=modificar_usuario)
    botonModificar.grid(row=2, column=0, columnspan=2, pady=10)
            

def menu_de_opciones(usuarios):
    menu = Tk()
    menu.title("Menu de Opciones")
    menu.geometry("300x200")
    menu.resizable(False, False)
    menu.iconbitmap("IMG_Grupo_24.ico")
    menu.config(bg="lightblue")

    Button(menu, text="Registrar Usuario", command=lambda: ventana_registro(usuarios)).pack(pady=10)
    Button(menu, text="Iniciar Sesión", command=lambda: ventana_login(usuarios)).pack(pady=10)
    Button(menu, text="Salir", command=menu.destroy).pack(pady=10)
    Button(menu, text="Eliminar Usuario", command=lambda: ventana_baja(usuarios)).pack(pady=10)
    Button(menu, text="Modificar Usuario", command=lambda: ventana_modificacion(usuarios)).pack(pady=10)
    menu.mainloop()
    
def main():
    usuarios = cargar_usuarios()
    menu_de_opciones(usuarios)
    guardar_usuarios(usuarios)

main()
