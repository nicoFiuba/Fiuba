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
            redimensionar(capacidad * 2);
            elementos[++cima] = elemento;
        }

    }

    public int pop() {

        if (estaVacia()) {
            throw new IllegalStateException("La pila está vacía"); // Porque usas IllegalStateException y no EmptyStackException? rta: Porque EmptyStackException es específica de la clase Stack y aquí estamos implementando nuestra propia pila.
        }

        int elemento = elementos[cima--];

        if (cima + 1 <= capacidad / 4 && capacidad / 2 >= 1) {
            redimensionar(capacidad / 2);
        }

        return elemento;
    }

    public int peek() {

        if (estaVacia()) {
            throw new IllegalStateException("La pila está vacía");
        }

        return elementos[cima];
    }
}

class PilaConMin {

    private Pila pilaDatos;
    private Pila pilaMinimos;

    public PilaConMin(int capacidad) {
        
        pilaDatos = new Pila(capacidad);
        pilaMinimos = new Pila(capacidad);
    
    }

    public void push(int elemento) {
        
        pilaDatos.push(elemento);
        
        if (pilaMinimos.estaVacia() || elemento <= pilaMinimos.peek()) {
            pilaMinimos.push(elemento);
        }
    
    }

    public int pop() {
        
        int elemento = pilaDatos.pop();
        
        if (elemento == pilaMinimos.peek()) {
            pilaMinimos.pop();
        }
        
        return elemento;
    
    }

    public int getMin() {
        
        if (pilaMinimos.estaVacia()) {
            throw new IllegalStateException("La pila está vacía");
        }
        
        return pilaMinimos.peek();
    
    }

    public int peek() {
        return pilaDatos.peek();
    }
}

public class Ejercicio13 {

    public static void main(String[] args) {
        
        PilaConMin pila = new PilaConMin(10); 

        pila.push(8);
        System.out.println("Tope: " + pila.peek() + " | Mínimo: " + pila.getMin());

        pila.push(5);
        System.out.println("Tope: " + pila.peek() + " | Mínimo: " + pila.getMin()); 

        pila.push(10);
        System.out.println("Tope: " + pila.peek() + " | Mínimo: " + pila.getMin()); 

        pila.push(5);
        System.out.println("Tope: " + pila.peek() + " | Mínimo: " + pila.getMin()); 
        
        System.out.println("POP: " + pila.pop() + " | Nuevo Tope: " + pila.peek() + " | Nuevo Mínimo: " + pila.getMin()); 
    
        System.out.println("POP: " + pila.pop() + " | Nuevo Tope: " + pila.peek() + " | Nuevo Mínimo: " + pila.getMin()); 

        System.out.println("POP: " + pila.pop() + " | Nuevo Tope: " + pila.peek() + " | Nuevo Mínimo: " + pila.getMin()); 

    }
    
}
