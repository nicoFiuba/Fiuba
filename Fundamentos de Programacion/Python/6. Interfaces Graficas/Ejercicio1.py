""" 
Luego de ver los videos indicados, escribí una función que cree una ventana que tenga por título “Ingreso de Datos”, y que su tamaño sea de 500 x 300 pixels.
"""
from tkinter import *

def crear_ventana():
    # Crear la ventana
    raiz = Tk()
    raiz.title("Ingreso de Datos")
    raiz.geometry("500x300")

    # Mostrar la ventana
    raiz.mainloop()
# Llamar a la función para crear la ventana
crear_ventana()
