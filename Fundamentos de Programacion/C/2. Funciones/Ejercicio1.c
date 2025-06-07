/*
Importante: Luego de escribir cada función, probala, invocándola desde el bloque principal del programa, pasándole distintos valores para que la prueba contemple varias alternativas y así estar seguro que funciona adecuadamente.

1) Escribir una función que reciba un valor n, entero, y devuelva la suma de los valores entre 0 y n.
Ejemplos:
suma_n(5) = 15
suma_n(120) = 7260
*/

# include <stdio.h>

int suma_n(int num){
    int suma = 0;
    for (int i = 0; i <= num; i++) {
        suma += i;
    }
    return suma;
}

int main() {
    // Pruebas de la función suma_n
    printf("Suma de valores entre 0 y 5: %d\n", suma_n(5)); // Debe imprimir 15
    printf("Suma de valores entre 0 y 120: %d\n", suma_n(120)); // Debe imprimir 7260
    return 0;
}