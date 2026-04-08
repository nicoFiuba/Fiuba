"""
TEORÍA DE ALGORITMOS - EJERCICIO 7: El Ágape Antillense (K-Core)

1. ESTRATEGIA (Elección Golosa Destructiva)
El problema puede modelarse como un grafo donde los nodos son los socios y las aristas son las relaciones de conocimiento. Buscamos el subgrafo inducido máximo donde todos los nodos tengan grado >= 4.

Estrategia greedy:
1. Asumimos inicialmente que TODOS los 'n' socios están invitados.
2. Contamos cuántos conocidos tiene cada socio dentro de la lista actual de invitados.
3. Identificamos a cualquier socio que tenga estrictamente menos de 4 conocidos. Ese socio NUNCA podrá cumplir el requisito, por lo que lo eliminamos de la lista.
4. Al eliminar a un socio, actualizamos la cantidad de conocidos de sus amigos. Si alguno de sus amigos pasa a tener menos de 4 conocidos por culpa de esta eliminación, lo agregamos a nuestra "lista negra" para eliminarlo también.
5. Repetimos hasta que no queden socios con menos de 4 conocidos. Los que sobreviven son la cantidad máxima de invitados posibles.
"""

from collections import deque

def seleccionar_invitados(n_socios, relaciones):
    # n_socios: entero con la cantidad total de socios (identificados del 0 al n-1)
    # relaciones: lista de tuplas (socio_A, socio_B) indicando que se conocen
    
    # 1. Armamos el grafo usando listas/sets de adyacencia
    grafo = {i: set() for i in range(n_socios)}
    for a, b in relaciones:
        grafo[a].add(b)
        grafo[b].add(a)
        
    # 2. Inicializamos el estado: Todos invitados, guardamos el grado actual de cada uno
    grados = {i: len(grafo[i]) for i in range(n_socios)}
    invitados = set(range(n_socios))
    
    # 3. Cola de procesamiento con los socios que ya sabemos que NO cumplen (< 4)
    cola_eliminar = deque([i for i in range(n_socios) if grados[i] < 4])
    
    # 4. Proceso de eliminación en cascada (Greedy)
    while cola_eliminar:
        actual = cola_eliminar.popleft()
        
        # Si ya lo habíamos eliminado, lo salteamos
        if actual not in invitados:
            continue
            
        # Lo eliminamos de la lista final
        invitados.remove(actual)
        
        # Le avisamos a sus amigos que ya no va a ir
        for amigo in grafo[actual]:
            if amigo in invitados:
                grados[amigo] -= 1
                
                # Si el amigo acaba de caer por debajo del umbral de 4, lo mandamos a la cola
                if grados[amigo] == 3:
                    cola_eliminar.append(amigo)
                    
    return invitados

"""
2. ANÁLISIS DE COMPLEJIDAD

Sea V la cantidad de socios (nodos) y E la cantidad de relaciones (aristas).

Complejidad Temporal: O(V + E)
- Armar el grafo inicial recorriendo las relaciones toma O(V + E).
- Identificar los nodos iniciales con grado < 4 toma O(V).
- En el ciclo while, cada nodo se inserta y se saca de la cola como máximo 1 vez. 
- Cuando un nodo es procesado, iteramos sobre sus vecinos. Esto significa que cada arista del grafo se evalúa como máximo 2 veces a lo largo de todo el algoritmo.
- Por lo tanto, el ciclo while toma tiempo lineal respecto a la cantidad de nodos y aristas.
- Complejidad final: O(V + E), lo cual es óptimo.

Complejidad Espacial: O(V + E)
- El diccionario/lista de adyacencia para modelar el grafo ocupa O(V + E).
- Los diccionarios de grados, el set de invitados y la cola ocupan O(V).
- Complejidad final: O(V + E).


3. JUSTIFICACIÓN DE OPTIMALIDAD (Eliminación Segura)

Demostramos que el algoritmo es óptimo probando que nunca eliminamos a un socio que podría haber pertenecido a la solución óptima.

Por el absurdo, supongamos que nuestro algoritmo se equivoca y elimina a un socio "S" que SÍ pertenece al subgrafo máximo válido (la solución óptima). Para que el algoritmo haya decidido eliminar a "S", en algún momento de la ejecución "S" debió tener estrictamente menos de 4 conocidos en el grupo actual de invitados. 

Sabemos que en cada paso el algoritmo solo achica el grupo de invitados (nunca se agrega gente nueva). Por lo tanto, el grupo de invitados en el momento en que "S" fue eliminado es un SUPERCONJUNTO de la solución óptima final. Si "S" tiene menos de 4 conocidos en este superconjunto, es matemáticamente imposible que tenga 4 o más conocidos en un subconjunto más pequeño (como lo es la solución óptima). El grado de un nodo en un subgrafo inducido siempre es menor o igual a su grado en el grafo original.

Por lo tanto, "S" jamás podría haber formado parte de un grupo válido. Esto demuestra que la decisión Greedy de eliminar vértices con grado menor a 4 es una "elección segura" (Safe Step) que no descarta ninguna solución válida. Al detenerse solo cuando todos 
cumplen la condición, el conjunto resultante es obligatoriamente el máximo posible.
"""

# Bloque de prueba
if __name__ == "__main__":
    n = 8
    # Relaciones: Un grafo donde 0, 1, 2, 3 y 4 forman una "pandilla" (se conocen todos)
    # y 5, 6, 7 están un poco colgados.
    relaciones_prueba = [
        (0,1), (0,2), (0,3), (0,4),
        (1,2), (1,3), (1,4),
        (2,3), (2,4),
        (3,4),
        (4,5), (5,6), (6,7)
    ]
    
    resultado = seleccionar_invitados(n, relaciones_prueba)
    
    print("--- Ejercicio 7: Ágape Antillense ---")
    print(f"Total de socios: {n}")
    print(f"Socios que cumplen el protocolo (asisten): {list(resultado)}")
    print(f"Cantidad máxima de invitados: {len(resultado)}")