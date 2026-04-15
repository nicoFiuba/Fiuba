def capicua(string: String): Boolean = {
    string == string.reverse
}

def capicuaRecursivo(string: String): Boolean = {
    string match {
        // CASO BASE: Usamos un guard para frenar si tiene 1 o 0 letras
        case _ if string.length <= 1 => true
        
        // CASO RECURSIVO: Usamos un guard para ver si los extremos coinciden
        case _ if string.head == string.last => capicuaRecursivo(string.tail.init)
        
        // CASO FALLA: El comodín '_' atrapa cualquier otra cosa (si no coincidieron)
        case _ => false
    }
}
