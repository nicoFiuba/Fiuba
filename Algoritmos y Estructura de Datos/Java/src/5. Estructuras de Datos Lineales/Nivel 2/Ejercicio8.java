import java.util.ArrayList;
import java.util.EmptyStackException;

class Pila {

    private int[] elementos;
    private int cima;
    private int capacidad;

    public Pila(int capacidadInicial) {
        
        this.capacidad = capacidadInicial;
        this.elementos = new int[capacidadInicial];
        this.cima = -1;
    
    }

    public boolean estaVacia() {
        return cima == -1;
    }

    public void redimensionar(int nuevaCapacidad) {
        
        int[] nuevosElementos = new int[nuevaCapacidad];
        
        System.arraycopy(elementos, 0, nuevosElementos, 0, Math.min(elementos.length, nuevaCapacidad));
        
        elementos = nuevosElementos;
        capacidad = nuevaCapacidad;
    
    }

    public void push(int elemento) {

        if (cima < capacidad - 1) {
            elementos[++cima] = elemento;
        } else {
            System.err.println("Pila llena. No se puede agregar el elemento: " + elemento);
        }

    }

    public int pop() {
        
        if (estaVacia()) {
            throw new EmptyStackException();
        }

        return elementos[cima--];
    }

}

public class Ejercicio8 {
    
    public static ArrayList<Integer> invertirLista(ArrayList<Integer> lista) {
        
        Pila pilaTemporal = new Pila(lista.size() * 2);
        
        for (int elemento : lista) {
            pilaTemporal.push(elemento);
        }
        
        ArrayList<Integer> listaInvertida = new ArrayList<>();
        
        while (!pilaTemporal.estaVacia()) {
            try {
                int elemento = pilaTemporal.pop();
    
                listaInvertida.add(elemento);
            } catch (EmptyStackException e) {
                System.err.println("Error al invertir la lista: " + e.getMessage());
            }
        }
    
        return listaInvertida;
    }

    public static void main(String[] args) {
        
        ArrayList<Integer> listaOriginal = new ArrayList<>();
        
        listaOriginal.add(1);
        listaOriginal.add(2);
        listaOriginal.add(3);
        listaOriginal.add(4);
        listaOriginal.add(5);
        
        System.out.println("Lista original: " + listaOriginal);
        
        ArrayList<Integer> listaInvertida = invertirLista(listaOriginal);
        
        System.out.println("Lista invertida: " + listaInvertida);
    
    }
}
