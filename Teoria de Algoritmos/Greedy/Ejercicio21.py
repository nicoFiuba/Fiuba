"""
TEORÍA DE ALGORITMOS - EJERCICIO 21: Servidor de Videojuegos (Interval Scheduling Circular)

1. ESTRATEGIA (Elección Golosa)
El problema busca maximizar la cantidad de intervalos seleccionados sin superposición. Si fuera un problema lineal, la estrategia greedy óptima es seleccionar siempre el intervalo con la fecha de FINALIZACIÓN más temprana.

Como el tiempo es semanal y circular (un contrato puede cruzar el límite del fin de semana), aplicamos una reducción:
1. Iteramos sobre cada contrato C asumiendo que pertenece a la solución óptima.
2. Al fijar el contrato C, el tiempo restante del servidor se convierte en una línea recta continua de (168 - duración_C) horas.
3. Filtramos los demás contratos que entran en ese hueco y les aplicamos la estrategia Greedy estándar (ordenar por hora de fin y seleccionar el que termine antes).
4. Nos quedamos con la iteración que haya logrado emparejar la mayor cantidad de contratos.
"""

def maximizar_contratos_servidor(contratos):
    # contratos: lista de tuplas (id, inicio, fin) medidas en horas de la semana (0 a 168)
    
    # 1. Normalizar: Si el fin es menor al inicio, significa que cruza el fin de semana.
    # Le sumamos 168 horas (1 semana) para tratarlo fácilmente.
    contratos_norm = []
    for id_c, ini, fin in contratos:
        if fin <= ini:
            fin += 168
        contratos_norm.append((id_c, ini, fin))
        
    max_contratos_global = []
    
    # 2. Desenrollar el círculo forzando cada contrato como punto de partida
    for contrato_base in contratos_norm:
        id_base, ini_base, fin_base = contrato_base
        seleccionados = [id_base]
        
        # Proyectar el resto de la semana como una línea recta desde fin_base
        candidatos = []
        for id_c, ini, fin in contratos_norm:
            if id_c == id_base: 
                continue
                
            # Si el contrato está "antes" en el reloj, lo empujamos a la semana siguiente
            if ini < fin_base:
                ini += 168
                fin += 168
                
            # Si entra perfectamente en el tiempo libre antes de que el contrato base 
            # vuelva a empezar la semana que viene, es un candidato válido.
            if ini >= fin_base and fin <= ini_base + 168:
                candidatos.append((id_c, ini, fin))
                
        # 3. Estrategia Greedy Lineal: Ordenar por finalización más temprana
        candidatos.sort(key=lambda x: x[2])
        
        ultimo_fin = fin_base
        for c in candidatos:
            id_c, ini, fin = c
            if ini >= ultimo_fin: # No se superpone
                seleccionados.append(id_c)
                ultimo_fin = fin
                
        # 4. Guardamos el mejor escenario
        if len(seleccionados) > len(max_contratos_global):
            max_contratos_global = seleccionados
            
    return max_contratos_global

"""
2. ANÁLISIS DE COMPLEJIDAD

Sea N la cantidad de contratos solicitados.

Complejidad Temporal: O(N^2 log N)
- El bucle exterior se ejecuta N veces (una por cada contrato base).
- Dentro del bucle:
Filtrar y normalizar candidatos toma O(N).
Ordenar los candidatos toma O(N log N).
El barrido greedy lineal toma O(N).
- Como hacemos un O(N log N) iterado N veces, la complejidad final es O(N^2 log N).
(Nota: Existen algoritmos más complejos teóricos de O(N log N) para la variante circular, pero O(N^2 log N) es altamente eficiente para N razonables y mantiene la claridad de la justificación Greedy).

Complejidad Espacial: O(N)
- La lista de contratos normalizados, los candidatos de cada iteración y el resultado final ocupan memoria proporcional a N.


3. JUSTIFICACIÓN DE OPTIMALIDAD (Greedy Stays Ahead + Exhaustividad)

Para el problema clásico de Selección de Actividades (tiempo lineal), la estrategia de elegir el intervalo que finaliza más temprano es estrictamente óptima. Demostración rápida por intercambio: Si la solución óptima 'O' elige un primer contrato que termina más tarde que nuestro contrato greedy 'G', podemos cambiar el de 'O' por 'G' sin generar conflictos con los contratos futuros de 'O' (porque G termina antes y deja 
más espacio libre). El tamaño de la solución no se reduce.

El problema que introduce el Servidor de Videojuegos es que el tiempo es Circular. Cualquier solución óptima en un círculo debe obligatoriamente contener al menos un intervalo 'X'. Si "cortamos" el círculo al final del intervalo 'X', el problema se reduce a un problema de tiempo lineal donde ya sabemos que el enfoque Greedy funciona a la perfección.

Como nuestro algoritmo itera sobre TODOS los contratos N obligando a cada uno a ser ese intervalo 'X' que rompe el círculo, estamos garantizando exhaustivamente que, en alguna de esas iteraciones, habremos adivinado al menos un contrato que pertenece a la solución óptima real. A partir de ese punto correcto, la subrutina Greedy lineal construye el resto de la respuesta óptima infaliblemente.
"""

# Bloque de prueba
if __name__ == "__main__":
    # Formato: ("ID", hora_inicio_semana, hora_fin_semana)
    # Lunes 00:00 es la hora 0. Domingo 23:59 es la hora 167.
    ofertas = [
        ("A", 10, 20),
        ("B", 15, 30),
        ("C", 25, 40),
        ("D", 160, 5),   # ¡Cruza el fin de semana! (De domingo a lunes)
        ("E", 2, 12)
    ]
    
    resultado = maximizar_contratos_servidor(ofertas)
    
    print("--- Ejercicio 21: Servidor de Videojuegos ---")
    print(f"Cantidad máxima de contratos aceptados: {len(resultado)}")
    print(f"Contratos elegidos: {resultado}")