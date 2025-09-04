package rolgar;

public class Enemigo {
    private String nombre;
    private int vida;
    private int posX;
    private int posY;

    public Enemigo(String nombre, int vida, int posX, int posY) {
        this.nombre = nombre;
        this.vida = vida;
        this.posX = posX;
        this.posY = posY;
    }

    public String getNombre() { return nombre; }
    public int getVida() { return vida; }
    public int getPosX() { return posX; }
    public int getPosY() { return posY; }

    public void setVida(int vida) { this.vida = vida; }
}
