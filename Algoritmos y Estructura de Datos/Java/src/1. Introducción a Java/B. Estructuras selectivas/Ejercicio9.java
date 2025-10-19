import java.util.Scanner;

public class Ejercicio9 {
    
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        int num1, num2;

        System.out.print("Ingrese un numero entero: ");
        num1 =scanner.nextInt();

        System.out.print("Ingrese otro numero entero: ");
        num2 = scanner.nextInt();

        if(num2 != 0 && num1 % num2 == 0){
            System.out.println("El numero " + num1 + " es divisible por " + num2);
        }

        scanner.close();
    }
}
