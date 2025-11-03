public class Ejercicio10 {

    public static void quickSort(int[] array, int menor, int mayor) {
        
        if (menor < mayor) {
            int indice = partirArray(array, menor, mayor);

            quickSort(array, menor, indice - 1);
            quickSort(array, indice + 1, mayor);

        }

    }

    public static int partirArray(int[] array, int menor, int mayor) {

        int pivote = array[mayor];
        int i = (menor - 1);

        for (int j = menor; j < mayor; j++) {
            if (array[j] <= pivote) {
                i++;
                
                int temporal = array[i];
                array[i] = array[j];
                array[j] = temporal;
            }

        }

        int temporal = array[i + 1];
        array[i + 1] = array[mayor];
        array[mayor] = temporal;
        
        return i + 1;
    }
    
    public static void main(String[] args) {
        int[] array = {10, 7, 8, 9, 1, 5};
        int n = array.length;

        quickSort(array, 0, n - 1);

        System.out.println("Array ordenado: ");
        
        for (int num : array) {
            System.out.print(num + " ");
        }
    }

}
