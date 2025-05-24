""" 
Luego de ver los videos indicados, escribí una función que cree una ventana que tenga por título “Ingreso de Datos”, y que su tamaño sea de 500 x 300 pixels.
"""
from tkinter import *

def crear_ventana():
    # Crear la ventana
    ventana = Tk()
    ventana.title("Ingreso de Datos")
    ventana.geometry("500x300")

    # Mostrar la ventana
    ventana.mainloop()
# Llamar a la función para crear la ventana
crear_ventana()
