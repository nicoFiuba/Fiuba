/*
3) Desarrollar una función recursiva para realizar una búsqueda binaria en un vector.
*/

#include <stdio.h>
#include <stdlib.h>

int binarySearch(int array[], int izq, int der, int target){
    if (izq > der) {
        return -1; // Elemento no encontrado
    }

    int mid = izq + (der - izq) / 2;

    if (array[mid] == target) {
        return mid; // Elemento encontrado
    } else if (array[mid] > target) {
        return binarySearch(array, izq, mid - 1, target); // Buscar en la mitad izquierda
    } else {
        return binarySearch(array, mid + 1, der, target); // Buscar en la mitad derecha
    }
}

int main() {
    int vect, target;

    // Solicitar al usuario la cantidad de elementos del vector
    printf("Ingrese la cantidad de elementos del vector: ");
    scanf("%d", &vect);

    // Reservar memoria dinámica para el vector 
    int *array = (int *)malloc(vect * sizeof(int));
    if (array == NULL) {
        printf("Error al reservar memoria.\n");
        return 1;
    }
    
    // Solicitar al usuario que ingrese los elementos del vector
    printf("Ingrese los elementos del vector en orden ascendente:\n");
    for (int i = 0; i < vect; i++) {
        printf("Elemento %d: ", i + 1);
        scanf("%d", &array[i]);
    }
    
    // Solicitar al usuario el elemento a buscar
    printf("Ingrese el elemento a buscar: ");
    scanf("%d", &target);
    
    // Realizar la búsqueda binaria
    int result = binarySearch(array, 0, vect - 1, target);
    
    // Mostrar el resultado
    if (result != -1) {
        printf("Elemento %d encontrado en la posición %d.\n", target, result);
    } else {
        printf("Elemento %d no encontrado en el vector.\n", target);
    }

    // Liberar la memoria reservada
    free(array);
    return 0;
}