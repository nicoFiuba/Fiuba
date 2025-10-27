class Entero {

    int valor;

}

public class Ejercicio17 {

    public static void main(String[] args) {
        
        Entero numero = new Entero();
        numero.valor = 5;

        Entero numero2 = numero;

        System.out.println("Valor de numero: " + numero.valor);
        System.out.println("La referencia de numero es: " + numero);

        System.out.println("La referencia de numero2 es: " + numero2);
        System.out.println("Valor de numero2: " + numero2.valor);

    }
    
    // la referencia anterior es la misma porque ambos apuntan al mismo objeto en memoria
}
