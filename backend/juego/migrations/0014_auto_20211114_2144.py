# Generated by Django 3.2.8 on 2021-11-15 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0013_categoriapuzzle_imagenpuzzle_subimagenpuzzle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoriapuzzle',
            name='bloqueado',
        ),
        migrations.RemoveField(
            model_name='categoriapuzzle',
            name='path',
        ),
        migrations.AlterField(
            model_name='categoriapuzzle',
            name='imagen_modojuego',
            field=models.FileField(db_column='imagen_categoria_puzzle', null=True, upload_to='juego/recursos'),
        ),
    ]
