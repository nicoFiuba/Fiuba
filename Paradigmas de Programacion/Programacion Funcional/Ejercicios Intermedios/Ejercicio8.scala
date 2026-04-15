def maximoConMatch(lista: List[Int]): Int = {
    lista match {
        // Si me pasan una lista vacía de entrada, atajo el error
        case Nil => throw new IllegalArgumentException("La lista no puede estar vacía")
        
        // CASO BASE: Si la cola está vacía (Nil), la cabeza es el máximo
        case cabeza :: Nil => cabeza
        
        // CASO RECURSIVO: Hay cabeza y hay una cola con cosas
        case cabeza :: cola => 
            // Calculamos el máximo del resto de la lista llamándonos a nosotros mismos
            val maximoCola = maximoConMatch(cola)
            
            // Devolvemos el ganador de la comparación
            if (cabeza > maximoCola) cabeza else maximoCola
    }
}

def maximoSinMatch(lista: List[Int]): Int = {
    lista.max
}
