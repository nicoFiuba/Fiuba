public class Ejercicio4 {
    
    // Esta solucion no va ya que es O(2^n), super ineficiente. Hay que usar memoizacion o programacion dinamica.
    // La dejo como principal solamente porque es la solucion recursiva del problema.

    static int fibonacci(int n) {
        
        if (n <= 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            return fibonacci(n - 1) + fibonacci(n - 2);
        }

    }

    public static void main(String[] args) {
        
        int n = 6;
        int resultado = fibonacci(n);
        
        System.out.println("El número Fibonacci en la posición " + n + " es: " + resultado);

    }

}

// Solucion con memoizacion
/*
import java.util.HashMap;

static HashMap<Integer, Integer> memoria = new HashMap<>(); //

static int fibonacci(int n) {

    if (n <= 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else if (memoria.containsKey(n)) {
        return memoria.get(n);
    } else {
        int resultado = fibonacci(n - 1) + fibonacci(n - 2);
        memoria.put(n, resultado);
        return resultado;
    }

}
*/

// Solucion iterativa
/*
static int fibonacci(int n) {

    if (n <= 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    }
    
    int a = 0;
    int b = 1;
    int fib = 0;

    for (int i = 2; i <= n; i++) {
        fibonacci = a + b;
        a = b;
        b = fibonacci;
    }

    return fibonacci;
}
*/
