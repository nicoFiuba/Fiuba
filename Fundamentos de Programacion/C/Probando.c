/*
B) Definir una función *pertenece* recursiva en C que recibe un vector de enteros por parámetro, su tamaño y un valor entero y devuelve 1 si dicho valor está en el vector, 0, en caso contrario.

`int pertenece(int vec[], int n, int valor);`
*/

# include <stdio.h>
#include <stdlib.h>

int pertenece(int vec[], int n, int valor) {
    // Caso base: si el tamaño es 0, el valor no está en el vector
    if (n <= 0) {
        return 0;
    }
    // Si el último elemento es igual al valor buscado, retornar 1
    if (vec[n - 1] == valor) {
        return 1;
    }
    // Llamada recursiva para el resto del vector
    return pertenece(vec, n - 1, valor);
}