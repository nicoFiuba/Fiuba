/*
Ingresar un número entero y decir si: a) es par o impar. b) es mayor, menor o igual a cero.
*/

#include <stdio.h>

int main(){
    int numero;

    printf("Ingrese un numero entero: ");
    scanf("%i", &numero);

    if (numero % 2 == 0){
        printf("El numero es par.\n");
    } else {
        printf("El numero es impar.\n");
    }

    if (numero > 0){
        printf("El numero es mayor que cero.\n");
    } else if (numero < 0){
        printf("El numero es menor que cero.\n");
    } else {
        printf("El numero es igual a cero.\n");
    }
    return 0;
}