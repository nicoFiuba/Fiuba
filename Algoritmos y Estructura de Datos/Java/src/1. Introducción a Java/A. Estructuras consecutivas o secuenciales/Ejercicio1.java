import java.util.Scanner;

public class Ejercicio1{
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);
        
        int numero;
        
        System.out.print("Ingrese un numero entero: ");
        numero = scanner.nextInt();

        System.out.println("Numero ingresado = " + numero);

        scanner.close();
    }
}