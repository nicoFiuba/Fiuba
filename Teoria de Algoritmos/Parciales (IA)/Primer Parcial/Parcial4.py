'''
-----------------------------------------------------------------------------
EJERCICIO 1: GREEDY (El tanque del Clio)
-----------------------------------------------------------------------------
Enunciado:
Trabajando en la app de viajes con tu Renault Clio, te salió un viaje largo de CABA a un pueblo en la
ruta. El trayecto total es una línea recta de D kilómetros. El tanque de tu auto te permite recorrer un máximo de K kilómetros con el tanque lleno. A lo largo de la ruta, hay N estaciones de servicio YPF ubicadas en distintas distancias desde el punto de partida (E_1, E_2, ..., E_N). Arrancás el viaje con el tanque completamente lleno. 
Diseñar un algoritmo Greedy que determine la cantidad MÍNIMA de paradas a cargar gasoil necesarias para llegar a destino (si no es posible llegar porque la distancia entre dos estaciones supera K, debe retornar -1).

Se pide:
1. Explicación de la estrategia y por qué es Greedy.
2. Pseudocódigo.
3. Complejidad temporal y espacial.
4. Demostración de optimalidad.
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion: la estrategia consiste en ordenar las estaciones por kilometro de menor a mayor. Pararse en la primera estacion y avanzar hasta cuando te quedes sin gasoil, si llegaste a una estacion cargas y si no, significa que tenes que cargar en la estacion anterior. Iteramos esta eleccion hasta lograr llegar al destino. Es Greedy porque en cada iteracion busca la mejor eleccion de estacion para evitar quedarse sin gasoil y asi poder frenar la menor cantidad de veces.

Pseudocodigo:

def paradas_minimas(estaciones, K, D):

    estaciones.sort()
    n = len(estaciones)
    paradas = 0
    posicion_actual = 0
    
    i = 0
    while posicion_actual + K < D:
        maximo_alcance = posicion_actual

        while i < n and estaciones[i] <= posicion_actual + K:
            maximo_alcance = estaciones[i]
            i += 1
        
        if maximo_alcance == posicion_actual:
            return -1
        
        posicion_actual = maximo_alcance
        paradas += 1
    
    return paradas

Complejidad:

- Temporal: ordenar la lista es O(n log(n)) mientras que recorrerla es O(n). Por lo tanto O(n log(n)) + O(n) = O(n log(n))

- Espacial: O(1) porque devolvemos un contador.

Demostracion de optimalidad: si otra solucion frena antes que la propuesta en Greedy, significa que todavia podia seguir avanzando, por lo tanto si en vez de frenar ahi, frenamos en el maximo_alcance (es lo que hace Greedy) estariamos ahorrando paradas.


-----------------------------------------------------------------------------
EJERCICIO 2: DIVISIÓN Y CONQUISTA (Auditoría del Presentismo)
-----------------------------------------------------------------------------
Enunciado:
En el backend del sistema de presentismo que estás armando para el gimnasio, tenés un registro de asistencias diario ordenado cronológicamente por el ID del alumno. Por una regla del sistema, cada vez que un alumno pasa su tarjeta, su ID se registra exactamente DOS veces seguidas (ej: [..., 14, 14, 45, 45, 88, 88, ...]). Sin embargo, al auditar la base de datos de hoy descubrís que hubo una falla o un alumno registró mal su entrada, y hay un único ID que quedó registrado UNA SOLA VEZ. Por lo tanto, el arreglo final tiene una longitud impar (2N + 1).
Diseñar un algoritmo de División y Conquista con complejidad O(log N) que encuentre cuál es el ID del alumno que está registrado una sola vez.

Se pide:
1. Explicación (Divide, Conquista, Combina).
2. Pseudocódigo.
3. Ecuación de recurrencia.
4. Complejidad con Teorema Maestro.
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion:

- Division: dividimos el array a la mitad, buscamos siempre que la mitad sea par

- Conquista:
Si alumno[mitad] == alumno[mitad + 1] significa que el error esta del lado derecho, por lo tanto descartamos la mitad izquierda
Si alumno[mitad] != alumno[mitad + 1] significa que el error esta del lado izquierdo, por lo tanto descartamos la mitad derecha

- Combina: el resultado esta en el caso base

Pseudocodigo:

def detectar_falla(alumnos, inicio, fin):

    if inicio == fin:
        return alumnos[inicio]

    mitad = (inicio + fin) // 2

    if mitad % 2 != 0:
        mitad -= 1
    
    if alumnos[mitad + 1] == alumnos[mitad]:
        return detectar_falla(alumnos, mitad + 2, fin)
    else:
        return detectar_falla(alumnos, inicio, mitad)

Ecuacion de recurrencia:

T(n) = a * T(n/b) + f(n)

a = 1, es la llamada recursiva
b = 2, dividimos el array en 2
f(n) = O(1) porque calcula los indices y los compara

Complejidad:

- Temporal: T(n) = a * T(n/b) + f(n) = 1 * T(n/2) + O(1) = 1 * T(n/2) + O(n^0)
a vs b^k = 1 vs 2^0 = 1 vs 1 => 1 = 1 por lo tanto O(n^k * log(n)) = O(n^0 * log(n)) = O(1 * log(n)) = O(log(n))

- Espacial: O(log(n)) es el call stack de la recursion


-----------------------------------------------------------------------------
EJERCICIO 3: PROGRAMACIÓN DINÁMICA (El script del Superclásico)
-----------------------------------------------------------------------------
Enunciado:
Para tu cuenta de TikTok, tenés un video crudo continuo de M segundos de duración con el análisis del Superclásico. Querés cortarlo en varios fragmentos (Shorts/Reels) para subir a lo largo de la semana. Por las analíticas de la plataforma, tenés un arreglo V donde V[i] te indica la cantidad de visualizaciones esperadas que obtendría un fragmento de exactamente i segundos de duración (para 1 <= i <= M). Podés hacer todos los cortes que quieras, e incluso podrías no cortarlo y subir los M segundos de una, o subir M videitos de 1 segundo.
Diseñar un algoritmo de Programación Dinámica que determine la cantidad MÁXIMA de visualizaciones totales que podés obtener haciendo los cortes óptimos.

Se pide:
1. Explicación de la estructura de memoización.
2. Pseudocódigo.
3. Ecuación de recurrencia.
4. Complejidad temporal y espacial.
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion: voy a usar un arreglo unidimensional DP de tamano M + 1, la celda DP[m] almacena las visualizaciones esperadas teniendo una duracion (m). Para calcular DP[m] iteramos sobre todos los segundos, si la duracion del recorte dura menos o igual que m, nos fijamos si las visualizaciones del recorte sumadas a las visualizaciones del tiempo restante son superiores al recorte que ya teniamos almacenado en DP[m]. Al hacerlo de menor a mayor podemos subir varias veces el mismo fragmento.

Psudocodigo:

def visualizaciones_maximas(visualizaciones, M):

    n = len(visualizaciones)
    DP = [0] * (M + 1)

    for m in range(1, M + 1):
        for i in range(n):
            duracion_recorte = i + 1

            if duracion_recorte <= m:
                posible_recorte = DP[m - duracion_recorte] + visualizaciones[i]

                if posible_recorte > DP[m]:
                    DP[m] = posible_recorte
    
    return DP[M]

Ecuacion de recurrencia:

- Caso base: DP[0] = 0

- Caso recursivo: DP[m] = max{DP[m], DP[m - duracion_recorte] + visualizaciones[i]}
(para todo recorte tal que su duracion <= m)

Complejidad:

- Temporal: el ciclo exterior itera 'M' veces mientras que el ciclo interior itera 'n' veces, por lo tanto O(M * n)

- Espacial: necesitamos un espacio proporcional a M, por lo tanto O(M)

'''
