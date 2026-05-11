/*
4) Solicitar al usuario el ingreso de una temperatura (puede tener decimales por ejemplo 24.5) y la unidad en la que se encuentra (siendo solo un carácter F ó C). Luego el programa debe mostrar la temperatura ingresada, convertida en la otra unidad. La relación entre temperaturas Celsius y Fahrenheit está dada por la fórmula: C=5.0 / 9.0 * (F − 32)
*/

#include <stdio.h>

int main(){
    float temperatura;
    char unidad;

    printf("Ingrese la temperatura: ");
    scanf("%f", &temperatura);
    printf("Ingrese la unidad (C para Celsius, F para Fahrenheit): ");
    scanf(" %c", &unidad);

    if (unidad == 'C' || unidad == 'c') {
        float farenheit = (temperatura * 9.0 / 5.0) + 32;
        printf("La temperatura en Fahrenheit es: %.2f F\n", farenheit);
    } else if (unidad == 'F' || unidad == 'f') {
        float celsius = 5.0 / 9.0 * (temperatura - 32);
        printf("La temperatura en Celsius es: %.2f C\n", celsius);
    } else {
        printf("Unidad no reconocida. Por favor, ingrese 'C' o 'F'.\n");
    }
    return 0;
}