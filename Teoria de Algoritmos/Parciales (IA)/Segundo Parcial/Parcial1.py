'''
-----------------------------------------------------------------------------
EJERCICIO 1: REDES DE FLUJO (La topología de la red HackITBA)
-----------------------------------------------------------------------------
Enunciado:
Como parte del equipo técnico de una competencia de programación, diseñaste una red de servidores locales interconectados para que los participantes puedan subir su código. Existe un servidor principal (Fuente S) que provee la conexión general, y un servidor de evaluación (Sumidero T) donde se testean los proyectos. En el medio hay decenas de routers interconectados mediante cables bidireccionales. Te preocupa la robustez de esta red ante posibles sabotajes o caídas de  tensión. Se te pide diseñar un algoritmo que, dada la red, determine cuál es la cantidad MÍNIMA de routers (nodos intermedios) que se pueden apagar para que sea IMPOSIBLE que cualquier paquete de datos llegue desde S hasta T, dejando el evento incomunicado. (Asumir que los servidores S y T están blindados y no se pueden apagar).

Se pide:
1. Explicación de la estrategia de modelado elegida.
2. Definición de la Red (explicar cómo se construye el grafo a resolver detallando Nodos, Aristas y Capacidades).
3. Pseudocódigo detallado (incluyendo armado de la red, llamada al algoritmo de flujo y obtención de la solución).
4. Complejidad temporal.

-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicación: el problema nos pide encontrar el corte minimo de vertices, por lo tanto como los algortimos clasicos de redes operan sobre aristas, necesitamos transformar el costo de romper un nodo en el costo de cortar una arista interna, para eso usamos Vertex Splitting. Gracias al teorema de Flujo Maximo - Corte Minimo, podemos asegurar que el valor resultante sera la cantidad minima de routers a apagar.

Red (Nodos, aristas y capacidades):

Dado el grafo G = (V, E), armamos una nueva red de flujo G' = (V', E') de la siguiente manera:

- Nodos: por cada nodo en V creamos dos nodos (nodo_interno y nodo_externo). La fuente S y el sumidero T se mantienen intactos.

- Aristas Internas: para representar la vulnerabilidad del router agregamos una arista dirigida (nodo_interno -> nodo_externo) con capacidad 1. Si se corta esta arista, significa que el router se apago.

- Aristas Externas: para cada cable bidireccional entre los routers ('origen' y 'destino'), agregamos dos aristas dirigidas con capacidad infinita (origen_externo -> destino_interno y destino_externo -> origen_interno). Esto fuerza al algoritmo a no cortar un cable.

- Conexiones: Las aristas que salen de S se conectan a los nodos internos de sus vecinos (con capacidad infinita) mientras que las que llegan a T provienen de los nodos externos (con capacidad infinita)

Pseudocodigo:

def routers_minimos_para_apagar(grafo, S, T):
    
    # Primero armamos la red
    red = GrafoDirigido()

    for nodo in grafo.nodos:
        red.agregar_nodo(nodo + "_interno")
        red.agregar_nodo(nodo + "_externo")
        red.agregar_arista(nodo + "_interno", nodo + "_externo", capacidad = 1)
    
    for origen, destino in grafo.aristas:
        red.agregar_arista(origen + "_externo", destino + "_interno", capacidad = float('inf'))
        red.agregar_arista(destino + "_externo", origen + "_interno", capacidad = float('inf'))
    
    red.agregar_nodo(S)
    red.agregar_nodo(T)

    for vecino in grafo.vecinos(S):
        red.agregar_arista(S, vecino + "_interno", capacidad = float('inf'))
    
    for vecino_de_T in grafo.incidentes(T):
        red.agregar_arista(vecino_de_T + "_externo", T, capacidad = float('inf'))
    
    # Llamada a Ford-Fulkerson con BFS => Edmonds-Karp
    flujo_maximo, grafo_residual = ford_fulkerson(red, S, T)

    # Solucion
    return flujo_maximo

Complejidad:

- Armar la red toma O(V + E)
- La red transformada tiene 2V nodos y V + 2E aristas
- Al usar Edmonds-Karp la complejidad teorica es O(V' * E'²) por lo tanto trayendolo a nuestra red, nos queda O(V * (V + E)²)


'''