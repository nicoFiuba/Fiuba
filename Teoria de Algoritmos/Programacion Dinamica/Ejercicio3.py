"""

EXPLICACIÓN: voy a usar dos arreglos unidimensionales OPT. Como es un arbol, primero ordenamos de menor a mayor segun su rango, luego iteramos los nodos en ese orden y calculamos: el rating maximo tanto si el empleado asiste como si no.

RELACION DE RECURRENCIA:

- Caso base: 
OPT_asiste[jefe] = rating[jefe]
OPT_no_asiste[jefe] = 0

- Caso recursivo: 
OPT_asiste[jefe] = rating[jefe] + sum(OPT_no_asiste[empleados])
OPT_no_asiste[jefe] = sum(max(OPT_asiste[empleados], OPT_no_asiste[empleados]))

PSEUDOCÓDIGO
"""

def obtener_invitados(organigrama):

    orden = orden_bottom_up(organigrama)

    OPT_asiste = {}
    OPT_no_asiste = {}
    lista_asisten = {}
    lista_no_asisten = {}

    for jefe in orden:
        OPT_asiste[jefe] = jefe.rating
        OPT_no_asiste[jefe] = 0
        lista_asisten[jefe] = [jefe.id]
        lista_no_asisten[jefe] = []

        for empleado in jefe.empleados:
            OPT_asiste[jefe] += OPT_no_asiste[empleado]
            lista_asisten[jefe] += lista_no_asisten[empleado]

            if OPT_asiste[empleado] > OPT_no_asiste[empleado]:
                OPT_no_asiste[jefe] += OPT_asiste[empleado]
                lista_no_asisten[jefe] += lista_asisten[empleado]
            else:
                OPT_no_asiste[jefe] += OPT_no_asiste[empleado]
                lista_no_asisten[jefe] += lista_no_asisten[empleado]

    ceo = orden[-1]
    if OPT_asiste[ceo] > OPT_no_asiste[ceo]:
        return lista_asisten[ceo]
    else:
        return lista_no_asisten[ceo]

""" 
ANÁLISIS DE COMPLEJIDAD

- Temporal: ordenar y recorrer el array toma O(N). Por lo tanto, la complejidad es O(N).

- Espacial: O(N) para almacenar los OPTs y la lista de invitados.

EJEMPLO: supongamos un organigrama con 4 empleados (Ceo, A, B, C) con los siguientes ratings:
- Ceo (rating 10) tiene a cargo a A y B.
- A (rating 20) tiene a cargo a C.
- B (rating 30) sin personas a cargo (hoja).
- C (rating 15) sin personas a cargo (hoja).

orden = [C, B, A, Ceo]

jefe = C
OPT_asiste[jefe] = OPT_asiste[C] = rating[C] = 15
OPT_no_asiste[jefe] = OPT_no_asiste[C] = 0
lista_asisten[jefe] = lista_asisten[C] = [C]
lista_no_asisten[jefe] = lista_no_asisten[C] = []

jefe = B
OPT_asiste[jefe] = OPT_asiste[B] = rating[B] = 30
OPT_no_asiste[jefe] = OPT_no_asiste[B] = 0
lista_asisten[jefe] = lista_asisten[B] = [B]
lista_no_asisten[jefe] = lista_no_asisten[B] = []

jefe = A
OPT_asiste[jefe] = rating[jefe] + OPT_no_asiste[empleado] = rating[A] + OPT_no_asiste[C] = 20 + 0 = 20
lista_asisten[jefe] = lista_asisten[jefe] + lista_no_asisten[empleado] = lista_asisten[A] + lista_no_asisten[C] = [A] + [] = [A]
OPT_no_asiste[jefe] = OPT_no_asiste[A] = max(OPT_asiste[empleado], OPT_no_asiste[empleado]) = max(OPT_asiste[C], OPT_no_asiste[C]) = max(15, 0) = 15
lista_no_asisten[jefe] = lista_no_asisten[A] = lista_asisten[empleado] = lista_asisten[C] = [C]

jefe = Ceo
OPT_asiste[jefe] = rating[jefe] + OPT_no_asiste[empleado1] + OPT_no_asiste[empleado2] = rating[Ceo] + OPT_no_asiste[A] + OPT_no_asiste[B]= 10 + 15 + 0 = 25
lista_asisten[jefe] = lista_asisten[Ceo] = [Ceo] + lista_no_asisten[empleado1] + lista_no_asisten[empleado2] = [Ceo] + [C] + [] = [Ceo, C]
OPT_no_asiste[jefe] = OPT_no_asiste[Ceo] = max(OPT_asiste[empleado1], OPT_no_asiste[empleado1]) + max(OPT_asiste[empleado2], OPT_no_asiste[empleado2]) = max(20, 15) + max(30, 0) = 20 + 30 = 50
lista_no_asisten[jefe] = lista_no_asisten[Ceo] = lista_asisten[empleado1] + lista_asisten[empleado2] = [A] + [B] = [A, B]

Como el Ceo es el último nodo del orden, evaluamos el resultado final ahí => OPT_no_asiste[Ceo] > OPT_asiste[Ceo] -> 50 > 25 
Por lo tanto, la ganancia máxima es 50 y la lista de invitados resultante es [A, B].
"""
