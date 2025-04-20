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