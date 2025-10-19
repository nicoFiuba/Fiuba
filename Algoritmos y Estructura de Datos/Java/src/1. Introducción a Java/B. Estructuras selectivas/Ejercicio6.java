import java.util.Scanner;

public class Ejercicio6 {
    
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        double numero;

        System.out.print("Ingrese un numero real: ");
        numero = scanner.nextDouble();

        if (numero > 0){
            System.out.println("El numero es mayor a cero");
        } else if (numero < 0) {
            System.out.println("El numero es menor a cero");
        } else{
            System.out.println("El numero es igual a cero");
        }

        scanner.close();
    }
}
