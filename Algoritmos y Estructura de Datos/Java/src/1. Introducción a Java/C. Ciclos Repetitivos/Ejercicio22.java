public class Ejercicio22 {
    
    public static void main(String[] args) {

        System.out.println("Fahrenheit - Celsius");

        for (int fahrenheit = 0; fahrenheit <= 200; fahrenheit += 10) {
            double celsius = 5/9.0 * (fahrenheit - 32);
            
            System.out.printf("%5d°F %10.2f°C\n", fahrenheit, celsius); // %[banderas][ancho][.precision][tipo], en este caso %[5][d(entero)] y %[10][.2(numeros despues de la coma)][f(decimal)]
        }    
    }        
}
