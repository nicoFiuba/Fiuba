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

    public void sacarElementos() {
        
        if (contador == 0) {
            throw new IllegalStateException("El vector está vacío");
        }

        contador--;
    }

    public int sumarElementos() {
        
        int suma = 0;
        
        for (int i = 0; i < contador; i++) {
            suma += elementos[i];
        }

        return suma;
    }

    public double promedioElementos() {
        
        if (contador == 0) {
            throw new IllegalStateException("El vector está vacío");
        }

        return (double) sumarElementos() / contador;
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

public class Ejercicio3 {
    
    public static void main(String[] args) {
        
        Vector vector = new Vector(5);
        Random random = new Random();

        for (int i = 0; i < 5; i++) {
            vector.agregar(random.nextInt(1000));
        }

        System.out.println("Vector: " + vector);

        for (int i = 0; i < 1000; i++) {
            vector.agregar(random.nextInt(1000));
        }

        System.out.println("Vector después de agregar 1000 elementos: " + vector);

        for (int i = 0; i < 500; i++) {
            vector.sacarElementos();
        }

        System.out.println("Vector después de sacar 500 elementos: " + vector);

        System.out.println("Suma de los elementos del vector: " + vector.sumarElementos());
        System.out.println("Promedio de los elementos del vector: " + vector.promedioElementos());
        
    }
}
