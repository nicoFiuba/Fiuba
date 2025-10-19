import java.util.Scanner;

public class Ejercicio10 {
    
    public static void main(String[] args){
        
        Scanner scanner = new Scanner(System.in);

        double num1, num2;
        char operacion;

        System.out.print("Ingrese un numero: ");
        num1 = scanner.nextDouble();

        System.out.print("Ingrese otro numero: ");
        num2 = scanner.nextDouble();

        System.out.print("Ingrese la operacion que desea realizar (Suma: +, Resta: -, Multiplicacion: *, Division: /): ");
        operacion = scanner.next().charAt(0);

        switch(operacion){
            case '+' -> System.out.println("El resultado de la suma es: " + (num1 + num2));
            case '-' -> System.out.println("El resultado de la resta es: " + (num1 -num2));
            case '*' -> System.out.println("El resultado de la multiplicacion es: " + (num1*num2));
            case '/' ->{
                if(num2 == 0){
                    System.out.println("No se puede dividir por cero.");
                } else {
                    System.out.println("El resultado de la division es: " + (num1/num2));
                }
            }
            default -> System.out.println("Operacion no valida.");
        }
        
        scanner.close();
    }
}
