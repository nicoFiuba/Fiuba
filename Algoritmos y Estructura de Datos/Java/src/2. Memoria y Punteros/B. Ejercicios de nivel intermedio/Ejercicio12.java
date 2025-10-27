class NumberHolder{
    
    int number;

}

public class Ejercicio12 {

    static void swap(NumberHolder a, NumberHolder b) {

        a.number += b.number;
        b.number = a.number - b.number;
        a.number -= b.number;
    }

    public static void main(String[] args) {

        NumberHolder x = new NumberHolder();
        NumberHolder y = new NumberHolder();

        x.number = 10;
        y.number = 20;

        System.out.println("Antes del intercambio:");
        System.out.println("x = " + x.number);
        System.out.println("y = " + y.number);

        swap(x, y);

        System.out.println("Después del intercambio:");
        System.out.println("x = " + x.number);
        System.out.println("y = " + y.number);

    }
}
