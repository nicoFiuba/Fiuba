"""
TEORÍA DE ALGORITMOS - EJERCICIO 17: Telecomunicaciones (Kruskal Máximo)

1. ESTRATEGIA (Elección Golosa)
El problema prohíbe explícitamente conectar dos ciudades que ya tengan un camino previo entre ellas. En teoría de grafos, esto significa "prohibido formar ciclos". Como queremos maximizar la suma de ganancias, el problema equivale a encontrar el Árbol Recubridor MÁXIMO.

Estrategia greedy: Algoritmo de Kruskal (Variante Máximo)
1. Ordenamos todas las líneas posibles de MAYOR a MENOR ganancia.
2. Utilizamos una estructura de Conjuntos Disjuntos (Union-Find) para llevar el rastro de qué ciudades ya están conectadas entre sí.
3. Iteramos la lista ordenada. Para cada línea, verificamos si sus extremos ya pertenecen al mismo conjunto.
4. Si no pertenecen, la decisión localmente óptima es construir esa línea (es la más rentable disponible que no forma ciclo) y unimos ambos conjuntos.
"""

class UnionFind:
    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0] * n

    def find(self, i):
        if self.padre[i] == i:
            return i
        self.padre[i] = self.find(self.padre[i])
        return self.padre[i]

    def union(self, i, j):
        raiz_i = self.find(i)
        raiz_j = self.find(j)
        if raiz_i != raiz_j:
            if self.rango[raiz_i] < self.rango[raiz_j]:
                self.padre[raiz_i] = raiz_j
            elif self.rango[raiz_i] > self.rango[raiz_j]:
                self.padre[raiz_j] = raiz_i
            else:
                self.padre[raiz_j] = raiz_i
                self.rango[raiz_i] += 1
                
def maximizar_ganancias_telecom(n_ciudades, posibles_lineas):
    # posibles_lineas: lista de tuplas (ciudad_A, ciudad_B, ganancia_Gl)
    
    # 1. Ordenamos de MAYOR a MENOR ganancia
    posibles_lineas.sort(key=lambda x: x[2], reverse=True)
    
    uf = UnionFind(n_ciudades)
    lineas_a_construir = []
    ganancia_total = 0
    
    # 2. Proceso Greedy
    for u, v, ganancia in posibles_lineas:
        # Si NO forman un ciclo, construimos la línea
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            lineas_a_construir.append((u, v, ganancia))
            ganancia_total += ganancia
            
    return ganancia_total, lineas_a_construir

"""
2. ANÁLISIS DE COMPLEJIDAD

Sea N la cantidad de ciudades y R la cantidad de líneas propuestas iniciales.

Complejidad Temporal: O(R log R)
- Ordenar la lista de R líneas por ganancia toma O(R log R).
- Las operaciones de find() y union() dentro del ciclo toman un tiempo amortizado casi constante, O(alfa(N)).
- El ciclo procesa las R líneas, tomando O(R * alfa(N)).
- La complejidad queda dominada por el ordenamiento inicial: O(R log R).

Complejidad Espacial: O(N + R)
- La estructura Union-Find requiere arreglos de tamaño N para padres y rangos: O(N).
- Almacenar la lista de líneas construidas toma a lo sumo O(N-1), pero el input tiene tamaño O(R).
- Complejidad Total: O(N + R).


3. JUSTIFICACIÓN DE OPTIMALIDAD (Argumento de Intercambio)

Supongamos por el absurdo que existe una solución óptima 'O' diferente a nuestra solución Greedy 'G'. Al ser diferentes, existe una línea 'e' (con ganancia Ge) que es elegida por G pero que no está en O. Por cómo funciona nuestro algoritmo, 'e' era la arista de mayor ganancia disponible en ese momento que NO formaba un ciclo.

Si forzamos la inclusión de la arista 'e' en la solución óptima 'O', obligatoriamente se formará un ciclo (ya que O ya era un árbol/bosque máximo válido). Dentro de este nuevo ciclo formado, debe existir alguna otra arista 'e_alt' que el algoritmo 'O' había elegido en lugar de 'e'. 

Como nuestro algoritmo Greedy evalúa las aristas en estricto orden decreciente y eligió 'e' antes que 'e_alt', sabemos con certeza que la ganancia de 'e' es MAYOR o IGUAL a la ganancia de 'e_alt' (Ge >= Ge_alt).

Si en el conjunto 'O' removemos 'e_alt' y dejamos 'e', rompemos el ciclo y volvemos a tener una red válida. Pero la nueva ganancia total será igual o estrictamente MAYOR a la que tenía 'O' originalmente. Esto contradice la suposición inicial de que 'O' era la solución óptima absoluta. Por lo tanto, la elección Greedy de agarrar siempre la arista más pesada es óptima.
"""

# Bloque de prueba
if __name__ == "__main__":
    n = 5 # Ciudades 0, 1, 2, 3, 4
    # (Ciudad A, Ciudad B, Ganancia_Mensual)
    licitacion = [
        (0, 1, 100),
        (1, 2, 500), # Súper rentable
        (2, 3, 50),
        (3, 4, 300),
        (0, 2, 200),
        (1, 4, 400)
    ]
    
    plata, construcciones = maximizar_ganancias_telecom(n, licitacion)
    
    print("--- Ejercicio 17: Telecomunicaciones ---")
    print(f"Ganancia máxima mensual: ${plata}")
    print("Líneas a construir (A - B | $Ganancia):")
    for u, v, g in construcciones:
        print(f" - Ciudad {u} a Ciudad {v} | +${g}")