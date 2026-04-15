// 1. Definimos el modelo de datos
case class Producto(nombre: String, precio: Double)

// 2. Definimos la función de filtrado
def filtrar(productos: List[Producto], n: Double): List[Producto] = {
    productos.filter(producto => producto.precio < n)
}
