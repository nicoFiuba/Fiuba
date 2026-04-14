import scala.collection.mutable.Map

def randomEntre(a: Int, b: Int): Int = {
    val rand = new scala.util.Random
    rand.between(a, b)
}

// La función randomEntre es impura porque genera un número aleatorio cada vez que se llama, lo que significa que no siempre devuelve el mismo resultado para los mismos argumentos. Además, tiene un efecto secundario al modificar el estado interno del generador de números aleatorios.