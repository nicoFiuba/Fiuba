public class Ejercicio19 {

    public static void main(String[] args) {

        int[] array = {3, 5, 7};

        System.out.println("Referencia del array original: " + array);

        array = null;

        System.out.println("Referencia del array después de perder la referencia: " + array);

    }
    
}
