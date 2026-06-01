"""
--------------------------------------------------------------------------------
EJERCICIO 1: GREEDY (Minimización de Multas)
--------------------------------------------------------------------------------
Enunciado:
Una consultora de software debe entregar N proyectos a sus clientes. Cada proyecto i requiere un tiempo de desarrollo continuo t_i (no se pueden pausar ni hacer en paralelo). Por contrato, cada proyecto tiene una multa diaria p_i. Esto significa que si el proyecto i se termina en el día C_i, la consultora deberá pagar una multa total de p_i * C_i por ese proyecto. Se desea minimizar la suma total de las multas a pagar por todos los proyectos.

Se pide:
1. Explicación y por qué es Greedy.
2. Pseudocódigo.
3. Complejidad temporal y espacial.
4. Demostración de optimalidad.
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion: la estrategia consiste en ordenar de mayor a menor segun su costo por dia (pi/ti), esto hace que se haga primero el de alto costo y ultimo el de bajo costo. Es greedy porque en cada iteracion el programa elige el proyecto de mayor costo y lo hace para minimizar las multas a pagar.

Pseudocodigo:

def minimizar_multas(proyectos):

    proyectos.sort(key = lambda x: x.multa / x.tiempo, reverse = True)

    multa_total = 0
    dias = 0
    orden_final = []
    for proyecto in proyectos:
        dias += proyecto.tiempo
        multa_total += (dias * proyecto.multa)

        orden_final.append(proyecto.id)
    
    return orden_final, multa_total

Complejidad:

- Temporal: calcular el costo toma O(N), ordenarla toma O(N * log(N)) y recorrerla toma O(N). Por lo tanto la complejidad es O(N * log(N))

- Espacial: O(N) para almacenar el orden_final

Demostracion de optimalidad: si una solución decide poner un proyecto de multa barata antes que uno de multa cara, estaría pagando la multa cara por más días de los necesarios. Por lo tanto, si los damos vuelta haciendo primero el caro (que es lo que hace Greedy), estaríamos ahorrando plata en multas.


-----------------------------------------------------------------------------
EJERCICIO 2: REDES DE FLUJO (Asignación de Servidores)
-----------------------------------------------------------------------------
Enunciado:
Una empresa de streaming tiene N servidores y M bases de datos de películas. 
* Cada servidor i tiene una capacidad máxima para manejar hasta K_i conexiones concurrentes.
* Cada base de datos j requiere exactamente R_j servidores asignados para garantizar redundancia.
* Por arquitectura técnica, el servidor i solo es compatible con un subconjunto específico de bases de datos.
* Para evitar cuellos de botella geográficos, existe una restricción global: los servidores ubicados en el "Datacenter Sur" (que son un subconjunto de los N servidores) no pueden manejar, en total y entre todos ellos, más de X conexiones concurrentes. Determinar si es posible asignar los servidores cumpliendo todas las restricciones.

Se pide:
1. Explicación de la estrategia de modelado elegida.
2. Definición de la Red (explicar cómo se construye el grafo a resolver detallando Nodos, Aristas y Capacidades).
3. Pseudocódigo detallado (incluyendo armado de la red, llamada al algoritmo de flujo y obtención de la solución).
4. Complejidad temporal.
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:


Explicacion: estamos ante uun problema de asignacion que vamos a resolver utilizando el algoritmo de flujo maximo, la idea es construir una red en donde cada unidad de flujo represente a un servidor asignado a una base de datos especifica, garantizando que se cumpla lo pedido.

Red (Nodos, Aristas y Capacidades)

Dado un conjunto N de servidores y un cnjunto M de bases de datos, creamos una nueva red de flujo G' de la siguiente manera:

Nodo: Agregamos una fuente S, un sumidero T, N nodos (uno por cada servidor), M nodos (uno por cada base de datos) y un nodo extra para representar la reestriccion global.

Aristas desde S: 
- Servidores Normales: conectamos S a cada servidor 'i' con capacidad k_i para garantizar que el servidor no sea asignado a mas bases de datos de las permitidas

- Datacenter Sur: conectamos S al nodo extra con capacidad X y a este lo conectamos a cada servidor 'i' con capacidad K_i para garantizar que el servidor no sea asignado a mas bases de las permitidas

Arista N-M: si el servidor 'i' es compatible con la base de datos 'j', agregamos una arista dirigida desde el servidor 'i' hasta la base de datos 'j' con capacidad 1. Esto garantiza la redundancia

Aristas hacias T: conectamos a cada base de datos 'j' con el sumidero T con capacidad R_j para poder garantizar la redundancia.


Pseudocodigo:

def es_posible_asignar_servidores(servidores, bases_de_datos, restricciones, datacenter_sur, X):

    # Primero armamos la red
    red = GrafoDirigido()
    S = "Fuente"
    T = "Sumidero"
    nodo_extra = "Nodo Extra"

    red.agregar_nodo(S)
    red.agregar_nodo(T)
    red.agregar_nodo(nodo_extra)
    red.agregar_arista(S, nodo_extra, capacidad = X)

    asignaciones_totales = 0

    # Conectamos S con los servidores
    for servidor in servidores:
        red.agregar_nodo(servidor.id)
        
        if servidor in datacenter_sur:
            red.agregar_arista(nodo_extra, servidor.id, capacidad = servidor.K)
        else:
            red.agregar_arista(S, servidor.id, capacidad = servidor.K)
    
    # Conectamos las bases de datos con T y sumamos las asignaciones totales
    for base_de_datos in bases_de_datos:
        red.agregar_nodo(base_de_datos.id)
        red.agregar_arista(base_de_datos.id, T, capacidad = base_de_datos.R)
        asignaciones_totales += base_de_datos.R
    
    # Conectamos Servidores con Bases de Datos, segun las reestricciones
    for servidor in servidores:
        for base_de_datos in bases_de_datos:
            if puede_conectarse(servidor, base_de_datos, reestricciones):
                red.agregar_arista(servidor.id, base_de_datos.id, capacidad = 1)

    # Llamada a Ford-Fulkerson con BFS => Edmonds - Karp
    flujo_maximo, grafo_residual = ford_fulkerson(red, S, T)

    #Solucion
    return flujo_maximo == asignaciones_totales

Complejidad:
- Armar la red toma O(N * M)
- V' tiene 3 + N + M nodos, por lo tanto O(N + M)
- E' tiene M + D + (N * M) aristas, por lo tanto O(N * M)
- Al usar Edmonds-Karps la complejidad teorica es O(V' * E'²), por lo tanto traayendolo a nuestra red, nos queda O((N + M) * (N * M)²)


-----------------------------------------------------------------------------
EJERCICIO 3: CLASES DE COMPLEJIDAD (Reducciones NP)
-----------------------------------------------------------------------------
Enunciado:
Se define el problema de decisión CONJUNTO DOMINANTE: Dado un grafo no dirigido G=(V,E) y un entero K, ¿existe un subconjunto de vértices D de tamaño a lo sumo K, tal que todo vértice del grafo esté en D o sea adyacente a un vértice en D? Sabiendo que el problema VERTEX COVER (Cobertura de Vértices) es NP-Completo, demuestre formalmente que CONJUNTO DOMINANTE pertenece a la clase NP-Completo.

Se pide:
1. Paso 1: Demostrar que el problema pertenece a NP (explicando certificado, pseudocódigo del certificador y su complejidad).
2. Paso 2: Demostrar que es NP-Hard mediante una reducción polinomial  (explicar la reducción, la complejidad de la transformación y la justificación de "Ida y vuelta"). Asumir que Independent Set es NP-C.
3. Conclusión final de su clasificación.
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Demostracion de pertenencia a NP

- Explicacion del certificado: la evidencia que nos dan es que existe un subconjunto S de a lo sumo K enteros

- Pseudocodigo del certificador:

def certificador(D, K, certificado_S):

    n = len(certificado_S)

    if n > K:
        return False
    
    for d in D:
        adyacente1 = d.origen
        adyacente2 = d.destino

        if adyacente1 not in certificado_S and adyacente2 not in certificado_S:
            return False
    
    return True

Complejidad:
- Verificar el tamaño toma O(1)
- Iterar sobre las aristas toma O(A)
- Si pensamos a certificado_S como un HashSet, verificarlo toma O(1)
Por lo tanto la complejidad nos queda O(A) y es estrictamente polinomial, por ende queda demostrado que pertenece a NP

Demostracion de pertenencia a NP-Hard

- Reduccion: el problema Independent Set (IS) busca un subconjunto de J vertices en un graafo G = (V, E) donde ningun par de vertices comparta una arista. Por lo tanto armamos una instancia con el mismo grafo (G = G') y definimos el limite de enteros como K = |V| - J

- Complejidad: copiar las referencias del grafo y realizar la resta toma O(1), lo cual es estrictamente polinomial.

- IDA: si definimos a un conjunto como S = V - IS, por definicion de IS es imposible que los dos extremos de una arista esten adentro del conjunto, por lo taanto uno de sus extremos pertenece a S.

- VUELTA: si definimos a un conjunto como I = V - S y suponemos por el absurdo que I no es un IS, significa que existen dos vertices conectados por una arista, por ende ninguno de estos vertices va a pertenecer a S. Esto significa que una arista va a quedar sin nada.

- CONCLUSION: como demostramos que nuestro problema pertenece a NP mediante un certificador polinomial y ademas demostramos que pertenece a NP-Hard mediante una reduccion polinomial, podemos afirmar que nuestro problema es un NP-Completo.


-----------------------------------------------------------------------------
EJERCICIO 4: BÚSQUEDA EXHAUSTIVA (Branch & Bound)
-----------------------------------------------------------------------------
Enunciado:
Queremos instalar antenas de WiFi en un campus modelado como un grafo G=(V, E). Instalar una antena en el vértice v tiene un costo de instalación C_v. Si se instala una antena en v, se provee internet a v y a todos sus vértices adyacentes. Queremos cubrir TODOS los vértices del grafo incurriendo en el mínimo costo total posible.

Se pide resolver usando Branch and Bound detallando:
1. Explicación de la técnica aplicada a este problema (definir cotas y condición de poda).
2. Diagrama/explicación de los estados y la ramificación del árbol.
3. Pseudocódigo de la solución.
4. Complejidad temporal y espacial.
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:


Explicacion:

- Solucion Parcial: es el valor acumulado actualmente

- Cota Inferior: es la estimacion del costo minimo de la rama y como queremos minimizar, sumamos el costo parcial mas el costo minimo de las antenas restantes

- Cota Superior: es la mejor solucion global valida hasta el momento. Se actualiza cada vez que encontramos una solucion mas barata que nuestro record

- Poda: si la cota Superior de un nodo es menor o igual que la cota inferior, podamos esa rama ya que nunca va a ser mas barata que nuestro record


Diagrama de estados:

- Definicion: se considera un estado de modo (k, costo_acumulado, vertices_ocupados)

- Estado inicial: (0, 0, Ø) ninguna antena fue procesada

- Decision en el nivel 'k': al evaluar la antena 'k', tenemos hasta dos opciones de ramificacion:
1) Incluir a k (esta opcion siempre es valida)
2) No incluir a k (esta opcion siempre es valida)

Pseudocodigo:

MEJOR_GLOBAL = float('inf')

def branch_and_bound(k, antenas, V, vertices_cubiertos, costo_parcial):
    
    global MEJOR_GLOBAL
    n = len(vertices_cubiertos)
    
    if n == V:
        if costo_parcial < MEJOR_GLOBAL:
            MEJOR_GLOBAL = costo_parcial
        return
    
    l = len(antenas)
    if l == k:
        return
        
    cota_inferior = costo_parcial + estimar_costo_min(k, antenas)
    if cota_inferior >= MEJOR_GLOBAL:
        return
        
    antena_actual = antenas[k]
    
    # Rama Izquierda
    nuevos_vertices = vertices_cubiertos.union(antena_actual.cobertura)
    nuevo_costo = costo_parcial + antena_actual.costo
    
    branch_and_bound(k + 1, antenas, V, nuevos_vertices, nuevo_costo)
    
    # Rama Derecha
    branch_and_bound(k + 1, antenas, V, vertices_cubiertos, costo_parcial)

Complejidad:

- Temporal: en el peor de los casos para las A antenas exploramos dos opciones (incluir o no incluir), por lo tanto O(2^A). Ademas por cada nodo tenemos que calcular la Cota Inferior que toma O(A), por lo tanto tenemos una complejidad de O(A * 2^A)

- Espacial: O(A) ya que es el call stack de la recursion

"""
