# Generated by Django 3.2.8 on 2021-11-15 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('juego', '0012_articulo_datocurioso_imagenpagina'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaPuzzle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200)),
                ('path', models.CharField(max_length=2000)),
                ('puntaje_limite', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('bloqueado', models.BooleanField(default=False)),
                ('puntaje_maximo', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('imagen_modojuego', models.FileField(db_column='imagen_modojuego', null=True, upload_to='juego/recursos')),
                ('juego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_puzzle', to='juego.juego')),
                ('puntaje_maximo_jugador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jugador_max_puzzle', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImagenPuzzle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('imagen', models.FileField(db_column='imagen_puzzle', null=True, upload_to='juego/recursos')),
                ('puntos_recompensa', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('puntos_error', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('puntos_acierto', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('descripcion', models.CharField(max_length=1200)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagen_categoria_puzzle', to='juego.categoriapuzzle')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubImagenPuzzle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('imagen', models.FileField(db_column='subimagen_puzzle', upload_to='juego/recursos')),
                ('identificador', models.IntegerField(default=0)),
                ('index', models.IntegerField(default=0)),
                ('imagen_puzzle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subimagen_puzzle_imagen', to='juego.imagenpuzzle')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
