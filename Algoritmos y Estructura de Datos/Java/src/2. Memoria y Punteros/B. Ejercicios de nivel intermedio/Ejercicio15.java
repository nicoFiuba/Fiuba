public class Ejercicio15 {

    static int factorial(int numero){

    if (numero == 0 || numero == 1) {
        return 1;
    } else {
        return numero * factorial(numero - 1);
    }
} 

    public static void main(String[] args) {
        
        int numero = 4;
        // int numero = 20000; // Entra en un bucle infinito por la profundidad de la pila
        int resultado = factorial(numero);
        System.out.println("El factorial de " + numero + " es: " + resultado);
    }
    
}
