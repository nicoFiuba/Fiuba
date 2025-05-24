"""
2) Escribir una funcion elegir_comidas en Python que reciba una lista de listas, cada sublista es una comida, en donde el primer elemento es el nombre de la comida y los siguientes elementos los respectivos ingredientes. Tambien recibe una lista de ingredientes prohibidos. Debe devolver una lista con los nombres de las comidas permitidas (no deben contener ingredientes prohibidos).
    Ejemplo:
        comidas = ["milanesa", "bifes de nalga", "pan rallado", "huevo"], 
        ["ravioles", "harina", "espinaca", "ricota"],["pizza", "queso", "harina", "tomate", "aceitunas"]]
    prohibidos_1 = ["huevo", "nueces", "aceitunas"]
    prohibidos_2 = ["huevo", "nueces"]
    elegir_comidas(comidas, prohibidos_1) => ["ravioles"]
    elegir_comidas(comidas, prohibidos_2) => ["ravioles", "pizza"]
Testea la funcion con DOS casos usando doctest, con 2 listas de prohibidos distintas a las del ejemplo.
"""
def elegir_comidas(comidas, prohibidos):
    comidas_permitidas = []
    for com in comidas:
        permitido = True
        for ingrediente in com[1:]:
            if ingrediente in prohibidos:
                permitido = False
    if permitido:
        comidas_permitidas.append(com[0])
    return comidas_permitidas

