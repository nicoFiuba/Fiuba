# Crear un script que le pregunte al usuario por una extensión.
# A continuación, el script debe evaluar la existencia de archivos con esa extensión y listarlos por pantalla.

#!/bin/bash

echo -n 'Ingrese la exension: '
read ext

find . -type f -name '*.'$ext
