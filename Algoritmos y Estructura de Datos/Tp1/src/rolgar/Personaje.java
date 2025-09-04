package rolgar;

public class Personaje {
    private String nombre;
    private int vida;
    private int posX;
    private int posY;
    private int vidaMaxima;

    public Personaje(String nombre, int vida, int posX, int posY) {
        this.nombre = nombre;
        this.vida = vida;
        this.vidaMaxima = vida;
        this.posX = posX;
        this.posY = posY;
    }

    public void recuperarVida() {
    int recuperacion = (int)(vida * 0.05); // 5%
    if (recuperacion < 1) recuperacion = 1; // mínimo 1 punto
    vida += recuperacion;
    if (vida > vidaMaxima) vida = vidaMaxima;
}

    // --- Getters y setters ---
    public String getNombre() { return nombre; }
    public int getVida() { return vida; }
    public int getPosX() { return posX; }
    public int getPosY() { return posY; }

    public void setVida(int vida) { this.vida = vida; }
    public void setPosX(int posX) { this.posX = posX; }
    public void setPosY(int posY) { this.posY = posY; }

    // --- Métodos de acción ---
    public void moverArriba() { posX--; }
    public void moverAbajo() { posX++; }
    public void moverIzquierda() { posY--; }
    public void moverDerecha() { posY++; }
    
}
