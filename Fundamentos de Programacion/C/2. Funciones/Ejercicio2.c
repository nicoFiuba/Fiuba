/*
2) Escribir una función que dado un número entero, devuelva un valor booleano que indique si dicho número es primo o no.
*/

# include <stdio.h>
#include <stdbool.h>

bool es_primo(int num) {
    bool primo = true; 
    if (num < 2){
        primo = false; 
    } else {
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                primo = false; 
            }
        }
    }
    return primo;
}

int main(){
    // Pruebas de la función es_primo
    printf("¿El número 5 es primo? %s\n", es_primo(5) ? "Sí" : "No"); // Debe imprimir Sí
    printf("¿El número 10 es primo? %s\n", es_primo(10) ? "Sí" : "No"); // Debe imprimir No
    printf("¿El número 13 es primo? %s\n", es_primo(13) ? "Sí" : "No"); // Debe imprimir Sí
    printf("¿El número 1 es primo? %s\n", es_primo(1) ? "Sí" : "No"); // Debe imprimir No
    printf("¿El número 2 es primo? %s\n", es_primo(2) ? "Sí" : "No"); // Debe imprimir Sí
    return 0;
}