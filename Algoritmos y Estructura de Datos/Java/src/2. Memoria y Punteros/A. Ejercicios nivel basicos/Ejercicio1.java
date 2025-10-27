public class Ejercicio1 {

    public static void main(String[] args) {
        
        int x = 5;
        int y = 10;

        System.out.println("Antes del intercambio: x = " + x + ", y = " + y);

        x += y; // x ahora es 15
        y = x - y; // y ahora es 5
        x -= y; // x ahora es 10

        System.out.println("Despues del intercambio: x = " + x + ", y = " + y);
    }
}
