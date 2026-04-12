"""
TEORÍA DE ALGORITMOS - EJERCICIO 14: Comité de Supervisión (Piercing Intervals)

1. ESTRATEGIA (Elección Golosa)
El objetivo es encontrar un subconjunto mínimo de ayudantes (el comité) tal que cada ayudante del laboratorio comparta al menos un momento de su turno con un miembro del comité.

Estrategia greedy:
1. Identificamos al ayudante que termine su turno MÁS TEMPRANO y que aún no haya sido "cubierto" por el comité. Llamemos a su fin de turno `E_min`.
2. Para cubrir a este ayudante, necesitamos a un supervisor cuyo turno se superponga. Es decir, alguien que empiece antes o igual a `E_min`.
3. De todos los candidatos que cumplen esta condición, tomamos la decisión localmente óptima: elegimos al que termine su turno LO MÁS TARDE POSIBLE.
4. Agregamos este candidato al comité.
5. Marcamos como "cubiertos" a todos los ayudantes que se superponen con este nuevo supervisor, y repetimos el proceso con los restantes.
"""

def diseñar_comite(ayudantes):
    # ayudantes: lista de tuplas (id, inicio, fin)
    
    no_cubiertos = set(a[0] for a in ayudantes)
    comite = []
    
    while no_cubiertos:
        # 1. Buscar al ayudante no cubierto que termina primero
        faltantes = [a for a in ayudantes if a[0] in no_cubiertos]
        primero_en_irse = min(faltantes, key=lambda x: x[2])
        e_min = primero_en_irse[2]
        
        # 2. Buscar a todos los candidatos que se superponen con 'primero_en_irse'
        # Un candidato se superpone si empieza antes o igual a e_min, y termina 
        # después o igual a la hora de inicio de 'primero_en_irse'.
        candidatos = [a for a in ayudantes if a[1] <= e_min and a[2] >= primero_en_irse[1]]
        
        # 3. Elección Greedy: Elegir al candidato que termina más tarde
        mejor_supervisor = max(candidatos, key=lambda x: x[2])
        comite.append(mejor_supervisor)
        
        # 4. Marcar como cubiertos a todos los que se cruzan con el mejor_supervisor
        # Dos intervalos se cruzan si: max(inicio1, inicio2) <= min(fin1, fin2)
        for a in ayudantes:
            if a[0] in no_cubiertos:
                inicio_interseccion = max(a[1], mejor_supervisor[1])
                fin_interseccion = min(a[2], mejor_supervisor[2])
                
                if inicio_interseccion <= fin_interseccion:
                    no_cubiertos.remove(a[0])
                    
    return comite


"""
2. ANÁLISIS DE COMPLEJIDAD

Sea N la cantidad de ayudantes totales.

Complejidad Temporal: O(N^2)
- El bucle `while` se ejecuta a lo sumo N veces (en el peor caso, agregamos a un ayudante al comité por iteración).
- Dentro del bucle, las operaciones `min()`, `max()`, la creación de listas por comprensión y el `for` de marcado recorren la lista de tamaño N. Todas toman O(N).
- Por lo tanto, buscar el mejor candidato y marcar a los cubiertos nos toma O(N) en cada una de las (a lo sumo) N iteraciones.
- Complejidad total: O(N^2). 
(Nota: Se podría optimizar a O(N log N) pre-ordenando los intervalos, pero O(N^2) es perfectamente eficiente y aceptable para la justificación del algoritmo).

Complejidad Espacial: O(N)
- Se utiliza un Set `no_cubiertos` de tamaño N, y arreglos auxiliares que a lo sumo tienen tamaño N.


3. JUSTIFICACIÓN DE OPTIMALIDAD (Argumento de Intercambio)

Supongamos por el absurdo que existe una solución óptima "O" que es mejor (más chica) o diferente a nuestra solución Greedy "G".

En la primera iteración, nuestro algoritmo identifica al ayudante 'A' que termina más temprano. Para cubrir a 'A', cualquier solución válida (incluida la óptima 'O') DEBE seleccionar a algún supervisor 'S_opt' que se cruce con 'A'. Nuestro algoritmo Greedy selecciona a un supervisor 'S_greedy' que también se cruza con 'A', pero que fue elegido específicamente porque es el que termina más tarde de todos los posibles.

Por lo tanto, la fecha de fin de 'S_greedy' es mayor o igual a la de 'S_opt'. Esto implica que 'S_greedy' abarca TODO el período de tiempo futuro que abarca 'S_opt', y posiblemente más. Todos los ayudantes que eran cubiertos por 'S_opt' seguirán estando cubiertos si lo reemplazamos por 'S_greedy'.

Si en la solución óptima "O" intercambiamos a 'S_opt' por nuestro 'S_greedy', la solución sigue siendo 100% válida y el tamaño del comité no aumenta. Aplicando este mismo argumento inductivamente en cada paso, demostramos que nuestra solución Greedy es paso a paso igual o superior a cualquier otra decisión, garantizando el tamaño mínimo global.
"""

# Bloque de prueba
if __name__ == "__main__":
    # Formato: (id_ayudante, inicio, fin) usando horas enteras
    lista_ayudantes = [
        ("Ayudante 1", 16, 20),
        ("Ayudante 2", 18, 22),
        ("Ayudante 3", 21, 23)
    ]
    
    resultado = diseñar_comite(lista_ayudantes)
    
    print("--- Ejercicio 14: Comité de Supervisión ---")
    print("Ayudantes totales:")
    for a in lista_ayudantes:
        print(f" - {a[0]}: {a[1]}hs a {a[2]}hs")
        
    print("\nComité seleccionado:")
    for c in resultado:
        print(f" -> {c[0]}")