import java.util.Scanner;

public class Ejercicio27 {
    
    static int calcularMCD(int num1, int num2) {
        
        int x = Math.abs(num1);
        int y = Math.abs(num2);

        while (y != 0) {
            int valorTemporal = y;
            y = x % y;
            x = valorTemporal;
        }
        return x;
    }
    
    static int calcularMCM(int x, int y, int mcd) {
        
        int mcm;

        if (mcd == 0){
            mcm = 0;
        } else {
            mcm = Math.abs(x * y) / mcd;
        }

        return mcm;
    }
    
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        
        int num1, num2;

        System.out.print("Ingrese un número entero: ");
        num1 = scanner.nextInt();

        System.out.print("Ingrese otro número entero: ");
        num2 = scanner.nextInt();

        int mcd = calcularMCD(num1, num2);
        int mcm = calcularMCM(num1, num2, mcd);

        System.out.println("El maximo común divisor (MCD) de " + num1 + " y " + num2 + " es: " + mcd);
        System.out.println("El mínimo común múltiplo (MCM) de " + num1 + " y " + num2 + " es: " + mcm);

        scanner.close();
    }
}
