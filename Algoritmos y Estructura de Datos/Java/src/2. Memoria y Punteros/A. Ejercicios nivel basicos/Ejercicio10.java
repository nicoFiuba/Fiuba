public class Ejercicio10 {
    
    public static void main(String[] args) {

        int x = 10;
        String texto = "Hola";
        String otroTexto = new String("Hola");

        System.out.println("Comparaciones con == y .equals(): ");
        System.out.println("x == 10: " + (x == 10)); // true
        // System.out.println("x.equals(10): " + x.equals(10)); // Error de compilación
        System.out.println("El .equals() no se puede usar con tipos primitivos como int.");

        System.out.println("Texto == Hola: " + (texto == "Hola")); // true
        System.out.println("Texto.equals(Hola): " + texto.equals("Hola")); // true
        System.out.println("OtroTexto == Hola: " + (otroTexto == "Hola")); // false
        System.out.println("OtroTexto.equals(Hola): " + otroTexto.equals("Hola")); // true

        System.out.println(" PARA TIPOS PRIMITIVOS (int, char, boolean, etc.), use '==' para comparar valores.");
        System.out.println(" PARA OBJETOS (String, Integer, etc.), use '.equals()' para comparar contenidos.");

    }
}
