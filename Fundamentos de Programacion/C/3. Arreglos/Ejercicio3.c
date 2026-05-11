/*
3) Dado un vector a ordenado ascendente de longitud ml y un elemento p del mismo tipo que los elementos del vector, insertar p en el vector a de modo que siga ordenado. Validar previamente que en el vector haya espacio libre para guardar el nuevo dato. Se solicita resolver lo solicitado recorriendo una sola vez el vector y sin utilizar un arreglo auxiliar.
Ejemplo:
nuevo elemento p=14
[3|6|9|16|21|45|...|...]
[3|6|9|14|16|21|45|...]
*/

#include <stdio.h>

#define MAX 10

int main() {
    int vector_ascendente[MAX] = {3, 6, 9, 16, 21, 45};
    int ml = 6; // longitud actual del vector 
    int p = 14; // elemento a insertar

    // Validar espacio
    if (ml >= MAX) {
        printf("No hay espacio para insertar un nuevo elemento.\n");
        return 1;
    }

    int i;
    // Buscar la posición donde insertar p
    for (i = 0; i < ml && vector_ascendente[i] < p; i++);

    // Desplazar los elementos a la derecha para hacer espacio
    for (int j = ml; j > i; j--) {
        vector_ascendente[j] = vector_ascendente[j - 1];
    }

    // Insertar p en la posición correcta
    vector_ascendente[i] = p;
    ml++;

    // Mostrar el vector resultante
    printf("Vector después de insertar %d:\n", p);
    for (int k = 0; k < ml; k++) {
        printf("%d ", vector_ascendente[k]);
    }
    printf("\n");

    return 0;
}