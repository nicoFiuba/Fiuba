import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Ejercicio22 {

    static void crearArchivo() {
        String archivo = "Ejercicio22.txt";
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(archivo))) {
            for (int i = 0; i < 10000; i++) {
                bw.write("Línea número " + i);
                bw.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        
        crearArchivo();
        
        String archivo = "Ejercicio22.txt";
        List<String> cache = new ArrayList<>();

        long timpoInicial, tiempoFinal, duracionLecturaArchivo, duracionLecturaCache;

        // Leer datos del archivo y almacenarlos en la caché
        timpoInicial = System.nanoTime();
        try (BufferedReader br = new BufferedReader(new FileReader(archivo))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                cache.add(linea);
            }
        } catch (IOException e) {
            e.printStackTrace(); // printStackTrace en caso de error que significa que hubo un error de entrada/salida
        }

        tiempoFinal = System.nanoTime();
        duracionLecturaArchivo = tiempoFinal - timpoInicial;
        System.out.println("Tiempo de lectura del archivo: " + duracionLecturaArchivo + " nanosegundos");

        // Leer datos de la caché
        timpoInicial = System.nanoTime();

        for (String dato : cache) {
            // Simular procesamiento de datos
            String procesado = dato.toUpperCase();
        }

        tiempoFinal = System.nanoTime();
        duracionLecturaCache = tiempoFinal - timpoInicial;

        System.out.println("Tiempo de lectura de la caché: " + duracionLecturaCache + " nanosegundos");

    }
    
}
