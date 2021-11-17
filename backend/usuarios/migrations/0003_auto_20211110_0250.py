# Generated by Django 3.2.8 on 2021-11-10 06:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_puntaje_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='estatus_actual',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='logros',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), null=True, size=None),
        ),
        migrations.AddField(
            model_name='usuario',
            name='logros_temporal',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), null=True, size=None),
        ),
    ]