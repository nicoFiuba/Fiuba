"""

EXPLICACIÓN: la estrategia consiste agregar a todos los "n" socios y evaluar a cada uno para decidir si se lo descarta o no. Esta estrategia es Greedy porque realiza una elección:
    - Localmente óptima porque en cada iteración, si el invitado no conoce a 4 personas, se lo descarta.
    - Factible ya que cumple con las restricciones del problema
    - Irrevocable ya que una vez tomada la decisión, no permite ser removida en posteriores elecciones del algoritmo.

PSEUDOCÓDIGO
"""

def greedy_destructivo(grafo):

    invitados = obtener_socios(grafo)
    cola_eliminacion = no_cumplen_condicion(grafo)

    while cola_eliminacion:

        invitado_actual = cola_eliminacion.popleft()
        invitados.remove(invitado_actual)

        for amigo in obtener_amigos(invitado_actual, grafo):

            if amigo in invitados:
                restar_amigo(amigo)

                if cantidad_amigos(amigo, grafo) == 3:
                    cola_eliminacion.append(amigo)

    return invitados

"""
ANÁLISIS DE COMPLEJIDAD

- TEMPORAL: recorrer los vértices toma O(V) mientras que recorrer las aristas toma O(E). Si bien existe un bucle anidado, cada vértice y arista se procesa como máximo una vez en toda la ejecución, por ende los tiempos se suman en lugar de multiplicarse. Por lo tanto, la complejidad es O(V + E).

- ESPACIAL: O(V + E) para almacenar el grafo.

ANÁLISIS DE OPTIMALIDAD: se demuestra mediante el absurdo, ya que si una persona no tiene 4 amigos en el grupo actual, es matemáticamente imposible que los encuentre en la lista final. Por lo tanto, eliminar siempre al invitado que tiene menos de 4 amigos nos asegura que vamos a alcanzar la solución óptima global.

EJEMPLO
- Entrada: Grafo con 6 invitados (A, B, C, D, E, F) todos conectados entre sí (cada uno tiene grado 5). Un invitado extra (G) conectado solo a A, B y C (grado 3).
- Ejecución: 
    - Condición inicial: G tiene menos de 4 amigos. cola_eliminacion = [G].
    - Evaluamos G: se lo extrae de la cola y se lo elimina de los invitados. 
    - Actualizamos conexiones: A, B y C pierden a G. Pasan de tener 5 amigos a tener 4. Como su cantidad de amigos no baja a 3, no entran a la cola de eliminación.
    - La cola queda vacía.
- Resultado: Retorna la lista [A, B, C, D, E, F].
"""
