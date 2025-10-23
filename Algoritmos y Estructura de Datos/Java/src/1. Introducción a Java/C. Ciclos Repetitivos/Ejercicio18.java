import java.util.Scanner;

public class Ejercicio18 {

    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        int num1, num2;
        int resultado = 0;

        System.out.print("Ingrese un numero entero: ");
        num1 = scanner.nextInt();

        System.out.print("Ingrese otro numero entero: ");
        num2 = scanner.nextInt();

        if (num1 == 0 || num2 == 0){
            System.out.println("El resultado de la multiplicacion es 0");
        } else if (num2 > 0) {
            
            System.out.print(num1);
            resultado = num1;

            for (int i = 2; i <= num2; i++){ 
                resultado += num1;
                
                if (num1 < 0) {
                    System.out.print(" " + num1); 
                } else {
                    System.out.print(" + " + num1);
                }
            }
            
            System.out.println(" = " + resultado);
        } else {
            int num1_inverso = -num1;
            
            System.out.print(num1_inverso);
            resultado = num1_inverso;

            for (int i = 2; i <= -num2; i++){ 
                resultado += num1_inverso;
                
                if (num1_inverso < 0) {
                    System.out.print(" " + num1_inverso);
                } else {
                    System.out.print(" + " + num1_inverso);
                }
            }
            
            System.out.println(" = " + resultado);
        }
        
        scanner.close();
    }
}
