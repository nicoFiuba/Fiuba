#Crear un script llamado menu.sh que reciba un parámetro con el nombre de un archivo. El script deberá tener el siguiente  menú que permita:
#   1) Ingresar una palabra y reemplazarla por **** en el archivo pasado por parámetro
#   2) abrir el archivo
#   3) realizar una copia del archivo llamada menu_copia.sh
#   4) Ingresar un email y validarlo mediante RE.
#   5)  Salir

#!/bin/bash


archivo=$1

if [ -z "$archivo" ]; then 
    echo "Por favor, proporciona el nombre de un archivo como argumento."
    exit 1
elif [ ! -f "$archivo" ]; then
    echo "El archivo '$archivo' no existe."
    exit 1
fi

echo "Seleccione una opción:"
echo "1) Ingresar una palabra y reemplazarla por **** en el archivo"
echo "2) Abrir el archivo"
echo "3) Realizar una copia del archivo llamada menu_copia.sh"
echo "4) Ingresar un email y validarlo mediante RE"
echo "5) Salir"
read -p "Ingrese su opción: " opcion

case $opcion in
    1)
        read -p "Ingrese la palabra a reemplazar: " palabra 
        if [ -z "$palabra" ]; then
            echo "No se ingresó ninguna palabra. Saliendo..."
            exit 1
        elif [ ! -f "$palabra" ]; then
            echo "La palabra '$palabra' no existe. Saliendo..."
            exit 1
        else 
        sed -i "s/$palabra/****/g" "$archivo"
        echo "La palabra '$palabra' ha sido reemplazada por **** en el archivo '$archivo'."
        exit 0
        fi
        ;;
    2)
        nano "$archivo"
        ;;
    3)
        cp "$archivo" menu_copia.sh
        echo "Se ha creado una copia del archivo '$archivo' llamada 'menu_copia.sh'."
        ;;
    4)
        read -p "Ingrese un email: " email
        if [ -z "$email" ]; then
            echo "No se ingresó ningún email. Saliendo..."
            exit 1
        elif [[ "$email" =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
            echo "El email '$email' es válido."
        else
            echo "El email '$email' no es válido."
        fi

        ;;
    5)
        echo "Saliendo..."
        ;;
esac
