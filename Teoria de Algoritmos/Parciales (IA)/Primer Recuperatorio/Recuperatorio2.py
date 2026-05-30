"""
--------------------------------------------------------------------------------
EJERCICIO 1: GREEDY (Maximización de Tareas)
--------------------------------------------------------------------------------
Enunciado:
Se dispone de un conjunto de N tareas de mantenimiento programadas para una máquina. Cada tarea i tiene un tiempo de inicio S_i y un tiempo de finalización F_i fijos. La máquina es un recurso único, lo que implica que solo puede procesar una tarea a la vez y una vez que inicia una tarea debe terminarla sin interrupciones (es decir, dos tareas i y j son compatibles si los intervalos [S_i, F_i) y [S_j, F_j) no se superponen). Se desea seleccionar la máxima cantidad posible de tareas compatibles para ejecutar en la máquina.

Se pide:
1. Explicación y por qué es Greedy.
2. Pseudocódigo.
3. Complejidad temporal y espacial.
4. Demostración de optimalidad.
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion: la estrategia consiste en ordenar a las tareas de menor a mayor segun el tiempo de finalizacion, es decir que agarramos la tarea que termina primero y la sumamos a nuestro contador para que luego cuando iteremos nos podamos fijar en el horario de inicio de la nueva solicitud, si este horario es mayor o igual que nuestro horario de finalizacion actual, agregamos la tarea. Es Greedy porque en cada iteracion elegimos la tarea que termina primero para poder liberarnos antes y asi hacer otras tareas.

def maximizar_tareas(tareas):

   tareas.sort(key = lambda x: x.fin)
   n = len(tareas)

   if n == 0:
      return 0
   
   cantidad_tareas = 1
   fin_tarea = tareas[0].fin

   for i in range(1, n):
      if tareas[i].inicio >= fin_tarea:
         cantidad_tareas += 1

         fin_tarea = tareas[i].fin
      
   return cantidad_tareas

Complejidad:

- Temporal: ordenar la lista toma O(N * log(N)) mientraas que recorrerla y compararla es O(N), por lo tanto O(N * log(N)) + O(N) = O(N * log(N))

- Espacial: O(1) ya que usamos un contador

Demostracion de optimalidad: si una solucion elige un horario de finalizacion superior, se estaria quedando sin tiempo libre para poder hacer otra tarea. Por lo tanto habria que intercambiar la eleccion de la tarea por la de Greedy para asi aprovechar al maximo la seleccion de tareas.


--------------------------------------------------------------------------------
EJERCICIO 2: REDES DE FLUJO (Sincronización de Datos)
--------------------------------------------------------------------------------
Enunciado:
Una empresa de tecnología posee N servidores locales y M bases de datos centrales.
* Cada servidor local i tiene una capacidad de transmisión para soportar hasta K_i procesos concurrentes.
* Cada base de datos central j requiere exactamente R_j procesos asignados para garantizar su correcta sincronización.
* Por arquitectura de red, un servidor i solo es compatible con un subconjunto específico de bases de datos.
* Existe una restricción geográfica: el subconjunto de servidores ubicados en la "Zona Sur" no puede emitir, en total y de forma conjunta, más de X procesos concurrentes para evitar saturar el enlace troncal. Determinar si es posible asignar los procesos de los servidores cumpliendo todas las restricciones.

Se pide:
1. Explicación de la estrategia de modelado elegida.
2. Definición de la Red (explicar cómo se construye el grafo a resolver detallando Nodos, Aristas y Capacidades).
3. Pseudocódigo detallado (incluyendo armado de la red, llamada al algoritmo de flujo y obtención de la solución).
4. Complejidad temporal.
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion: estamos ante un problema de asignacion el cual lo vamos a resolver utilizando el algoritmo de flujo maximo, la idea es construir una red en donde cada unidad de flujo represente a un servidor asignado a una base de datos especifica, garantizando que se cumpla lo pedido.

Definicion de la red:

Dado un conjunto N de servidores y un conjunto M de bases de datos, creqamos una nueva red de flujo G' de la siguiente manera:

Nodo: agregamos una fuente S, un sumidero T, N nodos (uno para cada servidor), M nodos (uno para cada base de datos) y un nodo extra para la reestriccion

Aristas desde S:

- Servidores normales: conectamos S a cada servidor 'i' con capacidad K_i para garantizar que el servidor asignado no sea asignado a mas bases de datos de las permitidas.
- Zona Sur: conectamos S al nodo extra con capacidad X y a este lo conectamos a cada servidor 'i' con capacidad K_i para garantizar que el servidor asignado no sea asignado a mas bases de datos de las permitidas.

Aristas N - M: si el servidor 'i' es compatible con la base de datos 'j', agregamos una arista dirigida desde el servidor 'i' hasta la base de datos 'j' con capacidad 1. Esto garantiza la redundancia.

Aristas hacia T: conectamos a cada base de datos 'j' con el sumidero T con capacidad R_j para poder garanmtizar la redundancia.

Pseudocodigo:

def es_posible_asignar_servidores(servidores, bases_de_datos, reestricciones, zona_sur, X):

   # Armamos la red
   red = GrafoDirigido()
   red.agregar_arista("S", "Nodo extra", X)

   # Conectamos S a los servidores y estos a las bases de datos
   for servidor in servidores:
      if servidor in zona_sur:
         red.agregar_arista("Nodo extra", servidor.id, capacidad = servidor.K)
      else:
         red.agregar_arista("S", servidor.id, capacidad = servidor.K)

      for base in bases_de_datos:
         if puede_conectarse(servidor, base, reestriciones):
            red.agregar_arista(servidor.id, base.id, capacidad = 1)
   
   # Conectamos las bases de datos a T y sumamos las asignaciones
   asignaciones_totales = 0
   for base in bases_de_datos:
      red.agregar_arista(base.id, "T", capacidad = base.R)
      asignaciones_totales += base.R
   
   # Llamada a Ford-Fulkerson con BFS => Edmonds-Karps
   flujo_maximo, grafo_residual = ford_fulkerson(red, "S", "T")

   # Solucion
   return flujo_maximo == asignaciones_totales

Complejidad:
- Armar la red toma O(N * M)
- V' tiene 3 + N + M nodos, por lo tanto O(N + M)
- E' tiene N + M + (N * M) aristas, por lo tanto O(N * M)
- Al usar Edmonds-Karps la complejidad teorica es O(V' * E'²), por lo tanto si lo traemos a nuestra red, nos queda que O((N + M) * (N * M)²)


--------------------------------------------------------------------------------
EJERCICIO 3: CLASES DE COMPLEJIDAD (Reducciones NP)
--------------------------------------------------------------------------------
Enunciado:
Se define el problema de decisión CONJUNTO DE EQUIPOS NO CONFLICTIVOS (CENC): Dado un grafo no dirigido G=(V,E) donde los vértices representan equipos y las aristas representan rivalidades históricas, y un entero J, ¿existe un subconjunto de vértices de tamaño exactamente J tal que ningún par de vértices en dicho subconjunto sea adyacente en G? Sabiendo que el problema INDEPENDENT SET (Conjunto Independiente) es NP-Completo, demuestre formalmente que CENC pertenece a la clase NP-Completo.

Se pide:
1. Paso 1: Demostrar que el problema pertenece a NP (explicando certificado, pseudocódigo del certificador y su complejidad).
2. Paso 2: Demostrar que es NP-Hard mediante una reducción polinomial (explicar la reducción, la complejidad de la transformación y la justificación de "Ida y vuelta").
3. Conclusión final de su clasificación.
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Demostracion de pertenencia a NP

- Explicacion del certificado: la evidencia que nos dan es que existe un subconjunto S de exactamente J enteros

- Pseudocodigo del certificado:

def certificador(equipos, J, certificado_S):

   n = len(certificado_S)

   if n != J:
      return False

   for equipo in equipos:
      adyacente1 = equipo.origen
      adyacente2 = equipo.fin

      if adyacente1 in certificado_S and adyacente2 in certificado_S:
         return False
   
   return True

Complejidad del certificado:

- Verificar el tamaño toma O(1)
- Iterar sobre las aristas toma O(A)
- Si pensamos al certificado como un HashSet, verificarlo toma O(1)
Por lo tanto la complejidad nos queda O(A) y es estrictamente polinomial, por ende queda demostrado que pertenece a NP

Demostracion de pertenencia a NP-Hard

- Reduccion: el problema Independent Set (IS) busca un conjunto de J vertices en un grafo G = (V, E) donde ningun par de vertices comparta una arista. Por lo tanto armamos una instancia con el mismo grafo (G' = G) y el mismo limite de vertices J' = J

- Complejidad: copiar las referencias del grafo y asignar la variable toma O(1) lo cual es estrictamente polinomial

- IDA: como G' = G y J' = J, si existe un conjunto independiente de tamaño J en G, entonces existe un subconjunto de equipos no conflictivos de tamaño J' en G'

- VUELTA: como en G' encontramos un subconjunto de equipos no conflictivos de tamaño J', entonces existe un conjunto independiente de tamaño J en G

- Conclusion: como demostramos que nuestro problema pertenece a NP mediante un certificado polinomial y ademas demostramos que pertenece a NP-Hard mediante una reduccion polinomial, podemos afirmar que nuestro problema es un NP-Completo


--------------------------------------------------------------------------------
EJERCICIO 4: BÚSQUEDA EXHAUSTIVA (Branch & Bound)
--------------------------------------------------------------------------------
Enunciado:
Queremos proveer cobertura de cámaras a un predio modelado como un conjunto de C zonas. Se cuenta con un catálogo de A cámaras disponibles. Cada cámara k tiene un costo de instalación C_k y su lente permite cubrir un subconjunto específico de zonas adyacentes. Queremos cubrir TODAS las zonas del predio incurriendo en el mínimo costo total posible de instalación.

Se pide resolver usando Branch and Bound detallando:
1. Explicación de la técnica aplicada a este problema (definir cotas y condición de poda).
2. Diagrama/explicación de los estados y la ramificación del árbol.
3. Pseudocódigo de la solución.
4. Complejidad temporal y espacial.
-----------------------------------------------------------------------------
RESOLUCIÓN ESPERADA:

Explicacion:

- Solucion Parcial: es el valor acumulado actualmente

- Cota Inferior: es la estimacion del costo minimo de la rama y como queremos minimizar, sumamos el costom parcial mas el costo minimo de las caamaras restantes

- Cota Superior: es la mejor solucion global valida hasta el momento. Se actualiza cada vez que encontramos una solucion mas barata que nuestro record

- Poda: si la cota superior de un nodo es menor o igual que la cota inferior, podamos esa rama ya que nunca va a ser mas barata que nuestro record

Diagrama de estados:

- Definicion: se considerqa el estado (k, costo_acumulado, zonas_cbiertas)

- Estado Inicial: (0, 0, Ø) ninguna camara fue procesada

- Decision en el nivel k: al evaluar la camara 'k', tenemos hasta dos opciones de ramificacion
1) Incluir a k siempre y cuando la zona 'z' escogida este disponible
2) No incluir a k (esta opcion siempre es valida)

Pseudocodigo:

MEJOR_GLOBAL = float('inf')

def branch_and_bound(k, camaras, C, zonas_cubiertas, costo_parcial):

   global MEJOR_GLOBAL
   n = len(zonas_cubiertas)

   if n == C:
      if costo_parcial < MEJOR_GLOBAL:
         MEJOR_GLOBAL = costo_parcial
      return
   
   l = len(camaras)

   if l == k:
      return
   
   cota_inferior = costo_parcial + estimar_costo_min(k, camaras)
   if cota_inferior >= MEJOR_GLOBAL:
      return
   
   camara_actual = camaras[k]
   
   # Rama Izquierda
   nuevas_zonas = zonas_cubiertas.union(camara_actual.cobertura)
   nuevo_costo = costo_parcial + camara_actual.costo
   
   branch_and_bound(k + 1, camaras, C, nuevas_zonas, nuevo_costo)
   
   # Rama Derecha
   branch_and_bound(k + 1, camaras, C, zonas_cubiertas, costo_parcial)

Complejidad:

- Temporal: en el peor de los casos para las A camaras exploramos dos opciones (incluir o no incluir), lo que toma O(2^A). Ademas por cada nodo tenemos que calcular la cota inferior, lo que toma O(C). Por lo tanto la complejidad que nos queda es O(C * 2^A)

- Espacial: O(A) ya que es el call stack de la recursion

"""
