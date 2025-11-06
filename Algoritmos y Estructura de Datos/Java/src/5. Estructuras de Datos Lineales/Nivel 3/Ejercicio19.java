import java.util.EmptyStackException;
import java.util.LinkedList;
import java.util.List;

class Casillero {

    private int fila;
    private int columna;
    private String contenido;

    public Casillero(int fila, int columna, String contenido) {
        this.fila = fila;
        this.columna = columna;
        this.contenido = contenido;
    }

    public int getFila() {
        return fila;
    }

    public int getColumna() {
        return columna;
    }

    public String getTipo() {
        return contenido;
    }
}

class PilaCasilleros {

    private LinkedList<Casillero> elementos;

    public PilaCasilleros() {
        this.elementos = new LinkedList<>();
    }

    public boolean estaVacia() {
        return elementos.isEmpty();
    }

    public void apilar(Casillero casillero) {
        elementos.addFirst(casillero);
    }

    public Casillero desapilar() {
        if (estaVacia()) {
            throw new EmptyStackException();
        }
        return elementos.removeFirst();
    }
}

class Laberinto {

    private int[][] mapa;
    private int filas;
    private int columnas;

    public Laberinto(int[][] mapa) {
        
        this.mapa = mapa;
        this.filas = mapa.length;
        this.columnas = mapa[0].length;
    
    }

    public List<Casillero> encontrarCaminoDFS(int inicioX, int inicioY) {

        boolean[][] visitado = new boolean[filas][columnas];
        PilaCasilleros pila = new PilaCasilleros();

        List<Casillero> camino = new LinkedList<>();

        Casillero inicio = new Casillero(inicioX, inicioY, "Inicio");
        pila.apilar(inicio);
        visitado[inicioX][inicioY] = true;

        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};

        while (!pila.estaVacia()) {
            Casillero actual = pila.desapilar();
            camino.add(actual);

            if (mapa[actual.getFila()][actual.getColumna()] == 3) {
                return camino;
            }

            for (int i = 0; i < 4; i++) {
                int proximoX = actual.getFila() + dx[i];
                int proximoY = actual.getColumna() + dy[i];

                if (proximoX >= 0 && proximoX < filas && proximoY >= 0 && proximoY < columnas) {
                    if (mapa[proximoX][proximoY] != 1 && !visitado[proximoX][proximoY]) {
                        visitado[proximoX][proximoY] = true;

                        pila.apilar(new Casillero(proximoX, proximoY, String.valueOf(mapa[proximoX][proximoY])));
                    }
                }
            }
        }
        return null;
    }
    
}


public class Ejercicio19 {

    private static final int[][] MAPA_EJEMPLO = {
        {1, 1, 1, 1, 1},
        {1, 2, 0, 0, 1},
        {1, 1, 1, 0, 1},
        {1, 0, 0, 0, 1},
        {1, 0, 1, 3, 1} 
    };
    
    public static void main(String[] args) {
        
        Laberinto laberinto = new Laberinto(MAPA_EJEMPLO);
        
        int inicioX = 1;
        int inicioY = 1;
        
        List<Casillero> camino = laberinto.encontrarCaminoDFS(inicioX, inicioY);

        if (camino != null) {
            System.out.println("\n¡Camino encontrado (DFS)!");
            System.out.print("Ruta: ");
            for (Casillero casillero : camino) {
                System.out.print("(" + casillero.getFila() + "," + casillero.getColumna() + ") -> ");
            }
            System.out.println("FIN");
        } else {
            System.out.println("\nNo se encontró un camino de la posición inicial a la salida.");
        }
    }
    
}
