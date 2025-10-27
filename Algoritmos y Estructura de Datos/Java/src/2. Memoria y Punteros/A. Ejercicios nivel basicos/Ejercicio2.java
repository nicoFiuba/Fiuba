class Entero {
    
    int valor;
}

public class Ejercicio2 {
    
    public static void main(String[] args) {

        Entero entero = new Entero();
        entero.valor = 5;

        System.out.println("La referencia del entero es: " + entero);
        System.out.println("El valor del entero es: " + entero.valor);

    }
}
