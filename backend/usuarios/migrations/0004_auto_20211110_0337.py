# Generated by Django 3.2.8 on 2021-11-10 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20211110_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='inicio_sesion_consecutivo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='puntaje_diario',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AddField(
            model_name='usuario',
            name='rachas_preguntas',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usuario',
            name='ultima_conexion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='puntaje_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]
