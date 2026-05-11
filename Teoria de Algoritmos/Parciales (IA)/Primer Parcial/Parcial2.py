'''
-----------------------------------------------------------------------------
EJERCICIO 1: GREEDY (Optimizando la jornada)
-----------------------------------------------------------------------------
Enunciado: 
Para aprovechar al máximo el día, un conductor de una aplicación de viajes tiene una lista de 'N' solicitudes de viaje posibles para realizar con su Renault Clio. Cada viaje 'i' tiene un horario de inicio exacto (Inicio[i]) y un horario de finalización exacto (Fin[i]). El conductor solo puede realizar un viaje a la vez (los horarios de los viajes elegidos no pueden superponerse).
Diseñar un algoritmo Greedy que seleccione la MÁXIMA CANTIDAD de viajes que el conductor puede realizar en el día.

Se pide:
1. Explicación y por qué la elección es Greedy.
2. Pseudocódigo.
3. Complejidad temporal y espacial.
4. Demostración de optimalidad.
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion: la estrategia consiste en ordenar las solicitudes de menor a mayor segun su horario de finalizacion, agarrar la solicitud que finaliza primero y sumarla a nuestro  contador, iteramos y nos fijamos si el horario de inicio de la nueva solicitud es mayor o igual que la finalizacion de nuestro viaje, si se cumple esta condicion aceptamos la solicitud y la sumamos al contador. Es Greedy porque en cada iteracion agarramos la solicitud que termina primero para lograr liberar el auto lo mas rapido posible y poder meter mas viajes.


Pseudocodigo:

def viajes_maximos(solicitudes):

    solicitudes.sort(key = lambda x: x.fin) # ordena los finales de las solicitudes de menor a mayor
    n = len(solicitudes)

    if n == 0:
        return 0
    
    cantidad_viajes = 1

    fin_viaje = solicitudes[0].fin 

    for i in range(1, n):
        if solicitudes[i].inicio >= fin_viaje:
            cantidad_viajes += 1

            fin_viaje = solicitudes[i].fin
    
    return cantidad_viajes

Complejidad:

- Temporal: ordenar la lista es O(n log(n)) mientras que recorrerla y comparar es O(n), por lo tanto, O(n log(n)) + O(n) = O(n log(n))

- Espacial: O(1) ya que usamos un contador

Demostracion de optimalidad: si una solucion elige un horario de finalizacion superior al de Greedy, se estaria quedando sin tiempo libre para meter otro viaje. Por lo tanto habria que cambiar la eleccion del viaje a la de Greedy para asi aprovechar al maximo la seleccion de viajes


-----------------------------------------------------------------------------
EJERCICIO 2: DIVISIÓN Y CONQUISTA (El algoritmo viral)
-----------------------------------------------------------------------------
Enunciado:
Una cuenta de Instagram que sube tutoriales de Excel analizó las visualizaciones de un Reel a lo largo de 'N' horas. Descubrieron un patrón particular: las visualizaciones subieron estrictamente hora tras hora hasta alcanzar un pico  máximo, y a partir de esa hora, empezaron a bajar estrictamente. (Es decir, el arreglo de visualizaciones es "bitónico": estrictamente creciente hasta un punto, y luego estrictamente decreciente).
Diseñar un algoritmo de División y Conquista con complejidad  (log N) que encuentre en qué hora (índice) ocurrió el PICO MÁXIMO de visualizaciones.

Se pide:
1. Explicación (Divide, Conquista, Combina).
2. Pseudocódigo.
3. Ecuación de recurrencia.
4. Complejidad con Teorema Maestro.
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion:

- Divide: se parte al array a la mitad

- Conquista:
Si las vistas de mitad son menores a mitad + 1 => el pico maximo esta a la derecha, por lo tanto descartamos la mitad izquierda.
Si las vistas de mitad son mayores a la mitad + 1 => el pico maximo esta en la mitad izquierda, por lo tanto descartamos la mitad derecha.

- Combina: el resultado esta en el caso base

Pseudocodigo:

def maximas_visualizaciones(visualizaciones, inicio, fin):

    if inicio == fin:
        return inicio

    mitad = (inicio + fin) // 2

    if visualizaciones[mitad] > visualizaciones[mitad + 1]:
        return maximas_visualizaciones(visualizaciones, inicio, mitad)
    else:
        return maximas_visualizaciones(visualizaciones, mitad + 1, fin)

Ecuacion de recurrencia:

T(n) = a*T(n/b) + f(n)

a = 1 es la llamada recursiva 
b = 2 porque dividimos el arreglo en 2
f(n) = O(1) porque calcula los indices centrales y los compara

Complejidad: 

- Temporal: T(n) = a*T(n/b) + f(n) = 1 * T(n/2) + O(1) = 1 * T(n/2) + O(n^0)
a vs b^k = 1 vs 2^0 = 1 vs 1 => 1 = 1 por lo tanto O(n^k * log(n)) = O(n^0 *log(n)) = O(1 * log(n)) = O(log(n)) 

- Espacial: O(log n) por el espacio que ocupa el call stack de recursion


-----------------------------------------------------------------------------
EJERCICIO 3: PROGRAMACIÓN DINÁMICA (Entrenamiento Express)
-----------------------------------------------------------------------------
Enunciado:
Para armar una rutina de gimnasio enfocada en hipertrofia teniendo muy poco tiempo, se cuenta con una lista de 'N' ejercicios distintos. Cada ejercicio 'i' consume una cantidad de tiempo T[i] (en minutos) y otorga un beneficio de hipertrofia H[i]. El tiempo total disponible en el gimnasio es de 'M' minutos. A diferencia del problema de los perfumes, cada ejercicio de la lista SOLO SE PUEDE REALIZAR UNA VEZ (no hay repeticiones del mismo ejercicio).
Diseñar un algoritmo de Programación Dinámica que encuentre el beneficio de hipertrofia MÁXIMO que se puede obtener sin pasarse de los M minutos.

Se pide:
1. Explicación de la estructura de memoización (matriz).
2. Pseudocódigo.
3. Ecuación de recurrencia.
4. Complejidad temporal y espacial.
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion: voy a usar un arreglo unidimensional DP de tamaño T + 1, la celda DP[t] guardara el maximo beneficio posible teniendo un tiempo (t). Para calcular DP[t] iteramos sobre todos los ejercicios, y por cada uno recorremos los tiempos de mayor a menor tiempo. Si el tiempo alcanza, evaluamos si el beneficio de este ejercicio sumado al beneficio optimo (beneficio[i] + DP[t - tiempo[i]) supera al valor que ya teniamos almacenado en DP[t]. Al construirlo de mayor a menor, no existe la posibilidad de hacer un ejercicio que ya hice. 

Pseudocodigo:

def maximo_beneficio(ejercicios, beneficio, T):

    n = len(ejercicios)
    DP = [0] * (T + 1)

    for i in range(n):
        for t in range(T, ejercicios[i] - 1, -1):
            posible_beneficio = beneficio[i] + DP[t - ejercicios[i]]
            
            if posible_beneficio > DP[t]:
                DP[t] = posible_beneficio
    
    return DP[T]

Ecuacion de recurrencia:

- Caso base: DP[0] = 0

- Caso recursivo: DP[t] = max{DP[t], beneficios[i] + DP[t - ejercicios[i]]}
(para todo i tal que ejercicios[i] <= t)

Complejidad:

- Temporal: el ciclo exterior itera 'n' veces mientras que el interior itera 'T' veces => O(n*T)

- Espacial: necesitamos un espacio proporcional al tiempo => O(T)

'''
