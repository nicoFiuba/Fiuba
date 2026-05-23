interface Dispositivo {
    String obtenerHora();
}

class Reloj implements Dispositivo {
    @Override
    public String obtenerHora() {
        return "20:19hs (Lectura mecanica)";
    }
}

class Celular implements Dispositivo {
    @Override
    public String obtenerHora() {
        return "20:19hs (Lectura via 4G)";
    }
}

class Computadora implements Dispositivo {
    @Override
    public String obtenerHora() {
        return java.time.LocalTime.now().toString() + " (Lectura via api)";
    }
}

public class Ejercicio3 {
    
    public static void main(String[] args) {
        Dispositivo reloj = new Reloj();
        Dispositivo celular = new Celular();
        Dispositivo computadora = new Computadora();

        System.out.println("Hora del reloj: " + reloj.obtenerHora());
        System.out.println("Hora del celular: " + celular.obtenerHora());
        System.out.println("Hora de la computadora: " + computadora.obtenerHora());
    }
}
