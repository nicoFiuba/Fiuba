"""
TEORÍA DE ALGORITMOS - EJERCICIO 22: La Fotocopiadora (Minimizar tiempo ponderado)

1. ESTRATEGIA (Elección Golosa)
El problema requiere minimizar la sumatoria de w_i * C_i, donde C_i es el tiempo en que termina el pedido i, y w_i es el peso/importancia del cliente.

Estrategia greedy:
1. Para cada pedido, calculamos su prioridad mediante el ratio: Importancia / Tiempo (w_i / t_i).
2. Ordenamos todos los pedidos de MAYOR a MENOR ratio.
3. Ejecutamos los pedidos secuencialmente siguiendo ese estricto orden.
"""

def planificar_fotocopiadora(pedidos):
    # pedidos: lista de tuplas ("Cliente", t_i, w_i)
    
    # 1. Ordenamos por el ratio (w_i / t_i) de forma descendente.
    # En caso de empate en el ratio, el orden entre ellos no afecta la suma final.
    pedidos.sort(key=lambda x: x[2] / x[1], reverse=True)
    
    tiempo_actual = 0
    costo_total_ponderado = 0
    cronograma = []
    
    # 2. Ejecutamos en orden
    for cliente, t_i, w_i in pedidos:
        # El tiempo de finalización de este pedido es el tiempo acumulado hasta ahora + su propio tiempo
        tiempo_actual += t_i 
        
        # C_i = tiempo_actual. Lo multiplicamos por el peso del cliente
        costo_total_ponderado += w_i * tiempo_actual
        
        cronograma.append((cliente, tiempo_actual)) # (Quien, Hora que se va con sus copias)
        
    return costo_total_ponderado, cronograma

"""
2. ANÁLISIS DE COMPLEJIDAD

Sea N la cantidad total de pedidos en la mañana.

Complejidad Temporal: O(N log N)
- Calcular el ratio se hace en el momento del ordenamiento.
- El algoritmo de ordenamiento interno (Timsort en Python) toma O(N log N).
- Recorrer la lista una vez ordenada para calcular el costo total toma O(N).
- La complejidad temporal queda dominada por el ordenamiento: O(N log N).

Complejidad Espacial: O(N)
- Guardar la lista de pedidos y generar la lista del cronograma final ocupa memoria directamente proporcional a la cantidad de pedidos: O(N).


3. JUSTIFICACIÓN DE OPTIMALIDAD (Argumento de Intercambio de Adyacentes)

Supongamos por el absurdo que existe un orden óptimo 'O' que es distinto al orden Greedy 'G' (el cual está ordenado estrictamente de mayor a menor ratio). Como están ordenados distinto, en la solución óptima 'O' debe existir obligatoriamente un par de trabajos adyacentes "i" y "j" (donde "i" se ejecuta inmediatamente antes que "j") que estén "invertidos" respecto a nuestra regla. Es decir: (w_i / t_i) < (w_j / t_j). Lo que es matemáticamente equivalente a decir que: w_i * t_j < w_j * t_i.

Llamemos T al tiempo en el que empieza a ejecutarse la tarea "i". En la solución 'O', el costo aportado por este par es:
Costo_O = w_i * (T + t_i) + w_j * (T + t_i + t_j)

Si proponemos hacer un intercambio (swap) e invertir el orden, ejecutando "j" antes que "i", las tareas anteriores no se ven afectadas y las posteriores tampoco (ya que la suma t_i + t_j es idéntica independientemente del orden de estos dos). El nuevo costo del par intercambiado será:
Costo_Swap = w_j * (T + t_j) + w_i * (T + t_j + t_i)

Para ver cuál es mejor, restamos (Costo_Swap - Costo_O).  Luego de distribuir y cancelar términos iguales (como w_i*T, w_i*t_i, w_j*T, w_j*t_j), la diferencia se simplifica a:
Diferencia = w_i * t_j - w_j * t_i

Por la condición de que estaban "invertidos" (w_i * t_j < w_j * t_i), sabemos con certeza que esta Diferencia es un número NEGATIVO. Al ser la diferencia negativa, significa que Costo_Swap es ESTRICTAMENTE MENOR que Costo_O.

Esto contradice la suposición inicial de que 'O' era la solución óptima. Hemos demostrado que cualquier par que no cumpla la regla Greedy puede ser invertido para mejorar el resultado. Por lo tanto, ordenar de mayor a menor ratio es la solución absolutamente óptima.
"""

# Bloque de prueba
if __name__ == "__main__":
    # Formato: ("ID_Cliente", duracion_t, importancia_w)
    # Ejemplo: Cliente B tiene mucha urgencia/importancia (w=100) pero tarda poco (t=2)
    trabajos_del_dia = [
        ("Cliente A", 5, 10),
        ("Cliente B", 2, 100),
        ("Cliente C", 10, 50),
        ("Cliente D", 1, 1)
    ]
    
    costo_minimo, agenda = planificar_fotocopiadora(trabajos_del_dia)
    
    print("--- Ejercicio 22: Fotocopiadora ---")
    print(f"Demora total ponderada (minimizada): {costo_minimo}")
    print("Orden óptimo de entrega:")
    for cli, hora_fin in agenda:
        print(f" - {cli} (Termina en T={hora_fin})")