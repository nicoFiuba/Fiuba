#!/bin/bash
cat ../Ejercicio1/Intro/Ejercicio/datos_personales.txt #muestra el contenido de datos personales.txt
cp ../Ejercicio1/Intro/Ejercicio/datos_personales.txt datos_personales_mod.txt #copia el contenido de datos personales.txt en un archivo llamado datos_personales_mod.txt
sed -i 's/soltero/casado/g' datos_personales_mod.txt #Busca las ocurrencias de la palabra ‘soletero’ y las cambia por ‘casado’. Se usa el ‘-i’ para que modifique el archivo. Se usa ‘…/g’ para que busque todas las ocurrencias (sino solo busca la primera)
cat datos_personales_mod.txt #Muestra el contenido de datos_personales_mod.txt
wc -c datos_personales_mod.txt #Cuenta la cantidad de caracteres letras en el archivo