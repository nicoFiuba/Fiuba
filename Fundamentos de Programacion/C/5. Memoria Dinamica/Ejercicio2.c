/*
2) Escribir un programa el cual reserve memoria dinámica para almacenar una cierta cantidad de números enteros (n * int), este valor n debe ser ingresado por el usuario. Luego solicitarle que ingresé n valores enteros ingresados de a uno y almacenarlos en la memoria previamente reservada. Mostrar luego todos los valores ingresados. Liberar la memoria reservada al finalizar el programa.
*/

#include <stdio.h>
#include <stdlib.h>

int main(){
    int num;
    
    // Solicitar al usuario la cantidad de números enteros
    printf("Ingrese la cantidad de números enteros a almacenar: ");
    scanf("%d", &num);
    
    // Reservar memoria dinámica para n enteros
    int *nums = (int *)malloc(num * sizeof(int));
    
    // Solicitar al usuario que ingrese los n valores enteros
    for (int i = 0; i < num ; i++) {
        printf("Ingrese el número %d: ", i + 1);
        scanf("%d", &nums[i]);
    }
    
    // Mostrar los valores ingresados
    printf("Los números ingresados son:\n");
    for (int i = 0; i < num; i++) {
        printf("%d ", nums[i]);
    }
    printf("\n");
    
    // Liberar la memoria reservada
    free(nums);
    
    return 0;
}