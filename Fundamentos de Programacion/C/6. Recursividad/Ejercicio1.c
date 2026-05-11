/*
1) Desarrollar un programa que calcule la factorial de un número en forma recursiva.
*/

# include <stdio.h>
# include <stdlib.h>

int factorial(int num){

    if (num == 0 || num == 1) {
        return 1;
    } else {
        return num * factorial(num - 1);
    }
} 

int main() {
    int num;

    // Solicitar al usuario un número
    printf("Ingrese un número entero para calcular su factorial: ");
    scanf("%d", &num);

    // Validar que el número sea no negativo
    if (num < 0) {
        printf("El factorial no está definido para números negativos.\n");
        return 1;
    }

    // Calcular el factorial
    int result = factorial(num);

    // Mostrar el resultado
    printf("El factorial de %d es: %d\n", num, result);

    return 0;
}
