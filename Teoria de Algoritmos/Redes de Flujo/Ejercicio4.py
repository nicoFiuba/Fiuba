"""
EXPLICACIÓN Y MODELADO: estamos ante un problema de actualización de flujo. En lugar de correr Ford-Fulkerson desde cero, vamos a operar directamente sobre el Grafo Residual actual. Pueden ocurrir dos casos si cambia la capacidad de una arista e=(u,v):

- Caso 1 (Aumento de capacidad): Actualizamos la capacidad en el grafo residual. Si esta arista pertenecía al Corte Mínimo (el cuello de botella de la red), es probable que ahora podamos enviar más flujo. Simplemente intentamos buscar nuevos caminos de aumento desde S hasta T en el grafo residual.

- Caso 2 (Disminución de capacidad): Si la nueva capacidad sigue siendo mayor o igual al flujo actual que pasa por ahí, no hacemos nada (el flujo es válido). Si la nueva capacidad es MENOR al flujo actual, tenemos una violación de capacidad (un exceso). 
    1. Reducimos el flujo en (u,v) a la nueva capacidad.
    2. "Devolvemos" el flujo excedente empujándolo desde 'u' hacia 'S' y desde 'T' hacia 'v' usando los caminos del grafo residual.
    3. Finalmente, intentamos enviar flujo nuevamente de S a T por si existe alguna ruta alternativa.

PSEUDOCÓDIGO
"""
def actualizar_flujo(grafo_residual, S, T, u, v, nueva_capacidad):

    flujo_actual = grafo_residual.obtener_flujo(u, v)

    if nueva_capacidad > grafo_residual.obtener_capacidad(u, v):
        grafo_residual.actualizar_capacidad(u, v, nueva_capacidad)
        ford_fulkerson(grafo_residual, S, T) 
    
    elif nueva_capacidad < flujo_actual:
        exceso = flujo_actual - nueva_capacidad
        grafo_residual.reducir_flujo(u, v, exceso)
        grafo_residual.actualizar_capacidad(u, v, nueva_capacidad)

        ford_fulkerson(grafo_residual, u, S)
        ford_fulkerson(grafo_residual, T, v)

        ford_fulkerson(grafo_residual, S, T)
        
    else:
        grafo_residual.actualizar_capacidad(u, v, nueva_capacidad)

"""
ANÁLISIS DE COMPLEJIDAD

- Temporal: como hacemos búsquedas (BFS/DFS) sobre el grafo residual, la complejidad es O(V + E). Ademas, si el cambio de capacidad es pequeño (una constante C), el algoritmo tomará O(C * (V + E))

- Espacial: O(V + E) porque seguimos utilizando el mismo grafo residual que ya teníamos almacenado en memoria, sin crear estructuras nuevas.

EJEMPLO

Supongamos una red simple: S -> A -> T. 
Ambas aristas (S -> A) y (A -> T) tienen capacidad 5. El flujo máximo actual es 5.
El grafo residual tiene aristas hacia atrás (A -> S) y (T -> A) con capacidad 5.

- Caso Aumento: La capacidad de A -> T sube a 10.
Actualizamos la capacidad, pero al correr BFS desde S a T, vemos que S -> A sigue limitando todo a 5 (S -> A es el corte mínimo). El flujo máximo se mantiene en 5.

- Caso Disminución: La capacidad de A -> T baja a 3. 
El flujo actual (5) es mayor a la nueva capacidad (3). Exceso = 2.
1. Bajamos el flujo de A -> T a 3.
2. Devolvemos el exceso 2 desde A hacia S usando la arista residual (A -> S). 
3. Intentamos buscar otro camino de S a T, pero no hay. El nuevo flujo máximo queda en 3.
"""
