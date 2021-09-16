# Generated by Django 3.2.6 on 2021-09-15 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0020_auto_20210908_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Iniciado', 'Iniciado'), ('Finalizado', 'Finalizado')], default=1, max_length=15)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.proyec')),
            ],
            options={
                'verbose_name': 'Sprint',
                'verbose_name_plural': 'Sprints',
            },
        ),
    ]