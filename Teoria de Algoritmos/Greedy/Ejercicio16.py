"""
TEORÍA DE ALGORITMOS - EJERCICIO 16: Reconstrucción de Antillense (MST + Scheduling)

1. ESTRATEGIA (Elección Golosa)
El problema se divide en dos fases puramente golosas:
- Fase 1 (Selección): Usamos el Algoritmo de Kruskal para encontrar el Árbol Recubridor Mínimo (MST). Esto garantiza conectar todas las ciudades con la menor cantidad de rutas (n-1) y el menor costo base total posible.
- Fase 2 (Planificación): Sabiendo que los costos aumentan un 100% anual (se multiplican por 2 cada año), ordenamos las rutas del MST seleccionado de MAYOR a MENOR costo. Construimos primero la más cara para que no sufra el multiplicador de la inflación.

Fórmula de costo con inflación: Costo_Base * (2 ** (año - 1))
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

def planificar_reconstruccion(n_poblaciones, posibles_rutas):
    # posibles_rutas: lista de tuplas (ciudad_A, ciudad_B, costo_base)
    
    # --- FASE 1: Obtener el MST (Kruskal) ---
    # Ordenamos de menor a mayor costo base
    posibles_rutas.sort(key=lambda x: x[2])
    
    uf = UnionFind(n_poblaciones)
    rutas_mst = []
    
    for u, v, costo in posibles_rutas:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            rutas_mst.append((u, v, costo))
            
    # Si no logramos n-1 rutas, el país está desconectado
    if len(rutas_mst) != n_poblaciones - 1:
        return "Imposible conectar todas las poblaciones."

    # --- FASE 2: Planificar construcción contra la inflación ---
    # Ordenamos las rutas elegidas de MAYOR a MENOR costo base
    rutas_mst.sort(key=lambda x: x[2], reverse=True)
    
    costo_total = 0
    cronograma = []
    
    # Asignamos años (1, 2, 3...) y calculamos inflación
    for anio, (u, v, costo_base) in enumerate(rutas_mst, start=1):
        # Aumenta 100% por año (potencias de 2)
        costo_inflacionado = costo_base * (2 ** (anio - 1))
        costo_total += costo_inflacionado
        cronograma.append((anio, u, v, costo_base, costo_inflacionado))
        
    return costo_total, cronograma


"""
2. ANÁLISIS DE COMPLEJIDAD

Sea V la cantidad de poblaciones y E la cantidad de rutas posibles iniciales.

Complejidad Temporal: O(E log E)
- Ordenar las aristas iniciales para Kruskal: O(E log E).
- Recorrer aristas y hacer Union-Find: O(E * alpha(V)).
- Ordenar las aristas finales del MST (que son V-1 aristas): O(V log V).
- La complejidad total queda dominada por el primer ordenamiento: O(E log E).

Complejidad Espacial: O(V + E)
- Arreglos para el Union-Find: O(V).
- Guardar el grafo y el cronograma: O(V + E).


3. JUSTIFICACIÓN DE OPTIMALIDAD (Argumento de Intercambio)

Fase 1 (MST): La optimalidad de Kruskal ya es conocida y asegura que el conjunto de aristas base elegido es el mínimo posible. Ningún otro árbol recubridor tendrá una suma de bases menor.

Fase 2 (Ordenamiento): Supongamos por el absurdo que existe una solución óptima 'O' que no ordena estrictamente de mayor a menor. Esto implica que, en algún año 't', se construye una ruta barata (costo B) y en el año siguiente 't+1' se construye una ruta cara (costo A), donde A > B.

El costo de este fragmento en la solución 'O' sería:
Costo_O = B * (2^(t-1)) + A * (2^t)

Si aplicamos nuestra estrategia Greedy intercambiando el orden (construimos A primero y B después), el nuevo costo sería:
Costo_Greedy = A * (2^(t-1)) + B * (2^t)

Comparemos la diferencia (Costo_Greedy - Costo_O):
Diferencia = [A * 2^(t-1) + B * 2^t] - [B * 2^(t-1) + A * 2^t]
Diferencia = A * [2^(t-1) - 2^t] + B * [2^t - 2^(t-1)]
Como 2^t es el doble de 2^(t-1), simplificamos:
Diferencia = A * [-2^(t-1)] + B * [2^(t-1)]
Diferencia = (B - A) * 2^(t-1)

Como habíamos establecido que A > B, entonces (B - A) es un número NEGATIVO. Al ser la diferencia negativa, significa que Costo_Greedy es ESTRICTAMENTE MENOR que Costo_O. 

Esto demuestra por el absurdo que cualquier planificación que no ordene las obras de mayor a menor costo pagará de más. La estrategia golosa propuesta es óptima.
"""

# Bloque de prueba
if __name__ == "__main__":
    n = 4 # Poblaciones 0, 1, 2, 3
    # (Ciudad A, Ciudad B, Costo_Base)
    rutas_disponibles = [
        (0, 1, 10),
        (0, 2, 5),
        (1, 2, 15),
        (1, 3, 20),
        (2, 3, 50) # Ruta muy cara, Kruskal la va a evitar si puede
    ]
    
    resultado = planificar_reconstruccion(n, rutas_disponibles)
    
    print("--- Ejercicio 16: Reconstrucción de Antillense ---")
    if isinstance(resultado, str):
        print(resultado)
    else:
        costo_final, agenda = resultado
        print("Cronograma óptimo de obras:")
        for anio, u, v, base, inf in agenda:
            print(f"Año {anio}: Ruta {u}-{v} | Costo Base: ${base} -> Costo a Pagar: ${inf}")
        print(f"\nCosto Total Final: ${costo_final}")