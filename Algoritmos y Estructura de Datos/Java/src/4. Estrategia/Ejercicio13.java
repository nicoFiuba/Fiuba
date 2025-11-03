public class Ejercicio13 {

    public static void countingSort(int[] array, int valorMaximo) {
        
        int n = array.length;
        
        int[] salidaOrdenada = new int[n]; 
        int[] contador = new int[valorMaximo + 1];

        for (int num : array) {
            contador[num]++;
        }

        for (int i = 1; i <= valorMaximo; i++) {
            contador[i] += contador[i - 1];
        }

        for (int i = n - 1; i >= 0; i--) {
            int posición = contador[array[i]] - 1; 
            
            salidaOrdenada[posición] = array[i];
            
            contador[array[i]]--;
        }

        System.arraycopy(salidaOrdenada, 0, array, 0, n);
    }

    public static void main(String[] args) {
        
        int[] array = {4, 2, 2, 8, 3, 3, 1};
        int valorMaximo = 8;
        
        countingSort(array, valorMaximo);
        
        for (int num : array) {
            System.out.print(num + " ");
        }

    }

}
