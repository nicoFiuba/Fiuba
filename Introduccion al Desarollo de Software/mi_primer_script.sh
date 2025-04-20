#!/bin/bash

echo -n 'Ingrese un nota: '
read x

if [ $x -ge 4 ]; then
echo 'Ud. aprobó el examen'
else
echo 'No aprobó el examen, su nota es menor a 4'
fi
