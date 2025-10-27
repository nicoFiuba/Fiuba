public class Ejercicio18 {

    static void cambiarMetodo(int[] arr) {
        
        arr[0] = 99;

    }

    public static void main(String[] args) {
        int[] miArray = {1, 2, 3, 4, 5};
        System.out.println("Antes de llamar a cambiarMetodo: " + miArray[0]);
        cambiarMetodo(miArray);
        System.out.println("Después de llamar a cambiarMetodo: " + miArray[0]);
    
    }
    
}
