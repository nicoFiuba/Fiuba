def fibonacci(n: Int): Int = {
    n match {
        case 0 => 0
        case 1 => 1
        case _ => fibonacci(n - 1) + fibonacci(n - 2)
    }
}

// Esta función es ineficiente para valores grandes de n, ya que hace muchas llamadas recursivas repetidas. Aca dejo la version eficiente:

import scala.annotation.tailrec

def fibonacciTail(n: Int): Int = {
    
    // Función auxiliar que lleva la cuenta. 
    // 'actual' y 'siguiente' son los acumuladores.
    
    @tailrec
    def loop(iteracion: Int, actual: Int, siguiente: Int): Int = {
        iteracion match {
            // Caso base: si llegamos a 0 iteraciones, devolvemos el acumulador 'actual'
            case 0 => actual
            // Caso recursivo: restamos 1 a las iteraciones, y avanzamos los acumuladores
            case _ => loop(iteracion - 1, siguiente, actual + siguiente)
        }
    }
    
    // Llamamos a la función auxiliar para arrancar el motor
    loop(n, 0, 1)
}
