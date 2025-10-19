import java.util.Scanner;

public class Ejercicio8 {

    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        int numero;

        System.out.print("Ingrese un numero entero: ");
        numero = scanner.nextInt();

        if(numero%2 == 0){
            System.out.println("El numero ingresado es par");
        }

        scanner.close();
    }
}
