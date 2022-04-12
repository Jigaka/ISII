# INSTRUCCIONES PARA CONFIGURAR Y LEVANTAR EL ENTORNO

## Instalar python 3.8.10
```shell
sudo apt-get install python3.8
```

## Instalar el módulo *venv* para crear entornos virtuales
```shell
sudo apt-get install python3.8-venv
```

## Instalar postgresql
```shell
sudo apt-get install postgresql postgresql-contrib
```

## Acceder al psql
```shell
sudo su postgres
```
```shell
psql
```
Una vez dentro, crear el usuario **postgres** con la contraseña **postgres**. 
```shell
CREATE USER postgres WITH ENCRYPTED PASSWORD 'postgres';
```
Crear la base de datos **desarrollo**.
```shell
CREATE DATABASE desarrollo;
```

## Crear entorno virtual de python, acceder al entorno y activarlo
Crear entorno
```shell
python3 -m venv <nombre_entorno>
```
Acceder al entorno
```shell
cd <nombre_entorno>
```
Activar entorno
```shell
source bin/activate
```

## Descargar repositorio
Dentro de la carpeta *<nombre_entorno>* descargar repositorio con el comando
```shell
git clone https://github.com/Jigaka/ISII.git
```
ó vía SSH
```shell
git clone git@github.com:Jigaka/ISII.git
```

## Instalar los paquetes necesarios para levantar el entorno
Ingresar a la carpeta del repositorio (IMPORTANTE: el entorno debe estar activado)
```shell
cd ISII
```
Instalar los paquetes 
```shell
pip install -r paquetes.txt
```
## Levantar entorno
```shell
python3 manage.py makemigrations
```
```shell
python3 manage.py migrate
```
```shell
python3 manage.py runserver
```
Ingresar a http://127.0.0.1:8000/

OBS: El login aún no funciona