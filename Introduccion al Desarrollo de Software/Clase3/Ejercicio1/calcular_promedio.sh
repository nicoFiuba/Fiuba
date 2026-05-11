# Solicitar al usuario el ingreso de 10 valores enteros y calcular el promedio de los mismos.

echo "Ingrese 10 valores enteros para calcular el promedio:"
suma=0
contador=0
while [ $contador -lt 10 ]; do
    read -p "Valor $((contador + 1)): " valor
    suma=$((suma + valor))
    contador=$((contador + 1))
done
promedio=$((suma / 10))
echo "El promedio de los valores ingresados es: $promedio"
