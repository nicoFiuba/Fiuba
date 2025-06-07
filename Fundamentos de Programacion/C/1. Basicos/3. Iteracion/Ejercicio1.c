/*
5) Solicitar un número entero positivo al usuario y calcular su factorial. En el caso de ingresar un número negativo mostrar un mensaje que diga “no se puede calcular el factorial del número ingresado”. Recordar que por definición factorial(0)=1 y factorial(1)=1
*/

# include <stdio.h>

int main(){
    int numero;
    int factorial = 1;

    printf("Ingrese un numero entero positivo: ");
    scanf("%d", &numero);
    if (numero < 0){
        printf("No se puede calcular el factorial del numero ingresado.\n");
    } else {
        for (int i =1; i <= numero; i++){
            factorial *= i;
        }
        printf("El factorial de %d es: %d\n", numero, factorial);
    }
    return 0;
}