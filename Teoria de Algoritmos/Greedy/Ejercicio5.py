"""
TEORÍA DE ALGORITMOS - EJERCICIO 5: Ironman (Triatlón)

1. ESTRATEGIA (Elección Golosa)
El problema radica en que el nado es por regulación un recurso compartido y exclusivo 
(secuencial) , mientras que el ciclismo y la carrera a pie se pueden hacer en 
simultáneo. Para minimizar el tiempo total, debemos mandar al agua primero 
a los competidores que más tiempo van a tardar en las etapas posteriores (bici + carrera). 
De esta forma, mientras ellos hacen sus etapas largas en paralelo, el lago se 
libera para que los demás vayan nadando.

Estrategia greedy:
1. Para cada participante, sumamos el tiempo estimado de ciclismo y carrera a pie (Tiempo_Restante = bici + carrera).
2. Ordenamos a los participantes de MAYOR a MENOR según su Tiempo_Restante.
3. Ese será el orden exacto de salida al lago.
"""

def planificar_ironman(participantes):
    # participantes es una lista de tuplas: (id_corredor, t_nado, t_bici, t_carrera)
    
    # 1. Calculamos el tiempo restante (bici + carrera) y ordenamos de mayor a menor.
    # Usamos reverse=True para que el orden sea descendente.
    orden_salida = sorted(participantes, key=lambda x: x[2] + x[3], reverse=True)
    
    # Opcional pero recomendado: Calcular el tiempo total de la competencia 
    # para demostrar que funciona
    tiempo_actual_lago = 0
    tiempo_total_competencia = 0
    
    for participante in orden_salida:
        id_corredor, t_nado, t_bici, t_carrera = participante
        
        # El corredor entra al lago cuando el anterior sale (acumulativo)
        tiempo_actual_lago += t_nado 
        
        # El corredor termina su carrera en el momento que salió del lago + lo que tarda en tierra
        tiempo_fin_corredor = tiempo_actual_lago + t_bici + t_carrera
        
        # El tiempo total del evento es el máximo entre el fin del corredor actual y el máximo anterior
        if tiempo_fin_corredor > tiempo_total_competencia:
            tiempo_total_competencia = tiempo_fin_corredor
            
    return orden_salida, tiempo_total_competencia

"""
2. ANÁLISIS DE COMPLEJIDAD

Sea N la cantidad de inscriptos en el triatlón.

Complejidad Temporal: O(N log N)
- Calcular el tiempo de (bici + carrera) para cada participante toma O(N).
- Ordenar la lista de N participantes según este valor de mayor a menor toma O(N log N).
- Iterar el arreglo para calcular el tiempo total toma O(N).
- La complejidad temporal total queda dominada por el ordenamiento: O(N log N).

Complejidad Espacial: O(N)
- Se necesita espacio para almacenar la lista original y/o la lista ordenada de N participantes.
- El algoritmo de ordenamiento de Python (Timsort) puede tomar hasta O(N) de espacio auxiliar.
- Complejidad espacial total: O(N).


3. JUSTIFICACIÓN DE OPTIMALIDAD (Argumento de Intercambio)

Para demostrar que esta estrategia minimiza el tiempo total, usamos un Argumento de Intercambio.

Supongamos por el absurdo que existe un orden óptimo global "O" diferente al de nuestro algoritmo. 
Como "O" es diferente y no está ordenado estrictamente de mayor a menor según el tiempo en tierra 
(bici + carrera), debe existir obligatoriamente en "O" un par de competidores adyacentes 
donde el corredor A sale justo antes que el corredor B, pero el tiempo en tierra de A es 
ESTRICTAMENTE MENOR al de B (T_A < T_B).

Llamemos "t" al momento exacto en que el corredor A entra al lago.
En este escenario (A seguido de B):
- A termina toda su carrera en el instante: t + Nado_A + T_A
- B termina toda su carrera en el instante: t + Nado_A + Nado_B + T_B
El momento en que la competencia termina para ellos dos es el máximo entre esos valores. 
Como T_B > T_A y los tiempos de nado son positivos, el tiempo máximo es claramente el de B: 
(t + Nado_A + Nado_B + T_B).

Ahora, proponemos INTERCAMBIAR el orden de este par adyacente para que B salga antes que A.
En este nuevo escenario (B seguido de A):
- B termina en: t + Nado_B + T_B
- A termina en: t + Nado_B + Nado_A + T_A

Comparemos el nuevo máximo con el máximo anterior (t + Nado_A + Nado_B + T_B):
1. El nuevo tiempo de B (t + Nado_B + T_B) es menor al máximo anterior (porque no incluye Nado_A).
2. El nuevo tiempo de A (t + Nado_B + Nado_A + T_A) también es menor al máximo anterior, porque sabemos por hipótesis que T_A < T_B.

Conclusión del intercambio:
Al intercambiar A y B para que respeten nuestro orden (el de mayor tiempo en tierra va primero), 
el tiempo máximo en el que este par termina la carrera DISMINUYE (o en el peor de los casos 
se mantiene igual). Además, este cambio local no afecta el inicio de los competidores que salieron 
antes, ni retrasa la liberación del lago para los competidores que salen después.
Esto contradice la suposición de que el orden "O" original (desordenado) era el óptimo. 
Repitiendo estos intercambios de a pares, llegaremos inevitablemente al orden propuesto por 
nuestro algoritmo Greedy, demostrando que produce el tiempo total mínimo posible.
"""

if __name__ == "__main__":
    # Formato: (Nombre, t_nado, t_bici, t_carrera)
    participantes_prueba = [
        ("Juan", 20, 120, 40),   # Restante (bici+pie) = 160
        ("Maria", 15, 140, 45),  # Restante (bici+pie) = 185
        ("Pedro", 25, 100, 30),  # Restante (bici+pie) = 130
    ]
    
    orden, tiempo_total = planificar_ironman(participantes_prueba)
    
    print("--- Ejercicio 5: Ironman ---")
    print("Orden de salida óptimo:")
    for participante in orden:
        print(f"- {participante[0]} (Tiempo restante post-lago: {participante[2]+participante[3]} min)")
    print(f"\nTiempo total de la competencia: {tiempo_total} minutos")