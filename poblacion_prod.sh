#!/bin/bash
#El primer argumento de este programa es la contrasenha del usuario de la database
START=$(date +%s.%N)
echo 'Creando database...'
heroku pg:reset DATABASE_URL -a apepu-gestor --confirm apepu-gestor
echo 'Poblando base de datos...'
heroku pg:psql postgresql-defined-44252 --app apepu-gestor < desarrollo_heroku.sql
END=$(date +%s.%N)
DIFF=$(echo "$END - $START" | bc)
echo '+-------------------------------------+'
echo '| Base de datos poblada correctamente |'
echo '+-------------------------------------+' 
echo 'Tiempo empleado: '$DIFF' segundos'
