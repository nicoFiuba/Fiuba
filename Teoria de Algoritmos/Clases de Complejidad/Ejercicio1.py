"""

EXPLICACIÓN: Como la caja negra A solo admite grafos conexos, si queremos calcular el tamaño máximo del IS de un grafo G cualquiera, lo dividimos en sus componentes conexas.
Para cada componente probamos k = 1, 2, 3... en la caja A hasta que devuelva "No", la suma de esos k - 1 nos da el tamaño total.
Para encontrar los vértices exactos, iteramos sobre los nodos: quitamos un nodo v. 
- Si el tamaño máximo total del grafo baja, significa que v era parte de la solución óptima (lo guardamos y borramos sus vecinos).
- Si el tamaño no baja, v no era indispensable y lo descartamos

PSEUDOCÓDIGO
"""

def max_conjunto_independiente(grafo):
    
    solucion = []
    k_max = calcular_tamaño(grafo) 
    
    for v in grafo.nodos():
        grafo_prueba = grafo.copiar_y_eliminar_nodo(v)
        
        if calcular_tamaño(grafo_prueba) == k_max:
            grafo = grafo_prueba
        else:
            solucion.append(v)
            grafo.eliminar_nodo(v)
            grafo.eliminar_vecinos(v)
            k_max -= 1
            
    return solucion

"""
ANÁLISIS DE COMPLEJIDAD

- TEMPORAL: en el peor de los casos, iterar los valores de k cuesta O(V) y el ciclo principal toma O(V).Por lo tanto, realizamos O(V²) llamadas a la caja negra. Ademas como el enunciado asume que A corre en tiempo polinomial, todo nuestro algoritmo se ejecuta estrictamente en tiempo polinomial.

-ESPACIAL: O(V + E) para almacenar el grafo y sus copias.

¿TIENE SENTIDO LA HIPÓTESIS? -> No ya que, el problema del Conjunto Independiente pertenece a la clase NP-Completo.
Es decir, que si existiera una caja negra que lo resuelva en tiempo polinomial, todos los problemas NP también podrían resolverse de manera eficiente, lo cual demostraría que P = NP.
"""
