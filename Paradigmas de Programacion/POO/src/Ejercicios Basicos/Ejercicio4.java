abstract class InstrumentoMusical {
    private String material;
    
    public InstrumentoMusical(String material) {
        this.material = material;
    }

    public String getMaterial() {
        return material;
    }

    abstract void tocar();

}

abstract class InstrumentoCuerda extends InstrumentoMusical {
    private int cantidadCuerdas;

    public InstrumentoCuerda(String material, int cantidadCuerdas) {
        super(material);
        this.cantidadCuerdas = cantidadCuerdas;
    }

    public int getCantidadCuerdas() {
        return cantidadCuerdas;
    }

    abstract void afinar();

}

class Guitarra extends InstrumentoCuerda {

    public Guitarra(String material, int cantidadCuerdas) {
        super(material, cantidadCuerdas);
    }

    @Override
    void tocar() {
        System.out.println("La guitarra está sonando.");
    }

    @Override
    void afinar() {
        System.out.println("Afinando las " + getCantidadCuerdas() + " cuerdas de la guitarra.");
    }
}

class Violín extends InstrumentoCuerda {
    
    public Violín(String material, int cantidadCuerdas) {
        super(material, cantidadCuerdas);
    }
    
    @Override
    void tocar() {
        System.out.println("El violín está sonando.");
    }

    @Override
    void afinar() {
        System.out.println("Afinando las " + getCantidadCuerdas() + " cuerdas del violín.");
    }

}

public class Ejercicio4 {
    
    public static void main(String[] args) {

        Guitarra guitarra = new Guitarra("Madera", 6);
        Violín violín = new Violín("Madera", 4);

        System.out.println("Guitarra:");
        System.out.println("Material: " + guitarra.getMaterial());
        System.out.println("Cantidad de cuerdas: " + guitarra.getCantidadCuerdas());
        guitarra.afinar();
        guitarra.tocar();

        System.out.println("\nViolín:");
        System.out.println("Material: " + violín.getMaterial());
        System.out.println("Cantidad de cuerdas: " + violín.getCantidadCuerdas());
        violín.afinar();
        violín.tocar();
        
    }
}
