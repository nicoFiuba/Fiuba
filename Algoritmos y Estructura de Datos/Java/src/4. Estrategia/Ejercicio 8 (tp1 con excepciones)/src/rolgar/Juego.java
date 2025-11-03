package rolgar;

import java.util.*;

public class Juego {
    private Tablero tablero;
    private Personaje personaje;
    private List<Enemigo> enemigos;
    private Scanner sc;

    public Juego(int filas, int columnas) {
        // Tablero ahora lanza una IllegalArgumentException si filas o columnas son <= 0
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
        
        // El scanner se cierra en el bloque finally o al salir del juego
        try (Scanner autoCloseSc = sc) { 
            while (jugando) {
                tablero = new Tablero(tableroFilas(), tableroColumnas());
                tablero.colocar(personaje.getPosX(), personaje.getPosY(), 'P');
                for (Enemigo e : enemigos) {
                    tablero.colocar(e.getPosX(), e.getPosY(), 'E');
                }
                tablero.mostrarVision(personaje.getPosX(), personaje.getPosY());

                System.out.println("WASD para moverte o Q para salir): ");

                // --- APLICAR EXCEPCIÓN: Bloque try-catch para la entrada de usuario ---
                try {
                    String input = autoCloseSc.next();
                    char opcion = input.toUpperCase().charAt(0);
                    
                    if (opcion == 'Q') {
                        jugando = false;
                    } else {
                        moverPersonaje(opcion);
                        verificarPelea();
                        personaje.recuperarVida();
                        System.out.println("Vida actual: " + personaje.getVida());
                        verificarVictoria();
                    }
                } catch (InputMismatchException | StringIndexOutOfBoundsException e) {
                    System.err.println("ERROR DE ENTRADA: Por favor, ingrese un único caracter (W, A, S, D o Q).");
                    // No salimos del juego, solo pasamos la ronda.
                } catch (NoSuchElementException e) {
                    // Atrapa si el flujo de entrada se cierra inesperadamente (EOF)
                    System.err.println("ERROR GRAVE: La entrada de usuario se cerró. Terminando el juego.");
                    jugando = false;
                }
                // --------------------------------------------------------------------------
            }
        } catch (Exception e) {
            // Captura cualquier excepción no manejada durante el cierre del Scanner.
            System.err.println("Un error fatal ocurrió durante el juego: " + e.getMessage());
        }
    }

    private void moverPersonaje(char opcion) {
        int nuevoX = personaje.getPosX();
        int nuevoY = personaje.getPosY();

        switch (opcion) {
            case 'W': nuevoX--; break;
            case 'S': nuevoX++; break;
            case 'A': nuevoY--; break;
            case 'D': nuevoY++; break;
            default: 
                System.out.println("Movimiento inválido");
                return;
        }

        if (esMovimientoValido(nuevoX, nuevoY)) {
            personaje.setPosX(nuevoX);
            personaje.setPosY(nuevoY);
        } else {
            System.out.println("Llegaste al límite del tablero.");
        }
    }

    private int tableroFilas() { return tablero == null ? 0 : 5; } // ajustar
    private int tableroColumnas() { return tablero == null ? 0 : 5; } // ajustar

    private boolean esMovimientoValido(int x, int y) {
    return x >= 0 && x < tablero.getFilas() && y >= 0 && y < tablero.getColumnas();
    }

    private void verificarPelea() {
        Iterator<Enemigo> it = enemigos.iterator();
        while (it.hasNext()) {
            Enemigo e = it.next();
            if (personaje.getPosX() == e.getPosX() && personaje.getPosY() == e.getPosY()) {
                System.out.println("Encontraste a " + e.getNombre() + " ahora te toca aguantar el 1v1");
                
                // Daños
                personaje.setVida(personaje.getVida() - 10);
                e.setVida(e.getVida() - 20);

                System.out.println(personaje.getNombre() + " tiene " + personaje.getVida() + " de vida.");
                System.out.println(e.getNombre() + " tiene " + e.getVida() + " de vida.");

                // Revisar si alguien murió
                if (e.getVida() <= 0) {
                    System.out.println(e.getNombre() + " fue derrotado");
                    it.remove(); // lo saco de la lista
                }
                if (personaje.getVida() <= 0) {
                    System.out.println("Te ganaron los bots, sos malisimo");
                    System.exit(0);
                }
            }
        }
    }

    private void verificarVictoria() {
        if (enemigos.isEmpty()) {
            System.out.println("Hiciste lo que tenias que hacer, ganaste");
            System.exit(0);
        }
    }
}