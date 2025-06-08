/*
5) Desarrollar una función recursiva que reciba un arreglo de enteros y su
máximo lógico. La función debe retornar la cantidad de números pares
presentes en el arreglo.
Ejemplo:
[23, 44, 68, 2, 24, 12] -> 5
*/

#include <stdio.h>
#include <stdbool.h>

int contar_pares(int arr[], int max_logico) {
    // Caso base: si el máximo lógico es 0, no hay elementos que contar
    if (max_logico <= 0) {
        return 0;
    }
    
    // Verificar si el último elemento es par
    int ultimo_elemento = arr[max_logico - 1];
    int es_par = (ultimo_elemento % 2 == 0) ? 1 : 0;

    // Llamada recursiva para el resto del arreglo
    return es_par + contar_pares(arr, max_logico - 1);
}

int main() {
    int arr[] = {23, 44, 68, 2, 24, 12};
    int max_logico = sizeof(arr) / sizeof(arr[0]); // Calcular el tamaño del arreglo

    // Contar los números pares en el arreglo
    int cantidad_pares = contar_pares(arr, max_logico);

    // Mostrar el resultado
    printf("Cantidad de números pares en el arreglo: %d\n", cantidad_pares);

    return 0;
}
