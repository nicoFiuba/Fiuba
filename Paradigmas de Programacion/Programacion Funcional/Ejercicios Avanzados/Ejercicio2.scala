def frecuenciaPalabras(texto: String): Map[String, Int] = {
    // 1. Preprocesamiento: Convertimos el texto crudo en una lista de palabras
    // El .toList es para convertir el Array que devuelve split a una Lista clásica
    val listaDePalabras = texto.split("\\s+").toList
    
    // 2. Lógica del Ejercicio 1: Agrupamos y contamos
    listaDePalabras.groupBy(identity).map {
        case (palabra, apariciones) => (palabra, apariciones.length)
    }
}

def frecuenciaPalabrasAtajo(texto: String): Map[String, Int] = {
    texto.split("\\s+").toList.groupBy(identity).map(t => (t._1, t._2.length))
}
