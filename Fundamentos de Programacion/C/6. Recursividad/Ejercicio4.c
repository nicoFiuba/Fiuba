/*
4) Desarrollar una función recursiva que compruebe si un número es binario. Un número binario está formado únicamente por ceros y unos.
Sugerencia: recordar el uso de operadores % (mod) y / (div)
202 % 10 = 2
202 / 10 = 20
Ejemplos:
es_binario(101) -> true
es_binario(2) -> false
es_binario(20) -> false
es_binario(1) -> true
es_binario(0) -> true
es_binario(100000) -> true
es_binario(100009) -> false
*/

#include <stdio.h>
#include <stdbool.h>

bool es_binario(int numero) {

    // Caso base: si el número es 0 o 1, es binario
    if (numero == 0 || numero == 1) {
        return true;
    }
    // Caso base: si el número es menor que 0, no es binario
    if (numero < 0) {
        return false;
    }
    // Verificar el último dígito del número
    if (numero % 10 > 1) {
        return false; // Si el último dígito es mayor que 1, no es binario
    }
    // Llamada recursiva eliminando el último dígito
    return es_binario(numero / 10);
}

int main() {
    int numero;

    // Solicitar al usuario que ingrese un número
    printf("Ingrese un número: ");
    scanf("%d", &numero);

    // Verificar si el número es binario
    if (es_binario(numero)) {
        printf("El número %d es binario.\n", numero);
    } else {
        printf("El número %d no es binario.\n", numero);
    }

    return 0;
}