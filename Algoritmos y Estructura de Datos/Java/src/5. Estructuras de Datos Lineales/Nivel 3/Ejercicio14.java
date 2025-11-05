import java.util.NoSuchElementException;

class ColaElementos {

    private String[] elementos;
    private int frente;
    private int fin;
    private int contador;
    private int capacidad;

    public ColaElementos(int capacidadInicial) {

        this.capacidad = capacidadInicial;
        this.elementos = new String[capacidadInicial];
        this.frente = 0;
        this.fin = 0;
        this.contador = 0;

    }

    public boolean estaVacia() {
        return contador == 0;
    }

    public int tamaño() {
        return contador;
    }

    public void encolar(String elemento) {

        if (contador == capacidad) {
            throw new IllegalStateException("La cola está llena");
        }

        elementos[fin] = elemento;
        fin = (fin + 1) % capacidad;
        contador++;
    }

    public String desencolar() {

        if (estaVacia()) {
            throw new IllegalStateException("La cola está vacía");
        }

        String elemento = elementos[frente];
        elementos[frente] = null;

        frente = (frente + 1) % capacidad;
        contador--;
        
        return elemento;
    }
}

class NodoPrioridad {

    int prioridad;
    ColaElementos elementos;
    NodoPrioridad siguiente;

    public NodoPrioridad(int prioridad, int capacidadCola) {

        this.prioridad = prioridad;
        this.elementos = new ColaElementos(capacidadCola);
        this.siguiente = null;

    }
}

class ColaDePrioridad {

    private NodoPrioridad cabeza;

    public ColaDePrioridad() {

        this.cabeza = null;

    }

    public void insertarTarea(String tarea, int prioridad) {

        NodoPrioridad nodoActual = buscadorNodoPrioridad(prioridad);

        if (nodoActual != null) {
            nodoActual.elementos.encolar(tarea);
        } else {
            insertarNodoPrioridad(prioridad);

            nodoActual = buscadorNodoPrioridad(prioridad);
            nodoActual.elementos.encolar(tarea);
        }

    }

    public String extraerTarea() {

        if (cabeza == null) {
            throw new NoSuchElementException("La cola de prioridad está vacía");
        }

        String tareaExtraida = cabeza.elementos.desencolar();

        if (cabeza.elementos.estaVacia()) {
            cabeza = cabeza.siguiente;
        }

        return tareaExtraida;
    }

    private NodoPrioridad buscadorNodoPrioridad(int prioridad) {

        NodoPrioridad nodoActual = cabeza;

        while (nodoActual != null) {
            if (nodoActual.prioridad == prioridad) {
                return nodoActual;
            }
            nodoActual = nodoActual.siguiente;
        }

        return null;
    }

    private void insertarNodoPrioridad(int prioridad) {

        NodoPrioridad nuevoNodo = new NodoPrioridad(prioridad, 10);

        if (cabeza == null || prioridad < cabeza.prioridad) {
            nuevoNodo.siguiente = cabeza;
            cabeza = nuevoNodo;
            
            return;
        }

        NodoPrioridad nodoActual = cabeza;

        while (nodoActual.siguiente != null && nodoActual.siguiente.prioridad < prioridad) {
            nodoActual = nodoActual.siguiente;
        }
        nuevoNodo.siguiente = nodoActual.siguiente;
        nodoActual.siguiente = nuevoNodo;
    }
}

public class Ejercicio14 {

    public static void main(String[] args) {
        
        ColaDePrioridad colaPrioridad = new ColaDePrioridad(); 
        
        
        colaPrioridad.insertarTarea("Reporte Básico", 3);
        
        colaPrioridad.insertarTarea("CORRECCIÓN CRÍTICA", 1); 
        
        colaPrioridad.insertarTarea("Reporte Diario", 3); 
        
        colaPrioridad.insertarTarea("Revisión Mensual", 2); 
        
        System.out.println("DESENCOLAR (P=1): " + colaPrioridad.extraerTarea()); 
        
        System.out.println("DESENCOLAR (P=2): " + colaPrioridad.extraerTarea()); 
        
        System.out.println("DESENCOLAR (P=3, FIFO 1): " + colaPrioridad.extraerTarea()); 

        System.out.println("DESENCOLAR (P=3, FIFO 2): " + colaPrioridad.extraerTarea()); 
        
        try {
            System.out.println("\nIntentando extraer de cola vacía...");
            colaPrioridad.extraerTarea(); 
        } catch (NoSuchElementException e) {
            System.err.println("ERROR ATTRAPADO: La Cola de Prioridad está vacía.");
        }
    }

}
