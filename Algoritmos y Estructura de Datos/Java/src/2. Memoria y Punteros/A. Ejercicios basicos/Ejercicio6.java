class Entero {

    int valor;

}

public class Ejercicio6 {
    
    public static void main(String[] args) {

        final double PI = 3.1416;

        // PI = 3.14;  Esto generará un error de compilación

        final Entero pi = new Entero();
        pi.valor = 31416;

        System.out.println("Valor inicial de pi: " + pi.valor);

        pi.valor = 30; // Esto es válido

        System.out.println("Valor modificado de pi: " + pi.valor);

        Entero pi2 = new Entero();
        pi2.valor = 31416;
        // pi = pi2;  Esto generará un error de compilación
    }
}
