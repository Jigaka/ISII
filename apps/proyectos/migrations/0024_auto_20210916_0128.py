# Generated by Django 3.2.6 on 2021-09-16 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0023_alter_historiausuario_fecha_creacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyec',
            name='US',
        ),
        migrations.AddField(
            model_name='historiausuario',
            name='proyecto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proyecto', to='proyectos.proyec'),
        ),
    ]