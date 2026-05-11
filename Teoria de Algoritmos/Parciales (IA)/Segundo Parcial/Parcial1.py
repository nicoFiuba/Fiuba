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

Explicación: el problema nos pide encontrar el corte minimo de vertices, por lo tanto como los algoritmos clasicos de redes operan sobre aristas, necesitamos transformar el costo de romper un nodo en el costo de cortar una arista interna, para eso usamos Vertex Splitting. Gracias al teorema de Flujo Maximo - Corte Minimo, podemos asegurar que el valor resultante sera la cantidad minima de routers a apagar.

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

-----------------------------------------------------------------------------
EJERCICIO 2: CLASES DE COMPLEJIDAD (El Lineup del Lollapalooza)
-----------------------------------------------------------------------------
Enunciado:
Se anunció el Lollapalooza 2026 y querés ir a ver la mayor cantidad de bandas. Hay un total de N bandas tocando durante el fin de semana. Algunas bandas tocan en escenarios distintos al mismo tiempo o en horarios superpuestos, lo que significa que "chocan" y no podés ir a ver a ambas. Querés saber si es posible armar un cronograma seleccionando exactamente K bandas para ir a ver sin que NINGUNA de las seleccionadas se superponga con otra. (Llamemos al problema: LOLLA)

Se pide:
1. Paso 1: Demostrar que el problema pertenece a NP (explicando certificado, pseudocódigo del certificador y su complejidad).
2. Paso 2: Demostrar que es NP-Hard mediante una reducción polinomial  (explicar la reducción, la complejidad de la transformación y la justificación de "Ida y vuelta"). Asumir que Independent Set es NP-C.
3. Conclusión final de su clasificación.

-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Demostracion de pertenencia a NP

- Explicacion del certificado: la evidencia que nos dan es que existe un subconjunto S que contiene exactamente las K bandas seleccionadas.

- Pseudocodigo del certificador:

def certificador_lolla(bandas, conflictos, K, certificado_S):

    n = len(certificado_S)

    if n != K:
        return False
    
    for i in range(n):
        for j in range(i + 1, n):
            banda1 = certificado_S[i]
            banda2 = certificado_S[j]

            if (banda1, banda2) in conflictos or (banda2, banda1) in conflictos:
                return False
    return True

- Complejidad del certificador: verificar el tamaño toma O(1) u O(K) y el doble loop toma O(K²). Si pensamos a los conflictos como un HashSet, verificar la existencia de uno es O(1). Como K <= N, entonces el tiempo maximo es O(N²), lo que quiere decir que corre en tiempo polinomial y por ende el programa pertenece a NP

Demostracion de pertenencia a NP-Hard

- Reduccion: el problema Independent Set (IS) busca un subconjunto de K vertices en un grafo G = (V, E) donde ningun par de vertices comparta una arista.
Dada una instancia de IS (G, K), armamos una instancia para nuestro problema:
1) Por cada vertice 'v' de G, creamos una banda 'v' en el lolla.
2) Por cada arista e = (u, v) en G, agregamos un conflicto entre las bandas 'u' y 'v'
3) El valor K de bandas a elegir sera el mismo K solicitado en IS

- Complejidad de la transformacion: mapear V vertices y E aristas es O(V + E) lo cual es estrictamente polinomial.

- Explicacion:

- IDA: si existe un IS de tamaño K en G, significa que esos K vertices no tienen ninguna arista que los conecte. Al trasladarlo a nuestro problema, elegimos K bandas que no tienen conflictos.

- VUELTA: si nuestro problema encuentra una solucion valida seleccionando K bandas sin conflictos, significa que los vertices en G no comparten ninguna arista, por lo tanto conforman un IS de tamaño K valido.

- Conclusion: como demostramos que nuestro programa pertenece a NP mediante un certificador polinomial y ademas demostramos que tambien pertenece a NP-Hard mediante una reduccion polinomial, podemos afirmar que nuestro problema es un NP-Completo.

-----------------------------------------------------------------------------
EJERCICIO 3: BÚSQUEDA EXHAUSTIVA (El grid de contenido)
-----------------------------------------------------------------------------
Enunciado:
Para una cuenta de redes sociales, tenés una matriz de planificación de contenido de N x N celdas. En cada celda (i,j) anotaste un valor v_ij > 0 que representa la cantidad de interacciones que estimás que tendría una publicación si la subís en ese bloque. Querés seleccionar un subconjunto de celdas para publicar y que la suma total de interacciones sea la MÁXIMA posible. Sin embargo, para no saturar al algoritmo, el sistema tiene una restricción: no podés seleccionar dos celdas que sean adyacentes entre sí (ni compartiendo borde horizontal ni vertical). 

Se pide resolver usando Branch and Bound detallando:
1. Explicación de la técnica aplicada a este problema (definir cotas y condición de poda).
2. Diagrama/explicación de los estados y la ramificación del árbol.
3. Pseudocódigo de la solución.
4. Complejidad temporal y espacial.

-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion:

- Solucion Parcial: es el valor acumulado actualmente

- Cota Inferior: es la mejor solucion global valida encontrada hasta el momento. Se actualiza cada vez que la solucion parcial supera el record.

- Cota Superior: es una cota admisible por exceso y como buscamos maximizar, sumamos la solucion parcial actual a la suma de todos los v_ij de las celdas restantes.

- Poda: Si la Cota Superior de un nodo es menor o igual a la Cota Inferior, entonces podamos esa rama ya que nunca va a superar a nuestro record

Diagrama de estados:

Metemos la matriz en un array unidimensional que va desde 0 hasta n² - 1
- Estado inicial: k = 0, ninguna celda fue evaluada ni seleccionada
- Decisiones en el nivel k: al evaluar la celda 'k', tenemos hasta dos opciones de ramificacion:
1) Incluir a k siempre y cuando ninguna celda adyacente a k en la matriz original haya sido previamente seleccionada
2) No incluir a k (esta opcion siempre es valida)
- Caso base: k = n², lo que significa que ya tomamos una decision para todas las n² celdas de la matriz

Pseudocodigo:

MEJOR_GLOBAL = 0

def branch_and_bound_grid(k, celdas, seleccionadas, suma_parcial):

    global MEJOR_GLOBAL
    n = len(celdas)

    # Caso Base
    if k == n:
        if suma_parcial > MEJOR_GLOBAL:
            MEJOR_GLOBAL = suma_parcial
        return
    
    # Calcular Cota Superior
    likes_restantes = 0
    for i in range(k, n):
        likes_restantes += celdas[i].valor
    
    cota_superior = suma_parcial + likes_restantes

    # Condicion de Poda
    if cota_superior <= MEJOR_GLOBAL:
        return
    
    celda_actual = celdas[k]

    # Rama Izquierda
    if no_tiene_adyacentes_seleccionados_anteriormente(celda_actual, seleccionadas):
        seleccionadas.add(celda_actual.id)
        nueva_suma = suma_parcial + celda_actual.valor

        branch_and_bound_grid(k + 1, celdas, seleccionadas, nueva_suma)
        
        seleccionadas.remove(celda_actual.id)

    # Rama Derecha
    branch_and_bound_grid(k + 1, celdas, seleccionadas, suma_parcial)

Complejidad:

- Temporal: en el peor de los casos, para las N² celdas, exploramos 2 decisiones (incluir o no incluir), por lo tanto O(2^N²). Ademas en cada nodo iteramos para calcular la cota superior, lo que toma O(N²). Por lo tanto la complejidad total es O(N² * 2^N²)

- Espacial: O(N²) debido a la profundidad maxima del call stack de la recursion

'''
