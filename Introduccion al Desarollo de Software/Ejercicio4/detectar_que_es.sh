# Crear un script que reciba un parámetro y determine…
#   a) Si es un directorio → que liste los archivos contenidos dentro del mismo
#   b) Si es un archivo → que muestre por pantalla su contenido
#   c) En otro caso → que muestre por pantalla el mensaje: “No es archivo, ni directorio”




#!/bin/bash

echo  -n 'Ingrese el nombre del archivo o directorio: '
read nombre

if [ -d $nombre ]; then
    echo 'Es un directorio y su contenido es:' 
    ls $nombre
elif [ -f $nombre ]; then
    echo 'Es un archivo y su contenido es:'
    cat $nombre
    echo
else
    echo 'No es archivo, ni directorio'
fi