// doblar(List("hola", "algo", "perro", "pelota", "palabraMuyLarga"))
// // => List("hola", "hola", "algo", "algo", "sabueso", "pelota")

def doblar(l: List[String]): List[String] = {
    l.flatMap {

        // Regla 1: Si es exactamente "perro", devolvemos "sabueso" en una lista
        case "perro" => List("sabueso")
        
        // Regla 2: Si tiene más de 10 letras, devolvemos una lista vacía (se elimina)
        case palabra if palabra.length > 10 => Nil
        
        // Regla 3: Si tiene exactamente 4 letras, la devolvemos duplicada
        case palabra if palabra.length == 4 => List(palabra, palabra)
        
        // Caso por defecto: Si no cumple ninguna de las anteriores, queda intacta
        case palabra => List(palabra)
    }
}
