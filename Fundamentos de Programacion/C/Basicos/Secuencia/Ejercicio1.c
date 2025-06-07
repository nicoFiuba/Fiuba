/*
1) Hallar la superficie de un triángulo conociendo la base y la altura. Solicitarle
los datos de entrada al usuario.
*/

#include <stdio.h>

int main() {
    float base, altura, superficie;

    printf("Ingrese el valor de la base del triangulo: ");
    scanf("%f", &base);

    printf("Ingrese el valor de la altura del triangulo: ");
    scanf("%f", &altura);

    superficie = (base * altura) / 2;

    printf("La superficie del triangulo es: %.2f \n", superficie);

    return 0;
}
