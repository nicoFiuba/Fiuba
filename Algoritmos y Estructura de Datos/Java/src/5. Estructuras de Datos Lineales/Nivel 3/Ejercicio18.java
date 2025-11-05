class Casillero {

    private int fila;
    private int columna;
    private String contenido;

    public Casillero(int fila, int columna, String contenido) {

        this.fila = fila;
        this.columna = columna;
        this.contenido = contenido;

    }

    public void setContenido(String contenido) {
        this.contenido = contenido;
    }

    public int getFila() {
        return fila;
    }

    public int getColumna() {
        return columna;
    }

    public String getContenido() {
        return contenido;
    }

    @Override
    public String toString() {
        return "(" + fila + ", " + columna + "): " + contenido;
    }
}

class ListaEnlazada<T> {

    private static class Nodo<T> {

        T dato;
        Nodo<T> siguiente;

        public Nodo(T dato) {
            
            this.dato = dato;

        }

    }

    private Nodo<T> cabeza;
    private int tamaño;

    public ListaEnlazada() {

        this.cabeza = null;
        this.tamaño = 0;

    }

    public void agregar(T dato) {

        Nodo<T> nuevoNodo = new Nodo<>(dato);
        if (cabeza == null) {
            cabeza = nuevoNodo;
        } else {
            Nodo<T> actual = cabeza;
            
            while (actual.siguiente != null) {
                actual = actual.siguiente;
            }
            actual.siguiente = nuevoNodo;
        }

        tamaño++;
    }

    public T obtener(int indice) {

        if (indice < 0 || indice >= tamaño) {
            throw new IndexOutOfBoundsException("Índice fuera de rango");
        }

        Nodo<T> actual = cabeza;
        
        for (int i = 0; i < indice; i++) {
            actual = actual.siguiente;
        }

        return actual.dato;
    }

    public int tamaño() {
        return tamaño;
    }
}

class Tablero {

    private ListaEnlazada<ListaEnlazada<Casillero>> casilleros;
    private int filas;
    private int columnas;

    public Tablero(int filas, int columnas) {

        this.filas = filas;
        this.columnas = columnas;
        this.casilleros = new ListaEnlazada<>();
        inicializar();

    }

    public void inicializar() {

        for (int i = 0; i < filas; i++) {
            ListaEnlazada<Casillero> filaCasilleros = new ListaEnlazada<>();

            for (int j = 0; j < columnas; j++) {
                filaCasilleros.agregar(new Casillero(i, j, ""));
            }

            casilleros.agregar(filaCasilleros);
        }

    }

    public Casillero obtenerCasillero(int i, int j) {

        if (i < 0 || i >= filas || j < 0 || j >= columnas) {
            return null;
        }

        ListaEnlazada<Casillero> fila = casilleros.obtener(i);

        return fila.obtener(j);
    }

    public Casillero obtenerVecino(int x, int y, int dx, int dy) {
        return obtenerCasillero(x + dx, y + dy);
    }

    public Casillero[][] obtenerVecinos3x3(int x, int y) {
        
        Casillero[][] matriz3x3 = new Casillero[3][3];

        for (int i = -1; i <= 1; i++) {
            for (int j = -1; j <= 1; j++) {

                int filaAbsoluta = x + i;
                int columnaAbsoluta = y + j;

                Casillero vecino = obtenerCasillero(filaAbsoluta, columnaAbsoluta);

                matriz3x3[i + 1][j + 1] = vecino;
            }
        }

        return matriz3x3;
    }
}

public class Ejercicio18 {
    
    private static void imprimirMatriz(Casillero[][] matriz) {

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (matriz[i][j] != null) {
                    System.out.print(matriz[i][j].getContenido() + " ");
                } else {
                    System.out.print("~ ");
                }
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {

        Tablero tablero = new Tablero(5, 5); 
        
        tablero.obtenerCasillero(2, 2).setContenido("X");
        tablero.obtenerCasillero(2, 3).setContenido("V");
        
        int xCentral = 2;
        int yCentral = 2;

        System.out.println("\n1. Vecino al Este (0, +1):");
        Casillero vecinoEste = tablero.obtenerVecino(xCentral, yCentral, 0, 1);
        System.out.println("Casillero (2, 2) tiene vecino: " + vecinoEste);
        
        System.out.println("\n2. Matriz 3x3 Centrada en (2, 2):");
        Casillero[][] matrizCentro = tablero.obtenerVecinos3x3(xCentral, yCentral);
        imprimirMatriz(matrizCentro);
        
        System.out.println("\n3. Matriz 3x3 en el Borde (0, 0):");
        Casillero[][] matrizBorde = tablero.obtenerVecinos3x3(0, 0);
        imprimirMatriz(matrizBorde);
    }
}
