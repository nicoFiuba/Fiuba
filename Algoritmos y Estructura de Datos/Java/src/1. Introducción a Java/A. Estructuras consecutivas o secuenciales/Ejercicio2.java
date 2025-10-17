import java.util.Scanner;

public class Ejercicio2 {

    public static void main (String[] args){

        Scanner scanner = new Scanner(System.in);
        
        int num1, num2;
        
        System.out.print("Ingrese el primer numero entero: ");
        num1 = scanner.nextInt();

        System.out.print("Ingrese el segundo numero: ");
        num2 = scanner.nextInt();

        int suma = num1 + num2;
        int resta = num1 - num2;
        int multiplicacion = num1 * num2;
        double division = (double) num1 / num2;

        System.out.println("La suma es: " + suma);
        System.out.println("La resta es: " + resta);
        System.out.println("La multiplicacion es: " + multiplicacion);
        System.out.println("La division es: " + division);

        scanner.close();
    }
}
