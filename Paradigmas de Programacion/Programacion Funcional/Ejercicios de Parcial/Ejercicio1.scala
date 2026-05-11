// campeon(
//   List(
//     ("Argentina", "Uruguay", "Equipo1"),
//     ("Brasil",    "Argentina", "Equipo2"),
//     ("Uruguay",   "Paraguay",  "Equipo2")
//   )
// ) // => "Argentina"

def campeon(partidos: List[(String, String, String)]): String = {
    
    // 1. Extraemos solo a los ganadores
    val ganadores: List[String] = partidos.map { 
        // Usamos pattern matching directamente. 
        // El guión bajo '_' significa "este dato no me importa".
        case (eq1, _, "Equipo1") => eq1
        case (_, eq2, "Equipo2") => eq2
    }
    
    // 2. Agrupamos y contamos (el truco que ya te sabés de memoria)
    val tablaDePosiciones: Map[String, Int] = ganadores.groupBy(identity).map { 
        case (equipo, victorias) => (equipo, victorias.length)
    }
        
    // 3. Buscamos el máximo según el puntaje (que es el segundo elemento de la tupla del mapa, o sea ._2)
    val equipoCampeon = tablaDePosiciones.maxBy {
        case (equipo, puntos) => puntos
    }
    
    // equipoCampeon es una tupla ("Argentina", 2). Como solo nos piden el nombre, devolvemos el ._1
    equipoCampeon._1
}
