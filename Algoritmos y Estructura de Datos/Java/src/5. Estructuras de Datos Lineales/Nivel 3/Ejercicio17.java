import java.util.Arrays;
import java.util.Collections;
import java.util.EmptyStackException;
import java.util.List;

class Carta {

    private String palo;
    private int valor;

    public Carta(String palo, int valor) {
        this.palo = palo;
        this.valor = valor;
    }

    @Override
    public String toString() {
        return valor + " de " + palo;
    }

}

class PilaDeCartas {

    private Carta[] elementos;
    private int capacidad;
    private int cima;

    public PilaDeCartas(int capacidadInicial) {

        this.capacidad = capacidadInicial;
        this.elementos = new Carta[capacidadInicial];
        this.cima = -1;

    }

    public boolean estaVacia() {
        return cima == -1;
    }

    public void apilar(Carta carta) {

        if (cima < capacidad - 1) {
            elementos[++cima] = carta;
        } else {
            System.err.println("El mazo está lleno.");
        }

    }

    public Carta desapilar() {

        if (estaVacia()) {
            throw new EmptyStackException();
        }

        Carta carta = elementos[cima];
        elementos[cima--] = null;

        return carta;
    }

    public Carta obtenerTope() {

        if (estaVacia()) {
            throw new EmptyStackException();
        }

        return elementos[cima];
    }

    public Carta[] getElementos() {
        return elementos;
    }

    public int getCima() {
        return cima;
    }
}

class JuegoDeCartas {

    private PilaDeCartas mazo;
    private String[] palos = {"Corazones", "Diamantes", "Tréboles", "Picas"};

    public JuegoDeCartas() {

        this.mazo = new PilaDeCartas(52);
        inicializarMazo();

    }

    private void inicializarMazo() {

        for (String palo : palos) {
            for (int valor = 1; valor <= 13; valor++) {
                mazo.apilar(new Carta(palo, valor));
            }
        }

        System.out.println("Mazo inicializado con 52 cartas.");

    }

    public void barajar() {

        int numCartas = mazo.getCima() + 1;
        Carta[] elementos = mazo.getElementos();

        List<Carta> listaCartas = Arrays.asList(Arrays.copyOf(elementos, numCartas));

        Collections.shuffle(listaCartas);

        for (int i = 0; i < numCartas; i++) {
            elementos[i] = listaCartas.get(i);
        }

        System.out.println("Mazo barajado.");

    }

    public Carta sacarCarta() {
        return mazo.desapilar();
    }

    public Carta mostrarTope() {
        return mazo.obtenerTope();
    }
}



public class Ejercicio17 {
    
    public static void main(String[] args) {

        JuegoDeCartas juego = new JuegoDeCartas();

        System.out.println("Tope actual: " + juego.mostrarTope());
        
        juego.barajar();
        System.out.println("Nuevo Tope: " + juego.mostrarTope());
        
        System.out.println("Carta Sacada (desapilar): " + juego.sacarCarta());
        System.out.println("Nueva carta superior: " + juego.mostrarTope());
        
        System.out.println("Carta Sacada (desapilar): " + juego.sacarCarta());
        System.out.println("Nueva carta superior: " + juego.mostrarTope());
    }
}
