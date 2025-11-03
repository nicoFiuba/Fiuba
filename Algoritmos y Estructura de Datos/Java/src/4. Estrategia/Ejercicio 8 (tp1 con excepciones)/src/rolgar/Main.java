package rolgar;

public class Main {
    public static void main(String[] args) {
        
        // --- APLICAR EXCEPCIÓN: Bloque try-catch para la inicialización ---
        try {
            // Si el constructor de Juego falla (ej. dimensiones negativas), la excepción es atrapada aquí.
            Juego juego = new Juego(5, 5); 
            juego.iniciar();
        } catch (IllegalArgumentException e) {
            // Atrapa el error lanzado por la clase Tablero
            System.err.println("¡ERROR FATAL DE INICIO!");
            System.err.println("El juego no pudo inicializarse. Razón: " + e.getMessage());
        }
        // -----------------------------------------------------------------
    }
}
