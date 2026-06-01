"""
--------------------------------------------------------------------------------
EJERCICIO 1: REDES DE FLUJO
--------------------------------------------------------------------------------
Enunciado:
Una empresa cuenta con n centros de producción, m centros de consumo y depósitos intermedios, conectados por rutas de capacidad diaria conocida. Cada centro de producción 'i' genera hasta p_i unidades por dia, cada centro de consumo 'j' recibe hasta q_j, y cada depósito 'v' procesa hasta c_v. Determinar la máxima cantidad de mercadería que puede distribuir por día e identificar el número mínimo de rutas y depósitos que, al quitarse simultáneamente, impedirían cualquier traslado de mercadería entre producción y consumo. Modelar como problema de redes de flujo y resolver, justificando las decisiones de diseño.

Se pide:
1. Explicación de la estrategia de modelado elegida.
2. Definición de la Red (explicar cómo se construye el grafo a resolver detallando Nodos, Aristas y Capacidades).
3. Pseudocódigo detallado (incluyendo armado de la red, llamada al algoritmo de flujo y obtención de la solución).
4. Complejidad temporal.
--------------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion: estamos ante un problema de asignacion el cual lo vamos a resolver mediante el algoritmo de flujo maximo, la idea es construir una red en donde cada unidad de flujo represente la mercaderia transportada, garantizando lo pedido. Ademas tenemos que partir al enrutador en dos para que no exceda su capacidad.

Definicion de la red

Dado un conjunto de N producciones, M consumos y D depositos, creamos dos redes (red_mercaderia y red_cortes) de la siguiente manera:

Nodos: agregamos una fuente S, un sumidero T, N nodos (uno por produccion), M nodos (uno por consumo) y 2D nodos (v_interno y v_externo) para la restriccion de cada deposito. Estos nodos van para ambas redes.

Aristas (Red Mercaderia):
1) S -> Produccion: capacidad p_i
2) v_interno -> v_externo: capacidad c_v
3) Consumo -> T: capacidad q_j
4) Rutas originales: capacidad original de la ruta

Aristas (Red Cortes):
1) S -> Produccion: capacidad infinita
2) v_interno -> v_externo y Rutas originales: capacidad 1
3) Consumo -> T: capacidad infinita

Pseudocodigo:

def resolver_logistica(producciones, consumos, depositos, rutas):

    red_mercaderia = GrafoDirigido()
    red_cortes = GrafoDirigido()

    for produccion in producciones:
        red_mercaderia.agregar_arista("S", produccion.id, capacidad = produccion.p)
        red_cortes.agregar_arista("S", produccion.id, capacidad = float('inf'))

    for consumo in consumos:
        red_mercaderia.agregar_arista(consumo.id, "T", capacidad = consumo.q)
        red_cortes.agregar_arista(consumo.id, "T", capacidad = float('inf'))

    for deposito in depositos:
        red_mercaderia.agregar_arista(deposito.id + "_interno", deposito.id + "_externo", capacidad = deposito.c)
        red_cortes.agregar_arista(deposito.id + "_interno", deposito.id + "_externo", capacidad = 1)

    for ruta in rutas:
        red_mercaderia.agregar_arista(ruta.origen, ruta.destino, capacidad = ruta.capacidad)
        red_cortes.agregar_arista(ruta.origen, ruta.destino, capacidad = 1)

    flujo_maximo, grafo_residual = ford_fulkerson(red_mercaderia, "S", "T")

    cantidad_minima_cortes, residual_cortes = ford_fulkerson(red_cortes, "S", "T")

    nodos_alcanzables = BFS_residual(residual_cortes, "S")
    rutas_a_quitar = obtener_aristas_corte(red_cortes, nodos_alcanzables)

    return flujo_maximo, cantidad_minima_cortes, rutas_a_quitar

Complejidad:

- Armar las redes toma O(N + M + D + R)
- V' tiene 2 + N + M + 2D nodos, por lo tanto O(N + M + D)
- E' tiene N + M + D + R aristas, por lo tanto O(N + M + D + R)
Al usar Edmonds-Karp la complejidad teorica es O(V' * E'²), por lo tanto si lo traemos a nuestra red, nos queda O((N + M + D) * (N + M + D + R)²)


--------------------------------------------------------------------------------
EJERCICIO 2: BÚSQUEDA EXHAUSTIVA
--------------------------------------------------------------------------------
Enunciado:
Contamos con "n" jugadores de ajedrez, cada uno con un puntaje ELO conocido. Se desea formar exactamente n/p equipos de "p" jugadores cada uno (asumir "n" múltiplo de "p"), de modo de minimizar la diferencia entre el ELO promedio del equipo más fuerte y el del más débil. Resolver con branch & bound, justificando las decisiones de diseño.

Se pide resolver usando Branch and Bound detallando:
1. Explicación de la técnica aplicada a este problema (definir cotas y condición de poda).
2. Diagrama/explicación de los estados y la ramificación del árbol.
3. Pseudocódigo de la solución.
4. Complejidad temporal y espacial.
--------------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion

- Solucion Parcial: es la asignacion actual de los jugadores a los distintos equipos

- Cota Inferior: es la diferencia entre el maximo y minimo promedio de los equipos que ya estan llenos (si no hay al menos dos equipos llenos, es 0). Como buscamos minimizar, esta es la estimacion mas optimista

- Cota Superior: es la mejor diferencia global valida encontrada hasta el momento. Se actualiza cuando todos los equipos estan llenos y la diferencia rompe el record

- Poda: si la cota inferior de un nodo es mayor o igual que la cota superior entonces podamos esa rama ya que nunca va a poder superar el record

Diagrama de estados

- Definicion: se considera un estado de modo (k, equipos) donde equipos es un arreglo de listas

- Estado Inicial: (0, [[], [], ...]) el jugador 0 a procesar y los n/p equipos vacios

- Decision en el nivel 'k': al evaluar al jugador 'k', tenemos hasta n/p opciones de ramificacion
1) Incluir a k en el equipo j siempre y cuando el equipo j tenga menos de 'p' jugadores

Pseudocodigo:

MEJOR_DIFERENCIA = float('inf')

def branch_and_bound_ajedrez(k, jugadores, p, equipos):

    global MEJOR_DIFERENCIA
    n = len(jugadores)

    if n == k:
        diferencia_actual = calcular_diferencia_promedios(equipos)
        if diferencia_actual < MEJOR_DIFERENCIA:
            MEJOR_DIFERENCIA = diferencia_actual
        return
    
    cota_inferior = estimar_diferencia_minima(equipos)

    if cota_inferior >= MEJOR_DIFERENCIA:
        return
    
    jugador_actual = jugadores[k]
    
    i = 0
    l = len(equipos)
    
    podar_simetria = False
    
    while i < l and not podar_simetria:
        if len(equipos[i]) < p:
            equipos[i].append(jugador_actual)
            branch_and_bound_ajedrez(k + 1, jugadores, p, equipos)
            equipos[i].pop()
            
            if len(equipos[i]) == 0:
                podar_simetria = True
        
        i += 1

Complejidad:

- Temporal: en el peor de los casos exploramos poner cada uno de los N jugadores en los N/P equipos, lo que toma O((N/P)^N)

- Espacial: O(N) ya que es la profundidad maxima del call stack de la recursion


--------------------------------------------------------------------------------
EJERCICIO 3: CLASES DE COMPLEJIDAD
--------------------------------------------------------------------------------
Enunciado:
Una empresa tiene n proyectos posibles. Cada proyecto 'i' tiene un beneficio b_i y un costo c_i. Algunos pares de proyectos son incompatibles entre sí. Dados valores B, C y k, decidir si existe un subconjunto de al menos k proyectos compatibles entre sí cuyo beneficio total sea al menos B y cuyo costo total no supere C. Demostrar que el problema es NP-Completo.

Se pide:
1. Paso 1: Demostrar que el problema pertenece a NP (explicando certificado, pseudocódigo del certificador y su complejidad).
2. Paso 2: Demostrar que es NP-Hard mediante una reducción polinomial (explicar la reducción, la complejidad de la transformación y la justificación de "Ida y vuelta").
3. Conclusión final de su clasificación.
--------------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Demostracion de pertenencia a NP

Explicacion del certificado: la evidencia que nos dan es un subconjunto S de proyectos seleccionados

Pseudocodigo del certificado:

def certificado(proyectos, incompatibilidades, K, B, C, certificado_S):

    n = len(certificado_S)

    if n < K:
        return False

    costo_total = 0
    for proyecto in certificado_S:
        costo_total += proyecto.costo
        
    if costo_total > C:
        return False

    beneficio_total = 0
    for proyecto in certificado_S:
        beneficio_total += proyecto.beneficio
        
    if beneficio_total < B:
        return False

    for i in range(n):
        for j in range(i + 1, n):
            if son_incompatibles(certificado_S[i], certificado_S[j], incompatibilidades):
                return False

    return True

Complejidad:

- Verificar el tamaño, sumar costos y sumar beneficios toma O(S)
- Iterar sobre cada par para verificar incompatibilidades toma O(S²)
Por lo tanto la complejidad que nos queda es O(S²) y como es estrictamente polinomial queda demostrado que pertenece a NP

Demostracion de NP-Hard

- Reduccion: el problema Independent Set (IS) busca un conjunto de J vertices en un grafo G = (V, E) donde ningun par de vertices compartan una arista. Para reducirlo a nuestro problema, creamos un proyecto por cada vertice de V. Si existe una arista entre dos vertices, definimos esos proyectos como incompatibles. Fijamos el costo de todos los proyectos en 0 y su beneficio en 1. Seteamos los parametros K = J, B = J y C = 0

- Complejidad: iterar sobre los vertices y aristas para mapearlos a proyectos e incompatibilidades toma O(V + E), por lo tanto es una reduccion estrictamente polinomial

- IDA: si existe un IS de tamaño J, tomamos esos mismos J proyectos. Como en IS no comparten aristas, los proyectos son todos compatibles. Son J proyectos (cumple >= K), suman costo 0 (cumple <= C) y suman beneficio J (cumple >= B)

- VUELTA: si nuestro algoritmo encuentra un subconjunto valido, sabemos que selecciono al menos J proyectos 100% compatibles entre si. Por la forma en que armamos la reduccion, que sean compatibles significa que en el grafo original no existe ninguna arista que conecte a esos J vertices, por lo tanto conforman un Independent Set valido.

Conclusion: como demostramos que el problema pertenece a NP mediante un certificado polinomial y que ademas pertenece a NP-Hard mediante una reduccion polinomial, podemos afirmar que nuestro problema es un NP-Completo

"""
