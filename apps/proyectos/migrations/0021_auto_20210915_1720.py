# Generated by Django 3.2.6 on 2021-09-15 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proyectos', '0020_auto_20210908_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyec',
            name='dias_estimados',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='proyec',
            name='encargado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='encargado', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='proyec',
            name='estado_anterior',
            field=models.CharField(default='Pendiente', max_length=200),
        ),
        migrations.AddField(
            model_name='proyec',
            name='fecha_cancelado',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='proyec',
            name='fecha_concluido',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='proyec',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, default=None, verbose_name='fecha de creacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proyec',
            name='fecha_inicio',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='HistoriaUsuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('ToDo', 'ToDo'), ('Doing', 'Doing'), ('Done', 'Done'), ('QA', 'QA')], default=1, max_length=15)),
                ('fecha', models.DateField(auto_now=True, verbose_name='fecha')),
                ('estimacion', models.PositiveIntegerField(default=0)),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='fecha cre')),
                ('fecha_inicio', models.DateField(null=True)),
                ('fecha_concluido', models.DateField(null=True)),
                ('fecha_cancelado', models.DateField(null=True)),
                ('estado_anterior', models.CharField(default='Pendiente', max_length=200)),
                ('prioridad', models.CharField(choices=[('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta')], default=1, max_length=15)),
                ('asignacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asignacion', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Historia de Usuario',
                'verbose_name_plural': 'Historias de Usuarios',
            },
        ),
        migrations.AddField(
            model_name='proyec',
            name='US',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='US', to='proyectos.historiausuario'),
        ),
    ]