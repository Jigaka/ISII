#!/bin/bash
#El primer argumento de este programa es la contrasenha del usuario de la database
START=$(date +%s.%N)
echo 'Creando database...'
PGPASSWORD=$1 psql -U postgres -h localhost -a -f crearDataBase.sql > /dev/null
echo 'Poblando base de datos...'
PGPASSWORD=$1 psql -U postgres -h localhost desarrollo < desarrollo.sql
END=$(date +%s.%N)
DIFF=$(echo "$END - $START" | bc)
echo '+-------------------------------------+'
echo '| Base de datos poblada correctamente |'
echo '+-------------------------------------+' 
echo 'Tiempo empleado: '$DIFF' segundos'
