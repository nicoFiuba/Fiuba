import java.util.Scanner;
public class Ejercicio17 {
    
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        int numero;
        int contadorMax = 0;
        int contadorMin = 0;
        int maximo = Integer.MIN_VALUE;
        int minimo = Integer.MAX_VALUE;
        boolean programaAtivo = true;

        
        while (programaAtivo){
            System.out.print("Ingrese un numero entero (0 para finalizar): ");
            numero = scanner.nextInt();

            if (numero == 0){
                programaAtivo = false;
                System.out.println("El programa ha finalizado.");
            } else {
                
                if (numero > maximo){
                    maximo = numero;
                    contadorMax = 1;
                } else if (numero == maximo){
                    contadorMax++;
                }
                
                if (numero < minimo){
                    minimo = numero;
                    contadorMin = 1;
                } else if (numero == minimo){
                    contadorMin++;
                }
            }
        }

        if (contadorMax == 0 && contadorMin == 0) {
            System.out.println("No se ingresaron numeros validos.");
        } else {
            System.out.println("El numero maximo es: " + maximo + " y se ingreso " + contadorMax + " veces.");
            System.out.println("El numero minimo es: " + minimo + " y se ingreso " + contadorMin + " veces.");
        }

        scanner.close();
    }
}
