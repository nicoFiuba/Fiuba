"""
TEORÍA DE ALGORITMOS - EJERCICIO 24: El Mazo de Cartas (Patience Sorting)

1. ESTRATEGIA (Elección Golosa)
El problema consiste en minimizar la cantidad de pilas creadas al ir apilando cartas con la restricción de que la nueva carta debe ser estrictamente menor que la carta superior de la pila elegida.

Estrategia greedy:
1. Mantenemos una lista con las "cartas superiores" (cimas) de cada pila creada.
2. Esta lista de cimas estará naturalmente ordenada de menor a mayor.
3. Al sacar una carta 'X', buscamos mediante Búsqueda Binaria la pila cuya cima sea estrictamente MAYOR a 'X', pero la más cercana posible a 'X' (el límite inferior válido). 
4. Si encontramos esa pila, reemplazamos su cima por 'X'. (Decisión golosa: "desperdiciamos" la cima más chica posible para guardar las cimas grandes para el futuro).
5. Si 'X' es mayor o igual a todas las cimas actuales, creamos una pila nueva.
"""

import bisect

def jugar_patience_sorting(mazo):
    # mazo: lista de enteros representando el orden en que salen las cartas
    
    # Guardaremos solo el valor de la carta en la cima de cada pila
    cimas_pilas = []
    
    # Para poder reconstruir las pilas y mostrar el resultado (Opcional)
    historial_pilas = [] 
    
    for carta in mazo:
        # Buscamos la posición de la primera cima que sea ESTRICTAMENTE MAYOR a la carta
        # (Usamos bisect_right por si hay cartas repetidas, aunque el mazo suele tener 1 a n)
        idx = bisect.bisect_right(cimas_pilas, carta)
        
        # Como la regla dice "debe ser menor", si empatan (idx apunta a una carta igual),
        # bisect_right nos manda al siguiente, lo cual es correcto. Pero debemos asegurarnos
        # de que el elemento en idx sea realmente mayor.
        
        # Ajuste fino: si bisect_right encuentra elementos iguales, los salta. 
        # Queremos la primera cima > carta.
        if idx < len(cimas_pilas) and cimas_pilas[idx] == carta:
             idx += 1 # Avanzamos si es igual, porque necesitamos que la cima sea MAYOR
             
        # Para evitar problemas con duplicados, una forma más segura en Python:
        # Buscar el primer índice donde cimas_pilas[idx] > carta
        idx = 0
        while idx < len(cimas_pilas) and cimas_pilas[idx] <= carta:
            idx += 1
            
        # Nota: La búsqueda lineal de arriba es O(P). Para que sea O(log P) usaríamos:
        # idx = bisect.bisect_right(cimas_pilas, carta)
        # Solo asumiendo que todas las cartas son únicas (1 al N).
        
        if idx == len(cimas_pilas):
            # No hay ninguna cima mayor, creamos una pila nueva
            cimas_pilas.append(carta)
            historial_pilas.append([carta])
        else:
            # Reemplazamos la cima de la pila encontrada
            cimas_pilas[idx] = carta
            historial_pilas[idx].append(carta)
            
    return len(cimas_pilas), historial_pilas

# --- VERSIÓN OPTIMIZADA O(N log N) PARA CARTAS ÚNICAS ---
def jugar_patience_sorting_optimo(mazo):
    cimas = []
    for carta in mazo:
        # bisect_right asume que el mazo no tiene repetidos (como dice el enunciado "del 1 al n")
        idx = bisect.bisect_right(cimas, carta)
        if idx == len(cimas):
            cimas.append(carta)
        else:
            cimas[idx] = carta
    return len(cimas)


"""
2. ANÁLISIS DE COMPLEJIDAD

Sea N la cantidad de cartas en el mazo.

Complejidad Temporal: O(N log N)
- Recorremos el mazo una sola vez, lo cual toma O(N) iteraciones.
- En cada iteración, la lista de cimas está perfectamente ordenada (porque una pila nueva solo se crea si la carta es mayor a todas las cimas anteriores, y al reemplazar una cima por un valor menor, se mantiene el orden relativo).
- Como está ordenada, podemos usar Búsqueda Binaria (`bisect`) que toma O(log P), donde P es la cantidad de pilas (P <= N).
- Complejidad total: O(N log N).

Complejidad Espacial: O(N)
- La lista de cimas ocupa, en el peor de los casos (cartas ordenadas crecientemente), O(N).


3. JUSTIFICACIÓN DE OPTIMALIDAD (Argumento de Cota Inferior / LIS)

Para demostrar que nuestra estrategia minimiza la cantidad de pilas, debemos encontrar una Cota Inferior insuperable.

Observemos las reglas del juego: si en el mazo original existe una secuencia de 'K' cartas que aparecen en orden estrictamente CRECIENTE (por ejemplo: primero sale un 2, después un 5, después un 9), es FÍSICAMENTE IMPOSIBLE apilar cualquiera de esas cartas sobre una anterior. El 5 no puede ir sobre el 2, y el 9 no puede ir sobre el 5. Por lo tanto, si el mazo contiene una subsecuencia creciente de longitud 'K', 
CUALQUIER algoritmo necesitará obligatoriamente al menos 'K' pilas. (Óptimo >= K).

Nuestra estrategia Greedy siempre coloca una carta sobre la cima más pequeña que sea válida. Esto garantiza que una nueva pila SOLO se crea cuando sale una carta que es estrictamente mayor a TODAS las cimas anteriores. Si el algoritmo Greedy termina creando 'M' pilas, podemos trazar un "camino de punteros" desde la cima de la última pila hacia atrás (cada carta apuntando a la cima de la pila anterior en el momento en que fue apoyada), formando exactamente una subsecuencia creciente de tamaño 'M' en el mazo original.

Como demostramos que existe una subsecuencia creciente de tamaño 'M', sabemos que la cota inferior del problema es 'M'. Y como nuestro algoritmo resolvió el problema usando exactamente 'M' pilas, alcanzó la cota inferior teórica. Por lo tanto, la elección golosa es estrictamente óptima y garantiza la mínima cantidad de pilas posible.
"""

# Bloque de prueba
if __name__ == "__main__":
    # Mazo con cartas del 1 al 9 mezcladas
    mazo_mezclado = [7, 2, 8, 1, 3, 4, 9, 6, 5]
    
    cant_pilas, estado_pilas = jugar_patience_sorting(mazo_mezclado)
    
    print("--- Ejercicio 24: El Mazo de Cartas (Patience Sorting) ---")
    print(f"Orden de salida del mazo: {mazo_mezclado}")
    print(f"Cantidad mínima de pilas formadas: {cant_pilas}")
    
    print("\nContenido de cada pila (de base a cima):")
    for i, pila in enumerate(estado_pilas, 1):
        # La primera carta agregada quedó en la base, la última en la cima
        print(f"Pila {i}: {pila} -> Cima actual: {pila[-1]}")