"""
--------------------------------------------------------------------------------
EJERCICIO 1: GREEDY
--------------------------------------------------------------------------------
Enunciado:
Un centro de supercómputo recibe N peticiones para ejecutar simulaciones climáticas. Cada simulación 'i' tiene un horario de inicio estricto S_i y un horario de fin F_i inamovibles. Cada servidor del centro puede procesar como máximo una simulación al mismo tiempo. Encender servidores físicos extra consume muchísima energía y presupuesto, por lo que el objetivo es procesar TODAS las simulaciones utilizando la menor cantidad posible de servidores. Proponga un algoritmo goloso (Greedy) que determine la asignación óptima minimizando la cantidad de servidores activos.

Se pide:
1. Explicación de la estrategia y justificación de por qué es Greedy.
2. Pseudocódigo de la solución.
3. Complejidad temporal y espacial.
4. Demostración de optimalidad.
--------------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion: la estrategia consiste en ordenar la peticiones de menor a mayor por orden de inicio, para que si una simulacion ya se inicio, se tenga que abrir un nuevo servidor para la nueva simulacion. Es greedy porque en cada iteracion el programa evalua si la simulacion esta activa para ver si tiene que abrir un nuevo servidor o no.

Pseudocodigo:

def minimizar_servidores_activos(peticiones):

    peticiones.sort(key = lambda x: x.inicio)
    n = len(peticiones)

    horario_servidor_libre = []
    for i in range(n):
        peticion_actual = peticiones[i]
        peticion_asignada = False
        cantidad_servidores = len(horario_servidor_libre)

        indice_servidor = 0
        while indice_servidor < cantidad_servidores and not peticion_asignada:
            if horario_servidor_libre[indice_servidor] <= peticion_actual.inicio:
                horario_servidor_libre[indice_servidor] = peticion_actual.fin
                peticion_asignada = True
            
            indice_servidor += 1

        if not peticion_asignada:
            horario_servidor_libre.append(peticion_actual.fin)

    return len(horario_servidor_libre)

Complejidad:

- Temporal: ordenar la lista es O(N * log(N)) mientras que recorrerla y compararla es O(N). Por lo tanto O(N log(N)) + O(N) = O(N log(N))

- Espacial: O(N) ya que tenemos que agregar N peticiones a la lista nueva que creamos.

Demostracion de optimalidad: si una solucion decide no abrir un nuevo servidor para una peticion que se esta ejecutando, entonces estaria desaprovechando un servidor. Por lo tanto habria que cambiar la eleccion a la de Greedy para poder minimizar la cantidad de servidores activos.


--------------------------------------------------------------------------------
EJERCICIO 2: REDES DE FLUJO
--------------------------------------------------------------------------------
Enunciado:
En un archipiélago hay N islas en peligro por la erupción de un volcán y M islas seguras que funcionan como refugios. Cada isla en peligro 'i' tiene P_i personas que deben ser evacuadas. Cada refugio 'j' tiene suministros para alojar hasta un máximo de C_j personas. Las islas están conectadas por rutas marítimas, cada una con una capacidad máxima de transporte de K personas por día. Además, debido a restricciones de infraestructura portuaria, ninguna isla (ya sea de origen, refugio o una isla intermedia de paso) puede procesar (sumando los que llegan y los que se van) a más de V_x personas por día.  Modelar como un problema de redes de flujo para determinar si es posible evacuar a TODAS las personas en peligro en un solo día.

Se pide:
1. Explicación de la estrategia de modelado elegida.
2. Definición de la Red (explicar cómo se construye el grafo a resolver detallando Nodos, Aristas y Capacidades).
3. Pseudocódigo detallado.
4. Complejidad temporal.
--------------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion: estamos ante un problema de asignancion el cual lo vamos a resolver mediante el algoritmo de flujo maximo, la idea es crear una nueva red de flujo en donde cada unidad de flujo represente a una persona evacuada, garantizando que se cumpla lo pedido.

Definicion de la Red:

Nodos: agregamos una fuente S, un sumidero T y 2 nodos para cada isla (uno interno y otro externo) para controlar el flujo de personas que pasan por cada isla.

Aristas:
1) S -> Isla_interno: capacidad P_i
2) Isla_interno -> Isla_externo: capacidad V_x
3) Rutas Maritimas: origen_externo -> destino_interno: capacidad K
4) Refugio_externo -> T: capacidad C_j

Pseudocodigo:

def es_posible_evacuar(islas, refugios, rutas):

    red = GrafoDirigido()
    personas_totales = 0

    for isla in islas:
        red.agregar_arista(isla.id + "_interno", isla.id + "_externo", capacidad = isla.V_x)

        if isla.en_peligro:
            red.agregar_arista("S", isla.id + "_interno", capacidad = isla.P_i)
            personas_totales += isla.P_i
    
    for refugio in refugios:
        red.agregar_arista(refugio.id + "_interno", refugio.id + "_externo", capacidad = refugio.V_x)
        red.agregar_arista(refugio.id + "_externo", "T", capacidad = refugio.C_j)

    for ruta in rutas:
        red.agregar_arista(ruta.origen + "_externo", ruta.destino + "_interno", capacidad = ruta.K)

    flujo_maximo, grafo_residual = ford_fulkerson(red, "S", "T")

    return flujo_maximo == personas_totales

Complejidad:
- Armar la red toma O(N + M + R)
- V' tiene 2(N + M) nodos, por lo tanto O(N + M)
- E' tiene N + M + R aristas, por lo tanto O(N + M + R)
Al usar Edmonds-Karp la complejidad teorica es O(V' * E'^2), por lo tanto si lo traemos a nuestra red nos queda O((N + M) * (N + M + R)²)


--------------------------------------------------------------------------------
EJERCICIO 3: CLASES DE COMPLEJIDAD
--------------------------------------------------------------------------------
Enunciado:
Se define el problema de decisión COMITÉS DE PAZ (CP): Dado un conjunto de N embajadores y una lista de pares de embajadores que tienen "conflictos diplomáticos" entre sí, además de un entero K. ¿Es posible retirar a lo sumo K embajadores de la reunión de manera tal que todo conflicto tenga al menos a uno de sus involucrados retirado (para que haya paz en la sala)?
Sabiendo que INDEPENDENT SET es NP-Completo, demuestre formalmente que el problema CP pertenece a la clase NP-Completo.

Se pide:
1. Paso 1: Demostrar que el problema pertenece a NP (certificado, pseudocódigo y complejidad).
2. Paso 2: Demostrar que es NP-Hard mediante una reducción polinomial (explicar reducción, complejidad, Ida y Vuelta).
3. Conclusión final.
--------------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Demostracion de pertenencia a NP:

Explicacion del certificado: la evidencia que nos dan es un subconjunto S de a lo sumo K embajadores.

Pseudocodigo del certificado:

def certificado(conflictos, K, certificado_S):

    n = len(certificado_S)

    if n > K:
        return False

    for conflicto in conflictos:
        embajador1 = conflicto.origen
        embajador2 = conflicto.destino

        if embajador1 not in certificado_S and embajador2 not in certificado_S:
            return False
        
    return True

Complejidad:
- Verificar el tamaño toma O(1)
- Iterar sobre las aristas toma O(A)
- Si pensamos al certificado como un HashSet, verificarlo toma O(1)
Por lo tanto la complejidad total es O(A) y como es polinomial, el problema pertenece a NP.


Demostracion de NP-Hard:

- Reduccion: el problema Independent Set (IS) busca un subconjunto J en un grafo G = (V, E) donde ningun par de vertices compartan una arista. Por lo tanto armamos una instancia con el mismo grafo y definimos el limite de enteros como K = |V| - J

- Complejidad: copiar las referencias y realizar las restas toma O(V + E), por lo tanto es polinomial.

- IDA: si definimos a un conjunto como S = V - IS, por definicion de IS es imposible que dos extremos de una arista esten adentro del conjunto. Por lo tanto al menos uno de sus extremos esta en S.

- VUELTA: si definimos a un conjunto como I = V - S y suponemos por el absurdo que I no es un IS, significa que existen dos vertices conectados por una arista, lo que significa que ninguno de estos vertices va a pertenecer a S y por lo tanto una arista va a quedar sin nada.

- Conclusion: como demostramos que el problema pertenece a NP mediante un certificado polinomial y que ademas pertenece a NP-Hard mediante una reduccion polinomial, podemos afirmar que nuestro problema es un NP-Completo.


--------------------------------------------------------------------------------
EJERCICIO 4: BÚSQUEDA EXHAUSTIVA (Branch & Bound)
--------------------------------------------------------------------------------
Enunciado:
Una empresa de logística de envíos tiene N paquetes para repartir y K camiones idénticos. Cada paquete 'i' tiene un peso W_i. Se debe asignar cada paquete a exactamente un camión de manera tal que se minimice el peso del camión más cargado (para balancear el desgaste de los vehículos y evitar multas en la ruta). Todos los paquetes deben ser asignados. Resolver utilizando Branch & Bound.

Se pide resolver detallando:
1. Explicación de la técnica aplicada (definir cotas optimista pesimista y condición de poda).
2. Diagrama/explicación de los estados y la ramificación del árbol.
3. Pseudocódigo de la solución.
4. Complejidad temporal y espacial.
--------------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion:

- Solucion Parcial: es el camion mas pesado actualmente

- Cota Inferior: es la estimacion del peso minimo de la rama y como buscamos minimizar, buscamos el maximo entre el peso maximo y el promedio de distribucion.

- Cota Superior: es la mejor solucion global encontrada hasta el momento. Se actualiza cada vez que se encuentra una solucion mas liviana que nuestro record

- Poda: si la cota superior de un nodo es menor o igual a la cota inferior, podamos esa rama ya que nunca va a ser mas liviana que nuestro record.

Diagrama de estados:

- Definicion: se considera el estado (k, pesos_camiones)

- Estado Inicial: (0, [0, ..., 0]) ningun paquete fue procesado

- Decision en el nivel k: al evaluar el paquete 'k', tenemos hasta C opciones de ramificacion

Pseudocodigo:

def branch_and_bound(k, pesos_camiones, paquetes, C, promedio_ideal, mejor_maximo):

    n = len(paquetes)
    if k == n:
        solucion_actual = max(pesos_camiones)
        if solucion_actual < mejor_maximo[0]:
            mejor_maximo[0] = solucion_actual
        return
        
    cota_inferior = max(max(pesos_camiones), promedio_ideal)
    if cota_inferior >= mejor_maximo[0]:
        return
        
    for i in range(C):
        if pesos_camiones[i] + paquetes[k] < mejor_maximo[0]:
            pesos_camiones[i] += paquetes[k]

            branch_and_bound(k + 1, pesos_camiones, paquetes, C, promedio_ideal, mejor_maximo)  
            
            pesos_camiones[i] -= paquetes[k]

Complejidad:

- Temporal: en el peor de los casos para cada N paquete exploramos C opciones, por lo tanto O(C^N)

- Espacial: O(N + C) ya que O(N) es el call stack de la recursion y O(C) es el espacio para almacenar los pesos de los camiones

"""
