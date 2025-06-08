/*
1) Dado un listado de números reales del cual no se conoce la cantidad, almacenar los números en un vector en el orden de entrada. Informar la cantidad de números y el contenido del vector indicando la posición ocupada por cada número a partir de la primera posición. Considerar una estructura de datos de tamaño físico máximo de 1000 posiciones.
*/

# include <stdio.h>

int main(){

    float numeros[1000];
    float numero = 0.0;
    int cantidad = 0;

    printf("Ingrese números reales (ingrese un número negativo para finalizar):\n");
    
    while (cantidad < 1000 && numero >= 0) {
        printf("Número %d: ", cantidad + 1);
        scanf("%f", &numero);

        numeros[cantidad] = numero;
        cantidad++;
    }

    printf("\nCantidad de números ingresados: %d\n", cantidad - 1);
    printf("Contenido del vector:\n");
    for (int i = 0; i < cantidad - 1; i++) {
        printf("Posición %d: %.2f\n", i + 1, numeros[i]);
    }
    return 0;
}