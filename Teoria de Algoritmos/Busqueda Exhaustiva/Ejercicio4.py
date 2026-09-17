"""

EXPLICACIÓN: la estrategia consiste en aplicar una restricción y si no la cumple, volvemos para atrás y buscamos otra alternativa.

ESTRUCTURA DEL ÁRBOL DE ESTADOS
- NODO: Es el estado del tablero y la posicion actual, representado con la tupla (fila, columna) 

- RAMAS: son los saltos posibles que puede dar el caballo

- HOJA: el caballo visito todo el tablero y volvio a su casa

- PODA: el caballo ya visito esa casilla o la casilla no existe

PSEUDOCÓDIGO
"""

def backtracking(estado_actual, casillas_visitadas, inicio):

    if len(casillas_visitadas) == 64:
        if salto_valido(estado_actual, inicio):
            return "Exito"

        return "Fracaso"

    posibles_saltos = mover_caballo(estado_actual)

    for salto in posibles_saltos:

        if existe(salto) and salto not in casillas_visitadas:
            casillas_visitadas.add(salto)

            resultado = backtracking(salto, casillas_visitadas, inicio)

            if resultado != "Fracaso":
                return resultado

        casillas_visitadas.remove(salto)

    return "Fracaso"

"""
ANÁLISIS DE COMPLEJIDAD

- TEMPORAL: En el peor de los casos, gracias a que llevamos un registro, el algoritmo explora un máximo de 8 posibles movimientos en cada salto. Por lo tanto, la complejidad es O(8^N²).

- ESPACIAL: O(N²), ya que es el call stack de la recursión
"""
