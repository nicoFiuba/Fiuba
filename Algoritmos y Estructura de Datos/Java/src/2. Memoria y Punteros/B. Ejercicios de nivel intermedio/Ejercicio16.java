public class Ejercicio16 {

    public static void imprimirReferenciaArray(int[] array) {

        System.out.println("La referencia del array dentro del metodo es: " + array);

    }
    
    public static void main(String[] args) {
        
        int[] array = new int[3];

        System.out.println("La referencia del array fuera del metodo es: " + array);
        imprimirReferenciaArray(array);

    }
    
}
