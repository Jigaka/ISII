# Generated by Django 3.2.6 on 2021-09-27 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0030_delete_sprint'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiausuario',
            name='sprint_backlog',
            field=models.BooleanField(default=False),
        ),
    ]