1- PARA EMPEZAR A TRABAJAR, ABRIR LA TERMINAL ABAJO DE VSC(click en los 2 simbolos abajo a la izq.) Y ESCRIBIR:

python manage.py runserver

2- PARA REGISTRAR CAMBIOS EN LA TABLA

python manage.py makemigrations

si añades un campo (default='') para que no sea un campo obligatorio, te pedira' que quieres hacer con los alumnos que ya estaban registrados:

opcion 1 darle un valor de default(null o blank o 0 si es un numero o un '-' )

opcion 2 darle un valor manualmente y te saca del proceso

3- UNA VEZ SOLUCIONADO EL PROBLEMA

python manage.py migrate

4- VOLVE' A ARRANCAR EL SERVIDOR

python manage.py runserver