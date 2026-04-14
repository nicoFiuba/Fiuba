import scala.collection.mutable.Map

def actualizarAUno(mapa: Map[Int, Int]) = {
    for (k, v) <- mapa do mapa(k) = 1
}

// La función actualizarAUno es impura porque modifica el estado del mapa que se le pasa como argumento. Al iterar sobre el mapa y actualizar sus valores a 1, está cambiando el contenido del mapa original, lo que constituye un efecto secundario.
