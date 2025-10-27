public class Ejercicio11 {

    public static void swap(int x, int y) {
        
        x += y;
        y = x - y;
        x -= y;

    }
    
    public static void main(String[] args) {

        int x = 10;
        int y = 20;

        System.out.println("Antes del intercambio:");
        System.out.println("x = " + x);
        System.out.println("y = " + y);

        swap(x, y);

        System.out.println("Después del intercambio:");
        System.out.println("x = " + x);
        System.out.println("y = " + y);

    }
}
