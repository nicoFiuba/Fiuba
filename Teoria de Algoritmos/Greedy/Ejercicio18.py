"""
TEORÍA DE ALGORITMOS - EJERCICIO 18: Evento Multideportivo (Partición de Intervalos)

1. ESTRATEGIA (Elección Golosa)
El problema busca agrupar un conjunto de intervalos (eventos) en la menor cantidad posible de subconjuntos (médicos), de forma tal que ningún subconjunto contenga intervalos superpuestos.

Estrategia greedy:
1. Ordenamos los eventos cronológicamente según su HORA DE INICIO.
2. Utilizamos una Cola de Prioridad (Min-Heap) para llevar el registro de las horas de finalización (cuándo se libera) de cada médico activo.
3. Por cada evento, verificamos el Min-Heap para ver si el médico que se libera más temprano ya está disponible (su hora de liberación es <= a la hora de inicio del evento actual).
4. Si está disponible, lo asignamos a este evento y actualizamos su hora de liberación en el Heap. Si no está disponible (hay superposición), creamos un nuevo médico.
"""

import heapq

def asignar_medicos(eventos):
    # eventos: lista de tuplas (nombre_disciplina, inicio, fin)
    
    # 1. Ordenamos por hora de inicio
    eventos.sort(key=lambda x: x[1])
    
    # Min-Heap para guardar tuplas: (hora_que_se_libera, id_medico)
    medicos_activos = []
    cronograma = []
    total_medicos = 0
    
    # 2. Proceso Greedy
    for nombre, inicio, fin in eventos:
        # Verificamos si el médico que se libera más temprano ya está libre
        if medicos_activos and medicos_activos[0][0] <= inicio:
            # ¡Decisión Golosa! Lo reutilizamos
            hora_libre, id_medico = heapq.heappop(medicos_activos)
            cronograma.append((nombre, id_medico, inicio, fin))
            # Vuelve al Heap con su nueva hora de liberación
            heapq.heappush(medicos_activos, (fin, id_medico))
        else:
            # No hay nadie libre, contratamos a uno nuevo
            total_medicos += 1
            id_medico = f"Médico {total_medicos}"
            cronograma.append((nombre, id_medico, inicio, fin))
            heapq.heappush(medicos_activos, (fin, id_medico))
            
    return total_medicos, cronograma

"""
2. ANÁLISIS DE COMPLEJIDAD

Sea N la cantidad de eventos deportivos.

Complejidad Temporal: O(N log N)
- Ordenar los eventos por hora de inicio toma O(N log N).
- Iterar sobre la lista de eventos toma O(N).
- En cada iteración, podemos hacer operaciones de extración e inserción en el Min-Heap. El Heap tendrá como máximo tamaño N (si todos los eventos se superponen). Las operaciones del Heap toman O(log N).
- Por lo tanto, el ciclo completo toma O(N log N).
- Complejidad total: O(N log N).

Complejidad Espacial: O(N)
- El Min-Heap guarda, en el peor de los casos, un registro por cada evento si es que todos se superponen simultáneamente: O(N).
- El arreglo para el cronograma final también ocupa O(N).
- Complejidad total: O(N).


3. JUSTIFICACIÓN DE OPTIMALIDAD (Argumento de Profundidad)

Definimos la "profundidad" de un conjunto de intervalos como la cantidad máxima de intervalos que se superponen en un mismo instante de tiempo 't'. Llamemos a esta profundidad máxima 'D'.

Por lógica fundamental, si en un momento exacto del día hay 'D' eventos transcurriendo en simultáneo, es FÍSICAMENTE IMPOSIBLE cubrirlos con menos de 'D' médicos. Un médico no puede estar en dos lugares a la vez. 
Por lo tanto, cualquier solución válida (incluida la óptima absoluta) requerirá como mínimo 'D' recursos. Esto establece nuestra cota inferior: Optimo >= D.

Ahora analizamos nuestro algoritmo Greedy. Supongamos que el algoritmo decide contratar a un nuevo médico (llegando a un total de 'k' médicos) al procesar el evento 'E'. Por cómo funciona nuestra regla de reutilización, si el algoritmo no pudo reutilizar a ninguno de los (k-1) médicos anteriores, significa que TODOS ellos terminan sus turnos DESPUÉS de que 'E' comience.

Como los eventos se procesaron ordenados por fecha de inicio, todos esos (k-1) eventos empezaron antes o al mismo tiempo que 'E'. Esto significa que en el instante exacto en que comienza el evento 'E', existen 
'k' eventos (los k-1 anteriores + el propio E) ocurriendo simultáneamente. 

Hemos encontrado un instante en el tiempo con una superposición de 'k' intervalos. Por lo tanto, la profundidad del sistema en ese instante es 'k'. Como demostramos que la cantidad de médicos que usa el algoritmo ('k') es exactamente igual a la profundidad máxima de superposición que encontró ('D'), y sabemos que ninguna solución puede usar menos recursos que la profundidad máxima, queda demostrado que el algoritmo Greedy es estrictamente óptimo (Usa exactamente D médicos).
"""

# Bloque de prueba
if __name__ == "__main__":
    # Formato: (Disciplina, hora_inicio, hora_fin)
    juegos_olimpicos = [
        ("Natación", 8, 11),
        ("Gimnasia", 9, 12),
        ("Atletismo", 10, 14),
        ("Ciclismo", 11, 13), # Puede usar al médico de Natación
        ("Boxeo", 13, 16),    # Puede usar al médico de Gimnasia o Ciclismo
        ("Esgrima", 14, 17)   # Puede usar al médico de Atletismo
    ]
    
    cant_medicos, turnos = asignar_medicos(juegos_olimpicos)
    
    print("--- Ejercicio 18: Médicos del Evento Multideportivo ---")
    print(f"Médicos totales requeridos: {cant_medicos}\n")
    
    print("Asignación de turnos (Ordenados por Disciplina):")
    # Ordenamos la salida por médico para que sea más fácil de leer
    turnos.sort(key=lambda x: x[1])
    for disciplina, medico, inicio, fin in turnos:
        print(f" - {medico}: {disciplina} (De {inicio}hs a {fin}hs)")