/*
1) Escribir un programa el cual reserve memoria dinámica para almacenar un número entero (int), le solicite al usuario el ingreso de un número y se asigna dicho valor en la memoria reservada, luego mostrar dicho valor por pantalla. Liberar la memoria reservada al finalizar el programa.
*/

#include <stdio.h>
#include <stdlib.h>

int main() {
    // Reservar memoria dinámica para un entero
    int *numero = (int *)malloc(sizeof(int));
    
    // Solicitar al usuario el ingreso de un número
    printf("Ingrese un número entero: ");
    scanf("%d", numero);

    // Mostrar el valor ingresado
    printf("El número ingresado es: %d\n", *numero);

    // Liberar la memoria reservada
    free(numero);

    return 0;
}
