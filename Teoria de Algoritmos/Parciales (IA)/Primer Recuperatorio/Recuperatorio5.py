""" 
SIMULACRO DE RECUPERATORIO INTEGRADOR

Tema 1: Greedy (Algoritmos Voraces)
"El Rescate Satelital"
Una agencia espacial tiene N satelites averiados en orbita. Por cada satelite i, se conoce el tiempo T_i en dias que demora un transbordador en repararlo, y una tasa de perdida P_i (en miles de dolares) por cada dia que el satelite pasa sin estar reparado. Solo hay un transbordador disponible. Proponga un algoritmo Greedy que determine el orden optimo de reparacion para minimizar el dinero total perdido. 
(Debe incluir: Demostracion de Optimalidad por argumento de intercambio).

Explicacion: la estrategia consiste en ordenar a los satelites de mayor a menor segun su ratio (costo/tiempo).
Es greedy porque en cada iteracion realiza una eleccion:
- Localmente optima porque elige siempre al de mayor penalizacion
- Factible: cumple con las restricciones del problema
- Irrevocable ya que una vez tomada la decision, esta no puede ser removida

Pseudocodigo:

def minimizar_perdida(satelites):

    satelites.sort(key = lambda x: x.costo / x.tiempo, reverse = True)
    orden_reparacion = []

    for satelite in satelites:
        orden_reparacion.append(satelite)

    return orden_reparacion

Analisis complejidad
- Temporal: ordenar los satelites toma O(N*log(N)) mientras que recorrerlos toma O(N), por lo tanto, la comlejidad es O(N*log(N)

- Espacial: O(N) para almacenar la lista de reparacion

Analisis de optimalidad: se demustrea mediante el argumento de la sustitucion ya que si en otra solucion ordenan diferente a la de greedy significa que en algun momento van a reparar un satelite que genera menos costo total que otro y por ende si intercambiamos esos satelites, podemos minimizar el costo y llegar a la solucion mas optima posible (es lo que hace greedy)

EJEMPLO
satelites = [(A, costo = 100, tiempo = 2), (B, costo = 50, tiempo = 5), (C, costo = 150, tiempo = 1)]
Ratios: A = 50, B = 10, C = 150
satelites ordenado = [(C, 150), (A, 50), (B, 10)]
Al reparar C => C no genera perdida ya que se repara en el momento
A genera 100 de perdida ya que para empezar a repararse tiene que esperar a que C se repare
B genera 150 porque espera el dia de C y los dos dias de A para poder reparase
Perdida total = 250
Si reparamos B primero => B no genera perdida
A espera los 5 dias de B y genera 500 de perdida
C espera los 5 dias de B y los 2 dias de A para repararse, lo que genera 1050 de perdida
Perdida total = 1550

Tema 2: Division y Conquista
"El Infiltrado Solitario"
En una base de datos militar de N registros (con N impar), todos los codigos de acceso de los soldados estan registrados exactamente dos veces y ubicados uno al lado del otro de forma contigua (ej: [A, A, B, B, C, C, ...]). Sin embargo, se descubrio que hay un "codigo solitario" infiltrado que aparece una sola vez, rompiendo la paridad. Diseñe un algoritmo O(log N) que encuentre el codigo solitario.
(Debe incluir: Relacion de Recurrencia y justificacion del Teorema Maestro).

Explicacion
- Divide: dividimos al arreglo a la mitad
- Conquista: resolvemos los sub areglos recursivamente
- Combina: la solucion esta en el caso base

Pseudocodigo

def encontrar_inflitrado(registros, inicio, final):

    if inicio == final:
        return registros[inicio]

    mitad = (inicio + final) // 2
    if mitad % 2 != 0:
        mitad -= 1

    if registro[mitad] == registro[mitad + 1]:
        return encontrar_infiltrados(registros, mitad + 2, final)
    else:
        return encontrar_infiltrados(registros, inicio, mitad)

relacion de recurrencia
T(N) = a * T(N/b) + c * f(n)
a = 1 es la llamada recursiva
b = 2 porque dividimos a la mitad
f(n) = O(1) porque compara indices

Analisis de complejidad
- Temporal: T(N) = a * T(N/b) + c * f(n) = 1 * T(N/2) + c * O(1) = 1 * T(N/2) + c * O(N^0)
a vs b^k = 1 vs 2^0 = 1 vs 1 => 1 == 1 por lo tanto O(N^k * log(N)) = O(N^0 * log(N)) = O(1 * log(N)) = O(log(N))

- Espacial: O(log(N)) ya que es el call stack de la recursion

Ejemplo
registro = [A, A, B, C, C] inicio = 0, final = 4
1) inicio == final? 0 == 4? NO
mitad = (inicio + final) // 2 = (0 + 4) // 2 = 4 // 2 = 2 y 2 es par y vale B
[mitad] == [mitad + 1]? => [2] == [3] -> B == C falso por ende descartamos la mitad derecha

2) inicio = 0, final = mitad = 2
inicio == final? => 0 == 2? NO
mitad = (inicio + final) // 2 = (0 + 2) // 2 = 2 // 2 = 1 y 1 es impar por ende mitad = 0 y vale A
[mitad] == [mitad + 1]? => [0] == [1] -> A == A verdadero por ende descartamos la mitad izquierda

3) inicio = mitad + 2 = 0 + 2 = 2, final = 2
inicio == final? 2 == 2? SI
Caso base, por lo tanto devuelvo [inicio] = [2] = B

Tema 3: Busqueda Exhaustiva (Backtracking)
"Mision de Evacuacion"
Un grupo de N diplomaticos debe ser evacuado en 2 helicopteros. Cada helicoptero tiene una capacidad maxima de peso W. Se tiene un arreglo con el peso P_i de cada diplomatico. Ademas, existe una matriz de incompatibilidad donde M[i][j] = 1 si el diplomatico i y el j son de facciones enemigas y no pueden viajar en el mismo helicoptero. Buscamos saber si es posible evacuar a todos cumpliendo las restricciones.
(Debe incluir: Estructura del arbol de estados y podas).

Explicacion: la estrategia consiste en aplicar una restriccion, y si se incumple, vovler para atras y probar otra alternativa

Estructura del arbol:
- Nodos: es el diplomatico actual
- Aristas: son los helicopteros disponibles para el diplomatico actual
- Hoja: viajaron todos los diplomaticos
- Poda: si el peso del diplomatico supera el peso maximo del helicopetro o si hay un diplomatico incompatible

Pseudocodigo:

def backtracking(indice_actual, diplomaticos, helicoptero1, helicoptero2, M, W):

    if indice_actual == len(diplomaticos):
        return True

    diplomatico_actual = diplomaticos[indice_actual]

    if helicoptero1.peso + diplomatio_actual.peso <= W and es_compatible(diplomatico_actual, helicoptero1, M):
        
        helicoptero1.append(diplomatico_actual)
        if backtracking(indice_actual + 1, diplomaticos, helicoptero1, helicoptero2, M, W):
            return True
        helicoptero1.pop()
    
    if helicoptero2.peso + diplomatico_actual.peso <= W and es_compatible(diplomatico_actual, helicoptero2, M):
        
        helicoptero2.append(diplomatico_actual)
        if backtracking(indice_actual + 1, diplomaticos, helicoptero1, helicoptero2, M, W):
            return True
        helicoptero2.pop()

    return False

Analisis de complejidad
- Temporal: en el peor de los casos, para cada diplomatico tendriamos que evaluar 2 opciones, meterlo el helicoptero 1 o 2. Por lo tanto, la complejidad es O(2^N)

- Espacial: O(N) ya que es el call stack de la recursión

Ejemplo
Diplomáticos = [(A, 50), (B, 60), (C, 50)], W = 100. Incompatibles: A y C.
1. A sube a H1. (Estado: H1=[A], H2=[])
2. B no entra en H1 por peso (110 > 100). Sube a H2. (Estado: H1=[A], H2=[B])
3. C no entra en H1 (es incompatible con A) ni en H2 por peso (110 > 100). Falla.
4. BACKTRACKING: Como C no tiene opciones, B deshace su decisión e intenta otra, pero tampoco tiene, A deshace su decisión y prueba subir a H2, reacomodando el árbol

Tema 4: Programacion Dinamica
"La Gira del Musico"
Sos el manager de un artista que hara una gira por una ruta recta que pasa por N ciudades. En cada ciudad i te ofrecen un contrato por G_i dolares. Por exigencia del sindicato, si el artista toca en la ciudad i, debe descansar obligatoriamente y no puede tocar ni en la ciudad i+1 ni en la i+2. Diseñe un algoritmo para determinar la ganancia maxima posible.
(Debe incluir: Definicion del estado y Ecuacion de recurrencia con casos base).

Explicacion: voy a usar un arreglo unidimensional OPT de tamano N, en donde OPT[i] guardara la ganancia maxima. Para calcular OPT[i] tenemos que iterar sobre las ciudades y fijarnos que es mejor: sumarla ganancia actual a la anterior (OPT[i - 3]) o no sumar la ciudad a la gira

Relacion de recurrencia
- Caso base:
    - OPT[0] = ciudades[0]
    - OPT[1] = max(ciudades[0], ciudades[1])
    - OPT[2] = max(ciudades[0], ciudades[1], ciudades[2])

- Caso recursivo: si i > 2 => OPT[i] = max(OPT[i - 1], ciudades[i] + OPT[i - 3])

Pseudocodigo

def maximizar_ganancia(ciudades):

    n = len(ciudades)
    if n == 0:
        return 0
    
    if n == 1:
        return ciudades[0]
    
    if n == 2:
        return max(ciudades[0], ciudades[1])
    
    if n == 3:
        return max(ciudades[0], ciudades[1], ciudades[2])

    OPT = [0] * n
    OPT[0] = ciudades[0]
    OPT[1] = max(ciudades[0], ciudades[1])
    OPT[2] = max(ciudades[0], ciudades[1], ciudades[2])

    for i in range(3, n):
        OPT[i] = max(OPT[i - 1], ciudades[i] + OPT[i - 3])
    
    return OPT[n - 1]

Analisis de complejidad
- Temporal: O(N) para recorrer las ciudades

- Espacial: O(N) para almacenar OPT

Ejemplo

ciudades = [10, 40, 30, 60, 50]
OPT[0] = ciudades[0] = 10
OPT[1] = max(ciudades[0], ciudades[1]) = max(10, 40) = 40
OPT[2] = max(ciudades[0], ciudades[1], ciudades[2]) = max(10, 40, 30) = 40
OPT[3] = max(OPT[i - 1], ciudades[i] + OPT[i - 3]) = max(OPT[3 - 1], ciudades[3] + OPT[3 - 3]) = max(OPT[2], 60 + OPT[0]) = max(40, 60 + 10) = max(40, 70) = 70
OPT[4] = max(OPT[i - 1], ciudades[i] + OPT[i - 3]) = max(OPT[4 - 1], ciudades[4] + OPT[4 - 3]) = max(OPT[3], 50 + OPT[1]) = max(70, 50 + 40) = max(70, 90) = 90

Retorna OPT[4] = 90

Tema 5: Redes de Flujo
"Asignacion de Entrevistas"
En una feria universitaria hay N empresas tecnologicas y M estudiantes. Cada estudiante tiene interes en un subconjunto especifico de empresas. Cada empresa dispone de tiempo para entrevistar a lo sumo a C_j estudiantes en total durante el dia. Para garantizar equidad, la facultad exige que ningun estudiante tenga mas de 3 entrevistas en total. Modele el problema para determinar la maxima cantidad total de entrevistas que se pueden concretar en la feria.
(Debe incluir: Explicacion y modelado claro del grafo, fuente, sumidero y capacidades).

Explicacion y modelado: estamos ante un problema de asignacion el cual lo vamos a resolver emdiante flujo maximo, para ello vamos a modelar el problema como un grafo dirigido, en donde:

- Nodos: una fuente S, un sumidero T, un nodo para cada empresa y un nodo para cada alumno
- Aristas:
S -> nodo empresa (capacidad Cj) porque cada empresa puede recibir a lo sumo Cj estudiantes
nodo_empresa -> nodo_estudiante (capacidad 1) porque cada eempresa le da la charla una vez al estudiante
nodo_estudiante -> T (capacidad 3) porque cada estudiante puede elegir 3 empresas

Pseudocodigo
def asignar_entrevistas(empresas, estudiantes, interes):

    grafo = GrafoDirigido()

    for empresa in empresas:
        grafo.agregar_arista("S", empresa.id, empresa.Cj)
    
    for estudiante in estudiantes:
        grafo.agregar_aristas(estudiante.id, "T", 3)

    for estudiante in estudiantes:
        for empresa in intereses[estudiante.id]:
            grafo.agregar_aristas(empresa.id, estudiante.id, 1)

    flujo_maximo, grafo_residual = ford_fulkerson(grafo, "S", "T")

    return flujo_maximo

Analisis de complejidad
- Armar la red toma O(N * M) en donde N son los estudiantes y M las empresas
- V' tiene 2 (fuente y sumidero) + N + M nodos, por lo tanto O(N + M)
- E' tiene N + M + N * M (intereses), por lo tanto O(N * M)
- Al usar Edmons Karp, la complejidad teorica es de O(V' * E'²), por lo tanto trayendolo a nuestro problema, nos queda O((N + M) * (N * M)²) = O((N + M) * (N² * M²)) = O((N + M) * N² * M²) = O((N³ + N² * M) * M²) = O(N³ * M² + N² * M³)

- Espacial: O(N * M) para almacenar el grafo

NO LLEGUE AL EJEMPLO NI AL EJ 6, SUPER F

Tema 6: Clases de Complejidad
"Vigilancia en el Castillo"
Dado un grafo G=(V,E) que representa un castillo, los vertices V son las torres y las aristas E son los muros que las conectan. Queremos saber si es posible colocar a lo sumo K guardias en las torres de tal forma que todos los muros esten vigilados (un muro esta vigilado si hay al menos un guardia en uno de sus dos extremos). Demuestre que este problema es NP-Completo. (Sugerencia: Utilizar Vertex Cover).
(Debe incluir: Certificador NP y Reduccion polinomial NPH).
"""