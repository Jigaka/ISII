# Generated by Django 3.2.6 on 2021-10-22 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0006_alter_historiausuario_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiausuario',
            name='rechazado_PB',
            field=models.BooleanField(default=False),
        ),
    ]