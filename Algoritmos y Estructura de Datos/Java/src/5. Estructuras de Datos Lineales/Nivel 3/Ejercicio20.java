import java.util.LinkedList;
import java.util.NoSuchElementException;

class Proceso {

    private String nombre;
    private int id;
    private int prioridad;

    public Proceso(String nombre, int id, int prioridad) {
        
        this.nombre = nombre;
        this.id = id;
        this.prioridad = prioridad;
    
    }

    public String getNombre() {
        return nombre;
    }

    public int getId() {
        return id;
    }

    public int getPrioridad() {
        return prioridad;
    }

    @Override
    public String toString() {
        return "Proceso " + id + " (" + nombre + ", P=" + prioridad + ")"; 
    }
}

class ColaProcesos {

    private LinkedList<Proceso> elementos;

    public ColaProcesos() {
        this.elementos = new LinkedList<>();
    }

    public boolean estaVacia() {
        return elementos.isEmpty();
    }

    public void encolar(Proceso proceso) {
        elementos.addLast(proceso);
    }

    public Proceso desencolar() {
        if (estaVacia()) {
            throw new NoSuchElementException("La cola está vacía");
        }

        return elementos.removeFirst();
    }
}

class NodoPrioridad {

    int prioridad;
    ColaProcesos procesos;
    NodoPrioridad siguiente;

    public NodoPrioridad(int prioridad) {
        this.prioridad = prioridad;
        this.procesos = new ColaProcesos();
        this.siguiente = null;
    }
}

class SimuladorProcesos {

    private NodoPrioridad cabeza;

    public SimuladorProcesos() {
        this.cabeza = null;
    }

    public void encolarProceso(Proceso proceso) {

        int prioridad = proceso.getPrioridad();

        NodoPrioridad actual = cabeza;
        NodoPrioridad anterior = null;

        while (actual != null && actual.prioridad <= prioridad) {
            if (actual.prioridad == prioridad) {
                actual.procesos.encolar(proceso);
                return;
            }
            anterior = actual;
            actual = actual.siguiente;
        }

        NodoPrioridad nuevoNodo = new NodoPrioridad(prioridad);
        nuevoNodo.procesos.encolar(proceso);

        if (anterior == null) {
            nuevoNodo.siguiente = cabeza;
            cabeza = nuevoNodo;
        } else {
            anterior.siguiente = nuevoNodo;
            nuevoNodo.siguiente = actual;
        }

    }

    public Proceso desencolarProceso() {

        if (cabeza == null) {
            throw new NoSuchElementException("No hay procesos en la cola");
        }

        Proceso proceso = cabeza.procesos.desencolar();

        if (cabeza.procesos.estaVacia()) {
            cabeza = cabeza.siguiente;
        }

        return proceso;
    }
}

public class Ejercicio20 {
    
    public static void main(String[] args) {
        
        SimuladorProcesos simulador = new SimuladorProcesos();
        int idCounter = 1;
        
        System.out.println("1. ENCOLANDO PROCESOS...");
        simulador.encolarProceso(new Proceso("Kernel Update", idCounter++, 1));
        simulador.encolarProceso(new Proceso("Render Video", idCounter++, 3));
        simulador.encolarProceso(new Proceso("System Log", idCounter++, 1)); 
        simulador.encolarProceso(new Proceso("Web Browser", idCounter++, 2));
        simulador.encolarProceso(new Proceso("Juego", idCounter++, 3));

        System.out.println("\n2. PROCESANDO (Extraer Mayor Prioridad)...");
        
        try {
            while (true) {
                Proceso p = simulador.desencolarProceso();
                System.out.println("  -> Procesado: " + p);
            }
        } catch (NoSuchElementException e) {
            System.out.println("\n3. COLA VACÍA: Todos los procesos han sido completados.");
        }
    }
}
