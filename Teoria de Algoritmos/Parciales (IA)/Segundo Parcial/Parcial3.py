'''
-----------------------------------------------------------------------------
EJERCICIO 1: REDES DE FLUJO (Las Pasantías de la Facultad)
-----------------------------------------------------------------------------
Enunciado:
La facultad está organizando su programa de pasantías de verano. Hay un total de E estudiantes inscritos y P empresas participando. Cada estudiante i necesita ser asignado a exactamente una pasantía. Cada empresa j ofreció un máximo de V_j vacantes disponibles para recibir estudiantes. Los estudiantes llenaron un formulario indicando en qué empresas les interesaría trabajar (cada estudiante armó una lista con varias opciones).
Se te pide diseñar un algoritmo basado en Redes de Flujo para determinar si es posible asignar a TODOS los estudiantes a una empresa que les interese, respetando los cupos máximos de cada empresa.

Se pide:
1. Explicación de la estrategia de modelado elegida.
2. Definición de la Red (explicar cómo se construye el grafo a resolver detallando Nodos, Aristas y Capacidades).
3. Pseudocódigo detallado.
4. Complejidad temporal.

-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion: estamos ante un problema de asignacion, que se resuelve mediante el algoritmo de Flujo Maximo. El objetivo es modelar una red de forma que cada unidad de flujo represente una pasantia asignada a un alumno especifico, garantizando que se respete lo pedido y los cupos de la misma.

Red (Nodos, Aristas y Capacidades)

Dado un conjunto P de pasantias y E de estudiantes, armamos una nueva red de flujo G' de la siguiente manera:

- Nodos: agregamos una fuente S, un sumidero T, P nodos (uno por cada pasantia) y E nodos (uno por cada estudiante)

- Aristas desde S: conectamos S a cada alumno 'i' con capacidad 1. Esto garantiza que cada estudiante sea asignado exactamente a una pasantia.

- Aristas E - P: si el estudiante 'i' indico que le gusta la empresa 'j', agregamos una arista dirigida desde el estudiante 'i' hasta la pasantia 'j' con capacidad 1. Esto garantiza que el estudiante aplique a su opcion correctamente.

- Aristas hacia T: conectamos a cada pasantia 'j' con el sumidero T con una capacidad V_j. Esto garantiza que no se superen los cupos maximos de cada pasantia

Pseudocodigo:

def es_posible_asignar_estudiantes(estudiantes, pasantias, interes):

    # Armamos la red
    red = GrafoDirigido()
    S = "Fuente"
    T = "Sumidero"

    red.agregar_nodo(S)
    red.agregar_nodo(T)

    # Conectamos S con los estudiantes
    for estudiante in estudiantes:
        red.agregar_nodo(estudiante.id)
        red.agregar_arista(S, estudiante.id, capacidad = 1)
    
    # Conectamos las pasantias con T
    for pasantia in pasantias:
        red.agregar_nodo(pasantia.id)
        red.agregar_arista(pasantia.id, T, capacidad = pasantia.V)
    
    # Conectamos Estudiantes con pasantias, segun interes
    for estudiante in estudiantes:
        for pasantia in pasantias:
            if le_interesa(estudiante, pasantia, interes):
                red.agregar_arista(estudiante.id, pasantia.id, capacidad = 1)
    
    # Llamada a Ford-Fulkerson con BFS => Edmonds-Karp
    flujo_maximo, grafo_residual = ford_fulkerson(red, S, T)

    # Solucion
    return flujo_maximo == len(estudiantes)

Complejidad:

- Armar la red toma O(E * P)
- La red transformada tiene 2 + E + P nodos
- E' tiene E + P + (E * P) aristas, por lo tanto O(E * P)
- Al usar Edmonds-Karp la complejidad teorica es O(V' * E'²) por lo tanto, trayendolo a nuestra red, nos queda O((E + P) * (E * P)²)

-----------------------------------------------------------------------------
EJERCICIO 2: CLASES DE COMPLEJIDAD (El Comité de Expertos)
-----------------------------------------------------------------------------
Enunciado:
Una multinacional quiere formar un "Comité de Expertos" de élite compuesto por exactamente K empleados. La empresa tiene una plantilla de N empleados, y el área de Recursos Humanos mapeó las relaciones interpersonales creando un grafo no dirigido G = (V, E), donde los vértices son los empleados y existe una arista entre ellos si "trabajan bien juntos". Para que el comité sea exitoso, la junta directiva exige que TODOS los miembros seleccionados para el comité deben llevarse bien con TODOS los demás miembros seleccionados (es decir, cada par de empleados elegidos debe tener una arista que los una). Queremos saber si es posible formar dicho comité. (Llamemos a este problema: COMITÉ).

Se pide:
1. Demostrar que COMITÉ pertenece a NP (explicando certificado, pseudocódigo del certificador y complejidad).
2. Demostrar que es NP-Hard mediante una reducción polinomial desde Independent Set (IS). (Explicar reducción, complejidad de la transformación e "Ida y vuelta").
3. Conclusión final.

-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Demostracion de pertenencia a NP

- Explicacion: la evidencia que se nos da es que exsiste un subconjunto N que contiene exactamente K empleados.

- Pseudocodigo

def comite(grafo, K, certificado_S):

    n = len(certificado_S)

    if n != K:
        return False
    
    for i in range(n):
        for j in range(i + 1, n):
            empleado1 = certificado_S[i]
            empleado2 = certificado_S[j]
    
            if not se_llevan_bien(empleado1, empleado2, grafo):
                return False
    
    return True

- Complejidad:

- Verificar el tamaño es O(1)
- El doble loop toma O(K²)
- Si pensamos al grafo como un HashSet, verificar quien se lleva bien toma O(1)
Por lo tanto el tiempo maximo es O(K²) y ademas como K <= N significa que corre en tiempo polinomial con lo cual nuestro problema pertenece a NP

Demostracion de pertenencia a NP-Hard

- Reduccion: el problema Independent Set (IS) busca un subconjunto de K vertices en un grafo G = (V, E) donde ningun par de vertices comparta una arista. Pero nuestro problema nos pide lo contrario, por ende creamos un grafo G' = (V, E') en el cual agregamos una arista entre dos vertices si en el grafo original esta no existia

- Complejidad de la transformacion: copiar el grafo y ver si hay que agregar aristas toma O(V²) lo cual es estrictamente polinomial

- IDA: si existe un IS de tamaño K vertices en el grafo original, significa que esos K vertices no estan conectados mediante una arista y por nuestra tranformacion existiria un grafo G' en el cual si lo estarian.

- VUELTA: si existe un comite de tamaño K en nuestro grafo G' significa que por regla de nuestra transformacion tuvo que existir un grafo G en el cual sus K vertices no esten conectados

- Conclusion: como demostramos que nuestro problema pertenece a NP mediante un certificador polinomial y que tambien pertenece a NP-Hard mediante una reduccion polinomial, podemos afirmar que nuestro problema es un NP-Completo 

-----------------------------------------------------------------------------
EJERCICIO 3: BÚSQUEDA EXHAUSTIVA (Asignación de Proyectos a Consultores)
-----------------------------------------------------------------------------
Enunciado:
Sos el gerente de una consultora. Tenés un equipo de N consultores estrella y acaban de entrar N proyectos nuevos de diferentes clientes. Tenés una matriz de N x N, donde cada celda G_{i,j} representa la ganancia en dólares que obtendría la empresa si el consultor i se hace cargo del proyecto j. Querés maximizar las ganancias de la empresa asignando exactamente un proyecto a cada consultor y asegurándote de que cada proyecto sea realizado por un único consultor (es decir, tenés que elegir exactamente una celda por fila y una celda por columna, maximizando la suma). Decidís usar Branch and Bound.

Se pide resolver detallando:
1. Explicación de la técnica aplicada (Cotas y Condición de Poda).
2. Diagrama/explicación de los estados y la ramificación.
3. Pseudocódigo de la solución.
4. Complejidad temporal y espacial.

-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion:

- Solucion Parcial: es valor acumulado actualmente

- Cota Inferior: es la mejor solucion global valida hasta el momento. Se actualiza cada vez que la solucion parcial supera el record

- Cota Superior: es una cota admisible por exceso y como buscamos maximizar, sumamos la suma parcial a la suma de la ganancia maxima de los proyectos restantes

- Poda: si la Cota Superior de un nodo es menor o igual que la Cota Inferior entonces podamos esa rama ya que nunca va a superar a nuestro record

Diagrama de estados:

Metemos a la matriz en un array unidimensional desde 0 hasta n² - 1

- Estado inicial: k = 0, ninguna celda fue evaluada ni seleccionada
- Decision en el nivel k: al evaluar la celda 'k', tenemos hasta dos opciones de ramificacion:
1) Incluir a K siempre y cuando ninguna celda en su misma fila o columna haya sido previamente seleccionada en la matriz original.
2) No incluir a K (esta opcion siempre es valida)
- Caso base: K = N² lo que significa que se tomo una decision para todas las N² celdas de la matriz

Pseudocodigo:

MEJOR_GLOBAL = 0

def branch_and_bound(k, celdas, seleccionadas, ganancia_parcial):

    global MEJOR_GLOBAL
    n = len(celdas)

    # Caso Base
    if k == n:
        if ganancia_parcial > MEJOR_GLOBAL:
            MEJOR_GLOBAL = ganancia_parcial
        return
    
    # Calculamos la Cota Superior
    ganancia_actual = 0
    for i in range(k, n):
        ganancia_actual += celdas[i].ganancia
    
    cota_superior = ganancia_parcial + ganancia_actual
    
    # Condicion de Poda
    if cota_superior <= MEJOR_GLOBAL:
        return
    
    celda_actual = celdas[k]

    # Rama Izquierda
    if no_hay_seleccionados(celda_actual, seleccionadas):
        seleccionadas.add(celda_actual.id)

        nueva_ganancia = ganancia_parcial + celda_actual.ganancia

        branch_and_bound(k + 1, celdas, seleccionadas, nueva_ganancia)

        seleccionadas.remove(celda_actual.id)
    
    # Rama Derecha
    branch_and_bound(k + 1, celdas, seleccionadas, ganancia_parcial)

Complejidad:

- Temporal: en el peor de los casos, para las N² celdas, exploramos 2 decisiones (incluir o no incluir) por lo tanto O(2^N²). Ademas por cada nodo tenemos que calcular la cota superior por ende toma O(N²). Entonces, finalmente tenemos O(N² * 2^N²)

- Espacial: O(N²) ya que es la profundidad maxima del call stack de la recursion

'''
