# Crear un script que reciba como parámetro el nombre de un archivo y muestre un menú con las siguientes opciones.
#   1- Ver el contenido del archivo
#   2- Editar el archivo con el editor nano
#   3- Ver los permisos del archivo
#   * - Salir

#!/bin/bash

archivo=$1

echo "Seleccione una opción:"
echo "1) Ver el contenido del archivo"
echo "2) Editar el archivo con nano"
echo "3) Ver los permisos del archivo"
echo "*) Salir"
read -p "Ingrese su opción: " opcion

case $opcion in
    1)
        echo "El contenido del archivo es:"
        cat "$archivo"
        ;;
    2)
        nano "$archivo"
        ;;
    3)
        ls -l "$archivo"
        ;;
    *)
        echo "Saliendo..."
        ;;
esac

