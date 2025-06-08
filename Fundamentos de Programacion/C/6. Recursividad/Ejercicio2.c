/*
2) Desarrollar un programa que calcule y muestre por pantalla los primeros N términos de la sucesión de Fibonacci en forma recursiva. N es un número ingresado por el usuario.
*/

#include <stdio.h>
#include <stdlib.h>

int fibonacci(int num) {
    if (num == 0) {
        return 0;
    } else if (num == 1) {
        return 1;
    } else {
        return fibonacci(num - 1) + fibonacci(num - 2);
    }
}

int main() {
    int n;

    // Solicitar al usuario el número de términos de Fibonacci
    printf("Ingrese el número de términos de la sucesión de Fibonacci a mostrar: ");
    scanf("%d", &n);

    // Validar que n sea no negativo
    if (n < 0) {
        printf("El número de términos debe ser no negativo.\n");
        return 1;
    }

    // Mostrar los primeros N términos de la sucesión de Fibonacci
    printf("Los primeros %d términos de la sucesión de Fibonacci son:\n", n);
    for (int i = 0; i < n; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n");

    return 0;
}