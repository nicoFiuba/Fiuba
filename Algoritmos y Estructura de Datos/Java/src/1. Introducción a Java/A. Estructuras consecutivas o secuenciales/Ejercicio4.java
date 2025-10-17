import java.util.Scanner;

public class Ejercicio4 {
    
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        double radio;

        System.out.print("Ingrese un radio: ");
        radio = scanner.nextDouble();

        double superficie = 4 * Math.PI * Math.pow(radio, 2);
        double volumen = (4.0/3.0) * Math.PI * Math.pow(radio, 3);

        System.out.println("La superficie es: " + superficie);
        System.out.println("El volumen es: " + volumen);

        scanner.close();
    }
}
