import java.util.Scanner;

public class Ejercicio7 {
    
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        double num1, num2;

        System.out.print("Ingrese un  numero real: ");
        num1 = scanner.nextDouble();

        System.out.print("Ingrese otro numero real: ");
        num2 = scanner.nextDouble();

        if (num1 > num2){
            System.out.println("El mayor de los numeros ingresados es: " + num1);
        } else if (num2 > num1){
            System.out.println("El mayor de los numeros ingresados es: " + num2);
        } else{
            System.out.println("Los numeros ingresados son iguales");
        }

        scanner.close();
    }
}
