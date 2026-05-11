/*
2) Escribir una función en C, que reciba una cadena que representa una palabra y devuelva si la misma es o no un palíndromo. Una palabra es un palíndromo, si se lee igual en ambos sentidos. Probar la función con los siguientes casos de prueba:
    - anilina (Es palíndromo)
    - ojo (Es palíndromo)
    - radar (Es palíndromo)
    - reconocer (Es palíndromo)
    - algoritmos (No es palíndromo)
    - programas (No es palíndromo)
Evitar realizar ciclos innecesarios.
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool esPalindromo(char palabra[]) {
    bool palindormo = true;
    int longitud = strlen(palabra);
    int i = 0;

    while (i< longitud/2 && palindormo) {
        if (palabra[i] != palabra[longitud - 1 - i]) {
            palindormo = false;
        }
        i++;
    }
    return palindormo;
}

int main() {
    // Casos de prueba
    printf("esPalindromo(\"anilina\") = %s\n", esPalindromo("anilina") ? "Es palíndromo" : "No es palíndromo");
    printf("esPalindromo(\"ojo\") = %s\n", esPalindromo("ojo") ? "Es palíndromo" : "No es palíndromo");
    printf("esPalindromo(\"radar\") = %s\n", esPalindromo("radar") ? "Es palíndromo" : "No es palíndromo");
    printf("esPalindromo(\"reconocer\") = %s\n", esPalindromo("reconocer") ? "Es palíndromo" : "No es palíndromo");
    printf("esPalindromo(\"algoritmos\") = %s\n", esPalindromo("algoritmos") ? "Es palíndromo" : "No es palíndromo");
    printf("esPalindromo(\"programas\") = %s\n", esPalindromo("programas") ? "Es palíndromo" : "No es palíndromo");

    return 0;
}