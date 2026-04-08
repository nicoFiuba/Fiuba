"""
TEORÍA DE ALGORITMOS - EJERCICIO 11: Reyes del Ajedrez

1. ESTRATEGIA (Elección Golosa)
Un Rey en ajedrez ataca a todas las casillas adyacentes (horizontal, vertical y diagonal).
Para maximizar la cantidad de reyes, debemos minimizar el espacio que desperdician sus zonas de ataque, empacándolos lo más juntos posible.

Estrategia greedy:
1. Recorremos el tablero secuencialmente (fila por fila, de izquierda a derecha). 
2. Si la casilla actual no está bajo el ataque de ningún Rey colocado anteriormente, tomamos la decisión localmente óptima de colocar un Rey en ella inmediatamente y marcamos las casillas a su alrededor como "atacadas".
"""

import math

def ubicar_reyes_simulacion(n, m):
    # n: filas, m: columnas
    reyes = []
    atacados = set()
    
    for i in range(n):
        for j in range(m):
            if (i, j) not in atacados:
                # ¡Casilla libre! Ubicamos un Rey (decisión greedy)
                reyes.append((i, j))
                
                # Marcamos la propia casilla y todas sus adyacentes como atacadas
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        atacados.add((i + di, j + dj))
                        
    return len(reyes), reyes

def ubicar_reyes_matematico(n, m):
    # Dado que el patrón Greedy siempre coloca reyes saltando una celda 
    # (en coordenadas pares), podemos resolverlo matemáticamente en O(1)
    return math.ceil(n / 2) * math.ceil(m / 2)

"""
2. ANÁLISIS DE COMPLEJIDAD

Sea N la cantidad de filas y M la cantidad de columnas.

Complejidad Temporal: 
- Simulador Greedy: O(N * M). Iteramos una única vez por cada celda del tablero. Las operaciones dentro del ciclo (verificar y agregar al Set) toman tiempo constante O(1).
- Fórmula Matemática: O(1). Conociendo el patrón geométrico, se calcula mediante una multiplicación simple.

Complejidad Espacial: 
- Simulador Greedy: O(N * M). En el peor caso guardamos las N*M celdas en el Set de atacados.
- Fórmula Matemática: O(1). No requiere almacenar estructuras adicionales.


3. JUSTIFICACIÓN DE OPTIMALIDAD (Cota Superior por Bloques)

Para demostrar que la estrategia Greedy es estrictamente óptima, dividimos el tablero completo de N x M en pequeños sub-bloques lógicos de 2x2 celdas. (Si N o M son impares, los bordes tendrán bloques más chicos de 1x2, 2x1 o 1x1).

La cantidad total de estos sub-bloques en el tablero es exactamente: Cantidad de bloques = ceil(N/2) * ceil(M/2).

Por las reglas de movimiento del ajedrez, en cualquier sub-bloque de 2x2 TODAS las celdas son adyacentes entre sí (se tocan por los lados o en diagonal). Esto significa que es físicamente IMPOSIBLE colocar más de 1 Rey dentro de un mismo bloque sin que se ataquen mutuamente.

Por lo tanto, la cantidad teórica MÁXIMA de reyes que puede soportar el tablero está rígidamente limitada por la cantidad de bloques que existen: Reyes_Maximos <= ceil(N/2) * ceil(M/2).

Nuestro algoritmo Greedy, al ubicar sistemáticamente reyes en las primeras posiciones disponibles, logra asentar exactamente 1 Rey dentro de cada uno de estos bloques sin violar ninguna regla. Como el algoritmo alcanza el límite de la cota superior teórica máxima, queda demostrado matemáticamente que la solución es óptima.
"""

# Bloque de prueba
if __name__ == "__main__":
    n_filas = 5
    m_columnas = 5
    
    total, posiciones = ubicar_reyes_simulacion(n_filas, m_columnas)
    
    print("--- Ejercicio 11: Reyes del Ajedrez ---")
    print(f"Tablero de {n_filas}x{m_columnas}")
    print(f"Total de reyes ubicados (Simulación Greedy): {total}")
    print(f"Comprobación con Fórmula O(1): {ubicar_reyes_matematico(n_filas, m_columnas)}")
    
    print("\nPosiciones asignadas (fila, columna):")
    print(posiciones)