# Generated by Django 3.1.1 on 2020-09-29 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fichero_alumnos', '0011_auto_20200929_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='dias',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='veces',
        ),
    ]
