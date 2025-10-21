import java.util.Scanner;

public class Ejercicio16 {

    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        boolean programaActivo = true;
        double numero;
        char respuesta;
        int posicion = 0;
        double maximo = Double.NEGATIVE_INFINITY;
        double minimo = Double.POSITIVE_INFINITY;
        // int posicionMinimo = -1;
        String posicionesMaximas = "";
        // int posicionMaximo = -1;
        String posicionesMinimas = "";

        
        while (programaActivo){
            System.out.print("Ingrese un numero real: ");
            numero = scanner.nextDouble();
            posicion++;
            
            if (numero > maximo){
                maximo = numero;
                posicionesMaximas = "" + posicion;
            } else if (numero == maximo){
                posicionesMaximas += ", " + posicion;
            }
            
            if (numero < minimo){
                minimo = numero;
                posicionesMinimas = "" + posicion;
            } else if (numero == minimo){
                posicionesMinimas += ", " + posicion;
            } 
            
            System.out.print("Desea ingresar otro numero? (s/n): ");
            respuesta = scanner.next().toLowerCase().charAt(0);
            
            while (respuesta != 's' && respuesta != 'n'){
                System.out.println("Respuesta no valida");
                
                System.out.print("Desea ingresar otro numero? (s/n): ");
                respuesta = scanner.next().toLowerCase().charAt(0);
            }
            
            if (respuesta == 'n'){
                programaActivo = false;
            }
        }
        
        System.out.println("El numero maximo es: " + maximo + " y se encuentra en la/s posicion/es: " + posicionesMaximas);
        System.out.println("El numero minimo es: " + minimo + " y se encuentra en la/s posicion/es: " + posicionesMinimas);
        
        scanner.close();
    }
}
