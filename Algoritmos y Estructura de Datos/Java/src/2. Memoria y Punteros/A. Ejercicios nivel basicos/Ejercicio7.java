public class Ejercicio7 {
    
    static int cambiarValor(int valor) {
        
        valor = 10;
        return valor;
    }

    public static void main(String[] args) {
        
        int numero = 5;
        System.out.println("Antes de cambiarValor: " + numero);
        cambiarValor(numero);
        System.out.println("Después de cambiarValor: " + numero);
    }
}
