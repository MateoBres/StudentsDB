# Generated by Django 3.1.1 on 2020-10-30 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichero_alumnos', '0022_auto_20201030_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno_mes',
            name='horario',
            field=models.CharField(blank=True, default='', help_text='00dia  /  00dia', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='alumno_mes',
            name='telefono',
            field=models.CharField(blank=True, default='', help_text='0000  012345', max_length=30, null=True),
        ),
    ]
