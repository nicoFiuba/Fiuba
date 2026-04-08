"""
TEORÍA DE ALGORITMOS - EJERCICIO 8: Ágape Antillense (Doble Restricción)

1. ESTRATEGIA (Elección Golosa Destructiva)
Al problema anterior se le agrega la restricción de que cada invitado debe tener al menos 4 "NO conocidos" (desconocidos) en la fiesta para sociabilizar. 

Estrategia greedy:
1. Asumimos inicialmente que todos los socios están invitados.
2. Un socio S es válido si y solo si:
- Sus amigos en la lista actual >= 4
- Sus desconocidos en la lista actual >= 4 (Nota: desconocidos = total_invitados - 1 - amigos_de_S)
3. Si alguien incumple CUALQUIERA de las dos reglas, lo eliminamos.
4. Al eliminar a X, actualizamos a los que quedan:
- Si un invitado era amigo de X, pierde 1 amigo.
- Si un invitado NO era amigo de X, pierde 1 desconocido.
5. Si tras la actualización alguien cae por debajo de 4 (en amigos o desconocidos), entra a la cola de eliminación. Repetimos hasta la convergencia.
"""

from collections import deque

def seleccionar_invitados_con_desconocidos(n_socios, relaciones):
    # 1. Armamos el grafo de amistades
    grafo = {i: set() for i in range(n_socios)}
    for a, b in relaciones:
        grafo[a].add(b)
        grafo[b].add(a)
        
    # 2. Inicializamos el estado
    grados = {i: len(grafo[i]) for i in range(n_socios)}
    invitados = set(range(n_socios))
    
    # Función auxiliar para calcular los desconocidos dinámicamente
    def cant_desconocidos(socio):
        return len(invitados) - 1 - grados[socio]

    # 3. Cola de procesamiento con los que fallan la doble condición
    cola_eliminar = deque()
    en_cola = set() # Set auxiliar para no encolar repetidos
    
    for i in range(n_socios):
        if grados[i] < 4 or cant_desconocidos(i) < 4:
            cola_eliminar.append(i)
            en_cola.add(i)
            
    # 4. Proceso de eliminación
    while cola_eliminar:
        actual = cola_eliminar.popleft()
        
        if actual not in invitados:
            continue
            
        invitados.remove(actual)
        
        # Al irse, altera los números de TODOS los que quedan
        # Tenemos que revisar tanto a sus amigos como a sus desconocidos
        for otro in list(invitados):
            if otro in grafo[actual]:
                # Era amigo: pierde un amigo.
                grados[otro] -= 1
                if grados[otro] < 4 and otro not in en_cola:
                    cola_eliminar.append(otro)
                    en_cola.add(otro)
            else:
                # No era amigo: pierde un desconocido. 
                # (Grados se mantiene igual, pero la lista total bajó, así que cant_desconocidos bajó)
                if cant_desconocidos(otro) < 4 and otro not in en_cola:
                    cola_eliminar.append(otro)
                    en_cola.add(otro)
                    
    return invitados

"""
2. ANÁLISIS DE COMPLEJIDAD

Sea V la cantidad de socios y E la cantidad de relaciones.

Complejidad Temporal: O(V^2)
- A diferencia del Ejercicio 7 (donde solo avisábamos a los amigos, O(E)), acá la eliminación de un socio S afecta el contador de desconocidos de las personas que NO son sus amigos.
- Por lo tanto, al eliminar a S, debemos iterar sobre TODOS los socios restantes en la lista para actualizar sus estados (los amigos pierden 1 grado, los no-amigos pierden 1 desconocido).
- Como en el peor caso podemos llegar a eliminar a los V socios de a uno, la complejidad temporal asciende a O(V^2). Esto es óptimo dado que implícitamente estamos trabajando con el grafo complemento.

Complejidad Espacial: O(V + E)
- Las estructuras de datos son las mismas que en el Ejercicio 7 (diccionarios para el grafo, arreglos de grados, cola de eliminación).

3. JUSTIFICACIÓN DE OPTIMALIDAD (Eliminación Segura Monótona)

El algoritmo mantiene la optimalidad por el principio de monotonía de subconjuntos. Sea O el conjunto óptimo de invitados (el más grande posible). Si un socio 's' en nuestra lista actual 'L' tiene menos de 4 amigos o menos de 4 desconocidos, afirmamos que es imposible que 's' pertenezca a 'O'.

Demostración:
Cualquier subconjunto válido O debe estar contenido en L (O ⊆ L) porque nosotros arrancamos con todos los socios y solo achicamos la lista.
1. Para los amigos: Los amigos de 's' en O no pueden ser más que sus amigos en L. Si ya en L tiene < 4 amigos, en O tendrá aún menos. Falla la condición 1.
2. Para los desconocidos: Los desconocidos de 's' en O son (O - 1 - amigos_en_O). Como vamos eliminando gente de L para llegar a O, la cantidad máxima de personas disponibles para ser "desconocidos" se reduce estrictamente o se mantiene igual. Si en el grupo grande L no llega a juntar 4 personas que no conoce, en un grupo más chico O, la cantidad de extraños será igual o menor. Falla la condición 2.

Por lo tanto, la decisión Greedy de eliminar a 's' es 100% segura y nunca descartará elementos de la solución óptima.
"""

# Bloque de prueba
if __name__ == "__main__":
    n = 10
    # Creamos un grafo donde 0 a 4 son muy amigos entre sí (clique).
    # Pero para sobrevivir, también necesitan que haya otros 4 en la fiesta que no conozcan.
    relaciones_prueba = [
        (0,1), (0,2), (0,3), (0,4),
        (1,2), (1,3), (1,4),
        (2,3), (2,4),
        (3,4),
        # 5 a 9 son conocidos sueltos
        (4,5), (5,6), (6,7), (7,8), (8,9)
    ]
    
    resultado = seleccionar_invitados_con_desconocidos(n, relaciones_prueba)
    
    print("--- Ejercicio 8: Ágape Antillense (Doble Restricción) ---")
    print(f"Total de socios: {n}")
    print(f"Socios que cumplen TODAS las reglas (amigos y desconocidos): {list(resultado)}")