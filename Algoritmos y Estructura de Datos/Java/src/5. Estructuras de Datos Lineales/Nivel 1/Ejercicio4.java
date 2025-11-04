import java.util.Scanner;

class ListaStrings {
    
    private String[] elementos;
    private int contador;

    public ListaStrings(int capacidad) {
        
        elementos = new String[capacidad];
        contador = 0;
    
    }

    public void agregar(String elemento) {
        
        if (contador >= elementos.length) {
            throw new IllegalStateException("La lista está llena");
        }

        elementos[contador++] = elemento;

    }

    public String obtenerElementos(int indice) {
        
        if (indice < 0 || indice >= contador) {
            throw new IndexOutOfBoundsException("Índice fuera de rango");
        }

        return elementos[indice];
    }

    public int tamaño() {    
        return contador;
    }

    public void eliminarElemento(int indice) {

        if (indice < 0 || indice >= contador) {
            throw new IndexOutOfBoundsException("Índice fuera de rango");
        }

        System.arraycopy(elementos, indice + 1, elementos, indice, contador - indice - 1);
        contador--;

        elementos[contador] = null;

    }

    public void imprimirLista() {

        for (int i = 0; i < contador; i++) {
            System.out.println(elementos[i]);
        }

    }

}



public class Ejercicio4 {
    
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        ListaStrings lista = new ListaStrings(5);

        System.out.print("Longitud a eliminar: ");
        int longitudAEliminar = scanner.nextInt();
        scanner.nextLine();

        System.out.println("Ingrese una frase de texto: ");
        String frase = scanner.nextLine();

        String[] palabras = frase.split(" ");
        for (String palabra : palabras) {
            if (!palabra.isEmpty()) {
                lista.agregar(palabra);
            }
        }

        for (int i = 0; i < lista.tamaño(); i++) {
            String palabraActual = lista.obtenerElementos(i);
            if (palabraActual.length() == longitudAEliminar) {
                lista.eliminarElemento(i);
                i--;
            }
        }

        System.out.println("Lista después de eliminar palabras de longitud " + longitudAEliminar + ":");
        lista.imprimirLista();

        scanner.close();
    }
}
