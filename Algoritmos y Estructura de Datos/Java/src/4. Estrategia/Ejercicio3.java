public class Ejercicio3 {
    
    static int producto(int a, int b) {
        if (b == 0) {
            return 0;
        } else if (b < 0) {
            return producto(-a, -b);
        } else {
            return a + producto(a, b - 1);
        }
    }

    public static void main(String[] args) {
        
        int a = 5;
        int b = 3;
        int resultado = producto(a, b);
        
        System.out.println("El producto de " + a + " y " + b + " es: " + resultado);

    }
}

// Solucion iterativa
/*
public static int productoIterativo(int a, int b) {
    
    if (b == 0) {
        return 0;
    }
    
    boolean resultadoNegativo = (a < 0) ^ (b < 0);
    int multiplicando = Math.abs(a);
    int multiplicador = Math.abs(b);
    int resultado = 0;

    for (int i = 0; i < multiplicador; i++) {
        resultado += multiplicando;
    }

    return resultadoNegativo ? -resultado : resultado;
}
*/
