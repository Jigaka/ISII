# Generated by Django 3.2.6 on 2021-10-27 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0014_merge_0011_actividad_fecha_0013_auto_20211025_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='fecha_fin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='fecha_inicio',
            field=models.DateField(blank=True, null=True),
        ),
    ]