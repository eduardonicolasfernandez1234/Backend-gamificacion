# Generated by Django 3.2.8 on 2021-11-10 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0004_alter_modojuego_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=1000)),
                ('imagen', models.FileField(db_column='imagen_juego', null=True, upload_to='juego/recursos')),
                ('miniatura', models.FileField(db_column='imagen_juego_miniatura', null=True, upload_to='juego/recursos')),
                ('temporal', models.BooleanField(default=False)),
                ('puntos', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
