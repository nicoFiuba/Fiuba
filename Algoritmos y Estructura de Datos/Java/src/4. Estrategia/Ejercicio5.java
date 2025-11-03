public class Ejercicio5 {

    static int mcd(int a, int b) {

        a = Math.abs(a);
        b = Math.abs(b);
        
        if (b == 0) {
            return a;
        }
        
        return mcd(b, a % b);
    }
    
    public static void main(String[] args) {
        
        int a = 48;
        int b = 18;
        
        System.out.println("El MCD de " + a + " y " + b + " es: " + mcd(a, b));

    }

}
