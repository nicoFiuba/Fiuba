import java.util.Scanner;

public class Ejercicio11 {
    
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        char opcion;

        System.out.println("MENU DE OPCIONES");
        System.out.println("a) Agregar");
        System.out.println("b) Modificar");
        System.out.println("c) Eliminar");
        System.out.println("d) Salir");

        System.out.print("Elije una opcion: ");
        opcion = scanner.next().toLowerCase().charAt(0);

        switch(opcion){
            case 'a' -> System.out.println("Elegiste la opcion Agregar");
            case 'b' -> System.out.println("Elegiste la opcion Modificar");
            case 'c' -> System.out.println("Elegiste la opcion Eliminar");
            case 'd' -> System.out.println("Elegiste la opcion Salir");
            default -> System.out.println("Opcion no valida");
        }

        scanner.close();
    }
}
