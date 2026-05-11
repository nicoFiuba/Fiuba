/*
2) Escribir una función en C, que reciba:
    a) como primer parámetro un vector de números enteros;
    b) como segundó parámetro, la cantidad de elementos en el vector;
    c) como tercer parámetro deberá devolver la cantidad de valores negativos que hay en el vector recibido;
    d) como cuarto parámetro, la cantidad de elementos positivos que hay en el vector recibido.
Escribir el programa que incluya a la función y las invocaciones con los
siguientes ejemplos, y la respectiva impresión de los valores devueltos:
Probar el programa con los siguiente casos:
v1 = [2,8,1,-5,4] -> Negativos: 1 Positivos: 4
v2 = [-2,-15,-3] -> Negativos: 3 Positivos: 0
v3 = [0,0,10,12,23,55,1] -> Negativos: 0 Positivos: 5
*/

# include <stdio.h>

void contarNegativosPositivos(int vector[], int cantidad, int cant_negativos[], int cant_positivos[]) {
    cant_negativos[0] = 0;
    cant_positivos[0] = 0;

    for (int i = 0; i < cantidad; i++) {
        if (vector[i] < 0) {
            cant_negativos[0]++;
        } else if (vector[i] > 0) {
            cant_positivos[0]++;
        }
    }
}

int main() {
    int v1[] = {2, 8, 1, -5, 4};
    int v2[] = {-2, -15, -3};
    int v3[] = {0, 0, 10, 12, 23, 55, 1};

    int cant_negativos[1], cant_positivos[1];

    contarNegativosPositivos(v1, 5, cant_negativos, cant_positivos);
    printf("v1 = [2, 8, 1, -5, 4] -> Negativos: %d Positivos: %d\n", cant_negativos[0], cant_positivos[0]);
    contarNegativosPositivos(v2, 3, cant_negativos, cant_positivos);
    printf("v2 = [-2, -15, -3] -> Negativos: %d Positivos: %d\n", cant_negativos[0], cant_positivos[0]);
    contarNegativosPositivos(v3, 7, cant_negativos, cant_positivos);
    printf("v3 = [0, 0, 10, 12, 23, 55, 1] -> Negativos: %d Positivos: %d\n", cant_negativos[0], cant_positivos[0]);
    
    return 0;
}