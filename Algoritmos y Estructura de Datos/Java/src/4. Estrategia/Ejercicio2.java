public class Ejercicio2 {
    
    static int potencia(int base, int exponente) {
        
        if (exponente == 0) {
            return 1;
        } else {
            return base * potencia(base, exponente - 1);
        }

    }

    public static void main(String[] args) {
        
        int base = 2;
        int exponente = 3;
        int resultado = potencia(base, exponente);

        System.out.println(base + " elevado a " + exponente + " es: " + resultado);

    }
    
}

// Solucion mediante Potencia Rapida (divide y vencerás)
/* 
static long potenciaOptimizada(long base, int exponente) {
    
    if (exponente == 0) {
        return 1;
    }
    
    long mitad = potenciaOptimizada(base, exponente / 2);
    
    if (exponente % 2 == 0) {
        return mitad * mitad;
    } else {
        return base * mitad * mitad;
    }

}
*/

// Solucion iterativa
/*
public static int potenciaIterativa(int base, int exponente) {
    
    int resultado = 1;
    
    for (int i = 0; i < exponente; i++) {
        resultado = resultado * base;
    }
    
    return resultado;
}
*/

// Solucion usando BigInteger para evitar desbordes en potencias grandes
/*
import java.math.BigInteger;

public static BigInteger potenciaBigInteger(int base, int exponente) {
    
    if (exponente < 0) {
        throw new IllegalArgumentException("El exponente debe ser no negativo");
    }
    
    BigInteger resultado = BigInteger.ONE;
    BigInteger baseBig = BigInteger.valueOf(base);
    
    for (int i = 0; i < exponente; i++) {
        resultado = resultado.multiply(baseBig);
    }
    
    return resultado;
} 
*/
