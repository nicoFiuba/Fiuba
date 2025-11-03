public class Ejercicio9 {

    public static void mergeSort(int[] array, int izquierda, int derecha) {
        
        if (izquierda < derecha) {
            int medio = izquierda + (derecha - izquierda) / 2;
            
            mergeSort(array, izquierda, medio);
            mergeSort(array, medio + 1, derecha);
            merge(array, izquierda, medio, derecha);

        }

    }

    public static void merge(int[] array, int izquierda, int medio, int derecha) {
        
        int num1 = medio - izquierda + 1;
        int num2 = derecha - medio;

        int[] Izquierda = new int[num1];
        int[] Derecha = new int[num2];

        for (int i = 0; i < num1; i++) {
            Izquierda[i] = array[izquierda + i];
        }

        for (int j = 0; j < num2; j++) {
            Derecha[j] = array[medio + 1 + j];
        }

        int i = 0, j = 0;
        int k = izquierda;
        
        while (i < num1 && j < num2) {
            if (Izquierda[i] <= Derecha[j]) {
                array[k] = Izquierda[i];
                
                i++;
            } else {
                array[k] = Derecha[j];
                
                j++;
            }

            k++;
        }

        while (i < num1) {
            array[k] = Izquierda[i];
            
            i++;
            k++;
        }

        while (j < num2) {
            array[k] = Derecha[j];
            
            j++;
            k++;
        }

    }

    public static void main(String[] args) {
        
        int[] array = {38, 27, 43, 3, 9, 82, 10};
        
        System.out.println("Array original:");
        
        for (int num : array) {
            System.out.print(num + " ");
        }
        
        System.out.println();

        mergeSort(array, 0, array.length - 1);

        System.out.println("Array ordenado:");
        
        for (int num : array) {
            System.out.print(num + " ");
        }
        
        System.out.println();
    }

}
