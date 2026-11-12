"""
EXPLICACIÓN: voy a usar una matriz OPT de tamaño N x 4, donde las filas "i" representan los días (de 0 a N-1) y las columnas "j" representan el rubro elegido ese día (Cantante, Danza, Variedades, Humorista). La celda OPT[i][j] guardará la ganancia máxima obtenida desde el día 0 hasta el día i, eligiendo obligatoriamente el rubro j en el día i. Para calcular OPT[i][j], sumamos la ganancia del rubro j en el día i más el máximo valor posible del día anterior (i-1), filtrando qué rubros estaban permitidos ayer según las reglas.

RELACION DE RECURRENCIA:
- Caso base (día 0): OPT[0][j] = ganancia[0][j] (para j = 0, 1, 2, 3)

- Caso recursivo (día i > 0; Rubros = (Cantante, Danza, Variedades, Humorista) = (0, 1, 2, 3))
    - Para Cantante: OPT[i][0] = ganancia[i][0] + max(OPT[i - 1][1], OPT[i - 1][2], OPT[i - 1][3])
    - Para Danza: OPT[i][1] = ganancia[i][1] + max(OPT[i - 1][2], OPT[i - 1][3])
    - Para Variedades: OPT[i][2] = ganancia[i][2] + max(OPT[i - 1][1], OPT[i - 1][3])
    - Para Humorista: OPT[i][3] = ganancia[i][3] + max(OPT[i - 1][0], OPT[i - 1][1], OPT[i - 1][2])

PSEUDOCÓDIGO
"""
def programar_eventos(ganancias):

    n = len(ganancias)
    if n == 0:
        return 0
    
    OPT = []
    for i in range(n):
        OPT.append([0] * 4)

    OPT[0][0] = ganancias[0][0] # Cantante
    OPT[0][1] = ganancias[0][1] # Danza
    OPT[0][2] = ganancias[0][2] # Variedades
    OPT[0][3] = ganancias[0][3] # Humorista

    for i in range(1, n):
        
        OPT[i][0] = ganancias[i][0] + max(OPT[i-1][1], OPT[i-1][2], OPT[i-1][3])
        
        OPT[i][1] = ganancias[i][1] + max(OPT[i-1][2], OPT[i-1][3])
        
        OPT[i][2] = ganancias[i][2] + max(OPT[i-1][1], OPT[i-1][3])
        
        OPT[i][3] = ganancias[i][3] + max(OPT[i-1][0], OPT[i-1][1], OPT[i-1][2])

    return max(OPT[n-1])

"""
ANÁLISIS DE COMPLEJIDAD
- Temporal: O(N) para iter sobre los N días y O(1) para comparar, por lo tanto, la complejidad es O(N)

- Espacial: O(N) para almacenar los valores de OPT.

EJEMPLO: supongamos N = 2 días con las siguientes ganancias para (0: Cantante, 1: Danza, 2: Variedades, 3: Humorista):
ganancias = [
                [10, 20, 30, 40], # Día 0
                [50, 10, 20, 30]  # Día 1
            ]

Día 0 (Caso base):
OPT[0][0] = 10
OPT[0][1] = 20
OPT[0][2] = 30
OPT[0][3] = 40
Estado de OPT: [[10, 20, 30, 40], [0, 0, 0, 0]]

Día 1:
OPT[1][0] = ganancias[1][0] + max(OPT[0][1], OPT[0][2], OPT[0][3]) = 50 + max(20, 30, 40) = 50 + 40 = 90
OPT[1][1] = ganancias[1][1] + max(OPT[0][2], OPT[0][3]) = 10 + max(30, 40) = 10 + 40 = 50
OPT[1][2] = ganancias[1][2] + max(OPT[0][1], OPT[0][3]) = 20 + max(20, 40) = 20 + 40 = 60
OPT[1][3] = ganancias[1][3] + max(OPT[0][0], OPT[0][1], OPT[0][2]) = 30 + max(10, 20, 30) = 30 + 30 = 60
Estado de OPT: [[10, 20, 30, 40], [90, 50, 60, 60]]

Resultado final:
max(OPT[1]) = max(90, 50, 60, 60) = 90. La ganancia máxima es 90.
"""
