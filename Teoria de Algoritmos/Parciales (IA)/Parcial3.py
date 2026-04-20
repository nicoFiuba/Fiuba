'''
-----------------------------------------------------------------------------
EJERCICIO 1: GREEDY (Armando el neceser para el vuelo)
-----------------------------------------------------------------------------
Enunciado:
Estás preparando el equipaje de mano para viajar en avión a Bariloche. Por regulaciones del aeropuerto, solo podés llevar una bolsa transparente tipo ziploc que soporta un máximo de W mililitros de líquidos. Tenés una colección de N fragancias distintas. De cada fragancia 'i', tenés una botella con una cantidad disponible C[i] (en mililitros) y le asignaste un puntaje de "facha" o valor total V[i] según lo bien que huele. Como tenés frasquitos para hacer decants (transvasar), podés llevar fracciones de cualquier perfume. Si llevás la mitad de los mililitros de una fragancia, te suma la mitad de su valor de facha.
Diseñar un algoritmo Greedy que determine qué cantidad de cada fragancia llevar para maximizar el valor total de facha en tu bolsa ziploc sin pasarte del límite W.

Se pide:
1. Explicación y justificación de por qué la estrategia es Greedy.
2. Pseudocódigo.
3. Complejidad temporal y espacial.
4. Demostración de optimalidad.
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion: la estrategia consiste evaluar la facha por mililitro de cada perfume y en base a eso ordenamos de mayor a menor, evaluamos si puedo meter el perfume entero o tengo que poner un poco. Es Greedy porque en cada iteracion el programa busca elegir el perfume que mas facha aporta por mililitro para poder maximizar el beneficio.


Pseudocodigo:

def maximizar_facha(fragancias, capacidad):

    n = len(fragancias)
    fragancias_clasificadas = []

    for i in range(n):
        proporcion = fragancias[i].facha / fragancias[i].mililitros

        fragancias_clasificadas.append((proporcion, fragancias[i].facha, fragancias[i].mililitros))
    
    fragancias_clasificadas.sort(reverse = True)

    facha_total = 0
    
    i = 0
    while i < n and capacidad > 0:
        proporcion = fragancias_clasificadas[i][0]
        facha = fragancias_clasificadas[i][1]
        mililitros = fragancias_clasificadas[i][2]
        
        if mililitros <= capacidad:
            facha_total += facha
            capacidad -= mililitros
        else:
            facha_total += capacidad * proporcion
            capacidad = 0
        i += 1
    
    return facha_total


Complejidad:

- Temporal: ordenar la lista es O(n log(n)) mientras que recorrerla y compararla es O(n). Por lo tanto O(n log(n)) + O(n) = O(n log(n))

- Espacial: O(n) ya que tenemos que agregar n fragancias a la lista nueva que creamos.

Demostracion de optimalidad: si una solucion decide poner un perfume de menor proporcion, entonces estaria desaprovechando la facha. Por lo tanto habria que cambiar la eleccion a la de Greedy para poder maximizar la facha


-----------------------------------------------------------------------------
EJERCICIO 2: DIVISIÓN Y CONQUISTA (Cazando el Bug en la Shell)
-----------------------------------------------------------------------------
Enunciado:
Estás programando un proyecto de una Shell para la facultad. Tenés un historial en GitHub con N commits, ordenados cronológicamente del más viejo al más nuevo. Sabés que en el commit 0 la Shell compilaba y funcionaba perfecto (True). Sin embargo, en el último commit N-1, al ejecutarla tira un Segmentation Fault (False). El problema es que una vez que un commit introduce el error, todos los commits siguientes también fallan. Tenés una función testear_commit(i) que toma un tiempo O(1) en decirte si el commit 'i' funciona (True) o falla (False).
Diseñar un algoritmo de División y Conquista con complejidad  (log N) que encuentre el índice del primer commit que introdujo el error.

Se pide:
1. Explicación (Divide, Conquista, Combina).
2. Pseudocódigo.
3. Ecuación de recurrencia y Complejidad (Teorema Maestro).
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion:

- Division: se parte el array en dos

- Conquista:
Si el commit de mitad = True entonces el error esta en la mitad derecha, por lo tanto descartamos mitad izquierda
Si el commit de mitad = False entonces el error esta en la mitad izquierda, por lo tanto descartamos mitad derecha

- Combina: el resultado esta en el caso base


Pseudocodigo:

def encontrar_error(commits, inicio, fin):

    if inicio == fin:
        return inicio
    
    mitad = (inicio + fin) // 2

    if commits[mitad] == False:
        return encontrar_error(commits, inicio, mitad)
    else:
        return encontrar_error(commits, mitad + 1, fin)
    

Ecuacion de recurrencia:

T(n) = a * T(n/b) + f(n)

a = 1, es la llamada recursiva
b = 2 porque dividimos el array en 2
f(n) = O(1) porque calcula los indices y los compara

Complejidad:

- Temporal: T(N) = a * T(n/b) + f(n) = 1 * T(n/2) + O(1) = 1 * T(n/2) + O(n^0)
a vs b^k = 1 vs 2^0 = 1 vs 1 => 1 = 1 por lo tanto O(n^k log(n)) = O(n^0 log(n)) = O(1 log(n)) = O(log(n))

- Espacial: O(log n) por el espacio que ocupa el call stack de recursion


-----------------------------------------------------------------------------
EJERCICIO 3: PROGRAMACIÓN DINÁMICA (El vuelto de la cuota)
-----------------------------------------------------------------------------
Enunciado:
Para el sistema de gestión del gimnasio, estás programando el módulo de caja. Cuando un alumno paga la cuota mensual en efectivo, el sistema tiene que decirle al profesor cuál es la cantidad mínima de billetes que debe darle como vuelto. Tenés un arreglo con las denominaciones de billetes disponibles en la caja (ej: [1000, 2000, 10000]), asumiendo que tenés cantidad infinita de cada billete. El vuelto total a devolver es un valor V.
Diseñar un algoritmo de Programación Dinámica que encuentre la cantidad mínima de billetes necesarios para sumar exactamente V. (Si no es posible dar el vuelto exacto, debe retornar infinito o -1).

Se pide:
1. Explicación de la estructura de memoización.
2. Pseudocódigo.
3. Ecuación de recurrencia.
4. Complejidad temporal y espacial.
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion: voy a usar un arreglo unidimensional DP de tamano V + 1, la celda DP[v] guardara la cantidad minima de billetes del vuelto (v). Para calcula DP[v] iteramos sobre todas las denominaciones que tenemos, si el billete es menor o igual al vuelto actual, nos fijamos si la cantidad de billetes es menor que el valor que ya tenemos almacenado en DP[v]. Al construirlo de menor a mayor da la posibilidad de usar la misma denominacion varias veces.



Pseudocodigo:

def minimos_billetes(denominaciones, V):

    n = len(denominaciones)
    DP = [float('inf')] * (V + 1)
    DP[0] = 0

    for v in range(1, V + 1):
        for i in range(n):
            if denominaciones[i] <= v:
                vuelto_actual = DP[v - denominaciones[i]] + 1

                if vuelto_actual < DP[v]:
                    DP[v] = vuelto_actual
    
    if DP[V] == float('inf'):
        return -1
    else:
        return DP[V]

Ecuacion de recurrencia:

- Caso base: DP[0] = 0

- Caso recursivo: DP[v] = min{DP[v], DP[v - denominaciones[i]] + 1}
(para todo i tal que denominaciones[i] <= v)

Complejidad:

- Temporal: el ciclo exterior itera 'V' veces mientras que el interior itera 'n' veces => O(V*n)

- Espacial: necesitamos un espacio proporcional al vuelto => O(V)

'''
