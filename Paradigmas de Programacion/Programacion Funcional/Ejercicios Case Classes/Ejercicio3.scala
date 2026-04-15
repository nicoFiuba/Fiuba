// 1. El Modelo de Datos (Jerarquía)
sealed trait Archivo

case class ArchivoSimple(nombre: String, tamano: Int) extends Archivo
case class Carpeta(nombre: String, archivos: List[Archivo]) extends Archivo

// 2. Las Funciones de Procesamiento
def tamañoTotal(archivo: Archivo): Int = {
    archivo match {
        // Si es archivo, devolvemos su tamaño
        case ArchivoSimple(_, tamano) => tamano
        // Si es carpeta, calculamos el tamaño de todo su contenido y lo sumamos
        case Carpeta(_, archivos) => archivos.map(tamañoTotal).sum
    }
}

def cantidadArchivos(archivo: Archivo): Int = {
    archivo match {
        // Si es archivo, cuenta como 1
        case ArchivoSimple(_, _)  => 1
        // Si es carpeta, sumamos la cantidad de archivos que haya adentro
        case Carpeta(_, archivos) => archivos.map(cantidadArchivos).sum
    }
}