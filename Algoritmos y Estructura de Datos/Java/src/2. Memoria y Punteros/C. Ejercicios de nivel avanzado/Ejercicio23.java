public class Ejercicio23 {

    public static void main(String[] args) {

        long tiempoInicial, tiempoFinal, duracionClonado1, duracionClonado2;

        int[] vector = {1, 2, 3, 4, 5};
        System.out.println("Vector original: " + vector[0] + ", " + vector[1] + ", " + vector[2] + ", " + vector[3] + ", " + vector[4]);

        System.out.println("Clonando el vector mediante la copia de referencia");

        tiempoInicial = System.nanoTime();
        int[] vector2 = vector;
        tiempoFinal = System.nanoTime();
        duracionClonado1 = tiempoFinal - tiempoInicial;

        System.out.println("Vector2: " + vector2[0] + ", " + vector2[1] + ", " + vector2[2] + ", " + vector2[3] + ", " + vector2[4]);
        System.out.println("El tiempo de clonado fue de: " + duracionClonado1 + " nanosegundos");

        System.out.println("Clonando el vector mediante la copia de valores");

        tiempoInicial = System.nanoTime();
        int[] vector3 = vector.clone();
        tiempoFinal = System.nanoTime();
        duracionClonado2 = tiempoFinal - tiempoInicial;

        System.out.println("Vector3: " + vector3[0] + ", " + vector3[1] + ", " + vector3[2] + ", " + vector3[3] + ", " + vector3[4]);
        System.out.println("El tiemplo de clonado fue de: " + duracionClonado2 + " nanosegundos");

    }

}
