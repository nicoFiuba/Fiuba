"""

EXPLICACIÓN: la estrategia consiste en ordenar de mayor a menor según la suscripción, ya que la mejor suscripción solo puede recibir un único tipo de pack. Esta estrategia es Greedy porque realiza una elección:
    - Localmente óptima ya que en cada iteración elige al suscriptor que menos packs puede recibir
    - Factible ya que le da el pack al subscriptor que puede recibirlo
    - Irrevocable ya que una vez tomada la decision, no se la puede remover.

PSEUDOCÓDIGO
"""

def asignar_packs(suscriptores, packs):

    suscriptores.sort(key=lambda x: x.categoria, reverse=True) # suscriptores = [Titanio, Oro, Plata, Basico]

    i = 0
    while len(packs) > 0 and i < len(suscriptores):

        pack_elegido = elegir_pack(suscriptores[i], packs)

        if pack_elegido is None:
            return  False
        
        packs.remove(pack_elegido)

        i += 1

    if len(suscriptores) == i:
        return True

    return False

"""
ANÁLISIS DE COMPLEJIDAD

- TEMPORAL: ordenar la lista toma O(N * log(N)) mientras que  recorrerla toma O(N). Por lo tanto, la complejidad es O(N * log(N)).

- ESPACIAL: O(N) para almacenar el orden.

ANÁLISIS DE OPTIMALIDAD: se demuestra mediante el argumento de la sustitución, ya que si una solución ordena diferente a la de Greedy, significa que un suscriptor puede que no reciba su pack debido a que no hay mas. Por lo tanto, tendríamos que cambiar las asignaciones para que el suscriptor pueda recibir su pack.
"""
