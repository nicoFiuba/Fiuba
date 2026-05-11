/*
3) Escribir una función que reciba un valor entero y calcule el factorial del mismo. Si no se puede calcular el factorial del valor recibido, la función deberá devolver 0, de lo contrario deberá devolver el valor calculado.
*/

#include <stdio.h>
#include <stdlib.h>

int calcular_factorial(int num){

    int factorial;

    if (num < 0){
        factorial = 0;
    } else if (num == 0 || num == 1){
        factorial = 1;
    } else {
        factorial = 1;
        for (int i = 2; i <= num; i++){
            factorial *= i;
        }
    }
    return factorial;
}


int main()
{
    // Ejemplo de uso de la función calcular_factorial
    printf("El factorial de 5 es: %d\n", calcular_factorial(5));   // Debe imprimir 120
    printf("El factorial de -3 es: %d\n", calcular_factorial(-3)); // Debe imprimir 0
    printf("El factorial de 0 es: %d\n", calcular_factorial(0));   // Debe imprimir 1
    printf("El factorial de 8 es: %d\n", calcular_factorial(8));   // Debe imprimir 40320
}