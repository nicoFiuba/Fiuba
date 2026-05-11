"""
Un comercio tiene 3 sucursales que trabajan de lunes a viernes. Los montos de las ventas se guardan en una matriz (lista de listas) de 3 x 5. Es decir que en cada sublista, tenemos las ventas correspondientes a cada una de las sucursales. Hacer un programa en Python que: 
"""

sucursales = ["Caballito", "Belgrano", "Palermo"]
ventasSucursales = [
    [1, 2, 3, 4, 5], 
    [5, 3, 3, 4, 1],
    [3, 2, 4, 1, 2]
]
diasSemana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# a) Calcule el total semanal de ventas.
def ventasTotales(ventasSucursales):
    total = 0
    for sucursal in ventasSucursales:
        for venta in sucursal:
            total += venta
    return total

# b) Indique qué sucursal vendió menos.
def sucursalMenorVenta(ventasSucursales):
    menorVenta = float("inf")
    sucursalMenor = ""
    
    for sucursal in range(len(ventasSucursales)):
        totalSucursal = sum(ventasSucursales[sucursal])
        if totalSucursal < menorVenta:
            menorVenta = totalSucursal
            sucursalMenor = sucursales[sucursal]
    return sucursalMenor

#c) Indique qué día se vendió más y de cuánto fue esa venta. """
def diaMayorVenta(ventasSucursales, diasSemana):
    ventasPorDia=float("-inf")
    diaMasVendido = ""

    for dia in range(len(diasSemana)):
        totalVenta = 0
        for sucursal in range(len(ventasSucursales)):
            totalVenta += ventasSucursales[sucursal][dia]
            
        if totalVenta > ventasPorDia:
            ventasPorDia = totalVenta
            diaMasVendido = diasSemana[dia]
    return diaMasVendido, ventasPorDia

def main():
    ventaSemanal = ventasTotales(ventasSucursales)
    print(f"El total semanal de ventas es: {ventaSemanal}")

    menorVenta = sucursalMenorVenta(ventasSucursales)
    print(f"La sucursal que vendió menos es: {menorVenta}")

    diaMasVendido, ventasPorDia= diaMayorVenta(ventasSucursales, diasSemana)
    print(f"El día que se vendió más fue el {diaMasVendido} con {ventasPorDia} ventas")

main()