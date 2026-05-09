'''
-----------------------------------------------------------------------------
EJERCICIO 1: REDES DE FLUJO (Asignación de Guardias Médicas)
-----------------------------------------------------------------------------
Enunciado:
Sos el administrador de un hospital y tenés que organizar las guardias médicas para los próximos D días. Tenés un equipo de M médicos. Cada día i requiere exactamente R_i médicos de guardia para cubrir la demanda. Además, por cuestiones sindicales, cada médico j tiene un límite máximo de K_j guardias que puede hacer en total durante este período. Para complicar las cosas, los médicos te pasaron sus disponibilidades: no todos pueden trabajar todos los días. 

Se te pide diseñar un algoritmo basado en Redes de Flujo para determinar si es posible armar un cronograma válido que cubra la demanda de todos los días respetando los límites de cada médico.

Se pide:
1. Explicación de la estrategia de modelado elegida.
2. Definición de la Red (explicar cómo se construye el grafo a resolver detallando Nodos, Aristas y Capacidades).
3. Pseudocódigo detallado (incluyendo armado de la red, llamada al algoritmo de flujo y obtención de la solución).
4. Complejidad temporal.

-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicación: este es un problema de asignacion que se resuelve mediante el algoritmo de Flujo Maximo. El objetivo es modelar la red de forma que cada unidad de flujo represente una guardia asignada a un medico en un dia especifico, garantizando que se respeten tanto sus disponibilidades como sus limites maximos de turnos

Redes (nodos, aristas y capacidades):

Dado un conjunto M de medicos y D dias, armamos una nueva red de flujo G' de la siguiente manera:

- Nodos: agregamos una fuente S, un sumidero T, M nodos (uno por cada medico) y D nodos (uno por cada dia)

- Aristas desde S: conectamos S a cada medico 'j' con una capacidad K_j para garantizar que el medico no sea asignado a mas guardias de las que puede cubrir.

- Aristas M - D: si el medico 'j' esta disponible el dia 'i', agregamos una arista dirigida desde el medico 'j' hasta el dia 'i' con capacidad 1. Esto asegura que un medico no pueda cubrir mas de una guardia el mismo dia.

- Aristas hacia T: conectamos cada dia 'i' con el sumidero T con una capacidad R_i para representar la demanda de medicos requeridos para ese dia

Pseudocodigo:

def es_posible_armar_cronograma(medicos, dias, disponibilidades):

    # Armamos la red
    red = GrafoDirigido()
    S = "Fuente"
    T = "Sumidero"

    red.agregar_nodo(S)
    red.agregar_nodo(T)

    demanda_total = 0

    # Conectamos S con los medicos
    for medico in medicos:
        red.agregar_nodo(medico.id)
        red.agregar_arista(S, medico.id, capacidad = medico.K)
    
    # Conectamos los dias con T y sumamos la demanda total
    for dia in dias:
        red.agregar_nodo(dia.id)
        red.agregar_arista(dia.id, T, capacidad = dia.R)
        demanda_total += dia.R
    
    # Conectamos Medicos con Dias, segun disponibilidad
    for medico in medicos:
        for dia in dias:
            if esta_disponible(medico, dia, disponibilidades):
                red.agregar_arista(medico.id, dia.id, capacidad = 1)
    
    # Llamada a Ford-Fulkerson con BFS => Edmons - Karp
    flujo_maximo, grafo_residual = ford_fulkerson(red, S, T)

    # Solucion
    return flujo_maximo == demanda_total

Complejidad:

- Armar la red toma O(M * D)
- La red transformada tiene 2 + M + D nodos
- E' tiene M + D + (M * D) aristas, por lo tanto O(M * D)
- Al usar Edmonds-Karps la complejidad teorica es O(V' * E'²) por lo tanto trayendolo a nuestra red, nos queda O((M + D) * (M *D)²)


-----------------------------------------------------------------------------
EJERCICIO 2: CLASES DE COMPLEJIDAD (Vigilancia Urbana)
-----------------------------------------------------------------------------
Enunciado:
El gobierno de la Ciudad quiere instalar un nuevo sistema de cámaras de seguridad en las calles. La ciudad se puede modelar como un grafo no dirigido G = (V, E), donde las esquinas son los vértices (V) y las cuadras son las aristas (E). El gobierno quiere instalar a lo sumo K cámaras. Cada cámara se instala en una esquina (vértice) y es capaz de vigilar todas las calles (aristas) que se conectan a esa esquina. Quieren saber si es posible elegir K o menos esquinas de tal forma que TODAS las calles de la ciudad queden vigiladas. (Llamemos a este problema: CAMARAS).

Se pide:
1. Paso 1: Demostrar que el problema pertenece a NP (explicando certificado, pseudocódigo del certificador y su complejidad).
2. Paso 2: Demostrar que es NP-Hard mediante una reducción polinomial (explicar la reducción, la complejidad de la transformación y la justificación de "Ida y vuelta").
3. Conclusión final de su clasificación.

-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Demostracion de pertenencia a NP:

- Explicacion del certificado: la evidencia que nos dan es que existe un subconjunto S que contiene a lo sumo K camaras

- Pseudocodigo del certificador:

def certificador_camaras(calles, K, certificado_S):

    n = len(certificado_S)

    if n > K:
        return False
    
    for calle in calles:
        esquina1 = calle.origen
        esquina2 = calle.destino

        if esquina1 not in certificado_S and esquina2 not in certificado_S:
                return False
    
    return True

- Complejidad del certificador:
- Verificar el tamaño toma O(1).
- Iterar sobre las calles toma O(E)
- Si pensamos al certificado_S como un HashSet, verificar su existencia toma O(1).
Por lo tanto el tiempo maximo es O(E) lo que significa que corre en tiempo polinomial y por ende el programa pertenece a NP

Demostracion de pertenencia a NP-Hard:

- Reduccion: el problema Independent Set (IS) busca un subconjunto de J vertices en un grafo G = (V, E) donde ningun par de vertices comparta una arista.

- Transformacion:
Dada una instancia generica de IS compuesta por un grafo G =(V, E) y un entero J, construimos una instancia para el problema de las camaras de la siguiente manera:
- El grafo de la ciudad es el mismo, osea G' = G
- El limite maximo de camaras sera K = |V| - J

- Complejidad de la transfromacion: copiar las referencias del grafo y realizar la resta toma O(1) lo cual es estrictamente polinomial

Explicacion:

- IDA: si existe un IS de tamaño J en el grafo G, definimos a nuestro conjunto de camaras como S = V - IS y por lo tanto como IS es un conjunto independiente, es imposible que existan dos vertices dentro de IS conectados por una arista. Por lo tanto uno de sus extremos pertenece a S. Esto demuestra que S cubre todas las calles y su tamaño es K.

- VUELTA: si existe un conjunto S de a lo sumo K camaras que cubre todas las calles, definimos a nuestro conjunto como I = V -S. Suponiendo por el absurdo que I no es un conjunto independiente, significaria que existen dos vertices conectados por una arista con lo cual ninguno de estos vertices pertenece a S y por ende habria una calle sin cubrir.

Conclusion: como demostramos que nuestro problema pertenece a NP mediante un certificador polinomial y tambien demostramos que pertenece a NP-Hard mediante una reduccion polinomial, queda demostrado que el problema es un NP-Completo

-----------------------------------------------------------------------------
EJERCICIO 3: BÚSQUEDA EXHAUSTIVA (El escape del Banco)
-----------------------------------------------------------------------------
Enunciado:
Un grupo de ladrones acaba de abrir la bóveda de un banco. Tienen una sola mochila que soporta un peso máximo W. En la bóveda hay N lingotes de diferentes metales preciosos (no se pueden fraccionar). Cada lingote i tiene un peso p_i y un valor de reventa v_i. Quieren elegir un subconjunto de lingotes para llevarse tal que la suma de los valores sea la MÁXIMA posible, sin que la suma de los pesos supere la capacidad W de la mochila. Deciden usar un algoritmo de Branch and Bound (Ramificación y Poda) para encontrar la combinación perfecta antes de que llegue la policía.

Se pide:
1. Explicación de la técnica aplicada a este problema (definir cotas y condición de poda).
2. Diagrama/explicación de los estados y la ramificación del árbol.
3. Pseudocódigo de la solución.
4. Complejidad temporal y espacial.

-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion:

- Solucion parcial: es el valor y peso acumulado actualmente en la mochila.

- Cota Inferior: es la mejor solucion global valida encontrada hasta el momento. Se actualiza cada vez que la solucion parcial supera el record.

- Cota Superior: es una cota admisible por exceso que se calcula mediante la mochila fraccionaria, es decir que sumamos la solucion parcial actual a la ganancia maxima (valor / peso) que obendriamos al llenar la mochila con los lingotes sobrantes.

- Poda: Si la Cota Superior de un nodo es menor o igual a la Cota Inferior, entonces podamos esa rama ya que nunca va a superar nuestro record.

Diagrama de estados:

Se representa al nodo con la tupla (k, peso_actual, valor_actual) donde:
k: es el indice del lingote que estamos evaluando
peso_actual: es el peso acumulado hasta el momento
valor_actual: es la ganancia acumulada en la mochila hasta el momento

- Estado inicial: k = 0 y peso actual = 0, ningun lingote fue evaluado ni seleccionado
- Decisiones en el nivel k: al evaluar el lingote k, tenemos hasta dos opciones de ramificacion:
1) Incluir a k siempre y cuando el peso_actual + peso_k no supere la capacidad maxima de la mochila
2) No incluir a k (esta opcion siempre es valida)

Pseudocodigo

RECORD_GLOBAL = 0

def escape_banco(k, peso_actual, valor_actual, lingotes, peso_maximo):

    global RECORD_GLOBAL
    n = len(lingotes)

    # Caso Base
    if k == n:
        if valor_actual > RECORD_GLOBAL:
            RECORD_GLOBAL = valor_actual
        
        return
    
    # Condicion de Poda
    # la funcion toma los lingotes con mejor valor/peso y fracciona el ultimo para calcular la ganancia
    cota_superior = cota_superior_fraccionaria(k, peso_actual, valor_actual, lingotes, peso_maximo)

    if cota_superior <= RECORD_GLOBAL:
        return
    
    # Rama Izquierda
    if peso_actual + lingotes[k].peso <= peso_maximo:
        escape_banco(k + 1, peso_actual + lingotes[k].peso, valor_actual + lingotes[k].valor, lingotes, peso_maximo)

    # Rama Derecha
    escape_banco(k + 1, peso_actual, valor_actual, lingotes, peso_maximo)

Complejidad:

- Temporal: en el peor de los casos, para todos los lingotes exploramos 2 decisiones (incluir o no incluir), y ademas calcular la cota fraccionaria toma O(N), por lo tanto O(N * 2^N)

- Espacial: O(N) debido a la profundidad maxima del call stack de la recursion

'''