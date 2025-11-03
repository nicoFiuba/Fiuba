public class Ejercicio14 {
    
    private static int getMaximo(int[] array) {
        
        int maximo = array[0];
        
        for (int x : array) {
            if (x > maximo) {
                maximo = x;
            }

        }

        return maximo;
    }
    
    private static void countingSortByDigit(int[] array, int posicionDigito) {
        
        int n = array.length;
        int[] salidaOrdenada = new int[n]; 
        int[] contador = new int[10]; 

        for (int i = 0; i < n; i++) {
            contador[(array[i] / posicionDigito) % 10]++; 
        }

        for (int i = 1; i < 10; i++) {
            contador[i] += contador[i - 1];
        }

        for (int i = n - 1; i >= 0; i--) {
            int digito = (array[i] / posicionDigito) % 10;
            
            salidaOrdenada[contador[digito] - 1] = array[i];
            
            contador[digito]--;

        }

        for (int i = 0; i < n; i++) {
            array[i] = salidaOrdenada[i];
        }
    }
    
    public static void radixSort(int[] array) {
        
        if (array == null || array.length < 2) return;
        
        int maximo = getMaximo(array);

        for (int posicionDigito = 1; maximo / posicionDigito > 0; posicionDigito *= 10) {
            countingSortByDigit(array, posicionDigito);
        }

    }
    
    public static void main(String args[]) {
        
        int[] array = {170, 45, 75, 90, 802, 24, 2, 66};
        
        System.out.println("Arreglo original:");
        
        for(int x : array) {
            System.out.print(x + " ");
        }
        
        radixSort(array);

        System.out.println("\nArreglo ordenado (Radix Sort):");
        
        for(int x : array) {
            System.out.print(x + " "); 
        }

        System.out.println();

    }

}
