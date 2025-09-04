package rolgar;

public class Tablero {
    private int filas;
    private int columnas;
    private char[][] grilla;

    public Tablero(int filas, int columnas) {
        this.filas = filas;
        this.columnas = columnas;
        this.grilla = new char[filas][columnas];
        inicializar();
    }

    private void inicializar() {
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                grilla[i][j] = '.';
            }
        }
    }

    public void mostrar() {
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                System.out.print(grilla[i][j] + " ");
            }
            System.out.println();
        }
    }

    public void colocar(int x, int y, char simbolo) {
        grilla[x][y] = simbolo;
    }

    public void limpiar(int x, int y) {
        grilla[x][y] = '.';
    }
}
