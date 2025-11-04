class ListaEnteros {

    private int[] elementos;
    private int contador;
    private static final int CAPACIDAD_INICIAL = 10;

    public ListaEnteros() {
        
        this.elementos = new int[CAPACIDAD_INICIAL];
        this.contador = 0;
    
    }

    public void agregarElemento(int elemento) {

        if (contador >= elementos.length) {
            throw new IllegalStateException("La lista está llena");
        }

        elementos[contador++] = elemento;
    
    }

    public int obtenerElemento(int indice) {

        if (indice < 0 || indice >= contador) {
            throw new IndexOutOfBoundsException("Índice fuera de rango");
        }

        return elementos[indice];
    }

    public int tamaño() {
        return contador;
    }

    public int buscarYContar(ListaEnteros otraLista, int numeroBuscado) {

        int contadorApariciones = 0;

        for (int i = 0; i < otraLista.tamaño(); i++) {
            if (otraLista.obtenerElemento(i) == numeroBuscado) {
                contadorApariciones++;
            }
        }

        return contadorApariciones;
    }
}

public class Ejercicio2 {
    
    public static void main(String[] args) {
        
        ListaEnteros lista1 = new ListaEnteros();

        lista1.agregarElemento(5);
        lista1.agregarElemento(10);
        lista1.agregarElemento(15);
        lista1.agregarElemento(5);
        lista1.agregarElemento(20);
        lista1.agregarElemento(5);

        int numeroBuscado = 5;
        int apariciones = lista1.buscarYContar(lista1, numeroBuscado);

        System.out.println("El número " + numeroBuscado + " aparece " + apariciones + " veces en la lista.");
    
    }

}
