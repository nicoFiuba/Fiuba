/*
6) Dada una serie de números ingresados de a uno. Indicar mayor, menor y promedio de la serie. El ingreso de números finaliza cuando el usuario ingresa 0.
*/

# include <stdio.h>

int main(){
    int numero, mayor, menor, suma = 0;
    float promedio;

    printf("Ingrese un numero (0 para finalizar): ");
    scanf("%d", &numero);

    if (numero == 0) {
        printf("No se ingresaron numeros.\n");
    } else{
        mayor = numero;
        menor = numero;
        suma = numero;
        int contador = 0;
        
        while (numero != 0) {
            printf("Ingrese un numero (0 para finalizar): ");
            scanf("%d", &numero);
            
            if (numero != 0) {
                if (numero > mayor) {
                    mayor = numero;
                } else if (numero < menor) {
                    menor = numero;
                }
                suma += numero;
            }
            contador++;
        }
        promedio = suma / contador;
        printf("Mayor: %i\n", mayor);
        printf("Menor: %i\n", menor);
        printf("Promedio: %.2f\n", promedio);
    }
    return 0;
}