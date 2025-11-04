import java.util.NoSuchElementException;

class NodoString {

    String palabra;
    NodoString siguiente;

    public NodoString(String palabra) {
        
        this.palabra = palabra;
        this.siguiente = null;
    
    }
}

class ListaDePalabras {

    private NodoString cabeza;
    private int tamaño;

    public ListaDePalabras() {
        this.cabeza = null;
        this.tamaño = 0;
    }

    public boolean estaVacia() {
        return cabeza == null;
    }

    public void agregarPalabra(String palabra) {

        NodoString nuevoNodo = new NodoString(palabra);
        
        if (estaVacia()) {
            cabeza = nuevoNodo;
        } else {
            NodoString actual = cabeza;
            
            while (actual.siguiente != null) {
                actual = actual.siguiente;
            }
            actual.siguiente = nuevoNodo;
        }
        tamaño++;
    }

    public void eliminarPalabra(String palabra) {
        
        if (estaVacia()) {
            throw new NoSuchElementException("La lista está vacía.");
        }

        if (cabeza.palabra.equals(palabra)) {
            cabeza = cabeza.siguiente;
            
            tamaño--;
            
            return;
        }

        NodoString actual = cabeza;

        while (actual.siguiente != null) {
            if (actual.siguiente.palabra.equals(palabra)) {
                actual.siguiente = actual.siguiente.siguiente;
                
                tamaño--;
                
                return;
            }
            actual = actual.siguiente;
        }

        throw new NoSuchElementException("La palabra '" + palabra + "' no se encontró en la lista.");

    }

    public ListaDePalabras buscarPalabras(String terminoBusqueda, boolean busquedaParcial) {

        ListaDePalabras resultados = new ListaDePalabras();
        NodoString actual = cabeza;

        String terminoLower = terminoBusqueda.toLowerCase();

        while (actual != null) {
            String palabraLower = actual.palabra.toLowerCase();
            boolean encontrado = false;

            if (busquedaParcial) {
                if (palabraLower.contains(terminoLower)) {
                    encontrado = true;
                }
            } else {
                if (palabraLower.equals(terminoLower)) {
                    encontrado = true;
                }
            }

            if (encontrado) {
                resultados.agregarPalabra(actual.palabra);
            }

            actual = actual.siguiente;
        }

        return resultados;
    }

    public int getTamaño() {
        return tamaño;
    }

    @Override
    public String toString() {

        if (estaVacia()) {
            return "[]";
        }

        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("[");

        NodoString actual = cabeza;

        while (actual != null) {
            stringBuilder.append(actual.palabra);
            
            if (actual.siguiente != null) {
                stringBuilder.append(", ");
            }

            actual = actual.siguiente;
        }

        stringBuilder.append("]");

        return stringBuilder.toString();
    }
}



public class Ejercicio6 {
    
    public static void main(String[] args) {
        
        ListaDePalabras lista = new ListaDePalabras();

        lista.agregarPalabra("Manzana");
        lista.agregarPalabra("Banana");
        lista.agregarPalabra("Cereza");
        lista.agregarPalabra("Mango");
        lista.agregarPalabra("Pera");
        lista.agregarPalabra("Melocotón");

        System.out.println("Lista completa: " + lista);

        ListaDePalabras resultadosExactos = lista.buscarPalabras("Mango", false);
        System.out.println("Búsqueda exacta de 'Mango': " + resultadosExactos);

        ListaDePalabras resultadosParciales = lista.buscarPalabras("an", true);
        System.out.println("Búsqueda parcial de 'an': " + resultadosParciales);

        lista.eliminarPalabra("Banana");
        System.out.println("Lista después de eliminar 'Banana': " + lista);
    }
}
