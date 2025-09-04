package rolgar;

import java.util.*;

public class Juego {
    private Tablero tablero;
    private Personaje personaje;
    private List<Enemigo> enemigos;
    private Scanner sc;

    public Juego(int filas, int columnas) {
        tablero = new Tablero(filas, columnas);
        personaje = new Personaje("Jugador", 100, filas / 2, columnas / 2);
        enemigos = new ArrayList<>();
        sc = new Scanner(System.in);
        generarEnemigos(3, filas, columnas);
    }

    private void generarEnemigos(int cantidad, int filas, int columnas) {
        Random rand = new Random();
        for (int i = 0; i < cantidad; i++) {
            int x, y;
            do {
                x = rand.nextInt(filas);
                y = rand.nextInt(columnas);
            } while (x == filas/2 && y == columnas/2); // evitar centro
            enemigos.add(new Enemigo("Enemigo" + (i+1), 50, x, y));
        }
    }

    public void iniciar() {
        boolean jugando = true;
        while (jugando) {
            tablero = new Tablero(tableroFilas(), tableroColumnas());
            tablero.colocar(personaje.getPosX(), personaje.getPosY(), 'P');
            for (Enemigo e : enemigos) {
                tablero.colocar(e.getPosX(), e.getPosY(), 'E');
            }
            tablero.mostrar();

            System.out.println("Mover (WASD, Q para salir): ");
            char opcion = sc.next().toUpperCase().charAt(0);
            if (opcion == 'Q') {
                jugando = false;
            } else {
                moverPersonaje(opcion);
            }
        }
    }

    private void moverPersonaje(char opcion) {
        tablero.limpiar(personaje.getPosX(), personaje.getPosY());
        switch (opcion) {
            case 'W': personaje.moverArriba(); break;
            case 'S': personaje.moverAbajo(); break;
            case 'A': personaje.moverIzquierda(); break;
            case 'D': personaje.moverDerecha(); break;
        }
    }

    private int tableroFilas() { return tablero == null ? 0 : 5; } // ajustar
    private int tableroColumnas() { return tablero == null ? 0 : 5; } // ajustar
}
