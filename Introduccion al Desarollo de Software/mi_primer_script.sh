# 1) Crear con algún editor un archivo llamado mi_script.sh
# 2) Dentro del mismo, incluir el siguiente código:
# 3) Ejecutar el script con el comando bash mi_script.sh

#!/bin/bash

echo -n 'Ingrese un nota: '
read x

if [ $x -ge 4 ]; then
echo 'Ud. aprobó el examen'
else
echo 'No aprobó el examen, su nota es menor a 4'
fi
