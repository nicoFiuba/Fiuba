abstract class Vehiculo {
    private String marca;
    private String modelo;
    private int año;
    
    public Vehiculo(String marca, String modelo, int año) {
        this.marca = marca;
        this.modelo = modelo;
        this.año = año;
    }
    public String getMarca() {
        return marca;
    }
    
    public String getModelo() {
        return modelo;
    }
    
    public int getAño() {
        return año;
    }
    
    public abstract void moverse();

}

class Auto extends Vehiculo {
    
    public Auto(String marca, String modelo, int año) {
        super(marca, modelo, año);
    }
    
    @Override
    public void moverse() {
        System.out.println("El auto se está moviendo.");
    }

}

class Bicicleta extends Vehiculo {
    
    public Bicicleta(String marca, String modelo, int año) {
        super(marca, modelo, año);
    }
    
    @Override
    public void moverse() {
        System.out.println("La bicicleta se está moviendo.");
    }

}

class Barco extends Vehiculo {
    
    public Barco(String marca, String modelo, int año) {
        super(marca, modelo, año);
    }
    
    @Override
    public void moverse() {
        System.out.println("El barco se está moviendo.");
    }

}

public class Ejercicio2 {
    
    public static void main(String[] args) {
        
        Auto auto = new Auto("Toyota", "Corolla", 2020);
        Bicicleta bicicleta = new Bicicleta("Giant", "Escape 3", 2021);
        Barco barco = new Barco("Yamaha", "242X", 2019);
        
        System.out.println("Auto:");
        System.out.println("Marca: " + auto.getMarca());
        System.out.println("Modelo: " + auto.getModelo());
        System.out.println("Año: " + auto.getAño());
        auto.moverse();
        
        System.out.println("\nBicicleta:");
        System.out.println("Marca: " + bicicleta.getMarca());
        System.out.println("Modelo: " + bicicleta.getModelo());
        System.out.println("Año: " + bicicleta.getAño());
        bicicleta.moverse();
        
        System.out.println("\nBarco:");
        System.out.println("Marca: " + barco.getMarca());
        System.out.println("Modelo: " + barco.getModelo());
        System.out.println("Año: " + barco.getAño());
        barco.moverse();
    }
}
