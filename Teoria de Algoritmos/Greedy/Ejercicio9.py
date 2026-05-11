"""
TEORÍA DE ALGORITMOS - EJERCICIO 9: Verdadero o Falso (MST)

a. El algoritmo de Prim genera el mismo resultado que el algoritmo de Kruskal, al calcular el MST de un Grafo.
Respuesta: FALSO.
Justificación: si bien ambos algoritmos son óptimos y siempre generarán un árbol con el MISMO costo total mínimo, no necesariamente seleccionarán el MISMO conjunto de aristas si el grafo tiene aristas con pesos repetidos (empates). Ante un empate, Prim elegirá la arista que le convenga según su frontera de nodos visitados, mientras que Kruskal elegirá la que aparezca primero en su lista ordenada. El resultado puede ser un árbol con forma distinta.


b. El algoritmo de Prim aplicado a un Grafo genera siempre el mismo MST.
Respuesta: FALSO.
Justificación: Prim requiere un nodo de inicio (raíz) para empezar a construir el árbol. Si el grafo tiene múltiples MST válidos (debido a aristas con el mismo peso), comenzar desde un nodo distinto o tener un criterio de desempate diferente al elegir qué arista mínima de la frontera procesar primero, puede derivar en un árbol completamente distinto (aunque del mismo peso total).


c. El algoritmo de Kruskal aplicado a un Grafo genera siempre el mismo MST.
Respuesta: FALSO.
Justificación: al igual que con Prim, si el grafo tiene aristas con pesos repetidos, Kruskal debe ordenarlas de menor a mayor. Si el algoritmo de ordenamiento utilizado no es estable, o simplemente desempata de una forma arbitraria, el orden en que se evalúan las aristas del mismo peso cambiará. Esto puede llevar a rechazar unas aristas por formar ciclos y aceptar otras, generando un MST diferente.


d. Si un Grafo posee todas sus aristas distintas, el MST es siempre el mismo sin importar qué algoritmo se utilice.
Respuesta: VERDADERO.
Justificación: esta es la "Propiedad de Unicidad" del MST. Si todos los pesos de las aristas de un grafo son estrictamente distintos entre sí, existe matemática y obligatoriamente un ÚNICO Árbol Recubridor Mínimo. En este escenario, Kruskal, Prim, o Reverse-Delete devolverán exactamente el mismo conjunto de aristas.


e. El MST del siguiente Grafo posee 2 MST.
Respuesta: VERDADERO.
Justificación: en este grafo específico, los nodos E, B y F forman un ciclo con las aristas EF(1), EB(2) y BF(2). Hay un empate en el peso máximo (2) entre EB y BF. Al poder descartar cualquiera de las dos, se generan exactamente 2 MST.

f. El MST del siguiente Grafo es: {AB, AE, BC, CG, GD, GF, GH}.
Respuesta: VERDADERO
Justificación: al aplicar Kruskal sobre este grafo, seleccionamos las aristas AB(1), GD(1), GF(1), GH(1), BC(2), CG(2) y AE(4) sin formar ciclos, lo que nos da exactamente el conjunto propuesto con un costo mínimo irreemplazable de 12.

Para verificarlo en un parcial: 
1. Sumá los pesos de esas aristas.
2. Resolvé el grafo rápido mentalmente con Kruskal. (Elijo las aristas de menor peso, evitando ciclos, hasta conectar todo el grafo).Si el costo de tu Kruskal es menor a esa suma, o si esas aristas dejan algún nodo desconectado, la afirmación es Falsa.


g. Dado un grafo G no dirigido con costos en cada arista c(e). Si suponemos que e* es la arista de menor costo (c(e*) < c(e) para cada arista de G/e<>e*), entonces podemos afirmar que cualquier MST de G contendrá a e*.
Respuesta: VERDADERO.
Justificación: se justifica mediante la "Propiedad del Corte" (Cut Property). Si dividimos el grafo en dos conjuntos de vértices cualesquiera de tal forma que un extremo de e* quede de un lado y el otro extremo del otro, e* será la arista más barata que cruza ese corte (ya que es la más barata de todo el grafo). La propiedad establece que la arista más barata que cruza cualquier corte DEBE pertenecer al MST.
"""
