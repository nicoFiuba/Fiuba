"""
TEORÍA DE ALGORITMOS - EJERCICIO 20: Matching Máximo en el Plano 2D

1. ESTRATEGIA (Elección Golosa)
Un punto a_i (de A) domina a b_j (de B) si a_i.x >= b_j.x y a_i.y >= b_j.y.
Buscamos emparejar la máxima cantidad de puntos.

Estrategia greedy:
1. Ordenamos el conjunto A y el conjunto B ascendentemente según su coordenada X.
2. Recorremos los puntos de A ordenados. Para cada a_i, agregamos a un "grupo de disponibles" todos los puntos de B que cumplan que b_j.x <= a_i.x.
3. Mantenemos este grupo de disponibles ordenado dinámicamente según la coordenada Y.
4. Para emparejar a_i, buscamos en los disponibles aquel punto b_j que cumpla b_j.y <= a_i.y, pero elegimos estrictamente el que tenga el MAYOR VALOR de 'y'.
(Justificación: Guardamos los puntos B con 'y' pequeña, que son más fáciles de emparejar, para futuros puntos A que puedan tener restricciones fuertes en 'y').
"""

import bisect

def maximizar_matching_2d(puntos_A, puntos_B):
    # puntos = [(x, y, id), ...]
    # 1. Ordenamos por coordenada X (de menor a mayor)
    A_ord = sorted(puntos_A, key=lambda p: p[0])
    B_ord = sorted(puntos_B, key=lambda p: p[0])
    
    matching = []
    disponibles_B = [] # Guardaremos tuplas (y, x, id) ordenadas por 'y'
    
    puntero_b = 0
    n_B = len(B_ord)
    
    # 2. Recorremos los puntos de A
    for x_a, y_a, id_a in A_ord:
        # Agregamos a los disponibles todos los B que ya superamos en X
        while puntero_b < n_B and B_ord[puntero_b][0] <= x_a:
            x_b, y_b, id_b = B_ord[puntero_b]
            # bisect.insort mantiene la lista 'disponibles_B' ordenada por el primer elemento (la 'Y')
            bisect.insort(disponibles_B, (y_b, x_b, id_b))
            puntero_b += 1
            
        # 3. Decisión Greedy: Buscar el mayor 'y' que sea <= y_a
        # Usamos bisect_right para encontrar rápido dónde estaría (y_a, infinito)
        idx = bisect.bisect_right(disponibles_B, (y_a, float('inf'), ""))
        
        # Si idx > 0, significa que hay al menos un elemento válido antes de ese índice
        if idx > 0:
            # El elemento en idx - 1 es exactamente el de MAYOR 'Y' que cumple la condición
            mejor_b = disponibles_B.pop(idx - 1)
            matching.append((id_a, mejor_b[2]))
            
    return matching

"""
2. ANÁLISIS DE COMPLEJIDAD

Sea N la cantidad de puntos en los conjuntos.

Complejidad Temporal: O(N log N) [Teórica]
- Ordenar los conjuntos A y B por coordenada X toma O(N log N).
- A nivel TEÓRICO, si el "grupo de disponibles" se implementa con un Árbol Binario de Búsqueda Balanceado (como AVL o Red-Black Tree), insertar un elemento y borrar el mayor <= y_a toma O(log N). Repetido N veces, da O(N log N).
- (Aclaración de implementación: En Python usamos 'bisect', que busca en O(log N) pero inserta/borra listas en O(N), dando un tiempo empírico de O(N^2). Sin embargo, la cota teórica óptima de este algoritmo es O(N log N)).

Complejidad Espacial: O(N)
- Guardar los puntos ordenados y la estructura de disponibles toma O(N) en el peor caso.


3. JUSTIFICACIÓN DE OPTIMALIDAD (Argumento de Intercambio)

Supongamos por el absurdo que existe una solución óptima 'O' distinta a la solución nuestra Greedy 'G'. Analizando los puntos de A de izquierda a derecha (menor a mayor X), nos detenemos en el primer punto a_i donde difieren. En este paso, G emparejó a a_i con b_greedy (el de MAYOR Y disponible). El óptimo 'O' emparejó a a_i con otro b_opt (que obligatoriamente tiene una Y menor a la de b_greedy, porque G agarró el máximo válido).

¿Qué pasó con b_greedy en la solución óptima 'O'? 
- Caso 1: 'O' lo dejó sin emparejar. En este caso, en la solución 'O' podemos simplemente cambiar el emparejamiento de a_i para que use a b_greedy en vez de b_opt. La solución sigue siendo válida y tiene el mismo tamaño.
- Caso 2: 'O' lo emparejó más adelante con un punto a_futuro. Sabemos que a_futuro está más a la derecha (su X es mayor a la de a_i). Si a_futuro pudo dominar a b_greedy, significa que: a_futuro.y >= b_greedy.y. Y como dijimos arriba, b_greedy.y > b_opt.y. Por pura transitividad matemática matemática: a_futuro.y > b_opt.y. Como a_futuro domina holgadamente a b_opt (tanto en X como en Y), podemos hacer un intercambio en la solución 'O': cruzamos las parejas. Le damos b_greedy a a_i (como hizo G) y le damos b_opt a a_futuro. Todos los emparejamientos siguen siendo 100% válidos. Acabamos de transformar a 'O' en 'G' sin perder ni una sola pareja en el camino. Aplicando esta lógica inductivamente, demostramos que la elección golosa NUNCA achica el tamaño del matching máximo, siendo estrictamente óptima.
"""

# Bloque de prueba
if __name__ == "__main__":
    # Formato: (x, y, "Nombre")
    equipo_A = [
        (5, 5, "A1"),
        (8, 2, "A2"),
        (3, 8, "A3")
    ]
    
    equipo_B = [
        (2, 4, "B1"),
        (6, 1, "B2"),
        (1, 9, "B3") # Este tiene una 'y' altísima, solo A3 o superiores podrían vencerlo
    ]
    
    resultado_matching = maximizar_matching_2d(equipo_A, equipo_B)
    
    print("--- Ejercicio 20: Matching Geométrico 2D ---")
    print(f"Total de emparejamientos logrados: {len(resultado_matching)}")
    print("Detalle de las parejas (A domina a B):")
    for a, b in resultado_matching:
        print(f" - El punto {a} captura al punto {b}")