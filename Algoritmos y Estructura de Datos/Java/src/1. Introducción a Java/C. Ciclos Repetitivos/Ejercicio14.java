import java.util.Scanner;

public class Ejercicio14 {
    
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        int numero;
        int factorial = 1;

        System.out.print("Ingrese un numero entero: ");
        numero = scanner.nextInt();

        if (numero <0){
            System.out.println("No se puede calcular el factorial de un numero negativo.");
        } else {
            for(int i = 1; i <= numero; i++){
                factorial *= i;
            }
            System.out.println("El factorial de " + numero + " es: " + factorial);
        }   
        
        scanner.close();
    }
}
