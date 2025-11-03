public class Ejercicio12 {
    
    public static int[][] multiplicar(int[][] A, int[][] B) {
        
        int longA = A.length;
        
        if (longA == 1) {
            return new int[][]{{A[0][0] * B[0][0]}};
        }

        int longMedia = longA / 2;

        int[][] A11 = new int[longMedia][longMedia];
        int[][] A12 = new int[longMedia][longMedia];
        int[][] A21 = new int[longMedia][longMedia];
        int[][] A22 = new int[longMedia][longMedia];

        int[][] B11 = new int[longMedia][longMedia];
        int[][] B12 = new int[longMedia][longMedia];
        int[][] B21 = new int[longMedia][longMedia];
        int[][] B22 = new int[longMedia][longMedia];
        
        dividirMatriz(A, A11, 0, 0);
        dividirMatriz(A, A12, 0, longMedia);
        dividirMatriz(A, A21, longMedia, 0);
        dividirMatriz(A, A22, longMedia, longMedia);

        dividirMatriz(B, B11, 0, 0);
        dividirMatriz(B, B12, 0, longMedia);
        dividirMatriz(B, B21, longMedia, 0);
        dividirMatriz(B, B22, longMedia, longMedia);
        
        int[][] S1 = agregarMatrices(A11, A22);
        int[][] S2 = agregarMatrices(B11, B22);
        int[][] P1 = multiplicar(S1, S2); 
        int[][] S3 = agregarMatrices(A21, A22);
        int[][] P2 = multiplicar(S3, B11); 
        int[][] S4 = subtractMatrices(B12, B22);
        int[][] P3 = multiplicar(A11, S4); 
        int[][] S5 = subtractMatrices(B21, B11);
        int[][] P4 = multiplicar(A22, S5); 
        int[][] S6 = agregarMatrices(A11, A12);
        int[][] P5 = multiplicar(S6, B22); 
        int[][] S7 = subtractMatrices(A21, A11);
        int[][] S8 = agregarMatrices(B11, B12);
        int[][] P6 = multiplicar(S7, S8); 
        int[][] S9 = subtractMatrices(A12, A22);
        int[][] S10 = agregarMatrices(B21, B22);
        int[][] P7 = multiplicar(S9, S10); 
        
        int[][] C11 = agregarMatrices(P1, P4);
        C11 = subtractMatrices(C11, P5);
        C11 = agregarMatrices(C11, P7);

        int[][] C12 = agregarMatrices(P3, P5);
        int[][] C21 = agregarMatrices(P2, P4);

        int[][] C22 = agregarMatrices(P1, P3);
        C22 = subtractMatrices(C22, P2);
        C22 = agregarMatrices(C22, P6);

        int[][] C = new int[longA][longA];
        combinarMatrices(C11, C, 0, 0);
        combinarMatrices(C12, C, 0, longMedia);
        combinarMatrices(C21, C, longMedia, 0);
        combinarMatrices(C22, C, longMedia, longMedia);
        
        return C;
    }
    
    private static void dividirMatriz(int[][] padre, int[][] hijo, int empezarFila, int empezarColumna) {
        
        int longMedia = hijo.length;
        
        for (int i = 0; i < longMedia; i++) {
            for (int j = 0; j < longMedia; j++) {
                hijo[i][j] = padre[empezarFila + i][empezarColumna + j];
            }

        }

    }

    private static void combinarMatrices(int[][] hijo, int[][] padre, int empezarFila, int empezarColumna) {
        
        int longMedia = hijo.length;

        for (int i = 0; i < longMedia; i++) {
            for (int j = 0; j < longMedia; j++) {
                padre[empezarFila + i][empezarColumna + j] = hijo[i][j];
            }

        }

    }

    private static int[][] agregarMatrices(int[][] A, int[][] B) {
        
        int n = A.length;
        int[][] C = new int[n][n];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                C[i][j] = A[i][j] + B[i][j];
            }

        }

        return C;
    }

    private static int[][] subtractMatrices(int[][] A, int[][] B) {
        
        int n = A.length;
        int[][] C = new int[n][n];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                C[i][j] = A[i][j] - B[i][j];
            }

        }

        return C;
    }

    private static void mostrarMatriz(int[][] matrix) {
        
        for (int[] row : matrix) {
            for (int val : row) {
                System.out.printf("%4d", val);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        
        int[][] A = {
            {1, 2, 3, 4},
            {5, 6, 7, 8},
            {9, 10, 11, 12},
            {13, 14, 15, 16}
        };

        int[][] B = {
            {16, 15, 14, 13},
            {12, 11, 10, 9},
            {8, 7, 6, 5},
            {4, 3, 2, 1}
        };

        System.out.println("--- Matriz A ---");
        mostrarMatriz(A);
        
        System.out.println();

        System.out.println("--- Matriz B ---");
        mostrarMatriz(B);

        int[][] C = multiplicar(A, B);

        System.out.println("\n--- Resultado Strassen (A * B) ---");
        mostrarMatriz(C);

    }

}
