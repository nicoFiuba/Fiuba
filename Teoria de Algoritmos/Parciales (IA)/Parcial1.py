'''
-----------------------------------------------------------------------------
EJERCICIO 1: GREEDY (Cobertura de Refugios) - [Parcial 1C 2025]
-----------------------------------------------------------------------------
Enunciado: 
Se tiene un sendero lineal de montaña donde hay 'N' campamentos base ubicados en distintas posiciones kilométricas (X1, X2, ..., XN). Se desea construir refugios. Cada refugio tiene un radio de cobertura de 'R' kilómetros hacia adelante y hacia atrás. Proponer un algoritmo Greedy para encontrar la cantidad MÍNIMA de refugios necesarios para cubrir todos los campamentos.

Se pide:
1. Explicación y por qué es Greedy.
2. Pseudocódigo.
3. Complejidad temporal y espacial.
4. Demostración de optimalidad.
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion: la estrategia consiste en ordenar las posiciones de los campamentos de menor a mayor, tomar el primer campamento sin cubrir y colocar un refugio los mas lejos posible mientras que siga cubriendo al campamento  (es decir, posicion del campamento + R). Ese refugio cubrira (posicion del campamento mas 2R). Iteramos hasta encontrar el proximo campamento. Esto lo repetimos hasta cubrir todos los campamentos. Es Greedy porque en cada iteracion el programa busca estirar la cobertura lo maximo posible hacia adelante sin importarle el sendero.

Pseudocodigo:

def minimizar_refugios(posiciones, R):
    
    posiciones.sort()
    n = len(posiciones)
    refugios = []

    i=0
    while i < n:
        posicion_refugio = posiciones[i] + R
        refugios.append(posicion_refugio)

        maximo_alcance = posicion_refugio + R

        while i < n and posiciones[i] <= maximo_alcance:
            i += 1
    
    return len(refugios)


Complejidad:

- Temporal: ordenar la lista es O(n log(n)) mientras que recorrerla es O(n) por lo tanto la complejidad temporal es O(n log(n)) + O(n) = O(n log(n))

- Espacial: O(n) ya que en el peor de los casos se requiere un refugio por campamento

Demostracion de optimalidad: si una solucion pone un refugio antes que la solucion Greedy, estaria desperdiciando cobertura. Por lo tanto si a ese refugio lo empujo hasta el maximo alcance (es lo que hace Greedy), ahi si estaria aprovechando el refugio y dejando a todos protegidos.


-----------------------------------------------------------------------------
EJERCICIO 2: DIVISIÓN Y CONQUISTA (Mediana en Sedes) - [Recu 1C 2025]
-----------------------------------------------------------------------------
Enunciado:
La universidad tiene los legajos de sus alumnos ordenados de menor a mayor en dos bases de datos distintas (Sede A y Sede B). Ambas sedes tienen exactamente N legajos cada una. Se desea encontrar el legajo que representa la mediana de todos los alumnos (posición N del total de 2N).
Diseñar un algoritmo DyC con complejidad O(log N).

Se pide:
1. Explicación (Divide, Conquista, Combina).
2. Pseudocódigo.
3. Ecuación de recurrencia.
4. Complejidad con Teorema Maestro.
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion:

- Divide: calculamos la posicion central del arreglo y tomamos las medianas de cada sede (mediana_a y mediana_b)
- Conquista: 
Si mediana_a == mediana_b => mediana global
Si mediana_a < mediana_b => la mediana global tiene que ser mayor que mediana_a y menor que mediana_b, para eso descartamos la mitad inferior de la sede A y la mitad superior de la sede B y hacemos la llamada recursiva con lo que nos queda.
- Combina: el resultado esta en el caso base

Pseudocodigo:

def encontrar_mediana(A, B):

    n = len(A)

    if n == 1:
        return min(A[0], B[0])
    
    if n == 2:
        return max(A[0], B[0])

    mitad = n//2
    mediana_a = A[mitad]
    mediana_b = B[mitad]
    
    if mediana_a == mediana_b:
        return mediana_a
    
    if mediana_a < mediana_b:
        return encontrar_mediana(A[mitad:], B[:mitad])
    else:
        return encontrar_mediana(A[:mitad], B[mitad:])

Ecuacion de recurrencia:

T(N) = a * T(n/b) + f(n)

a = 1, es la llamada recursiva
b = 2 porque partimos el problema a la mitad
f(n) = O(1) porque calcula los indices centrales y los compara.

Complejidad:

- Temporal: T(N) = a * T(n/b) + f(n) = a * T(n/b) + O(1) = a * T(n/b) + O(n^0) 
a vs b^k = 1 vs 2^0 = 1 vs 1 => 1 = 1 por lo tanto O(n^k * log(n)) = O(n^0 * log(n)) = O(1 * log(n)) = O(log(n))

- Espacial: O(log n) por el espacio que ocupa el call stack de recursion


-----------------------------------------------------------------------------
EJERCICIO 3: PROGRAMACIÓN DINÁMICA (Perfumes) - [Parcial 1C 2025]
-----------------------------------------------------------------------------
Enunciado:
Juan desea comprar perfumes para maximizar su nivel de satisfacción. Cuenta con un presupuesto P. Hay N tipos de perfumes distintos, cada uno con un costo C[i] y una satisfacción S[i]. Hay stock ilimitado de cada tipo.
Encontrar la máxima satisfacción total sin exceder el presupuesto.

Se pide:
1. Explicación de la estructura de memoización.
2. Pseudocódigo.
3. Ecuación de recurrencia.
4. Complejidad temporal y espacial.
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion: voy usar un arreglo unidimensional DP de tamaño P + 1, la celda DP[p] guardara la satisfaccion maxima posible teniendo un presupuesto (p). Para calcular DP[p] iteramos sobre todos los perfumes, si el costo es menor a p => nos fijamos si la satisfaccion del presupuesto sobrante (DP[p - costo[i]]) supera el valor que ya teniamos almacenado en DP[p]. Al construirlo de menor a mayor, existe la posibilidad de comprar un perfume que ya tengo.

Pseudocodigo:

def comprar_perfumes(costos, satisfaccion, P):

    n = len(costos)
    DP = [0] * (P +1)

    for p in range(1, P + 1):
        for i in range(n):
            if costos[i] <= p:
                posible_valor = DP[p - costos[i]] + satisfaccion[i]
                if posible_valor > DP[p]:
                    DP[p] = posible_valor
    
    return DP[P]

Ecuacion de recurrencia: 

- Caso base: DP[0] = 0

- Caso recursivo: DP[p] = max{DP[p - costo[i]] + satisfaccion[i]}
(para todo i tal que costos[i] <= p).

Complejidad:

- Temporal: el ciclo exterior itera p veces mientras que el interior itera n veces => O(n*p)

- Espacial: necesitamos un espacio proporcional al presupuesto => O(p)

'''
