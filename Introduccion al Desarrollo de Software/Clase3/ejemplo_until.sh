# Crear un script utilizando until que genere un número random entre 1 y 20, si los valores están entre 5 y 10 el bucle deberá terminar.

#!/bin/bash

numero_random=$((RANDOM % 20 + 1))

until [ $numero_random -le 10 -a $numero_random -ge 5 ]
do
echo "El numero $numero_random no esta entre 5 y 10, voy a generar otro numero"
numero_random=$((RANDOM % 21))
done
echo "El numero $numero_random esta entre 5 y 10, el bucle ha terminado"
