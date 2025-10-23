import java.util.Scanner;

public class Ejercicio21 {
    

    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        int cantidadNumeros = 0;
        boolean ascendente = true;
        boolean descendente = true;
        
        System.out.print("Ingrese la cantidad de numeros que quiere ingresar: ");
        cantidadNumeros = scanner.nextInt();

        while (cantidadNumeros < 2){
            System.out.print("Se necesitan dos numeros o mas para poder analizar. Ingrese nuevamente la cantidad de numeros: ");
            cantidadNumeros = scanner.nextInt();
        }
        
        System.out.print("Ingrese el numero 1: ");
        double numeroAnterior = scanner.nextDouble();
        
        for (int i = 2; i <= cantidadNumeros; i++){
            System.out.print("Ingrese el numero: " + i + ": ");
            double numeroActual = scanner.nextDouble();
            
            if (numeroActual < numeroAnterior){
                ascendente = false;
            }
            
            if (numeroActual > numeroAnterior){
                descendente = false;
            }
            
            numeroAnterior = numeroActual;
        }

        if (ascendente){
            System.out.println("Los numeros estan en orden ascendente");
        } else if (descendente){
            System.out.println("Los numeros estan en orden descendente");
        } else {
            System.out.println("Los numeros no estan ordenados");
        }

        scanner.close();
    }
}
