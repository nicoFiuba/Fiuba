import java.util.Scanner;

public class Ejercicio15 {
    
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        double numero;
        double suma = 0;
        double sumaParcial = 0;
        boolean programaActivo = true;

        while (programaActivo){
            System.out.print("Ingrese un numero real (0 para finalizar): ");
            numero = scanner.nextDouble();
            
            if (numero != 0){
                suma += numero;
                
                System.out.println("La suma es: " + sumaParcial + " + " + numero + " = " + suma);
                
                sumaParcial = suma;
            } else {
                programaActivo = false;
                
                System.out.println("Ingresaste 0, el programa ha finalizado.");
            }
        }
        
        /* En el do-while la linea boolean programaActivo = true; no es necesaria
        do {
            System.out.print("Ingrese un numero real (0 para finalizar): ");
            numero = scanner.nextDouble();
            
            suma += numero;

            if (numero != 0){
                System.out.println("La suma es: " + sumaParcial + " + " + numero + " = " + suma);
                
                sumaParcial = suma;
            }
        } while(numero != 0); 
        
        System.out.println("Ingresaste 0, el programa ha finalizado.");
         */

        scanner.close();
    }
}
