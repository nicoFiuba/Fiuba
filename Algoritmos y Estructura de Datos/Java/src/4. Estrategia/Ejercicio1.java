public class Ejercicio1 {
    
    static int factorial(int numero){
        
        if (numero == 0 || numero == 1) {
            return 1;
        } else {
            return numero * factorial(numero - 1);
        }

    }
        
    public static void main(String[] args) {
        
        int numero = 4;
        int resultado = factorial(numero);
        
        System.out.println("El factorial de " + numero + " es: " + resultado);
    
    }
    
}

// Solucion iterativa
/*
public static long factorialIterativo(int numero) {
    
    if (numero < 0) {
        throw new IllegalArgumentException("El número debe ser no negativo");
    }
    
    long resultado = 1; // Usamos long por desborde.
    
    for (int i = 2; i <= numero; i++) {
        resultado = resultado * i;
    }
    
    return resultado;
}
*/

// Solucion usando BigInteger para evitar desbordes en factoriales grandes
/*
import java.math.BigInteger;

public static BigInteger factorialBigInteger(int numero) {
    
    if (numero < 0) {
        throw new IllegalArgumentException("El número debe ser no negativo");
    }
    
    BigInteger resultado = BigInteger.ONE;
    
    for (int i = 2; i <= numero; i++) {
        resultado = resultado.multiply(BigInteger.valueOf(i));
    }
    
    return resultado;
}
*/
