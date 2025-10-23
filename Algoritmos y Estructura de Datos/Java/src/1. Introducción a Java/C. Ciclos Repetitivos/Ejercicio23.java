import java.util.Scanner;

public class Ejercicio23 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int cantidadLotes = 1;
        double sumaTotal = 0;
        int contadorTotal = 0;
        
        System.out.print("Ingrese los lotes que va a ingresar: ");
        cantidadLotes = scanner.nextInt();

        for (int i = 1; i <= cantidadLotes; i++) {
            System.out.println("Lote " + i + ":");

            int contadorLote = 0;
            double sumaLote = 0;
            double numero;
            boolean programaActivo = true;

            while (programaActivo) {
                System.out.print("Ingrese un número real (0 para finalizar): ");
                numero = scanner.nextDouble();
                
                if (numero == 0){
                    programaActivo = false;
                    System.out.println("El lote " + i + " ha finalizado.");
                } else {
                    sumaLote += numero;
                    
                    contadorLote++;
                }
            }

            if (contadorLote > 0) {
                double mediaLote = sumaLote / contadorLote;
                System.out.println("La media del lote " + i + " es: " + mediaLote);
                
                sumaTotal += sumaLote;
                contadorTotal += contadorLote;
            } else {
                System.out.println("No se ingresaron números en el lote " + i + ".");
            }
        }

        if (contadorTotal > 0) {
            double mediaTotal = sumaTotal / contadorTotal;
            System.out.println("La media total de todos los lotes es: " + mediaTotal);
        } else {
            System.out.println("No se ingresaron números en ningún lote.");
        }

        scanner.close();
    }
}
