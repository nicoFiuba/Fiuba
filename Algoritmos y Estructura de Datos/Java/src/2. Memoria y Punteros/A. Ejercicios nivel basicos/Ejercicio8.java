public class Ejercicio8 {

    static void cambiarValor(int[] arreglo) {
        
        arreglo[0] = 10;
    }

    public static void main(String[] args) {
        
        int[] numeros = {5};
        System.out.println("Antes de cambiarValor: " + numeros[0]);
        cambiarValor(numeros);
        System.out.println("Después de cambiarValor: " + numeros[0]);
    }
    
}
