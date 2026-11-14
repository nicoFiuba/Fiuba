"""

EXPLICACIÓN: la estrategia consiste en poner al rey en el primer casillero del tablero y recorrer el tablero para que si hay un casillero libre de ataque poner al siguiente rey. Esta estrategia es Greedy porque realiza una elección:
    - Localmente óptima porque en cada iteración, pone al rey en un lugar libre de amenazas.
    - Factible ya que cumple con las restricciones del problema
    - Irrevocable ya que una vez tomada la decisión, no permite ser removida en posteriores elecciones del algoritmo.

PSEUDOCÓDIGO
"""

def ubicar_reyes(tablero, filas, columnas):

    reyes = 0
    for i in range(filas):
        for j in range(columnas):
            if zona_liberada(tablero, i, j, filas, columnas):
                tablero[i][j] = 1
                reyes += 1

    return reyes

"""
ANÁLISIS DE COMPLEJIDAD

- TEMPORAL: recorrer el tablero toma O(N (filas) * M (columnas)) y chequear si la zona está liberada toma O(1) ya que se evalúan 8 casilleros. Por lo tanto, la complejidad temporal es O(N * M)

- ESPACIAL: O(1) por el contador de reyes 

ANÁLISIS DE OPTIMALIDAD: se demuestra mediante el argumento de la sustitución, ya que si una solución distribuye diferente a Greedy, significa que en algún momento no se va a colocar a un rey en un aposicion segura y por ende nos va a quedar una zona liberada. Por lo tanto, tendríamos que cambiar la distribución para poder evitar que esto suceda y asi llegar a la mejor solucion posible (es lo que hace Greedy).

EJEMPLO
- Entrada: Tablero vacío de 2x3 (N=2 filas, M=3 columnas).
- Ejecución:
    - Fila 0: ubica rey en (0,0), avanza a (0,1) y evalua si es zona liberada, como no lo es, avanza a (0,2) y evalua si es zona liberada, como lo es, coloca un rey en (0,2).
    - Fila 1: Todas las celdas (1,0), (1,1) y (1,2) quedan amenazadas por los reyes de la fila 0, por ende no coloca ningun rey.
- Resultado: Retorna 2 reyes ubicados en las coordenadas (0,0) y (0,2).
"""
