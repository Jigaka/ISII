# Generated by Django 3.2.6 on 2021-11-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0022_historiausuario_horas_trabajadas'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiausuario',
            name='horas_trabajadas_en_total',
            field=models.IntegerField(default=0),
        ),
    ]
