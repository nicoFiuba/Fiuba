import java.util.EmptyStackException;

class Pila {

    private int[] elementos;
    private int capacidad;
    private int cima;

    public Pila(int capacidadInicial) {

        this.capacidad = capacidadInicial;
        this.elementos = new int[capacidadInicial];
        this.cima = -1;

    }

    public boolean estaVacia() {
        return cima == -1;
    }

    public void push(int elemento) {

        if (cima < capacidad - 1) {
            elementos[++cima] = elemento;
        } else {
            System.out.println("La pila está llena. No se puede agregar el elemento.");
        }

    }

    public int pop() {

        if (estaVacia()) {
            throw new EmptyStackException();
        }
        
        return elementos[cima--];
    }
}


public class Ejercicio10 {
    
    public static String decimalABinario(int numeroDecimal) {
        
        if (numeroDecimal < 0) {
            throw new IllegalArgumentException("El número debe positivo.");
        }

        if (numeroDecimal == 0) {
            return "0";
        }
        
        Pila pila = new Pila(32); 

        int numero = numeroDecimal;

        while (numero > 0) {
            int residuo = numero % 2;
            pila.push(residuo);
            numero /= 2;
        }

        StringBuilder numeroBinario = new StringBuilder();

        while (!pila.estaVacia()) {
            numeroBinario.append(pila.pop());
        }

        return numeroBinario.toString();
    }

    public static void main(String[] args) {
        int numeroDecimal = 42; 

        String numeroBinario = decimalABinario(numeroDecimal);
        
        System.out.println("El número decimal " + numeroDecimal + " en binario es: " + numeroBinario);
    
    }
}
