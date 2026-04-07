"""
TEORÍA DE ALGORITMOS - EJERCICIO 6: Club de Vinos (Asignación de Recursos)

1. ESTRATEGIA (Elección Golosa)
El problema se resuelve asignando primero los recursos a los elementos más restrictivos,
y priorizando el consumo de los recursos menos flexibles.

Orden de prioridad de asignación:
1. Socios Titanio: Solo aceptan Alfa. Se les asigna Alfa. Si faltan, es IMPOSIBLE.
2. Socios Oro: Aceptan Alfa o Beta. Como Alfa es más demandado (lo usa Plata y Titanio), priorizamos agotar los packs Beta. Si no alcanzan los Beta, cubrimos el resto con Alfa.
3. Socios Plata: Aceptan Alfa o Gamma. Priorizamos agotar los packs Gamma. Si no alcanzan, cubrimos el resto con Alfa.
4. Socios Básico: Aceptan cualquier pack. Sumamos todos los packs restantes. Si la suma es mayor o igual a la cantidad de socios Básicos, es posible satisfacer la demanda.
"""


def distribuir_vinos(St, So, Sp, Sb, Pa, Pb, Pg, Pe):
    # St: sociosTitanio, So: sociosOro, Sp: sociosPlata, Sb: sociosBasico
    # Pa: packsAlfa, Pb: packsBeta, Pg: packsGamma, Pe: packsEpsilon

    asignacion = {
        "Titanio": {"alfa": 0},
        "Oro": {"alfa": 0, "beta": 0},
        "Plata": {"alfa": 0, "gamma": 0},
        "Basico": {"alfa": 0, "beta": 0, "gamma": 0, "epsilon": 0},
    }

    # --- PASO 1: Socios Titanio (Solo Alfa) ---
    if Pa < St:
        return "Imposible: Faltan packs Alfa para los socios Titanio."
    asignacion["Titanio"]["alfa"] = St
    Pa -= St  # Descontamos los packs alfa usados

    # --- PASO 2: Socios Oro (Beta, luego Alfa) ---
    usar_beta_oro = min(So, Pb)
    asignacion["Oro"]["beta"] = usar_beta_oro
    Pb -= usar_beta_oro
    So -= usar_beta_oro  # Socios Oro que aún no tienen pack

    if So > 0:
        if Pa < So:
            return "Imposible: Faltan packs para los socios Oro."
        asignacion["Oro"]["alfa"] = So
        Pa -= So
        So = 0

    # --- PASO 3: Socios Plata (Gamma, luego Alfa) ---
    usar_gamma_plata = min(Sp, Pg)
    asignacion["Plata"]["gamma"] = usar_gamma_plata
    Pg -= usar_gamma_plata
    Sp -= usar_gamma_plata  # Socios Plata que aún no tienen pack

    if Sp > 0:
        if Pa < Sp:
            return "Imposible: Faltan packs para los socios Plata."
        asignacion["Plata"]["alfa"] = Sp
        Pa -= Sp
        Sp = 0

    # --- PASO 4: Socios Básico (Cualquier cosa) ---
    total_packs_restantes = Pa + Pb + Pg + Pe
    if total_packs_restantes < Sb:
        return "Imposible: Faltan packs generales para los socios Básicos."

    # Asignamos lo que vaya sobrando a los Básicos (solo para mostrar el reporte)
    usar_pe = min(Sb, Pe)
    asignacion["Basico"]["epsilon"] = usar_pe
    Pe -= usar_pe
    Sb -= usar_pe
    usar_pb = min(Sb, Pb)
    asignacion["Basico"]["beta"] = usar_pb
    Pb -= usar_pb
    Sb -= usar_pb
    usar_pg = min(Sb, Pg)
    asignacion["Basico"]["gamma"] = usar_pg
    Pg -= usar_pg
    Sb -= usar_pg
    usar_pa = min(Sb, Pa)
    asignacion["Basico"]["alfa"] = usar_pa
    Pa -= usar_pa
    Sb -= usar_pa

    return asignacion


"""
2. ANÁLISIS DE COMPLEJIDAD

Complejidad Temporal: O(1)
- El algoritmo consiste en una serie de operaciones aritméticas básicas (restas, sumas y cálculo de mínimos) y condicionales (if). 
- El tiempo de ejecución no depende de la cantidad de socios ni de la cantidad de packs, ya que no hay ciclos que iteren sobre ellos. Se resuelve en tiempo constante.

Complejidad Espacial: O(1)
- Solo se utilizan variables para almacenar cantidades y un diccionario de tamaño fijo (con 4 claves predefinidas) para guardar el reporte. 
- La memoria no crece en función de los datos de entrada.


3. JUSTIFICACIÓN DE OPTIMALIDAD (Argumento de Intercambio / Restricciones)

Demostramos la optimalidad comprobando que cualquier otra elección conduciría a un 
escenario peor o igual.

- Titanio: Como solo aceptan Alfa, asignarles Alfa es una condición necesaria y obligatoria para cualquier solución válida. No hay decisión Greedy acá, es una restricción dura.
- Oro y Plata: Ambos compiten por el pack Alfa como plan de contingencia. El pack Beta es exclusivo para Oro (y Básico), y el pack Gamma es exclusivo para Plata (y Básico). Supongamos que, en lugar de agotar primero Beta para los Oro, usamos un pack Alfa mientras aún hay Beta disponible. Al hacer esto, reducimos la cantidad de packs Alfa disponibles para los Plata, mientras dejamos un pack Beta que los Plata NO pueden usar. Esta decisión estrictamente reduce el espacio de soluciones posibles para las siguientes etapas sin aportar ningún beneficio. Por lo tanto, la estrategia Greedy de consumir primero los recursos menos flexibles (Beta para Oro, Gamma para Plata) es localmente óptima y garantiza dejar la mayor cantidad del recurso compartido (Alfa) para satisfacer las contingencias de ambos.
- Básicos: Dado que aceptan cualquier pack, siempre y cuando la sumatoria de packs restantes sea mayor o igual a la cantidad de socios, se los podrá satisfacer. El orden en qué pack se les da es irrelevante para la optimalidad global.
"""

# Bloque de prueba
if __name__ == "__main__":
    # St, So, Sp, Sb
    socios = (10, 15, 20, 5)
    # Pa, Pb, Pg, Pe
    packs = (25, 10, 15, 10)

    print("--- Ejercicio 6: Club de Vinos ---")
    print(
        f"Socios: {socios[0]} Titanio, {socios[1]} Oro, {socios[2]} Plata, {socios[3]} Basicos"
    )
    print(
        f"Packs: {packs[0]} Alfa, {packs[1]} Beta, {packs[2]} Gamma, {packs[3]} Epsilon\n"
    )

    resultado = distribuir_vinos(*socios, *packs)

    if isinstance(resultado, str):
        print(resultado)
    else:
        print("Distribución exitosa:")
        for categoria, asignaciones in resultado.items():
            print(f"- {categoria}: {asignaciones}")
