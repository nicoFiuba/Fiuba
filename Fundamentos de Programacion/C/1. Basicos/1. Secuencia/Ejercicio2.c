/*
2) Calcular el sueldo de un operario ingresando por teclado la cantidad de horas que trabajó en el mes y el valor de la hora. Mostrarle el resultado al usuario con un mensaje adecuado.
*/

#include <stdio.h>

int main() {
    float horasTrabajadas, valorHora, sueldo;

    printf("Ingrese la cantidad de horas trabajadas en el mes: ");
    scanf("%f", &horasTrabajadas);

    printf("Ingrese el valor de la hora: ");
    scanf("%f", &valorHora);

    sueldo = horasTrabajadas * valorHora;

    printf("El sueldo del operario es: %.2f \n", sueldo);

    return 0;
}