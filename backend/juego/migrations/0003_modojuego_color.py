# Generated by Django 3.2.8 on 2021-11-09 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0002_auto_20211107_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='modojuego',
            name='color',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]