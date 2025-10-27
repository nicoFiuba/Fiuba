import java.lang.ref.SoftReference;
import java.lang.ref.WeakReference;

public class Ejercicio21 {

    public static void main(String[] args) {

        System.out.println("Creando referencias débiles");

        WeakReference<Object> weakRef = new WeakReference(new Object());
        System.out.println("Referencia débil creada: " + weakRef.get());

        System.out.println("Forzando recolección de basura");
        System.gc();

        System.out.println("Referencia débil después de GC: " + weakRef.get());
        
        System.out.println("\nCreando referencias suaves");
        SoftReference<Object> softRef = new SoftReference(new Object());
        System.out.println("Referencia suave creada: " + softRef.get());
        System.out.println("Forzando recolección de basura");
        System.gc();
        System.out.println("Referencia suave después de GC: " + softRef.get());
        
    }
    
}
