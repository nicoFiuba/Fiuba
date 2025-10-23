class Entero{

    int valor;

}

public class Ejercicio3 {
    
    public static void main(String[] args) {

        for (int i = 1; i <= 5; i++) {
            Entero entero = new Entero();
            entero.valor = 5;

            System.out.println("En la vuelta " + i + ":");
            System.out.println("La referencia del entero es: " + entero);
            System.out.println("El valor del entero es: " + entero.valor);
        }
    }
}
