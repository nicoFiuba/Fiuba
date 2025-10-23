import java.util.Scanner;

public class Ejercicio20 {
    
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        String nombre;
        double salario;
        double salaroMaximo = Double.NEGATIVE_INFINITY;
        double salarioMinimo = Double.POSITIVE_INFINITY;
        String personaConSalarioMax = "";
        String personaConSalarioMin = "";
        boolean programaActivo = true;

        int contadorPersonas = 0;

        while (programaActivo) {
            System.out.println("Ingrese los datos de la persona:");
            
            System.out.print("Nombre: ");
            nombre = scanner.nextLine();
            
            System.out.print("Salario: ");
            salario = scanner.nextDouble();
            scanner.nextLine(); // Limpiar el buffer

            contadorPersonas++;

            if (salario > salaroMaximo) {
                salaroMaximo = salario;
                personaConSalarioMax = nombre;
            }

            if (salario < salarioMinimo) {
                salarioMinimo = salario;
                personaConSalarioMin = nombre;
            }

            System.out.print("¿Desea ingresar otra persona? (s/n): ");
            char respuesta = scanner.nextLine().toLowerCase().charAt(0);

            while (respuesta != 's' && respuesta != 'n') {
                System.out.print("Respuesta inválida. Por favor ingrese 's' para sí o 'n' para no: ");
                respuesta = scanner.nextLine().toLowerCase().charAt(0);
            }

            if (respuesta == 'n') {
                programaActivo = false;
            }
        }

        if (contadorPersonas == 0){
            System.out.println("No se ingresaron datos de personas.");
        } else {
            System.out.println("Persona con salario máximo: " + personaConSalarioMax + " - Salario: " + salaroMaximo);
            System.out.println("Persona con salario mínimo: " + personaConSalarioMin + " - Salario: " + salarioMinimo);
        }

        scanner.close();
    }
}
