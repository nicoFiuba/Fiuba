import java.util.NoSuchElementException;

class ColaCircular {

    private String[] elementos;
    private int capacidad;
    private int frente;
    private int fin;
    private int contador;

    public ColaCircular(int capacidadInicial) {

        this.capacidad = capacidadInicial;
        this.elementos = new String[capacidadInicial];
        this.frente = 0;
        this.fin = 0;
        this.contador = 0;

    }

    public boolean estaVacia() {
        return contador == 0;
    }

    public void redimensionar() {

        int nuevaCapacidad = capacidad * 2;

        String[] nuevosElementos = new String[nuevaCapacidad];

        for (int i = 0; i < contador; i++) {
            nuevosElementos[i] = elementos[(frente + i) % capacidad];
        }

        elementos = nuevosElementos;
        capacidad = nuevaCapacidad;
        frente = 0;
        fin = contador;

    }

    public void encolar(String elemento) {

        if (contador == capacidad) {
            redimensionar();
        }

        elementos[fin] = elemento;
        fin = (fin + 1) % capacidad;
        contador++;

    }

    public String desencolar() {

        if (estaVacia()) {
            throw new NoSuchElementException();
        }

        String elemento = elementos[frente];
        elementos[frente] = null;

        frente = (frente + 1) % capacidad;
        contador--;

        return elemento;
    }

    public String obtenerTope() {

        if (estaVacia()) {
            throw new NoSuchElementException("La cola está vacía.");
        }

        return elementos[frente];
    }
}

public class Ejercicio11 {
    
    public static void main(String[] args) {

        ColaCircular cola = new ColaCircular(3); 
        
        cola.encolar("Tarea A");
        cola.encolar("Tarea B");
        cola.encolar("Tarea C");

        System.out.println("Frente -> " + cola.obtenerTope());
        
        cola.encolar("Tarea D (Desborde)"); 
        System.out.println("Capacidad aumentada. Frente -> " + cola.obtenerTope());
        
        System.out.println("DESENCOLAR: " + cola.desencolar()); 
        System.out.println("Frente actual: " + cola.obtenerTope());
        
        System.out.println("DESENCOLAR: " + cola.desencolar()); 
        System.out.println("Frente actual: " + cola.obtenerTope()); 
        
        try {
            cola.desencolar(); 
            cola.desencolar(); 
            
            System.out.println("La cola está vacía. Intento de DESENCOLAR...");
            cola.desencolar();
            
        } catch (NoSuchElementException e) {
            System.err.println("ERROR ATRAPADO: La operación de extracción falló porque la cola está vacía.");
        }

    }
}
