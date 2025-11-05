import java.util.NoSuchElementException;

class Cola {

    private int[] elementos;
    private int frente;
    private int fin;
    private int contador;
    private int capacidad;

    public Cola(int capacidadInicial) {

        this.capacidad = capacidadInicial;
        this.elementos = new int[capacidadInicial];
        this.frente = 0;
        this.fin = 0;
        this.contador = 0;
    }

    public boolean estaVacia() {
        return contador == 0;
    }

    public void redimencionar() {

        int nuevaCapacidad = capacidad * 2;
        int[] nuevosElementos = new int[nuevaCapacidad];

        for (int i = 0; i < contador; i++) {
            nuevosElementos[i] = elementos[(frente + i) % capacidad];
        }

        elementos = nuevosElementos;
        capacidad = nuevaCapacidad;
        frente = 0;
        fin = contador;
    }

    public void encolar(int elemento) {

        if (contador == capacidad) {
            redimencionar();
        }

        elementos[fin] = elemento;
        fin = (fin + 1) % capacidad;
        contador++;

    }

    public int desencolar() {

        if (estaVacia()) {
            throw new NoSuchElementException("La cola está vacía");
        }

        int elemento = elementos[frente];
        elementos[frente] = 0;

        frente = (frente + 1) % capacidad;
        contador--;

        return elemento;
    }

    public int obtenerTope() {

        if (estaVacia()) {
            throw new NoSuchElementException("La cola está vacía");
        }

        return elementos[frente];
    }

}


public class Ejercicio5 {
    
    public static void main(String[] args) {

        Cola cola = new Cola(3);

        int[] elementosParaAgregar = {10, 20, 30, 40, 50};

        for (int elemento : elementosParaAgregar) {
            cola.encolar(elemento);
            System.out.println("ENCOLADO: " + elemento); 
        }

        System.out.println("Elementos agregados a la cola.");

        try {
            for (int i = 0; i < elementosParaAgregar.length; i++) {
                System.out.println("Elemento al frente: " + cola.obtenerTope() + " | Elemeto eliminado: " + cola.desencolar());
            }

            System.out.println("La cola está vacía? " + cola.estaVacia());

            System.out.println("Intentando desencolar en una cola vacía...");
            cola.desencolar();

        } catch (NoSuchElementException e) {
            System.err.println("ERROR ATTRAPADO: " + e.getClass().getSimpleName() + ". No se puede desencolar.");
        }
        
    }
}
