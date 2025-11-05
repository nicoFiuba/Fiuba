import java.util.EmptyStackException;

class PilaUrls {

    private String[] elementos;
    private int cima;
    private int capacidad;

    public PilaUrls(int capacidadInicial) {

        this.capacidad = capacidadInicial;
        this.elementos = new String[capacidadInicial];
        this.cima = -1;

    }

    public boolean estaVacia() {
        return cima == -1;
    }

    public void apilar(String url) {

        if (cima < capacidad -1) {
            elementos[++cima] = url;
        } else {
            System.err.println("Advertencia: Historial lleno. No se guardará la URL: " + url);
        }

    }

    public String desapilar() {

        if (estaVacia()) {
            throw new EmptyStackException();
        }

        String url = elementos[cima];
        elementos[cima--] = null;

        return url;
    }

    public String obtenerTope() {

        if (estaVacia()) {
            return "Pagina de inicio";
        }

        return elementos[cima];
    }
}

public class Ejercicio15 {
    
    class Navegador {
    
        private PilaUrls historial;
        private String paginaActual;
    
        public Navegador() {
    
            this.historial = new PilaUrls(10);
            this.paginaActual = "PAGINA_ACTUAL";
        
        }
    
        public void visitarPagina(String urlNueva) {
    
            if (!paginaActual.equals("PAGINA_ACTUAL")) {
                historial.apilar(paginaActual);
            }
            paginaActual = urlNueva;
            System.out.println("Visitando: " + paginaActual);
            
        }
    
        public void retroceder() {
    
            try {
                String urlAnterior = historial.desapilar();
                paginaActual = urlAnterior;
                System.out.println("Retrocediendo a: " + paginaActual);
            } catch (EmptyStackException e) {
                System.out.println("No hay paginas en el historial para retroceder.");
                paginaActual = "PAGINA_ACTUAL";
            }
    
        }
    }

    public static void main(String[] args) {

        Ejercicio15 instancia = new Ejercicio15();
        Navegador navegador = instancia.new Navegador();
        
        navegador.visitarPagina("google.com");
        navegador.visitarPagina("facebook.com");
        navegador.visitarPagina("youtube.com");
        navegador.visitarPagina("wikipedia.org");
        
        System.out.println("\nPágina Actual: " + navegador.paginaActual);
        System.out.println("Última página en Historial (Tope): " + navegador.historial.obtenerTope());
        
        navegador.retroceder();
        navegador.retroceder();
        navegador.retroceder(); 
        
        navegador.retroceder();
        
        System.out.println("Página Final: " + navegador.paginaActual);

    }
}
