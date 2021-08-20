# ISII

## Tener instalado

- python 3.8.10
- para crear entornos virtuales
```shell
$ sudo apt-get install python3.8-venv
```
- para tener la base de datos postgresql
```shell
$ sudo apt-get install postgresql postgresql-contrib
```

En postgres se debe crear el usuario postgres con la contraseña postgres. Luego crear una base de datos llamada **desarrollo**

## Crear entorno virtual de python

```shell
$ python3 -m venv nombredelentorno
```

## Activar entorno
```shell
$ cd nombre_entorno
$ source bin/activate
```

## Descargar repositorio
Dentro de la carpeta del entorno descargar repositorio
```shell
$ git clone https://github.com/Jigaka/ISII.git
```
## Instalar los paquetes del entorno
Ingresar a la carpeta del repositorio

OBS: tener activado el entorno virtual
```shell
$ pip install -r paquetes.txt
```
## Generar la documentacion automatica
```shell
$ pycco **/*.py -i
```
## Probar el entorno
```shell
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```
Ingresar a http://localhost:8000
OBS: Si el login con google falla, avisarme
