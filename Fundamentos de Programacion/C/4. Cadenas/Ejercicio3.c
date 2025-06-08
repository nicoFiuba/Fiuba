/*
3) Escribir un programa modular en C, que solicite el ingreso de 3 oraciones, de no más de 50 caracteres cada una. Luego informar: 1. Cuál es la oración más larga. 2. Si hay al menos 2 oraciones iguales. 3. Solicitar el ingreso de una palabra o parte de una oración, e indicar si la misma se encuentra en las oraciones, y en cuales.
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX_LENGTH 51 // 50 caracteres + '\0'
#define NUM_ORACIONES 3

// Función para ingresar las oraciones
void ingresarOraciones(char oraciones[NUM_ORACIONES][MAX_LENGTH])
{
    printf("Ingrese 3 oraciones (max 50 caracteres cada una):\n");
    for (int i = 0; i < NUM_ORACIONES; i++)
    {
        printf("Oracion %d: ", i + 1);
        fgets(oraciones[i], MAX_LENGTH, stdin);
        fflush(stdin); // Limpiar el buffer de entrada
        oraciones[i][strcspn(oraciones[i], "\n")] = '\0'; // Eliminar el salto de línea
    }
}

// Función para encontrar la oración más larga
void encontrarMasLarga(char oraciones[NUM_ORACIONES][MAX_LENGTH])
{
    int max_longitud = 0;
    int indice_mas_larga = 0;

    for (int i = 0; i < NUM_ORACIONES; i++)
    {
        int longitud = strlen(oraciones[i]);
        if (longitud > max_longitud)
        {
            max_longitud = longitud;
            indice_mas_larga = i;
        }
    }

    printf("\n1. La oracion mas larga es: \"%s\" (longitud: %d)\n", oraciones[indice_mas_larga], max_longitud);
}

// Función para verificar si hay al menos 2 oraciones iguales
void verificarOracionesIguales(char oraciones[NUM_ORACIONES][MAX_LENGTH])
{
    bool iguales = false;

    for (int i = 0; i < NUM_ORACIONES - 1 && !iguales; i++)
    {
        for (int j = i + 1; j < NUM_ORACIONES && !iguales; j++)
        {
            if (strcmp(oraciones[i], oraciones[j]) == 0)
            {
                iguales = true;
            }
        }
    }

    printf("2. ¿Hay al menos 2 oraciones iguales? %s\n", iguales ? "Si" : "No");
}

// Función para buscar una palabra en las oraciones
void buscarPalabra(char oraciones[NUM_ORACIONES][MAX_LENGTH])
{
    char palabra[MAX_LENGTH];
    printf("\n3. Ingrese una palabra o parte de una oracion a buscar: ");
    fgets(palabra, MAX_LENGTH, stdin);
    fflush(stdin); // Limpiar el buffer de entrada
    palabra[strcspn(palabra, "\n")] = '\0';

    bool encontrada = false;
    printf("   Resultados de busqueda:\n");

    for (int i = 0; i < NUM_ORACIONES; i++)
    {
        if (strstr(oraciones[i], palabra) != NULL)
        {
            printf("   - La palabra \"%s\" esta en la oracion %d: \"%s\"\n", palabra, i + 1, oraciones[i]);
            encontrada = true;
        }
    }

    if (!encontrada)
    {
        printf("   - La palabra \"%s\" no se encontro en ninguna oracion.\n", palabra);
    }
}

int main()
{
    char oraciones[NUM_ORACIONES][MAX_LENGTH];

    ingresarOraciones(oraciones);
    encontrarMasLarga(oraciones);
    verificarOracionesIguales(oraciones);
    buscarPalabra(oraciones);

    return 0;
}