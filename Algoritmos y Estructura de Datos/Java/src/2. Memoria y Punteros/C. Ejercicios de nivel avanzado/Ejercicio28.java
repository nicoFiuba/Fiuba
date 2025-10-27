public class Ejercicio28 {

    public static void main(String[] args) {
        
        Runtime runtime = Runtime.getRuntime();
        long memoriaAntes = runtime.totalMemory() - runtime.freeMemory();
        System.out.println("Memoria usada antes de asignar el array: " + memoriaAntes + " bytes");

        int[] array = new int[1000000];

        long memoriaDespues = runtime.totalMemory() - runtime.freeMemory();
        System.out.println("Memoria usada despues de asignar el array: " + memoriaDespues + " bytes");
        
    }
    
}
