// doblar(List("hola", "algo", "perro", "pelota", "palabraMuyLarga"))
// // => List("hola", "hola", "algo", "algo", "sabueso", "pelota")

def doblar(l: List[String]): List[String] = {
    l.flatMap {

        // Regla 1: Si tiene más de 10 letras, devolvemos una lista vacía (se elimina)
        case palabra if palabra.length > 10 => Nil
        
        // Regla 2: Si tiene exactamente 4 letras, la devolvemos duplicada
        case palabra if palabra.length == 4 => List(palabra, palabra)
        
        // Regla 3: Si es exactamente "perro", devolvemos "sabueso" en una lista
        // (Nota: el orden importa. Conviene atajar "perro" antes de la regla de 4 letras, 
        // aunque "perro" tiene 5, es una buena práctica atajar casos específicos primero).
        case "perro" => List("sabueso")
        
        // Caso por defecto: Si no cumple ninguna de las anteriores, queda intacta
        case palabra => List(palabra)
    }
}
