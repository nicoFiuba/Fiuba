// palabraMasFrecuente("a y b y c y a y a")                         // => "a"
// palabraMasFrecuente("scala es genial y scala es divertido")     // => "scala"
// palabraMasFrecuente("perro   gato  perro  y gato  perro")       // => "perro"

def palabraMasFrecuente(texto: String): String = {
    texto.split("\\s+").filterNot(palabra => palabra == "y").groupBy(identity).maxBy {
        case (palabra, ocurrencias) => ocurrencias.length
    } match {
        case (palabra, _) => palabra
    }
}
