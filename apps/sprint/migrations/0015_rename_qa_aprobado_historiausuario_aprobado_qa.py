# Generated by Django 3.2.6 on 2021-10-28 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0014_merge_0011_actividad_fecha_0013_auto_20211025_0120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historiausuario',
            old_name='QA_aprobado',
            new_name='aprobado_QA',
        ),
    ]