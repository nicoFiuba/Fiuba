import java.util.Arrays;
import java.util.Random;

class Vector {
    
    private int[] elementos;
    private int capacidad;
    private int contador;

    public Vector(int capacidadInicial) {
        
        this.capacidad = capacidadInicial;
        this.elementos = new int[capacidadInicial];
        this.contador = 0;
    
    }

    public int tamaño() {
        return contador;
    }

    public int getIndice(int indice) {
        
        if (indice < 0 || indice >= contador) {
            throw new IndexOutOfBoundsException("Índice fuera de rango");
        }

        return elementos[indice];
    }
    
    private void redimensionar() {
        
        int nuevaCapacidad = (int) (capacidad * 2);
        
        if (nuevaCapacidad <= capacidad) {
            nuevaCapacidad = capacidad + 1;
        }
        
        int[] nuevosElementos = new int[nuevaCapacidad];
        System.arraycopy(elementos, 0, nuevosElementos, 0, contador);
        
        this.elementos = nuevosElementos;
        this.capacidad = nuevaCapacidad;
        
    }
    
    public void agregar(int elemento) {
        
        if (contador == capacidad) {
            redimensionar();
        }
        
        elementos[contador] = elemento;
        contador++;
    
    }

    public void ordenar() {
        Arrays.sort(elementos, 0, contador);
    }

    @Override
    public String toString() {
        
        StringBuilder stringBuilder = new StringBuilder();
        
        stringBuilder.append("[");
        
        for (int i = 0; i < contador; i++) {
            stringBuilder.append(elementos[i]);
            
            if (i < contador - 1) {
                stringBuilder.append(", ");
            }

        }

        stringBuilder.append("]");
            
        return stringBuilder.toString();
    }
}

public class Ejercicio1 {

    public static void main(String[] args) {
        
        Random random = new Random();
        Vector vector = new Vector(10);

        for (int i = 0; i < 10; i++) {
            vector.agregar(i);
        }

        System.out.println("Vector inicial: " + vector);

        for (int i = 0; i < 100; i++) {
            int numeroAleatorio = (int) (Math.random() * 100);
            
            vector.agregar(numeroAleatorio);
        }

        System.out.println("Vector luego de agregarle 100 numeros: " + vector);
        
        vector.ordenar();
        
        System.out.println("Vector después de ordenar: " + vector);

        System.out.println("Vector en orden inverso");

        System.out.println("[");

        for (int i = vector.tamaño() - 1; i >= 0; i--) {
            System.out.print(vector.getIndice(i));
            
            if (i > 0) {
                System.out.print(", ");
            }
        }

        System.out.println("]");
        
    }

}
