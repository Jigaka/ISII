# Generated by Django 3.2.6 on 2021-10-28 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0015_rename_qa_aprobado_historiausuario_aprobado_qa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiausuario',
            name='aprobado_QA',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
