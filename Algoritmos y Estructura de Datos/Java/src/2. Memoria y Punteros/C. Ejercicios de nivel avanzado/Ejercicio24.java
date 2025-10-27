public class Ejercicio24 {

    static void velocidadArray(int[] array) {
        long inicio = System.nanoTime();

        for (int i = 0; i < 100000; i++) {
            for (int j = 0; j < array.length; j++) {
                array[j] = j;
            }
        }

        long fin = System.nanoTime();
        long duracion = fin - inicio;

        System.out.println("Tiempo para array de tamaño " + array.length + ": " + duracion + " nanosegundos");
    }
    
    public static void main(String[] args) {

        int[] array1 =new int[5];
        int[] array2 =new int[50000];

        velocidadArray(array1);
        velocidadArray(array2);
    }
}
