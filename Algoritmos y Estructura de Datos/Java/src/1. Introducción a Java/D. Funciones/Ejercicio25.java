import java.util.Scanner;

public class Ejercicio25 {
    
    static boolean numeroPrimo (int numero){
        
        boolean esPrimo = true;
        
        if (numero <2) {
            esPrimo = false;
        } else {

            int i = 2;
            
            while(i <= Math.sqrt(numero) && esPrimo) {
                if (numero % i == 0) {
                    esPrimo = false;
                }
                i++;
            }
        }
        
        return esPrimo;
    }
    
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int numero;

        System.out.print("Ingrese un numero entero: ");
        numero = scanner.nextInt();

        boolean esPrimo = numeroPrimo(numero);

        if (esPrimo) {
            System.out.println("El numero " + numero + " es primo.");
        } else {
            System.out.println("El numero " + numero + " no es primo.");
        }

        scanner.close();
    }
}
