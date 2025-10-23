import java.util.Scanner;

public class Ejercicio24 {
    
    static boolean tieneRaices(double a, double b, double c) {
        
        double discriminante = Math.pow(b, 2) - 4 * a * c;
        boolean existenSusRaices = true;
        
        if (discriminante < 0) {
            existenSusRaices = false;
        }

        return existenSusRaices;
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        double a, b, c;

        System.out.print("Ingrese el valor de a: ");
        a = scanner.nextDouble();

        System.out.print("Ingrese el valor de b: ");
        b = scanner.nextDouble();

        System.out.print("Ingrese el valor de c: ");
        c = scanner.nextDouble();

        boolean tieneRaices = tieneRaices(a, b, c);

        if (tieneRaices) {
            System.out.println("La ecuacion tiene raices reales.");
        } else {
            System.out.println("La ecuacion no tiene raices reales.");
        }

        scanner.close();
    }
}
