import java.util.NoSuchElementException;

class NodoDoble {

    int dato;
    NodoDoble siguiente;
    NodoDoble anterior;

    public NodoDoble(int datoInicial) {
        
        this.dato = datoInicial;
        this.siguiente = null;
        this.anterior = null;
    
    }
}

class ListaDoblementeEnlazada {

    private NodoDoble cabeza;
    private NodoDoble cola;
    private int tamaño;

    public ListaDoblementeEnlazada() {
        
        this.cabeza = null;
        this.cola = null;
        this.tamaño = 0;
    
    }

    public boolean estaVacia() {
        return tamaño == 0;
    }

    public void agregarAlInicio(int dato) {
        
        NodoDoble nuevoNodo = new NodoDoble(dato);
        
        if (estaVacia()) {
            cabeza = nuevoNodo;
            
            cola = nuevoNodo;
        } else {
            nuevoNodo.siguiente = cabeza;
            
            cabeza.anterior = nuevoNodo;
            
            cabeza = nuevoNodo;
        }

        tamaño++;
    }

    public void agregarAlFinal(int dato) {
        
        NodoDoble nuevoNodo = new NodoDoble(dato);
        
        if (estaVacia()) {
            cabeza = nuevoNodo;
            
            cola = nuevoNodo;
        } else {
            cola.siguiente = nuevoNodo;
            
            nuevoNodo.anterior = cola;
            
            cola = nuevoNodo;
        }

        tamaño++;
    }

    public int eliminarDelInicio() {
        
        if (estaVacia()) {
            throw new NoSuchElementException("La lista está vacía.");
        }

        int datoEliminado = cabeza.dato;

        if (cabeza == cola) {
            cabeza = null;
            
            cola = null;
        } else {
            cabeza = cabeza.siguiente;
            
            cabeza.anterior = null;
        }

        tamaño--;

        return datoEliminado;
    }

    public int eliminarDelFinal() {
        
        if (estaVacia()) {
            throw new NoSuchElementException("La lista está vacía.");
        }

        int datoEliminado = cola.dato;

        if (cabeza == cola) {
            cabeza = null;
            
            cola = null;
        } else {
            cola = cola.anterior;
            
            cola.siguiente = null;
        }

        tamaño--;

        return datoEliminado;
    }

    public void intercambiarPosiciones(int indice1, int indice2) {
        
        if (indice1 == indice2) {
            return; 
        }

        if (indice1 < 0 || indice1 >= tamaño || indice2 < 0 || indice2 >= tamaño) {
            throw new IndexOutOfBoundsException("Índices fuera de rango.");
        }

        NodoDoble nodo1 = obtenerNodoEnIndice(indice1);
        NodoDoble nodo2 = obtenerNodoEnIndice(indice2);

        int temporal = nodo1.dato;
        nodo1.dato = nodo2.dato;
        nodo2.dato = temporal;
    }

    private NodoDoble obtenerNodoEnIndice(int indice) {

        if (indice < 0 || indice >= tamaño) {
            throw new IndexOutOfBoundsException("Índice fuera de rango.");
        }
        
        NodoDoble actual = cabeza;
        
        for (int i = 0; i < indice; i++) {
            actual = actual.siguiente;
        }

        return actual;
    }

    @Override
    public String toString() {

        if (estaVacia()) {
            return "[]";
        }
        
        StringBuilder stringBuilder = new StringBuilder("[");
        
        NodoDoble actual = cabeza;
        
        while (actual != null) {
            stringBuilder.append(actual.dato);
            
            if (actual.siguiente != null) {
                stringBuilder.append(", ");
            }
            
            actual = actual.siguiente;
        }
        
        stringBuilder.append("]");
        
        return stringBuilder.toString();
    }
}

public class Ejercicio9 {
    
    public static void main(String[] args) {
        
        ListaDoblementeEnlazada lista = new ListaDoblementeEnlazada(); 
        
        lista.agregarAlFinal(20);
        lista.agregarAlFinal(30); 

        System.out.println("Lista: " + lista.toString());

        lista.agregarAlInicio(10);
        lista.agregarAlInicio(5);
        
        System.out.println("Lista: " + lista.toString()); 
        
        System.out.println("Eliminado al inicio (5): " + lista.eliminarDelInicio());
        System.out.println("Lista: " + lista.toString()); 
        
        System.out.println("Eliminado al final (30): " + lista.eliminarDelFinal());
        System.out.println("Lista: " + lista.toString());

        
        System.out.println("Lista antes de intercambiar (0, 1): " + lista.toString());
        lista.intercambiarPosiciones(0, 1); 
        System.out.println("Lista después del intercambio: " + lista.toString()); 
    }
}
