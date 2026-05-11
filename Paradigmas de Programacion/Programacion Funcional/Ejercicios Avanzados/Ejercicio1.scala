def contar(palabras: List[String]): Map[String, Int] = {
    
    // 1. Agrupamos pasando una función que devuelve la palabra intacta
    val mapaAgrupado = palabras.groupBy(palabra => palabra)
    // se puede escribir también como: palabras.groupBy(identity) porque 'identity' es una función que devuelve su argumento sin modificarlo.
    
    // 2. Transformamos el mapa usando pattern matching para desarmar la tupla (clave, valor)
    mapaAgrupado.map {
        case (palabra, listaDeApariciones) => (palabra, listaDeApariciones.length)
    }
}

def atajoContar(palabras: List[String]): Map[String, Int] = {
    palabras.groupBy(identity).map(tupla => (tupla._1, tupla._2.length))
}
