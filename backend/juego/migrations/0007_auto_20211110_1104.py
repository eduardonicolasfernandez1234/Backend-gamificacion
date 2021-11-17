# Generated by Django 3.2.8 on 2021-11-10 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0006_logro_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logro',
            old_name='puntos',
            new_name='puntos_diarios',
        ),
        migrations.AddField(
            model_name='logro',
            name='ayuda_solicitada',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='logro',
            name='inicio_consecutivo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='logro',
            name='puntos_recompensa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='logro',
            name='respuesta_consecutiva',
            field=models.IntegerField(default=0),
        ),
    ]
