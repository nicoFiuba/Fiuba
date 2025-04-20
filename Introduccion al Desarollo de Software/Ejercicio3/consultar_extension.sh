#!/bin/bash

echo -n 'Ingrese la exension: '
read ext

find . -type f -name '*.'$ext
