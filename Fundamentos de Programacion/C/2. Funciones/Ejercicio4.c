/*
4) Escribir una función que dado un tiempo expresado en segundos, devuelva por parámetros el equivalente en días, horas, minutos y segundos. Utilizar esta función dentro de un programa que solicite el valor al usuario. Se debe validar que el valor ingresado sea entero positivo, de lo contrario, deberá mostrarse el mensaje: “Valor ingresado inválido”. 
Ejemplo:
Valor ingresado representando una cantidad de segundos: 1234567
Resultado: Días: 14, Horas: 6, Minutos: 56, Segundos 7
Para verificar el resultado pueden ir a la siguiente web:
https://www.satsig.net/training/seconds-days-hours-minutes-calculator.htm
*/

# include <stdio.h>

void calcular_fecha(int segundos){
    int minuto = 60, hora = 60*minuto, dia = 24*hora;

    int dias = segundos / dia;
    segundos %= dia;
    int horas = segundos / hora;
    segundos %= hora;
    int minutos = segundos / minuto;
    segundos %= minuto;

    printf("Días: %d, Horas: %d, Minutos: %d, Segundos: %d\n", dias, horas, minutos, segundos);
}

int main() {
    
    int segundos;

    printf("Ingrese una cantidad de segundos (entero positivo): ");
    scanf("%i", &segundos);

    if (segundos < 0) {
        printf("Valor ingresado inválido\n");
        return 1;
    }
    calcular_fecha(segundos);
    return 0;
}