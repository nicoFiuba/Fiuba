"""

EXPLICACIÓN: la estrategia consiste en aplicar una restricción y si no la cumple, volvemos para atrás y buscamos otra alternativa.

ESTRUCTURA DEL ÁRBOL DE ESTADOS

- NODO: es el estado del tablero y la posicion actual, representado con la tupla (fila, columna) 

- RAMAS: son los saltos posibles que puede dar el caballo

- HOJA: el caballo visito todo el tablero y volvio a su casa

- PODA: el caballo ya visito esa casilla o la casilla no existe

PSEUDOCÓDIGO
"""

def backtracking(estado_actual, casillas_visitadas, inicio):

    if len(casillas_visitadas) == 64:
        if salto_valido(estado_actual, inicio):
            return True

        return False

    posibles_saltos = mover_caballo(estado_actual)

    for salto in posibles_saltos:

        if existe(salto) and salto not in casillas_visitadas:

            casillas_visitadas.add(salto)

            resultado = backtracking(salto, casillas_visitadas, inicio)

            if resultado == True:
                return True

            casillas_visitadas.remove(salto)

    return False

"""
ANÁLISIS DE COMPLEJIDAD

- TEMPORAL: en el peor de los casos, gracias a que llevamos un registro, el algoritmo explora un máximo de 8 posibles movimientos en cada salto. Por lo tanto, la complejidad es O(8^N²).

- ESPACIAL: O(N²) ya que es el call stack de la recursión

EJEMPLO
- Entrada: Tablero de ajedrez (8x8) y posición de inicio en la esquina superior izquierda, tupla (0, 0).
- Ejecución:
    - Estado inicial: caballo en (0, 0). Agregamos (0, 0) a casillas_visitadas.
    - Rama 1: intentamos saltar hacia arriba e izquierda, por ejemplo a (-2, -1). Como la casilla no existe (cae fuera del tablero), se poda la rama.
    - Rama 2: intentamos saltar a (2, 1). Como existe en el tablero y no fue visitada, la agregamos a casillas_visitadas y seguimos explorando esa rama.
    - Rama 2.a: desde (2, 1) intentamos saltar de vuelta a (0, 0). Como (0, 0) ya está en casillas_visitadas, se poda la rama para evitar ciclos.
- Resultado: el algoritmo avanza y retrocede hasta que casillas_visitadas tiene 64 elementos y verifica si desde la última casilla puede saltar de vuelta al inicio (0, 0) para retornar True.
"""
