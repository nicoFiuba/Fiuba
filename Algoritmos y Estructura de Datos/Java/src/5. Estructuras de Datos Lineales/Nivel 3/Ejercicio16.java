import java.util.NoSuchElementException;

class NodoDoble<T> {

    T dato;
    NodoDoble<T> siguiente;
    NodoDoble<T> anterior;

    public NodoDoble(T dato) {

        this.dato = dato;
        this.siguiente = null;
        this.anterior = null;

    }
}

class IteradorDeListaDoble<T> {
    
    private NodoDoble<T> actual;
    
    public IteradorDeListaDoble(NodoDoble<T> inicio) {
        this.actual = inicio;
    }
    
    public boolean tieneSiguiente() {
        return actual != null;
    }
    
    public T siguiente() {

        if (!tieneSiguiente()) {
            throw new NoSuchElementException("No hay más elementos en la lista.");
        }

        T dato = actual.dato;
        actual = actual.siguiente; 

        return dato;
    }

    public boolean tieneAnterior() {
        return actual != null && actual.anterior != null;
    }

    public T anterior() {

        if (actual == null || actual.anterior == null) {
            throw new NoSuchElementException("No hay elemento anterior en la lista.");
        }
        actual = actual.anterior; 
        return actual.dato;
    }
}

class ListaDoblementeEnlazada<T> {

    private NodoDoble<T> cabeza;
    private NodoDoble<T> cola;
    private int tamaño;

    public ListaDoblementeEnlazada() {

        this.cabeza = null;
        this.cola = null;
        this.tamaño = 0;

    }
    
    public void agregarAlFinal(T dato) {

        NodoDoble<T> nuevoNodo = new NodoDoble<>(dato);

        if (tamaño == 0) {
            cabeza = nuevoNodo;
        } else {
            cola.siguiente = nuevoNodo;
            nuevoNodo.anterior = cola;
        }

        cola = nuevoNodo;
        tamaño++;
    }

    public int getTamaño() { 
        return tamaño;
    }
    
    public IteradorDeListaDoble<T> obtenerIteradorDesdeElInicio() {
        return new IteradorDeListaDoble<>(cabeza);
    }

    public IteradorDeListaDoble<T> obtenerIteradorDesdeElFinal() {
        return new IteradorDeListaDoble<>(cola);
    }

    @Override
    public String toString() {

        StringBuilder stringBuilder = new StringBuilder();

        NodoDoble<T> actual = cabeza;

        while (actual != null) {
            stringBuilder.append(actual.dato).append(" ");
            actual = actual.siguiente;
        }

        return stringBuilder.toString().trim();
    }
}

public class Ejercicio16 {
    
    public static void main(String[] args) {
        
        ListaDoblementeEnlazada<String> lista = new ListaDoblementeEnlazada<>();

        lista.agregarAlFinal("A");
        lista.agregarAlFinal("B");
        lista.agregarAlFinal("C");
        lista.agregarAlFinal("D");

        System.out.println("Lista: " + lista.toString());

        IteradorDeListaDoble<String> cursorAdelante = lista.obtenerIteradorDesdeElInicio();
        IteradorDeListaDoble<String> cursorAtras = lista.obtenerIteradorDesdeElFinal();

        try {
            String datoAdelante = null;
            
            if (cursorAdelante.tieneSiguiente()) {
                datoAdelante = cursorAdelante.siguiente();
            }

            String datoAtras = cursorAtras.siguiente();

            if (datoAdelante != null) {
                System.out.println("  Cursor Adelante: " + datoAdelante + " | Cursor Atrás: " + datoAtras);
            }
            
            cursorAtras = lista.obtenerIteradorDesdeElFinal(); 
            cursorAtras.anterior(); 

            while (cursorAdelante.tieneSiguiente()) {
                datoAdelante = cursorAdelante.siguiente(); 
                datoAtras = cursorAtras.anterior(); 

                if (datoAdelante != null && datoAtras != null) {
                    System.out.println("  Cursor Adelante: " + datoAdelante + " | Cursor Atrás: " + datoAtras);
                }
            }
            
        } catch (NoSuchElementException e) {
            System.err.println("Error al iterar: " + e.getMessage());
        }
    }
}
