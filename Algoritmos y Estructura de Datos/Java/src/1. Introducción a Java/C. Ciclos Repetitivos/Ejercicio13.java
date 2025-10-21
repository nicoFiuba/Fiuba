import java.util.Scanner;

public class Ejercicio13 {

    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        int numero;

        System.out.print("Ingrese un numero entero: ");
        numero = scanner.nextInt();

        for(int i = numero +1; i <= numero + 20; i++){
            System.out.println(i);
        }

        scanner.close();
    }
}
