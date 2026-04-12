"""
TEORÍA DE ALGORITMOS - EJERCICIO 12: Club de Campo (Cobertura de Intervalos)

1. ESTRATEGIA (Elección Golosa)
El problema consiste en cubrir un intervalo de tiempo total (un mes) utilizando la menor cantidad de sub-intervalos (turnos de guardias) posibles.

Estrategia greedy:
1. Ordenamos a los guardias según su fecha de inicio (de menor a mayor).
2. Mantenemos una variable `cobertura_actual` que indica hasta qué día tenemos seguridad garantizada (inicialmente es el inicio del mes).
3. En cada iteración, evaluamos a TODOS los guardias cuyo turno comience en un día menor o igual a nuestra `cobertura_actual` (es decir, que no dejen baches).
4. De ese grupo de candidatos válidos, tomamos la decisión localmente óptima: elegimos al guardia cuyo turno termine LO MÁS TARDE POSIBLE.
5. Actualizamos nuestra `cobertura_actual` con la fecha de fin de este guardia y repetimos el proceso hasta llegar al fin del mes.
"""

def licenciar_guardias(mes_inicio, mes_fin, guardias):
    # guardias es una lista de tuplas: (id_guardia, dia_inicio, dia_fin)
    
    # 1. Ordenamos a los guardias por día de inicio. 
    # (En caso de empate, priorizamos al que termina más tarde)
    guardias.sort(key=lambda x: (x[1], -x[2]))
    
    seleccionados = []
    cobertura_actual = mes_inicio
    indice = 0
    n = len(guardias)
    
    while cobertura_actual < mes_fin:
        mejor_fin = cobertura_actual
        mejor_guardia = None
        
        # Evaluamos a todos los guardias que pueden empalmar sin dejar baches
        while indice < n and guardias[indice][1] <= cobertura_actual:
            if guardias[indice][2] > mejor_fin:
                mejor_fin = guardias[indice][2]
                mejor_guardia = guardias[indice]
            indice += 1
            
        # Si no encontramos a nadie que extienda la cobertura, hay un bache irresoluble.
        if mejor_guardia is None:
            return "Imposible: Hay un hueco en el mes que ningún guardia cubre."
            
        # Contratamos al guardia seleccionado
        seleccionados.append(mejor_guardia)
        cobertura_actual = mejor_fin
        
    return seleccionados


"""
2. ANÁLISIS DE COMPLEJIDAD

Sea N la cantidad total de guardias de seguridad en la plantilla.

Complejidad Temporal: O(N log N)
- Ordenar la lista inicial de N guardias por fecha de inicio toma O(N log N).
- En el ciclo `while` principal, el `indice` para recorrer la lista de guardias nunca retrocede. Cada guardia se evalúa exactamente una sola vez a lo largo de toda la ejecución del algoritmo. Por lo tanto, el proceso de selección toma O(N).
- La complejidad temporal queda dominada por el ordenamiento inicial: O(N log N).

Complejidad Espacial: O(N)
- En el peor de los casos (donde necesitamos a todos los guardias porque ninguno se superpone significativamente), la lista de `seleccionados` ocupará O(N).
- El algoritmo de ordenamiento interno de Python (Timsort) puede ocupar hasta O(N) de memoria adicional.
- Complejidad espacial total: O(N).


3. JUSTIFICACIÓN DE OPTIMALIDAD (Greedy Stays Ahead)

Para demostrar que este algoritmo minimiza la cantidad de guardias, utilizamos la técnica "El algoritmo goloso lleva la delantera" (Greedy Stays Ahead).

Supongamos que existe una solución óptima O, diferente a nuestra solución golosa G.
Ordenamos los guardias elegidos por ambas soluciones de manera cronológica:
G = {g1, g2, ..., gk}
O = {o1, o2, ..., om} (donde m <= k por ser supuestamente óptima).

Demostramos por inducción que en cada paso 'i', el algoritmo goloso cubre un intervalo igual o más extenso que el óptimo. Es decir: Fin(gi) >= Fin(oi).

- Caso base (i=1): Ambos algoritmos deben cubrir el inicio del mes. G elige, de todos los guardias que empiezan al inicio, aquel que termina más tarde. Por lo tanto, Fin(g1) >= Fin(o1). G lleva la delantera.
- Paso inductivo: Supongamos que en el paso 'i', G lleva la delantera: Fin(gi) >= Fin(oi). Para el paso 'i+1', O debe elegir un guardia o(i+1) que empiece antes o igual a Fin(oi) para no dejar baches. Como Fin(gi) >= Fin(oi), todas las opciones válidas para O en ese momento TAMBIÉN fueron opciones válidas para G. Al tener acceso al mismo o mayor pozo de candidatos, G toma al que termina más lejos. Por lo tanto, obligatoriamente Fin(g(i+1)) >= Fin(o(i+1)).

Conclusión:
En cada iteración, el algoritmo goloso abarca al menos tanto territorio como la solución óptima. Esto significa que G llegará al fin del mes (cubrirá el intervalo completo) en, a lo sumo, la misma cantidad de pasos (guardias) que O. Por lo tanto, k <= m. Como O es el óptimo absoluto, deducimos que k = m, demostrando que nuestra solución golosa es estrictamente óptima.
"""

# Bloque de prueba
if __name__ == "__main__":
    # mes_inicio, mes_fin (días 1 al 31)
    inicio = 1
    fin = 31
    
    # Formato: (Nombre, dia_empieza, dia_termina)
    lista_guardias = [
        ("Guardia_A", 1, 10),
        ("Guardia_B", 1, 5),
        ("Guardia_C", 8, 20),
        ("Guardia_D", 15, 25),
        ("Guardia_E", 19, 31),
        ("Guardia_F", 22, 28)
    ]
    
    resultado = licenciar_guardias(inicio, fin, lista_guardias)
    
    print("--- Ejercicio 12: Club de Campo (Turnos de Guardias) ---")
    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"Se necesitan {len(resultado)} guardias para cubrir el mes.")
        print("Guardias seleccionados para no ser licenciados:")
        for g in resultado:
            print(f"- {g[0]} (Cubre del día {g[1]} al {g[2]})")