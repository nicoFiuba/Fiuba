"""
TEORÍA DE ALGORITMOS - EJERCICIO 10: Fabricante de Perfumes (Mochila Fraccionaria con cotas)

1. ESTRATEGIA (Elección Golosa)
El problema busca minimizar el costo total de una mezcla de volumen fijo X, sujeta a restricciones de mínimo y máximo por ingrediente.

Estrategia greedy:
1. Asegurar la viabilidad: Agregamos a la fórmula la cantidad MÍNIMA de todos los ingredientes. Si esto supera X, es imposible.
2. Calculamos cuánto volumen nos falta llenar (Volumen_Restante = X - suma_minimos).
3. Calculamos cuánto "espacio extra" le queda a cada ingrediente (capacidad_extra = max - min).
4. Ordenamos los ingredientes de MENOR a MAYOR costo por mililitro.
5. Iteramos sobre la lista ordenada, agregando de cada ingrediente la cantidad máxima posible (el mínimo entre el Volumen_Restante y su capacidad_extra) hasta que el Volumen_Restante sea 0.
"""

def crear_perfume(X, ingredientes):
    # X: volumen final deseado
    # ingredientes: lista de tuplas (nombre, min_vol, max_vol, costo_ml)
    
    receta = {nombre: 0 for nombre, _, _, _ in ingredientes}
    volumen_actual = 0
    costo_total = 0
    
    # --- PASO 1: Cubrir las cantidades mínimas obligatorias ---
    for nombre, min_vol, max_vol, costo_ml in ingredientes:
        receta[nombre] = min_vol
        volumen_actual += min_vol
        costo_total += min_vol * costo_ml
        
    if volumen_actual > X:
        return "Imposible: Las cantidades mínimas superan el volumen X del frasco."
        
    volumen_restante = X - volumen_actual
    
    # --- PASO 2: Preparar y ordenar el volumen extra disponible ---
    # Guardamos tuplas de (costo_ml, capacidad_extra, nombre) para ordenar fácil
    ingredientes_extra = []
    for nombre, min_vol, max_vol, costo_ml in ingredientes:
        capacidad_extra = max_vol - min_vol
        if capacidad_extra > 0:
            ingredientes_extra.append((costo_ml, capacidad_extra, nombre))
            
    # Ordenamos de más barato a más caro
    ingredientes_extra.sort(key=lambda item: item[0])
    
    # --- PASO 3: Rellenar (Greedy) con lo más barato ---
    for costo_ml, capacidad_extra, nombre in ingredientes_extra:
        if volumen_restante == 0:
            break # Ya llenamos el frasco
            
        # Agregamos todo lo que podamos de este ingrediente barato
        agregar = min(volumen_restante, capacidad_extra)
        
        receta[nombre] += agregar
        volumen_restante -= agregar
        costo_total += agregar * costo_ml
        
    if volumen_restante > 0:
        return "Imposible: Aún usando las cantidades máximas de todo, no se llega al volumen X."
        
    return receta, costo_total


"""
2. ANÁLISIS DE COMPLEJIDAD

Sea N la cantidad de ingredientes disponibles.

Complejidad Temporal: O(N log N)
- El recorrido inicial para sumar los mínimos toma O(N).
- Calcular la capacidad extra y armar la nueva lista toma O(N).
- Ordenar la lista de capacidades extra por costo toma O(N log N).
- El ciclo Greedy para rellenar el frasco toma como máximo O(N).
- La complejidad queda dominada por el algoritmo de ordenamiento: O(N log N).

Complejidad Espacial: O(N)
- Se utiliza un diccionario `receta` para la salida que ocupa O(N).
- Se utiliza una lista auxiliar `ingredientes_extra` que en el peor caso ocupa O(N).
- Complejidad final: O(N).


3. JUSTIFICACIÓN DE OPTIMALIDAD (Argumento de Intercambio)

Supongamos por el absurdo que existe una solución óptima "O" distinta a la que genera nuestro algoritmo Greedy "G". Como ambas soluciones deben ser válidas, ambas cumplen con las cuotas mínimas y máximas, y ambas suman exactamente un volumen total X.

Al ser distintas, debe existir necesariamente un volumen "v" que en "O" está ocupado por un ingrediente A, mientras que en "G" ese mismo volumen "v" está ocupado por un ingrediente B. Por cómo funciona nuestro algoritmo, G siempre elige llenar el espacio con el ingrediente más barato disponible que aún no haya alcanzado su cota máxima. Si G eligió B en lugar de A, es estrictamente porque el Costo(B) < Costo(A).

Si en la solución óptima "O" reemplazamos un volumen "v" del ingrediente A por un volumen "v" del ingrediente B, el volumen total sigue siendo X y las restricciones de capacidad se siguen respetando (porque sabíamos que G pudo meter B ahí sin pasarse del máximo).  Sin embargo, el costo total de esta nueva mezcla será menor, ya que Costo(B) < Costo(A). 

Esto contradice la suposición inicial de que "O" era la solución de costo mínimo. 
Por lo tanto, la estrategia de seleccionar siempre el elemento más barato (Fractional Knapsack) es estrictamente óptima.
"""

# Bloque de prueba
if __name__ == "__main__":
    volumen_frasco = 100
    
    # (Nombre, min_ml, max_ml, costo_por_ml)
    # Total de mínimos = 10 + 5 + 0 + 20 = 35ml. Faltan 65ml.
    lista_ingredientes = [
        ("Esencia de Rosas", 10, 30, 50), # Caro
        ("Alcohol", 5, 80, 2),            # Muy barato
        ("Fijador", 0, 10, 15),           # Medio
        ("Agua Destilada", 20, 100, 0.5)  # Regalado
    ]
    
    resultado = crear_perfume(volumen_frasco, lista_ingredientes)
    
    print("--- Ejercicio 10: Fabricante de Perfumes ---")
    if isinstance(resultado, str):
        print(resultado)
    else:
        receta_final, costo = resultado
        print(f"Volumen objetivo: {volumen_frasco} ml")
        print("Receta óptima:")
        for ing, cant in receta_final.items():
            print(f"- {ing}: {cant} ml")
        print(f"\nCosto total minimizado: ${costo}")