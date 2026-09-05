"""
TEORÍA DE ALGORITMOS - EJERCICIO 1

EXPLICACIÓN: la estrategia consiste en ordenar los pueblos de menor a mayor según su kilómetro. Nos paramos en el primer pueblo sin cobertura y le sumamos 50 km para determinar el alcance máximo. Luego, buscamos el último pueblo cuya ubicación sea menor o igual a ese límite y colocamos la patrulla allí. Esta estrategia es Greedy porque en cada iteración opta por estirar lo máximo posible la cobertura, realizando una elección que es localmente óptima, factible (cumple con las restricciones del problema) e irrevocable (una vez tomada no permite ser removida en posteriores elecciones del algoritmo).

PSEUDOCÓDIGO
"""