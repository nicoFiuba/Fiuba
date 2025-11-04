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

    private void redimensionar() {

        int nuevaCapacidad = capacidad * 2;
        int[] nuevosElementos = new int[nuevaCapacidad];
        
        System.arraycopy(elementos, 0, nuevosElementos, 0, elementos.length);
        
        elementos = nuevosElementos;
        capacidad = nuevaCapacidad;

    }

    public void push(int elemento) {
        
        if (cima == capacidad - 1) {
            redimensionar();
        }
        
        elementos[++cima] = elemento;

    }

    public int pop() {
        
        if (estaVacia()) {
            throw new EmptyStackException();
        }
        
        return elementos[cima--];
    }

    public int peek() {
        
        if (estaVacia()) {
            throw new EmptyStackException();
        }
        
        return elementos[cima];
    }
}


public class Ejercicio7 {
    
    public static void main(String[] args) {
        
        Pila pila = new Pila(2);
        
        pila.push(10);
        System.out.println("Cima de la pila: " + pila.peek()); 

        pila.push(20);
        System.out.println("Cima de la pila: " + pila.peek()); 

        pila.push(30); 
        System.out.println("Cima de la pila: " + pila.peek()); 
        
        System.out.println("Elemento desapilado: " + pila.pop()); 
        System.out.println("Cima de la pila después de pop: " + pila.peek()); 
        
    }
}
