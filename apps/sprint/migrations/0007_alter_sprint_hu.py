# Generated by Django 3.2.6 on 2021-09-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0031_historiausuario_sprint_backlog'),
        ('sprint', '0006_alter_sprint_hu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='hu',
            field=models.ManyToManyField(blank=True, limit_choices_to={'aprobado_PB': True, 'sprint_backlog': False}, null=True, related_name='hu', to='proyectos.HistoriaUsuario'),
        ),
    ]
