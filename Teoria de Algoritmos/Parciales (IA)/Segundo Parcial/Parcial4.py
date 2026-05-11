'''
-----------------------------------------------------------------------------
EJERCICIO 1: REDES DE FLUJO (El Torneo de Fútbol)
-----------------------------------------------------------------------------
Enunciado:
Estás organizando la logística de un torneo de fútbol amateur. Se anotaron T equipos y cada uno pagó su inscripción de $180.000. Para la primera fecha, cada equipo debe jugar exactamente un partido. Tenés un convenio con un predio que tiene C canchas disponibles. Cada cancha j tiene un límite máximo de K_j partidos que puede albergar durante el fin de semana por cuestiones de mantenimiento y disponibilidad de árbitros. A su vez, en el formulario de inscripción, cada equipo pasó una lista indicando en qué canchas específicas les queda cómodo jugar.

Se pide:
1. Explicación de la estrategia de modelado elegida.
2. Definición de la Red (explicar cómo se construye el grafo a resolver detallando Nodos, Aristas y Capacidades).
3. Pseudocódigo detallado.
4. Complejidad temporal.

-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion: estamos ante un problema de asignacion el cual lo vamos a resolver usando el algoritmo de flujo maximo, la idea es construir una red en donde cada unidad de flujo represente a un equipo asignado a una cancha especifica, garantizando que se cumpla lo pedido.

Red (Nodos, Aristas y Capacidades):

Dado un conjunto E de equipos y C de canchas, creamos una nueva red de flujo G' de la siguiente manera:

- Nodo:  agregamos una fuente S, un sumidero T, E nodos (uno por cada equipo) y C nodos (uno por cada cancha)

- Aristas desde S: conectamos S a cada equipo 'i' con capacidad 1, lo que garantiza que cada equipo sea asignado a una cancha

- Arista E - C: si el equipo 'i' indico que quiere jugar en la cancha 'j', agregamos una arista dirigida desde el equipo 'i' hasta la cancha 'j' con capacidad 1. Esto garantiza que cada equipo juegue en la cancha que pidio.

- Aristas hacia T: conectamos cada cancha 'j' al sumidero T con capacidad K_j, lo que garantiza que ninguna cancha tenga mas partidos de los permitidos

Pseudocodigo:

def es_posible_asignar(equipos, canchas, interes):

    # Armamos el grafo
    red = GrafoDirigido()
    S = "Fuente"
    T = "Sumidero"

    red.agregar_nodo(S)
    red.agregar_nodo(T)

    # Conectamos S con los equipos
    for equipo in equipos:
        red.agregar_nodo(equipo.id)
        red.agregar_arista(S, equipo.id, capacidad = 1)
    
    # Conectamos las canchas con T
    for cancha in canchas:
        red.agregar_nodo(cancha.id)
        red.agregar_arista(cancha.id, T, capacidad = cancha.K)
    
    # Conectamos a los equipos con las canchas, segun interes
    for equipo in equipos:
        for cancha in canchas:
            if le_interesa(equipo, cancha, interes):
                red.agregar_arista(equipo.id, cancha.id, capacidad = 1)
    
    # Llamada a Ford-Fulkerson con BFS => Edmonds-Karp
    flujo_maximo, grafo_residual = ford_fulkerson(red, S, T)

    # Solucion
    return flujo_maximo == len(equipos)

Complejidad

- Armar la red toma O(E + C)
- V' tiene 2 + E + C nodos, por lo tanto O(E + C)
- E' tiene E + C + (E * C) aristas, por lo tanto O(E * C)
- Al usar Edmonds-Karps la compljidad teorica es de O(V' * E'²), trayendolo a nuestro problema nos queda: O((E + C) * (E * C)²)

-----------------------------------------------------------------------------
EJERCICIO 2: CLASES DE COMPLEJIDAD (Vigilancia en el Predio)
-----------------------------------------------------------------------------
Enunciado:
Para la seguridad del torneo, se necesita instalar cámaras. Tenés un mapa  representado como un grafo no dirigido G = (V, E), donde los vértices son  intersecciones de pasillos y las aristas son los pasillos en sí. Querés elegir un subconjunto de vértices (intersecciones) de tamaño máximo K para poner las  cámaras, de tal forma que TODAS las aristas (pasillos) tengan al menos uno de sus extremos vigilado por una cámara. A este problema de decisión lo llamamos  VERTEX-COVER.

Se pide:
1. Paso 1: Demostrar que el problema pertenece a NP (explicando certificado, pseudocódigo del certificador y su complejidad).
2. Paso 2: Demostrar que es NP-Hard mediante una reducción polinomial (explicar la reducción, la complejidad de la transformación y la justificación de "Ida y vuelta").
3. Conclusión final de su clasificación.

-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Demostracion de pertenencia a NP

- Explicacion: la evidencia que nos dan es que existe un subconjunto S que contiene a lo sumo K camaras

- Pseudocodigo:

def certificador(pasillos, K, certificado_S):

    n = len(certificado_S)

    if n > K:
        return False
    
    for pasillo in pasillos:
        interseccion1 = pasillo.origen
        interseccion2 = pasillo.destino

        if interseccion1 not in certificado_S and interseccion2 not in certificado_S:
            return False
    
    return True

- Complejidad

- Verificar el tamaño toma O(1)
- Iterar sobre los pasillos toma O(E)
- si pensamos a certificado_S como un HashSet, verificarlo toma O(1)
Por lo tanto la complejidad nos queda en O(E) y esta es estrictamente polinomial, por ende queda demostrado que nuestro problema pertenece a NP

Demostracion de pertenencia a NP-Hard

- Reduccion: el problema Independent Set (IS) busca un subconjunto de J vertices en un grafo G = (V, E) donde ningun par de vertices comparta una arista. Por lo tanto armamos una instancia con el mismo grafo (G' = G) y definimos el limite de camaras como K = |V| - J

- Complejidad: copiar las referencias del grafo y realizar la resta toma O(1), lo cual es estrictamente polinomial

- IDA: si definimos a un conjunto como S = V - IS, por definicion de IS es imposible que los dos extremos de una arista esten adentro del conjunto, por lo tanto uno de sus extremos pertenece a S.

- VUELTA: si definimos a un conjunto como I = V - S y suponemos por el absurdo que I no es un IS, significa que existen dos vertices conectados por una arista por ende ninguno de estos vertices va a pertenecer a S. Esto significa que habria un pasillo sin vigilar.

- Conclusion: como demostramos que nuestro problema pertenece a NP mediante un certificador polinomial y ademas demostramos que pertenece a NP-Hard mediante una reduccion polinomial, podemos afirmar que nuestro problema es un NP-Completo

-----------------------------------------------------------------------------
EJERCICIO 3: BRANCH & BOUND (El Sistema de Pilates)
-----------------------------------------------------------------------------
Enunciado:
Estás desarrollando el módulo de optimización de ingresos para el sistema  administrativo de una profesora de Pilates. La profesora da clases personalizadas (de a un solo alumno por vez) y tiene H franjas horarias disponibles en el día. Hay A alumnos interesados en tomar una clase hoy. Cada alumno i tiene un perfil en el sistema que indica:
- Un monto V_i que está dispuesto a pagar por la clase.
- Una lista con los horarios específicos a los que puede asistir.
Como es la parte administrativa enfocada en la profesora, el objetivo del sistema es elegir qué alumno asignar a qué horario para MAXIMIZAR la ganancia total del día (sabiendo que un alumno toma a lo sumo una clase, y cada horario puede tener a lo sumo un alumno).

Se pide:
1. Explicación de la técnica aplicada a este problema (definir cotas y condición de poda).
2. Diagrama/explicación de los estados y la ramificación del árbol.
3. Pseudocódigo de la solución.
4. Complejidad temporal y espacial.

-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion:

- Solucion Parcial: es el valor acumulado actualmente

- Cota Inferior: es la mejor solucion global valida hasta el momento. Se actualiza cada vez que la solucion parcial supere el record.

- Cota Superior: es una cota admisible por exceso y como buscamos maximizar, sumamos la ganancia parcial a la suma de la ganancia maxima de los alumnos restantes.

- Poda: si la cota Superior de un nodo es menor o igual que la cota inferior, podamos esa rama ya que nunca va a superar a nuestro record

Diagrama de estados:

- Estado inicial: k = 0, ningun alumno fue procesado
- Decision en el nivel 'k': al evaluar al alumno 'k', tenemos hasta dos opciones de ramificacion:
1) Incluir a k siempre y cuando el horario 'h' escogido este libre.
2) No incluir a k (esta opcion siempre es valida)

Pseudocodigo:

MEJOR_GLOBAL = 0

def branch_and_bound(k, alumnos, horarios_ocupados, ganancia_parcial):

    global MEJOR_GLOBAL
    n = len(alumnos)

    # Caso Base
    if k == n:
        if ganancia_parcial > MEJOR_GLOBAL:
            MEJOR_GLOBAL = ganancia_parcial
        
        return
    
    # Calculamos la Cota Superior
    ganancia_actual = 0
    for i in range(k, n):
        ganancia_actual += alumnos[i].ganancia
    
    cota_superior = ganancia_parcial + ganancia_actual

    # Condiciones de Poda
    if cota_superior <= MEJOR_GLOBAL:
        return
    
    alumno_actual = alumnos[k]

    # Rama Izquierda
    horario_libre =  no_esta_ocupado(alumno_actual, horarios_ocupados)

    if horario_libre != None:
        
        horarios_ocupados.add(horario_libre)

        nueva_ganancia = ganancia_parcial + alumno_actual.ganancia
        
        branch_and_bound(k + 1, alumnos, horarios_ocupados, nueva_ganancia)

        horarios_ocupados.remove(horario_libre)
    
    # Rama derecha
    branch_and_bound(k + 1, alumnos, horarios_ocupados, ganancia_parcial)

Complejidad:

- Temporal: en el peor de los casos para los A alumnos exploramos dos opciones (incluir o no incluir), por lo tanto O(2^A). Ademas por cada nodo tenemos que calcular la Cota Superior que toma O(A), por lo tanto tenemos una complejidad de O(A * 2^A)

- Espacial: O(A) ya que es el call stack de la profundidad maxima de la recursion

'''
