// val ventas = List(
//   ("Lucía", 1000),
//   ("Pedro", 500),
//   ("Lucía", 2000),
//   ("Sofía", 500),
//   ("Pedro", 1500),
//   ("Lucía", 500),
//   ("Mario", 2100)
// )

// mejoresVendedores(ventas) // => List("Lucía", "Mario", "Pedro")


def mejoresVendedores(ventas: List[(String, Int)]): List[String] = {
    ventas.groupBy(_._1).map { //.Agrupamos por el primer elemento de la tupla (el nombre).Calculamos el total vendido por cada empleado 
        case (nombre, listaVentas) => (nombre, listaVentas.map(_._2).sum) // listaVentas es una List[(String, Int)], extraemos los montos y los sumamos
        }.filter { // 3. Filtramos los que vendieron 2000 o más 
            case (_, total) => total >= 2000
        }.toList.sortBy { // 4. Pasamos el Map a List para poder ordenarlo libremente
            case (_, total) => -total // 5. Ordenamos por el total. El signo menos (-) hace que sea de mayor a menor (descendente)
        }.map { // 6. Finalmente, nos quedamos solo con los nombres
            case (nombre, _) => nombre
        }
}

