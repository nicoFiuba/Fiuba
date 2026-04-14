def buscarElemento(lista: List[Int], elemento: Int): Boolean = {
    
    lista match {
    // CASO BASE: Si el tren está vacío (Nil), significa que buscamos en todos lados y no estaba.
    case Nil => false

    // CASO RECURSIVO: Desenganchamos el primer vagón (cabeza) del resto (cola)
    case cabeza :: cola =>
        if (cabeza == elemento) {
        // ¡Bingo! El vagón que desenganchamos es el que buscábamos.
        true
        } else {
        // Pucha, no era. Bueno, vuelvo a llamar a MI MISMA función,
        // pero pasándole el tren más cortito (la cola) para que siga buscando.
        buscarElemento(cola, elemento)
        }
    }
}
