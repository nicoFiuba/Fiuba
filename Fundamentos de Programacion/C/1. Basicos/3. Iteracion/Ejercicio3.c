/*
7) Dado un número entero positivo ingresado por el usuario, procesarlo e indicar: (realizar un programa diferente para cada caso)
    a) La cantidad de dígitos pares e impares que lo componen.
    b) El menor y el mayor dígito del número.
Recordar uso de división y módulo:
Ejemplo:
111 / 10 = 11
111 % 10 = 1
*/

// a)

#include <stdio.h>

int main(){
    int numero, cant_pares = 0, cant_impares = 0;

    printf("Ingrese un numero entero positivo: ");
    scanf("%i", &numero);

    if (numero <= 0) {
        printf("El numero debe ser positivo.\n");
    }

    while (numero > 0) {
        int digito = numero % 10;
        
        if (digito % 2 == 0) {
            cant_pares++;
        } else {
            cant_impares++;
        }
        numero /= 10;
    }
    printf("Cantidad de digitos pares: %i\n", cant_pares);
    printf("Cantidad de digitos impares: %i\n", cant_impares);
    return 0;
}  

// b)

# include <stdio.h>

int main(){

    int numero, mayor, menor;

    printf("Ingrese un numero entero positivo: ");
    scanf("%i", &numero);

    if (numero <= 0) {
        printf("El numero debe ser positivo.\n");
    }

    mayor = numero % 10; 
    menor = numero % 10;

    while (numero > 0) {
        int digito = numero % 10;

        if (digito > mayor) {
            mayor = digito;
        }
        if (digito < menor) {
            menor = digito;
        }
        numero /= 10;
    }
    printf("El mayor digito es: %i\n", mayor);
    printf("El menor digito es: %i\n", menor);
    return 0;
}