# Generated by Django 3.2.8 on 2021-11-10 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20211110_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cantidad_ayuda_solicitada',
            field=models.IntegerField(default=0),
        ),
    ]
