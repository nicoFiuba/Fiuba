'''
-----------------------------------------------------------------------------
EJERCICIO 1: GREEDY (Delivery de Comida)
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion: 
La función a minimizar es la sumatoria de w_i * (C_i + a_i). Si aplicamos propiedad distributiva, nos queda: Sumatoria(w_i * C_i) + Sumatoria(w_i * a_i).
La "trampa" del ejercicio es que la sumatoria de (w_i * a_i) es una CONSTANTE, ya que el tiempo de viaje a_i y la prioridad w_i de cada pedido no cambian sin importar en qué orden los preparemos. Por lo tanto, el problema se reduce a minimizar únicamente Sumatoria(w_i * C_i).
Esta es la variante clásica del problema de "Minimizar el tiempo de finalización ponderado". La estrategia Greedy óptima es calcular el ratio (w_i / t_i) para cada pedido (prioridad aportada por cada minuto invertido) y ordenarlos de MAYOR a MENOR ratio.

Pseudocodigo:

def orden_preparacion(pedidos):
    
    pedidos.sort(key = lambda x: x.w / x.t, reverse=True) # Ordenamos de mayor a menor ratio peso/tiempo
    
    orden_final = []
    for pedido in pedidos:
        orden_final.append(pedido.id)
        
    return orden_final

Complejidad:

- Temporal: Calcular el ratio toma O(N), ordenar la lista toma O(N log N) y recorrerla para armar el resultado O(N). Complejidad final: O(N log N).

- Espacial: O(N) para almacenar el arreglo con el orden final.

Demostracion de optimalidad (Argumento de intercambio): 
Supongamos que tenemos una solución óptima S que tiene una inversión, es decir, un pedido 'j' se prepara inmediatamente después de un pedido 'i', pero el ratio de 'j' es mayor (w_j/t_j > w_i/t_i). Si intercambiamos el orden de estos dos pedidos, el tiempo de finalización C de todos los pedidos anteriores y posteriores se mantiene igual. Sin embargo, el pedido 'j' termina t_i minutos antes, y el pedido 'i' termina t_j minutos después. El cambio en el costo total es: (w_i * t_j) - (w_j * t_i). Como sabíamos que w_j/t_j > w_i/t_i, al despejar nos da que (w_i * t_j) - (w_j * t_i) < 0. Esto significa que el costo DISMINUYÓ. Por lo tanto, cualquier solución que no esté ordenada por este ratio puede mejorarse, demostrando que la estrategia Greedy es la óptima.


-----------------------------------------------------------------------------
EJERCICIO 2: DIVISIÓN Y CONQUISTA (Auditoría de Satisfacción)
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion:
Este problema es la búsqueda de un "valle" en un arreglo bitónico invertido (primero desciende estrictamente y luego asciende estrictamente). 
- Divide: Calculamos la posición central 'mitad'.
- Conquista: Comparamos el nivel de satisfacción en 'mitad' con el nivel en 'mitad + 1'. 
Si satisfaccion[mitad] > satisfaccion[mitad + 1] => Seguimos en la pendiente de descenso, por lo que el cambio (el punto más bajo) tiene que estar hacia la derecha. Descartamos la mitad izquierda.
Si satisfaccion[mitad] < satisfaccion[mitad + 1] => Ya pasamos el punto más bajo y estamos en la subida, por lo que el cambio ocurrió en la mitad izquierda (o en la posición actual). Descartamos la mitad derecha.
- Combina: El resultado (el mes del cambio) se encuentra en el caso base.

Pseudocodigo:

def buscar_mes_cambio(satisfaccion, inicio, fin):

    if inicio == fin:
        return inicio

    mitad = (inicio + fin) // 2

    if satisfaccion[mitad] > satisfaccion[mitad + 1]:
        return buscar_mes_cambio(satisfaccion, mitad + 1, fin)
    else:
        return buscar_mes_cambio(satisfaccion, inicio, mitad)

Ecuacion de recurrencia:

T(N) = a * T(N/b) + f(N)
a = 1, es la llamada recursiva
b = 2, el arreglo se parte a la mitad
f(N) = O(1) porque calcula los indices y los compara

Complejidad:

- Temporal: T(N) = a * T(n/b) + f(n) = 1 * T(n/2) + O(1) = 1 * T(n/2) + O(n^0) 
a vs b^k = 1 vs 2^0 = 1 vs 1 => 1 = 1 por lo tanto O(n^k * log(n)) = O(n^0 * log(n)) = O(1 * log(n)) = O(log(n))


- Espacial: O(log (n)) es el call stack de la recursion.


-----------------------------------------------------------------------------
EJERCICIO 3: PROGRAMACIÓN DINÁMICA (Paradas de Colectivo)
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion:
Voy a usar un arreglo unidimensional DP de tamaño N + 1, donde la celda DP[i] guardará la cantidad máxima de dinero que se puede recaudar analizando hasta la cuadra 'i'. Para calcular DP[i], iteramos por cada cuadra de menor a mayor. En cada cuadra 'i', tenemos dos opciones:
1. NO poner la parada: la ganancia será la misma que traíamos hasta la cuadra anterior (DP[i-1]).
2. SÍ poner la parada: ganamos el aporte de esta cuadra (w_i), pero por normativa no pudimos haber puesto paradas ni en (i-1) ni en (i-2). Por lo tanto, le sumamos la ganancia óptima que traíamos hasta 3 cuadras atrás (DP[i-3]).
Nos quedamos con el máximo entre esas dos opciones.

Pseudocodigo:

def maximizar_recaudacion(W, N):
    
    if N == 0:
        return 0
    if N <= 3:
        return max(W)
        
    DP = [0] * (N + 1)
    
    DP[1] = W[0]
    DP[2] = max(W[0], W[1])
    DP[3] = max(W[0], W[1], W[2])
    
    for i in range(4, N + 1):
        opcion_no_poner = DP[i - 1]
        opcion_si_poner = W[i - 1] + DP[i - 3]
        
        DP[i] = max(opcion_no_poner, opcion_si_poner)
        
    return DP[N]

Ecuacion de recurrencia:

- Casos base: 
DP[0] = 0
DP[1] = W[1]
DP[2] = max(W[1], W[2])
DP[3] = max(W[1], W[2], W[3])

- Caso recursivo (para i >= 4): 
DP[i] = max(DP[i - 1] , W[i] + DP[i - 3] )

Complejidad:

- Temporal: El ciclo itera exactamente N-3 veces haciendo operaciones de tiempo constante (max y suma). Por lo tanto, O(N).

- Espacial: O(N) porque necesitamos mantener un vector DP de tamaño N+1.


'''