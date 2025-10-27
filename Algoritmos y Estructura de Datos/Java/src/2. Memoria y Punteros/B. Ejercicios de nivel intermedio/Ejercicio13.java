public class Ejercicio13 {
    
    public static void main(String[] args) {

        Integer entero = 128;
        Integer otroEntero = 128;

        if (entero == otroEntero) {
            System.out.println("Son iguales, use el operador ==");
        } else {
            System.out.println("No son iguales con el operador =="); 
        }

        if (entero.equals(otroEntero)) {
            System.out.println("Son iguales, use el método equals");
        } else {
            System.out.println("No son iguales con el método equals");
        }

        // En este caso como 128 está fuera del rango de -128 a 127, dará false al comparar con ==. Pero si el numero fuera menor a 128 y mayor que -128, daría true.
    }
}
