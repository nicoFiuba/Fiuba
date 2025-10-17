import java.util.Scanner;

public class Ejercicio5 {
    
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        double base, altura;

        System.out.print("Ingrese una base para su rectangulo: ");
        base = scanner.nextDouble();

        System.out.print("Ingrese una altura para su rectangulo: ");
        altura = scanner.nextDouble();

        double perimetro = 2 * (base + altura);
        double superficie = base * altura;

        System.out.println("El perimetro de su rectangulo es: " + perimetro);
        System.out.println("La superficie de su rectangulo es: " + superficie);

        scanner.close();
    }
}
