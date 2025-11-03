public class Ejercicio6 {
    
    static long ackermann(long m, long n) {
        
        if (m < 0 || n < 0) {
            throw new IllegalArgumentException("m y n no deben ser negativos.");
        }
        
        if (m == 0) {
            return n + 1;
        } else if (n == 0) {
            return ackermann(m - 1, 1);
        } else {
            return ackermann(m - 1, ackermann(m, n - 1));
        }

    }
    
    public static void main(String[] args) {
        System.out.println(ackermann(0, 5)); // Salida: 6
        System.out.println(ackermann(1, 5)); // Salida: 7
        System.out.println(ackermann(2, 5)); // Salida: 13
        System.out.println(ackermann(3, 3)); // Salida: 13
    }
    
}

// Solucion por formula cerrada
/*
static int ackermann(int m, int n) {
    
    if (m == 0) {
        return n + 1;
    } else if (m == 1) {
        return n + 2;
    } else if (m == 2) {
        return 2 * n + 3;
    } else if (m == 3) {
        return (int) Math.pow(2, n + 3) - 3;
    } else {
        throw new IllegalArgumentException("m debe ser menor o igual a 3");
    }

}
*/
