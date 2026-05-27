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

"""