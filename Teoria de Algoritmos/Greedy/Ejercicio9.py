"""
a) Falso, ya que si bien generan el mismo caso óptimo total, si el grafo tiene pesos repetidos, pueden devolver resultados distintos.

b) Falso, ya que el MST de Prim depende del nodo raiz y de la forma de resolver un empate.

c) Falso, ya que el MST de Krustal depende de la forma de resolver un empate.

d) Verdadero, ya que si todas las aristas son distintas, el MST es único y por lo tanto, ambos algoritmos generan el mismo resultado.

e) 

A---6---B---5---C---6---D
|     / |     / |     / |
1   2   2   5   4   5   7
| /     | /     | /     |
E---1---F---3---G---3---H

Verdero ya que como hay aristas repetidas pero sin ciclos, vamos a tener que elegir por que camino ir pero ambos son validos, es decir que existen varios MST.

f) 

A---1---B---2---C---3---D
| \     | \     |     / |
4   8   6   6   2   1   4
|     \ |     \ | /     |
E---5---F---1---G---1---H

Verdadero ya que {AB, AE, BC, CG, GD, GF, GH} agrupa las aristas de menor peso y por lo tanto, es un MST. 

g) Verdadero ya que por propiedad si aislamos uno de los extremos de e* mediante un corte, e* es la arista de menor peso que cruza el corte y por lo tanto, debe estar en el MST.
"""
