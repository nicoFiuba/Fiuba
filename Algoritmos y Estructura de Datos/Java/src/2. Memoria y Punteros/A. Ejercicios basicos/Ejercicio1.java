public class Ejercicio1 {

    public static void main(String[] args) {
        
        int x = 5;
        int y = 10;

        System.out.println("Antes del intercambio: x = " + x + ", y = " + y);

        x += y; // a ahora es 15
        y = x - y; // b ahora es 5
        x = x - y; // a ahora es 10

        System.out.println("Despues del intercambio: x = " + x + ", y = " + y);
    }
}
