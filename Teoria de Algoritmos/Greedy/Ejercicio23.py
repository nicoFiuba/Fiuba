"""
TEORÍA DE ALGORITMOS - EJERCICIO 23: Impresora Central (Minimizar Lateness + Gaps)

1. ESTRATEGIA (Elección Golosa)
El problema exige minimizar el apercibimiento (el retraso máximo del mes) y, simultáneamente, espaciar los trabajos para darle descanso a la máquina.

Estrategia greedy:
1. Fase Forward (Earliest Deadline First): Ordenamos los documentos por fecha de entrega de menor a mayor. Simulamos una ejecución continua (sin descansos) para descubrir cuál es el Retraso Máximo (L_max) estrictamente inevitable.
2. Fase Backward (Patear para adelante): Recorremos la lista desde el último trabajo hasta el primero. Programamos cada trabajo para que termine en su (fecha_entrega + L_max), limitándolo únicamente si choca con el inicio del trabajo siguiente. Esto compacta los trabajos hacia el futuro y maximiza los "huecos" de descanso en el presente.
"""

def planificar_impresiones(documentos):
    # documentos: lista de tuplas ("ID_Doc", duracion, fecha_entrega)
    
    # 1. Ordenamos por Fecha de Entrega más temprana (EDF)
    documentos.sort(key=lambda x: x[2])
    
    # 2. Fase Forward: Descubrir el Retraso Máximo (L_max) inevitable
    tiempo_actual = 0
    lateness_maximo = 0
    
    for id_doc, duracion, entrega in documentos:
        tiempo_actual += duracion
        retraso = max(0, tiempo_actual - entrega)
        if retraso > lateness_maximo:
            lateness_maximo = retraso
            
    # 3. Fase Backward: Programar lo más tarde posible para dejar descansos
    n = len(documentos)
    cronograma = [None] * n
    
    # El trabajo no puede pisar al que le sigue. Para el último, no hay límite.
    limite_superior = float('inf')
    
    for i in range(n - 1, -1, -1):
        id_doc, duracion, entrega = documentos[i]
        
        # El trabajo termina en su límite tolerado O cuando empieza el siguiente
        fin_ideal = entrega + lateness_maximo
        hora_fin = min(fin_ideal, limite_superior)
        hora_inicio = hora_fin - duracion
        
        cronograma[i] = (id_doc, hora_inicio, hora_fin)
        
        # Actualizamos el límite para el trabajo anterior
        limite_superior = hora_inicio
        
    return lateness_maximo, cronograma

"""
2. ANÁLISIS DE COMPLEJIDAD

Sea N la cantidad de documentos a imprimir.

Complejidad Temporal: O(N log N)
- El ordenamiento inicial por fecha de entrega (Timsort) toma O(N log N).
- La simulación Forward para encontrar el L_max recorre la lista una vez: O(N).
- La fase Backward para asignar los horarios recorre la lista una vez: O(N).
- La complejidad temporal queda dominada por el ordenamiento: O(N log N).

Complejidad Espacial: O(N)
- Crear la lista final del `cronograma` requiere almacenar N tuplas.
- Complejidad total: O(N).


3. JUSTIFICACIÓN DE OPTIMALIDAD (Argumento de Intercambio / Inversiones)

Para demostrar que la estrategia Earliest Deadline First (EDF) minimiza el retraso máximo absoluto, utilizamos el argumento de intercambio.

Supongamos por el absurdo que existe un orden óptimo 'O' que minimiza el retraso máximo, pero que NO está ordenado por fecha de entrega. 
Si no está ordenado por fecha de entrega, obligatoriamente debe existir en 'O' al menos un par de trabajos adyacentes invertidos. Es decir, un Trabajo A que se imprime inmediatamente antes que un Trabajo B, pero donde la entrega de A vence DESPUÉS que la de B (Entrega_A > Entrega_B).

Llamemos T al momento en el que la impresora empieza el Trabajo A. 
En la solución 'O', el Trabajo B termina en T + Duracion_A + Duracion_B. 
Su retraso es: Retraso_B = (T + Duracion_A + Duracion_B) - Entrega_B.

Si proponemos hacer un intercambio (swap) y ejecutamos B antes que A:
- El nuevo tiempo en que termina A será exactamente el mismo en el que antes terminaba B. Pero como Entrega_A > Entrega_B, el retraso que sufra A en este nuevo puesto será ESTRICTAMENTE MENOR al retraso que sufría B en el orden original.
- El Trabajo B ahora termina más temprano, por lo que su propio retraso disminuye.
- Todos los demás trabajos de la cola no se ven afectados porque la suma de las duraciones de A+B sigue ocupando el mismo bloque de tiempo total.

Al realizar el intercambio, el retraso máximo del par de trabajos disminuye (o en el peor de los casos, se mantiene igual, nunca empeora). Podemos repetir estos intercambios sucesivos deshaciendo todas las "inversiones" hasta llegar al ordenamiento perfecto por fecha de entrega (EDF). Como en ningún paso de la transformación empeoró el retraso máximo, queda demostrado matemáticamente que ordenar de menor a mayor fecha de entrega genera el retraso máximo mínimo posible.

(Nota: La fase backward simplemente ajusta los tiempos de inicio sin alterar el orden relativo ni exceder el retraso máximo garantizado, siendo óptima para generar los espacios de inactividad).
"""

# Bloque de prueba
if __name__ == "__main__":
    # Formato: ("ID_Documento", duracion_horas, limite_entrega_hora)
    impresiones = [
        ("Doc_Finanzas", 3, 5),   # Urgente, debe estar en la hora 5
        ("Doc_Legales", 4, 14),
        ("Doc_Marketing", 2, 8)
    ]
    
    max_retraso, agenda = planificar_impresiones(impresiones)
    
    print("--- Ejercicio 23: Impresora Central ---")
    print(f"Retraso Máximo del mes (Inevitable): {max_retraso} horas")
    print("\nCronograma óptimo con descansos para la impresora:")
    
    for doc, inicio, fin in agenda:
        print(f" - Empezar '{doc}' en hora {inicio}. Termina en hora {fin}")