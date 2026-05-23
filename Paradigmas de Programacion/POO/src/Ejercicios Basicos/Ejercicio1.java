interface FiguraGeometrica {
    double calcularArea();
    double calcularPerimetro();
}

class Circulo implements FiguraGeometrica {
    private double radio;

    public Circulo(double radio) {
        this.radio = radio;
    }
    
    @Override
    public double calcularArea() {
        return Math.PI * Math.pow(radio, 2);
    }

    @Override
    public double calcularPerimetro() {
        return 2 * Math.PI * radio;
    }

}

class Rectangulo implements FiguraGeometrica {
    private double base;
    private double altura;

    public Rectangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
    }

    @Override
    public double calcularArea() {
        return base * altura;
    }

    @Override
    public double calcularPerimetro() {
        return 2 * (base + altura);
    }

}

class Triangulo implements FiguraGeometrica {
    private double lado1;
    private double lado2;
    private double lado3;

    public Triangulo(double lado1, double lado2, double lado3) {
        this.lado1 = lado1;
        this.lado2 = lado2;
        this.lado3 = lado3;
    }

    @Override
    public double calcularArea() {
        double semiperimetro = (lado1 + lado2 + lado3) / 2;
        return Math.sqrt(semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3));
    }

    @Override
    public double calcularPerimetro() {
        return lado1 + lado2 + lado3;
    }

}

public class Ejercicio1 {
    
    public static void main(String[] args) {

        Circulo circulo = new Circulo(5);
        Rectangulo rectangulo = new Rectangulo(4, 6);
        Triangulo triangulo = new Triangulo(3, 4, 5);

        System.out.println("Círculo:");
        System.out.println("Área: " + circulo.calcularArea());
        System.out.println("Perímetro: " + circulo.calcularPerimetro());

        System.out.println("\nRectángulo:");
        System.out.println("Área: " + rectangulo.calcularArea());
        System.out.println("Perímetro: " + rectangulo.calcularPerimetro());

        System.out.println("\nTriángulo:");
        System.out.println("Área: " + triangulo.calcularArea());
        System.out.println("Perímetro: " + triangulo.calcularPerimetro());
    }
}
