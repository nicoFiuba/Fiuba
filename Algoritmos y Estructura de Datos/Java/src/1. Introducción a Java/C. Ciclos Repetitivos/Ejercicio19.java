import java.util.Scanner;

public class Ejercicio19 {

    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        int numero;
        int mayor1 = Integer.MIN_VALUE;
        int mayor2 = Integer.MIN_VALUE;
        int mayor3 = Integer.MIN_VALUE;
        boolean programaActivo = true;

        int contador = 0;

        while (programaActivo) {
            System.out.print("Ingrese un número (0 para terminar): ");
            numero = scanner.nextInt();

            if (numero == 0){
                programaActivo = false;
                System.out.println("El programa ha finalizado.");
            } else {
                contador++;
                
                if (numero > mayor1){
                    mayor3 = mayor2;
                    mayor2 = mayor1;
                    mayor1 = numero;
                } else if (numero > mayor2){
                    mayor3 = mayor2;
                    mayor2 = numero;
                } else if (numero > mayor3){
                    mayor3 = numero;
                }
            }
        }

        if (contador < 3){
            System.out.println("No se ingresaron suficientes números para determinar los tres mayores.");
        } else {
            System.out.println("Los tres numeros mayores son: " + mayor1 + ", " + mayor2 + ", " + mayor3);
        }
        
        scanner.close();
    }
}
