// def esSolvente(
//   consumos:    List[List[(String, String, Int)]],
//   tiposCambio: Map[String, Int],
//   saldo:       Int
// ): Boolean

// val consumos1 = List(
//   List(("Rappi", "Peso", 7700)),
//   List(("Jumbo", "Peso", 10300))
// ) // Suman 18000 pesos

// val consumos2 = List(
//   List(("Steam", "Dolar", 20)),
//   List(("KLM", "Euro", 100), ("Apple", "Euro", -70))
// ) // Suman 170000 pesos

// val tiposCambio = Map("Peso" -> 1, "Dolar" -> 1000, "Euro" -> 1500)

// esSolvente(consumos1, tiposCambio, 10000)    // => false
// esSolvente(consumos2, tiposCambio, 5000000)  // => true

def esSolvente(
    consumos: List[List[(String, String, Int)]],
    tiposCambio: Map[String, Int],
    saldo: Int
    ): Boolean = {
        
        // 1. Calculamos el gasto total en pesos
        val gastoTotal = consumos.flatten.filter { // .Rompemos la lista de listas. Nos quedamos solo con valores positivos 
            case (_, _, valor) => valor > 0
            }.map { // Calculamos el valor en pesos
                case (_, moneda, valor) => valor * tiposCambio(moneda)
                }.sum // Sumamos todos los gastos
        
        // 2. Evaluamos si nos alcanza la plata
        saldo >= gastoTotal
}
