# Crear un script utilizando while que permita imprimir el mensaje “Bienvenido por vez número: “  5 veces.

#!/bin/bash
i=1
while [ $i -le 5 ]
do
    echo "Bienvenido por vez número: $i"
    i=$((i + 1))
done
