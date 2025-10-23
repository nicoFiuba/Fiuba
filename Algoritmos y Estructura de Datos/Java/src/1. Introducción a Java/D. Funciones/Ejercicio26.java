import java.util.Scanner;

public class Ejercicio26 {
    
    static void raices(double a, double b, double c) {
        
        if (a == 0){
            System.out.println("No es una ecuacion de segundo grado.");
        } else {
            double discriminante = Math.pow(b, 2) - 4 * a * c;

            if (discriminante == 0){
                System.out.println("La ecuacion tiene una unica raiz real y es: " + (-b / (2 * a)));
            } else {
                double raiz1 = (-b + Math.sqrt(discriminante)) / (2 * a);
                double raiz2 = (-b - Math.sqrt(discriminante)) / (2 * a);
                
                System.out.println("Las raices son: " + raiz1 + " y " + raiz2);
            }
        }
    }

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
            raices(a, b, c);
        } else {
            System.out.println("La ecuacion no tiene raices reales.");
        }
        
        scanner.close();
    }
}
