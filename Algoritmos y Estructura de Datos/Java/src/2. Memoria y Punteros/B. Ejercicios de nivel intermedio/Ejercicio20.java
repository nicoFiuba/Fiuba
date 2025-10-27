public class Ejercicio20 {

    public static void main(String[] args) {

        int[] array1 = {10, 20, 30};
        int[] array2 = array1;

        System.out.println("Copia superficial");
        System.out.println("Contenido del array1: " + array1[0] + ", " + array1[1] + ", " + array1[2]);
        System.out.println("Contenido del array2: " + array2[0] + ", " + array2[1] + ", " + array2[2]);

        int[] array3 = {40, 50, 60};
        System.arraycopy(array3, 0, array2, 0, array3.length);

        System.out.println("Copia usando System.arraycopy");
        System.out.println("Contenido de array2 después de copiar desde array3: " + array2[0] + ", " + array2[1] + ", " + array2[2]);

        int[] array4 = {70, 80, 90};
        
        for (int i = 0; i < array4.length; i++) {
            array4 [i] = array3 [i];
        }

        System.out.println("Copia manual profunda");
        System.out.println("Contenido de array4 después de copiar desde array3: " + array4[0] + ", " + array4[1] + ", " + array4[2]);
    
    }
}
