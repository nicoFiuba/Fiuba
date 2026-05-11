/*
1) Escribir una función para validar una nueva clave de acceso. La función deberá recibir una cadena de caracteres, que contendrá la clave candidata, que ya fue ingresada previamente por el usuario. Devolverá true o false, dependiendo de si cumple o no, con las siguientes condiciones:
    - La clave debe estar formada únicamente por, entre 6 y 12 caracteres numéricos
    - La cantidad de dígitos pares debe ser mayor a la de los impares.
A los sumo debe recorrer una vez la cadena.
Evite realizar ciclos innecesarios.
Compruebe el correcto funcionamiento, incluyendo los siguientes casos de prueba:
validar("j20893") devuelve false
validar("20893a") devuelve false
validar("208X930") devuelve false
validar("20201") devuelve false
validar("23445776") devuelve false
validar("089010") devuelve true
validar("02784532132567") devuelve false
validar("027845320011") devuelve true
*/

# include <stdio.h>
# include <stdbool.h>
# include <string.h>

bool validar(char clave[]){
    bool valida= true;
    int longitud = strlen(clave);

    if (longitud < 6 || longitud > 12) {
        valida = false;
    }
    
    int cant_pares = 0, cant_impares = 0, i = 0;

    while ( i< longitud && valida) {
        if (clave[i] < '0' || clave[i] > '9') {
            valida = false;
        } else {
            int digito = clave[i] - '0'; 
            if (digito % 2 == 0) {
                cant_pares++;
            } else {
                cant_impares++;
            }
        }
        i++;
    }

    if (valida && cant_impares >= cant_pares) {
        valida = false;
    }

    return valida;
}

int main() {
    // Casos de prueba
    printf("validar(\"j20893\") = %s\n", validar("j20893") ? "true" : "false");
    printf("validar(\"20893a\") = %s\n", validar("20893a") ? "true" : "false");
    printf("validar(\"208X930\") = %s\n", validar("208X930") ? "true" : "false");
    printf("validar(\"20201\") = %s\n", validar("20201") ? "true" : "false");
    printf("validar(\"23445776\") = %s\n", validar("23445776") ? "true" : "false");
    printf("validar(\"089010\") = %s\n", validar("089010") ? "true" : "false");
    printf("validar(\"02784532132567\") = %s\n", validar("02784532132567") ? "true" : "false");
    printf("validar(\"027845320011\") = %s\n", validar("027845320011") ? "true" : "false");
    return 0;
}