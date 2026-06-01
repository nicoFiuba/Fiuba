"""
--------------------------------------------------------------------------------
EJERCICIO 1: ALGORITMOS GOLOSOS
--------------------------------------------------------------------------------
Enunciado:
Una plataforma de streaming de e-sports debe procesar N videos de análisis táctico de un torneo. Cada video 'i' requiere un tiempo de procesamiento continuo e ininterrumpido T_i en el servidor central. Además, cada video tiene un horario límite de publicación D_i acordado con los organizadores. Si un video finaliza su procesamiento en el instante F_i, el impacto negativo en el algoritmo de recomendación (penalización) se calcula como max(0, F_i - D_i). Se desea diseñar un algoritmo eficiente que planifique el orden de procesamiento de los videos para minimizar la máxima penalización sufrida entre todos los videos.

Se pide:
1. Explicación y por qué es Greedy.
2. Pseudocódigo.
3. Complejidad temporal y espacial.
4. Demostración de optimalidad.
--------------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion: la estrategia consiste en ordenar los videos de menor a mayor segun su horario limite, esto hace que siempre se haga primero el que vence antes. Es greedy porque en cada iteracion el programa elije el video mas proximo a vencer.

Pseudocodigo:

def minimizar_penalizaciones(videos):

    videos.sort(key = lambda x: x.horario)

    penalizacion = 0
    tiempo_actual = 0
    orden_final = []
    for video in videos:
        tiempo_actual += video.procesamiento
        penalizacion_actual = max(0, tiempo_actual - video.horario)

        if penalizacion_actual > penalizacion:
            penalizacion = penalizacion_actual

        orden_final.append(video.id)

    return orden_final, penalizacion

Complejidad:

- Temporal: ordenar toma O(N log(N)) y recorrerla toma O(N). Por lo tanto la comllejidad es O(N * log(N))

- Espacial: O(N) para almacenar el orden_final

Demostracion de optimalidad: si una solucion decide agregar un video de mayor horario limite, estaria empeorando la penalizacion. Por lo tanto tendriamos que intercambiar el orden de los videos, es decir poner el de menor horario limite (es lo que hace Greedy) para asi poder minimizar la penalizacion


--------------------------------------------------------------------------------
EJERCICIO 2: MODELADO DE GRAFOS
--------------------------------------------------------------------------------
Enunciado:
El sistema central de inscripciones universitarias debe enrutar el tráfico de datos desde N sedes regionales hacia M facultades de destino a través de una red de P nodos de ruteo intermedios. Cada enlace de fibra óptica entre dos puntos de la red soporta un máximo de K conexiones concurrentes. Sin embargo, debido a limitaciones físicas del hardware, cada nodo de ruteo intermedio 'p' tiene un límite estricto de procesamiento interno: no puede procesar (sumando todo el tráfico que entra y todo el que sale de él) más de W_p peticiones concurrentes, independientemente del ancho de banda de los enlaces conectados a él. Modele el problema para determinar la cantidad máxima de inscripciones concurrentes que el sistema puede soportar desde las sedes hasta las facultades.

Se pide:
1. Explicación de la estrategia de modelado elegida.
2. Definición de la Red (explicar cómo se construye el grafo a resolver detallando Nodos, Aristas y Capacidades).
3. Pseudocódigo detallado (incluyendo armado de la red, llamada al algoritmo de flujo y obtención de la solución).
4. Complejidad temporal.
--------------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Exlicacion: estamos ante un problema de asignacion el cual lo vamos a resolver mediante el algoritmo de flujo maximo, la idea es construir una red en donde cada unidad de flujo represente a una inscripcion, garantizando lo pedido. Ademas teemos qeu partir al enrutador en dos para que no exceda su capacidad

Definicion de la red

Dado un conjunto de N sedes y un conjunto de M facultades, creamos una nueva red G' de la siguiente manera:

Nodos: agregamos una fuente S, un sumidero T, N nodos (uno por cada sede), M nodos (uno por cada facultad) y 2P nodos (p_interno y p_externo) para la restriccion

Aristas:
1) S -> Sedes: capacidad infinita
2) Sedes -> p_interno: capacidad K
3) p_interno -> p_externo: capacidad W_p
4) p_externo -> Facultades: capacidad K
5) Facultades -> T: capacidad infinita

Pseudocodigo:

def cantidad_maxima(sedes, facultades, P):

    red = GrafoDirigido()

    for sede in sedes:
        red.agregar_arista("S", sede.id, capacidad = float('inf'))

        
    for p in P:
        red.agregar_arista(p.id + "_interno", p.id + "_externo", capacidad = p.W_p)
    
        for sede in sedes:
            red.agregar_arista(sede.id, p.id + "_interno", capacidad = sede.K)

        for facultad in facultades:
            red.agregar_arista(p.id + "_externo", facultad.id, capacidad = facultad.K)

    for facultad in facultades:
        red.agregar_arista(facultad.id, "T", capacidad = float('inf'))

    # Ford-Fulkerson con BFS => Edmonds-Karps
    flujo_maximo, grafo_residual = ford_fulkerson(red, "S", "T")

    return flujo_maximo

Complejidad
- Armar la red toma O(P * (N + M))
- V' tiene 2 + 2P + N + M nodos, por lo tanto O(P + N + M)
- E' tiene N + P + M + (N * P) + (P * M) aristas, por lo tanto O(P * (N + M))
Al usar Edmonds-Karps la complejidad teorica es O(V' * E'²), por lo tanto si lo traemos a nustra red, nos queda que O((P + N + M) * (P * (N + M))²)


--------------------------------------------------------------------------------
EJERCICIO 3: CLASES DE COMPLEJIDAD
--------------------------------------------------------------------------------
Enunciado:
Se define el problema de decisión SEGURIDAD EN EL ESTADIO (SE): Dado un plano modelado como un grafo no dirigido G=(V,E) donde los vértices son puntos de observación y las aristas son los pasillos que los conectan, y un presupuesto K, ¿es posible instalar cámaras en a lo sumo K puntos de observación de manera tal que TODOS LOS PASILLOS queden vigilados por al menos una cámara ubicada en alguno de sus extremos? Sabiendo que el problema CONJUNTO INDEPENDIENTE (Independent Set) es NP-Completo, demuestre formalmente que el problema SE pertenece a la clase NP-Completo.

Se pide:
1. Paso 1: Demostrar que el problema pertenece a NP (explicando certificado, pseudocódigo del certificador y su complejidad).
2. Paso 2: Demostrar que es NP-Hard mediante una reducción polinomial (explicar la reducción, la complejidad de la transformación y la justificación de "Ida y vuelta").
3. Conclusión final de su clasificación.
--------------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Demostracion de pertenencia a NP

Explicacion del certificado: la evidencia que nos dan es un subconjunto S de a lo sumo K puntos de observacion

Pseudocodigo del certificado:

def certificado(pasillos, K, certificado_S):

    n = len(certificado_S)

    if n > K:
        return False

    for pasillo in pasillos:
        extremo1 = pasillo.origen
        extremo2 = pasillo.destino

        if extremo1 not in certificado_S and extremo2 not in certificado_S:
            return False
    
    return True

Complejidad:

- Verificar el tamaño toma O(1)
- Iterar sobre las aristas toma O(A)
- Si pensamos al certificado como un HashSet, verificarlo toma O(1)
Por lo tanto la comlejidad que nos queda es de O(A) y como es estrictamente polinomial queda demostrado que pertenece a NP

Demostracion de NP-Hard

- Reduccion: el problema Independent Set (IS) busca un conjunto de J vertices en un grafo G = (V, E) donde ningun par de vertices compartan una arista. Por lo tanto armamos una instancia con el mismo grafo y definimos el limite de enteros como K = |V| - J

- Complejidad: copiar las referencias y realizar la resta toma O(V + E), por lo tanto es estrictamente polinomial

- IDA: si definimos a un conjunto como S = V - IS, por definicion del IS es imposible que los dos extremos de una arista esten adentro del conjunto, por lo tanto al menos uno de sus extremos esta en S

- VUELTA: si definimos a un conjunto como I = V - S y suponemos por el absurdo que I no es un IS, significa que existen dos vertices conectados por una arista, lo que significa que ninguno de estos vertices va a pertenecer a S y por lo tanto una arista va a quedar sin nada.

Conclusion: como demostramos que el problema pertenece a NP mediante un certificado polinomial y que ademas pertenece a NP-Hard mediante una reduccion polinomial, podemos afirmar que nuestro problema es un NP-Completo


--------------------------------------------------------------------------------
EJERCICIO 4: BÚSQUEDA EXHAUSTIVA
--------------------------------------------------------------------------------
Enunciado:
La fundación YPF dispone de un fondo de inversión total de W millones de pesos para financiar proyectos de optimización. Se han postulado N proyectos. Cada proyecto 'i' requiere una asignación exacta e indivisible de P_i millones de pesos y garantiza un impacto energético cuantificado en V_i unidades. Se desea seleccionar un subconjunto de proyectos a financiar de modo tal que se maximice el impacto energético total, respetando el límite estricto del presupuesto W.

Se pide resolver usando Branch and Bound detallando:
1. Explicación de la técnica aplicada a este problema (definir cotas y condición de poda).
2. Diagrama/explicación de los estados y la ramificación del árbol.
3. Pseudocódigo de la solución.
4. Complejidad temporal y espacial.
--------------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion

- Solucion Parcial: es la solucion actualmente acumulada

- Cota Inferior: es la mejor solucion global hasta el momento, se actualiza cada vez que la solucion parcial rompe record.

- Cota Superior: es la estimacion del impacto maximo de la rama y como buscamos maximizar, sumamos el impacto parcial al impacto maximo de todos los proyectos restantes

- Poda: si la cota superior de un nodo es menor o igual que la cota inferior entonces podamos esa rama ya que esta nunca va a poder superar el record

Diagrama de estados

- Definicion: se considera un estado de modo (k, impacto_acumulado, presupuesto_gastado)

- Estado Inicial: (0, 0, Ø) ningun proyecto fue evaluado

- Decision en el nivel 'k': al evaluar el proyecto 'k', tenemos hasta dos opciones de ramificacion
1) Incluir a k siempre y cuando el costo del proyecto no supere a presupuesto restante
2) No incluir a k (esta opcion siempre es valida)

Pseudocodigo

MEJOR_GLOBAL = 0

def branch_and_bound(k, proyectos, W, presupuesto_gastado, impacto_parcial):

    global MEJOR_GLOBAL
    n = len(proyectos)

    if n == k:
        if impacto_parcial > MEJOR_GLOBAL:
            MEJOR_GLOBAL = impacto_parcial
        return
    
    cota_superior = impacto_parcial + estimar_impacto_max(k, proyectos, W - presupuesto_gastado)

    if cota_superior <= MEJOR_GLOBAL:
        return
    
    proyecto_actual = proyectos[k]

    # Rama Izquierda
    if presupuesto_gastado + proyecto_actual.costo <= W:
        nuevo_presupuesto = presupuesto_gastado + proyecto_actual.costo
        nuevo_impacto = impacto_parcial + proyecto_actual.impacto
        
        branch_and_bound(k + 1, proyectos, W, nuevo_presupuesto, nuevo_impacto)

    # Rama Derecha
    branch_and_bound(k + 1, proyectos, W, presupuesto_gastado, impacto_parcial)

Complejidad

- Temporal: en el peor de los casos para cada P proyecto exploramos dos opciones (incluir o no incluir), lo que toma O(2^P). Ademas por cada nodo tenemos que calcular la cota superior, lo que toma O(P). Por lo tanto la complejidad nos queda O(P * 2^P)

- Espacial: O(P) ya que es el call stack de la recursion

"""
