public class Ejercicio5 {

    public static void main(String[] args) {

        int entero = 10;
        float flotante;
        double doble;

        System.out.println("Conversión implícita");

        flotante = entero;
        System.out.println("Entero a flotante: " + flotante);

        doble = flotante;
        System.out.println("Flotante a doble: " + doble);

        System.out.println("\nConversión explicita");

        double doble2 = 45.67;
        float flotante2;
        int entero2;

        flotante2 = (float) doble2;
        System.out.println("Doble a flotante: " + flotante2);

        entero2 = (int) flotante2;
        System.out.println("Flotante a entero: " + entero2);

    }
}
