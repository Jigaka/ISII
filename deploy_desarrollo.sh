#!/bin/bash
cd '..'
source 'bin/activate'
cd 'ISII'
git pull
# $1 el nombre de la rama a probar el tag
# $2 el nombre del tag
git checkout -b $1 $2
sh poblacion_dev.sh postgres
python3 manage.py runserver
