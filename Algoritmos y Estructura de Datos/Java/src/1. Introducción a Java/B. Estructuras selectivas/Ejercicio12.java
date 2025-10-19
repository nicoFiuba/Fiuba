import java.util.Scanner;

public class Ejercicio12 {
    
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        int segundos;

        System.out.print("Ingrese los segundos a convertir: ");
        segundos = scanner.nextInt();

        if(segundos >= 0){
            int horas = segundos / 3600;
            int minutos = (segundos % 3600) /60;
            int segundosRestantes = segundos % 60;

            System.out.println("Lo que ingresaste equivale a: " + horas + " hora/s, " + minutos + " minuto/s y " + segundosRestantes + " segundo/s.");
        } else if (segundos < 0){
            System.out.println("No podes ingresar segundos negativos.");
        }

        scanner.close();
    }
}
