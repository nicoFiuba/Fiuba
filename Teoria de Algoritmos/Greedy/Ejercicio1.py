def ubicar_patrulleros(bifurcaciones):

    # Asumimos que bifurcaciones es una lista de enteros (los kilómetros)
    bifurcaciones.sort()

    patrulleros = []
    cantidad_bifurcaciones = len(bifurcaciones)

    i = 0
    while i < cantidad_bifurcaciones:

        # El pueblo actual que necesita cobertura (nuestro extremo izquierdo)
        pueblo_a_cubrir = bifurcaciones[i]

        # Buscar la bifurcación Y más lejana a <= 50km
        posicion_patrullero = bifurcaciones[i]
        while (i + 1 < cantidad_bifurcaciones and bifurcaciones[i + 1] - pueblo_a_cubrir <= 50):
            i += 1
            posicion_patrullero = bifurcaciones[i]
            
        # Ubicamos el patrullero en Y
        patrulleros.append(posicion_patrullero)
            
        # Ahora el patrullero cubre hasta Y + 50km hacia adelante.
        # Avanzamos el índice para saltear todos los pueblos que ya quedaron cubiertos
        rango_cobertura = posicion_patrullero + 50
            
        while (i + 1 < cantidad_bifurcaciones and bifurcaciones[i + 1] <= rango_cobertura):
            i += 1
                
        # Pasamos al siguiente pueblo sin cobertura
        i += 1
    
    return patrulleros


"""
2. ANÁLISIS DE COMPLEJIDAD

Complejidad Temporal: O(N log N)
- Ordenar el arreglo inicial de N bifurcaciones tiene un costo de O(N log N).
- El ciclo while principal y sus ciclos internos recorren la lista de bifurcaciones de izquierda a derecha. Como el índice 'i' únicamente se incrementa y nunca retrocede, cada elemento se visita una cantidad constante de veces. Por lo tanto, el recorrido toma tiempo lineal O(N).
- La complejidad final está dominada por el ordenamiento: O(N log N) + O(N) = O(N log N).

Complejidad Espacial: O(N)
- La lista 'patrulleros' guardará las posiciones elegidas. En el peor caso (si todas las bifurcaciones están a más de 100 km), se necesitará un patrullero por pueblo, ocupando O(N).
- El método de ordenamiento también requiere espacio auxiliar. En conjunto, la complejidad espacial es O(N).


3. JUSTIFICACIÓN DE OPTIMALIDAD

Para demostrar que nuestra solución Greedy es óptima, utilizamos el argumento de que 
"la elección golosa siempre se mantiene adelante" (Greedy stays ahead).

Supongamos que existe una solución óptima distinta a la nuestra. Al evaluar el primer 
pueblo sin cobertura desde la izquierda, nuestra estrategia Greedy ubica el patrullero 
en la bifurcación más a la derecha posible que aún alcance a cubrir ese pueblo (a <= 50 km). 

Cualquier otra solución óptima deberá poner su patrullero en la misma bifurcación o en 
una que esté más a la izquierda. Como el patrullero Greedy está situado lo más a la 
derecha posible, su rango de cobertura hacia adelante (posición + 50 km) será mayor o 
igual al rango de cobertura del patrullero de la solución óptima. 

Esto significa que, tras la primera elección, el subproblema restante que debe resolver 
nuestro algoritmo (los pueblos que aún quedan por cubrir) es siempre un subconjunto 
(es igual o más pequeño) del subproblema que le queda a la solución óptima. 

Aplicando este mismo razonamiento de forma inductiva en cada paso, nuestra solución 
Greedy siempre cubre al menos la misma cantidad de pueblos con la misma cantidad de 
patrulleros. Por lo tanto, es imposible que una solución óptima logre cubrir toda la 
ruta utilizando estrictamente menos patrulleros que nuestro algoritmo. Concluimos que 
la estrategia Greedy garantiza la cantidad mínima y óptima de patrulleros.
"""

# Bloque de prueba opcional para que lo corras en tu compu
if __name__ == "__main__":
    # Ejemplo de la guía: (Castelli, 185), (Gral Guido, 249), (Lezama 156), (Maipu, 270), (Sevigne, 194)
    bifurcaciones_prueba = [185, 249, 156, 270, 194]
    resultado = ubicar_patrulleros(bifurcaciones_prueba)
    print(f"Bifurcaciones originales: {bifurcaciones_prueba}")
    print(f"Ubicación de patrulleros: {resultado}")
    print(f"Cantidad total de patrulleros usados: {len(resultado)}")
