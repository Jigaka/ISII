# Generated by Django 3.2.6 on 2021-09-15 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0022_auto_20210915_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiausuario',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='fecha cre'),
        ),
    ]
