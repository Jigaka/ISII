# Generated by Django 3.2.6 on 2021-10-28 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0016_alter_historiausuario_aprobado_qa'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiausuario',
            name='rechazado_QA',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='historiausuario',
            name='aprobado_QA',
            field=models.BooleanField(default=False),
        ),
    ]