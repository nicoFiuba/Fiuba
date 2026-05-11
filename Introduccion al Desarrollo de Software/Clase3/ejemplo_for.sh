# Crear un script que permita recorrer todos los archivos de un directorio y muestre el contenido de los que sean de extención .txt

#!/bin/bash

archivos=$(ls)
for archivo in $archivos;
do
    if [[ $archivo == *.txt ]]; then
        echo "El contenido del archivo $archivo es:"
        cat "$archivo"
        echo ""
    fi
done