"""
TEORÍA DE ALGORITMOS - EJERCICIO 19: Adivinar la Carta (Codificación de Huffman)

1. ESTRATEGIA (Elección Golosa)
El problema busca minimizar la longitud esperada de una secuencia de preguntas binarias (Sí/No) dadas las frecuencias de aparición de cada elemento. Esto se modela perfectamente mediante la construcción de un Árbol de Huffman.

Estrategia greedy:
1. Creamos un nodo hoja para cada número de carta, asignándole como "peso" su frecuencia (cantidad de cartas de ese número).
2. Insertamos todos los nodos en una Cola de Prioridad (Min-Heap).
3. Mientras haya más de 1 nodo en el Heap, aplicamos la elección localmente óptima: extraemos los DOS nodos con MENOR peso.
4. Creamos un nuevo nodo interno que tenga a estos dos como hijos. Su peso será la suma de los pesos de sus hijos.
5. Insertamos el nuevo nodo interno de vuelta al Heap.
6. Al finalizar, el único nodo restante es la raíz del árbol. Los caminos desde la raíz a las hojas determinan las preguntas óptimas (Izquierda = Sí, Derecha = No).
"""

import heapq

class NodoHuffman:
    def __init__(self, cartas, frecuencia):
        self.cartas = cartas # Lista de cartas que representa este nodo
        self.frecuencia = frecuencia
        self.izq = None
        self.der = None

    # Redefinimos el comparador para que el Min-Heap funcione por frecuencia
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def construir_arbol_preguntas():
    # Inicializamos las cartas y sus frecuencias (1 de 1, 2 de 2, ..., 9 de 9)
    heap = []
    for i in range(1, 10):
        nodo = NodoHuffman([i], i)
        heapq.heappush(heap, nodo)
        
    # Construimos el árbol
    while len(heap) > 1:
        nodo1 = heapq.heappop(heap)
        nodo2 = heapq.heappop(heap)
        
        # El nuevo nodo representa la unión de ambos conjuntos de cartas
        cartas_combinadas = nodo1.cartas + nodo2.cartas
        frec_combinada = nodo1.frecuencia + nodo2.frecuencia
        
        nuevo_nodo = NodoHuffman(cartas_combinadas, frec_combinada)
        nuevo_nodo.izq = nodo1
        nuevo_nodo.der = nodo2
        
        heapq.heappush(heap, nuevo_nodo)
        
    return heap[0] # Retorna la raíz del árbol de Huffman

def imprimir_preguntas(nodo, prefijo=""):
    # Función recursiva para mostrar cómo queda armado el árbol
    if nodo.izq is None and nodo.der is None:
        print(f"Llegamos a la carta: {nodo.cartas[0]} (Camino: {prefijo})")
        return
        
    print(f"Pregunta: ¿La carta está en el grupo {nodo.izq.cartas}?")
    print(f"  -> Si dice SÍ: bajamos por el camino '{prefijo}S'")
    imprimir_preguntas(nodo.izq, prefijo + "S")
    print(f"  -> Si dice NO: bajamos por el camino '{prefijo}N' hacia {nodo.der.cartas}")
    imprimir_preguntas(nodo.der, prefijo + "N")

"""
2. ANÁLISIS DE COMPLEJIDAD

Sea N la cantidad de tipos de cartas diferentes (N = 9 en este caso).

Complejidad Temporal: O(N log N)
- Insertar los N nodos iniciales en el Min-Heap toma O(N log N).
- El bucle `while` se ejecuta N-1 veces. En cada iteración hace dos pop y un push, operaciones que toman O(log N). Todo el bucle toma O(N log N).
- Complejidad final: O(N log N).

Complejidad Espacial: O(N)
- El Min-Heap almacena a lo sumo N nodos simultáneamente: O(N).
- El árbol final creado tiene 2N - 1 nodos en total: O(N).
- Complejidad final: O(N).


3. JUSTIFICACIÓN DE OPTIMALIDAD (Argumento de Intercambio de Huffman)

La demostración de que este enfoque minimiza el número esperado de preguntas se basa en probar que las dos cartas con MENOR frecuencia deben ser obligatoriamente "hermanas" en el nivel más profundo de cualquier árbol de decisión óptimo.

Supongamos por el absurdo que existe un árbol de decisión óptimo 'O' donde las dos cartas menos frecuentes (llamémoslas X e Y) NO están en el nivel más profundo. Esto significa que en el nivel más profundo de 'O' hay alguna otra carta 'Z' que tiene una frecuencia MAYOR a la de X o Y.

El costo esperado del árbol se calcula sumando: Frecuencia(carta) * Profundidad(carta). Si en el árbol 'O' intercambiamos la posición de X (que está más arriba) con Z (que está más abajo), la carta de mayor frecuencia (Z) pasará a resolverse con menos preguntas, y la carta rara (X) pasará a resolverse con más preguntas.

Matemáticamente, como Frec(Z) > Frec(X) y Profundidad(Z) > Profundidad(X), el intercambio genera una reducción neta en el costo total esperado. Esto contradice la suposición de que 'O' ya era óptimo. Por lo tanto, cualquier árbol óptimo DEBE tener a las cartas de menor frecuencia en la base, que es exactamente lo que garantiza la elección Greedy de agarrar siempre los mínimos del Heap.
"""

# Bloque de prueba
if __name__ == "__main__":
    print("--- Ejercicio 19: Juego de Cartas (Huffman) ---")
    raiz = construir_arbol_preguntas()
    print("Estructura de las preguntas generadas por el algoritmo Greedy:\n")
    imprimir_preguntas(raiz)