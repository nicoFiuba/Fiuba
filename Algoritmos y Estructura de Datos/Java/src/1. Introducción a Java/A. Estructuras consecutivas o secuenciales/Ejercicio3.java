import java.util.Scanner;

public class Ejercicio3 {

    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        String nombre;

        System.out.print("Ingrese su nombre: ");
        nombre = scanner.nextLine();

        System.out.print("Hola " + nombre);

        scanner.close();
    }
}
