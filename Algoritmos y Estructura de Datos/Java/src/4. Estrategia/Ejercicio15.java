public class Ejercicio15 {
    
    public static void bucketSort(float[] array, int numeroDeBaldes) {
        
        if (array == null || array.length < 2) {
            return;
        }
        
        int n = array.length;

        float[][] baldes = new float[numeroDeBaldes][n];
        int[] conteoBaldes = new int[numeroDeBaldes];

        for (float flotante : array) {
            int indiceDelBalde = (int) (flotante * numeroDeBaldes); 
            
            if (indiceDelBalde == numeroDeBaldes) {
                indiceDelBalde--;
            }

            baldes[indiceDelBalde][conteoBaldes[indiceDelBalde]] = flotante;
            conteoBaldes[indiceDelBalde]++;

        }

        for (int i = 0; i < numeroDeBaldes; i++) {
            insertionSort(baldes[i], conteoBaldes[i]); 
        }

        int indice = 0;

        for (int i = 0; i < numeroDeBaldes; i++) {
            for (int j = 0; j < conteoBaldes[i]; j++) { 
                array[indice++] = baldes[i][j];
            }

        }
        
    }

    private static void insertionSort(float[] array, int tamaño) {
        for (int i = 1; i < tamaño; ++i) {
            float llave = array[i];
            int j = i - 1;

            while (j >= 0 && array[j] > llave) {
                array[j + 1] = array[j];
                j = j - 1;
            }
            array[j + 1] = llave;
        }
    }

    public static void main(String args[]) {

        float[] array = {0.89f, 0.45f, 0.67f, 0.12f, 0.03f, 0.34f, 0.99f};
        int numeroDeBaldes = 5; 

        System.out.println("Arreglo original:");
        
        for(float flotante : array) {
            System.out.print(flotante + " ");
        }

        System.out.println();
        
        bucketSort(array, numeroDeBaldes); 

        System.out.println("\nArreglo ordenado (Bucket Sort):");
        
        for(float flotante : array) {
            System.out.print(flotante + " ");
        }

        System.out.println();
        
    }

}
