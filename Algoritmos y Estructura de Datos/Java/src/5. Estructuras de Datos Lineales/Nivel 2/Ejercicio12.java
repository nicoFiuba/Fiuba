class Nodo {

    int dato;
    Nodo siguiente;

    public Nodo(int dato) {
        
        this.dato = dato;
        this.siguiente = null;
    
    }
}

class ListaEnlazada {

    Nodo cabeza;

    public ListaEnlazada() {
        this.cabeza = null;
    }

    public boolean estaVacia() {
        return cabeza == null;
    }

    public void agregar(int dato) {

        Nodo nuevoNodo = new Nodo(dato);

        if (estaVacia()) {
            this.cabeza = nuevoNodo;
        } else {
            Nodo actual = cabeza;

            while (actual.siguiente != null) {
                actual = actual.siguiente;
            }

            actual.siguiente = nuevoNodo;
        }

    }

    public Nodo getCabeza() {
        return cabeza;
    }

    @Override
    public String toString() {

        StringBuilder stringBuilder = new StringBuilder("[");

        Nodo actual = cabeza;

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

public class Ejercicio12 {

    public static ListaEnlazada combinarListas(ListaEnlazada lista1, ListaEnlazada lista2) {
        
        Nodo centinela = new Nodo(0);
        Nodo cola = centinela;

        Nodo actual1 = lista1.getCabeza();
        Nodo actual2 = lista2.getCabeza();

        while (actual1 != null && actual2 != null) {
            if (actual1.dato <= actual2.dato) {
                cola.siguiente = actual1;
                actual1 = actual1.siguiente;
            } else {
                cola.siguiente = actual2;
                actual2 = actual2.siguiente;
            }
            cola = cola.siguiente;
        }
        
        if (actual1 != null) {
            cola.siguiente = actual1;
        } else if (actual2 != null) {
            cola.siguiente = actual2;
        }

        ListaEnlazada listaCombinada = new ListaEnlazada();
        listaCombinada.cabeza = centinela.siguiente;

        return listaCombinada;
    }

    public static void main(String[] args) {

        ListaEnlazada lista1 = new ListaEnlazada();
        lista1.agregar(1);
        lista1.agregar(5);
        lista1.agregar(10);

        ListaEnlazada lista2 = new ListaEnlazada();
        lista2.agregar(2);
        lista2.agregar(3);
        lista2.agregar(20);

        System.out.println("Lista 1: " + lista1);
        System.out.println("Lista 2: " + lista2);
        
        ListaEnlazada listaCombinada = combinarListas(lista1, lista2);
        
        System.out.println("Lista Combinada: " + listaCombinada);
    }
    
}
