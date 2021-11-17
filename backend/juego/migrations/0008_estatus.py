# Generated by Django 3.2.8 on 2021-11-10 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0007_auto_20211110_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200)),
                ('imagen', models.FileField(db_column='imagen_juego', null=True, upload_to='juego/recursos')),
                ('miniatura', models.FileField(db_column='imagen_juego_miniatura', null=True, upload_to='juego/recursos')),
                ('categoria', models.PositiveBigIntegerField(choices=[(1, 'Basico'), (2, 'Medio'), (3, 'Intermedio'), (4, 'Avanzado'), (5, 'Superior'), (6, 'Lider')], default=1)),
                ('puntos_recompensa', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('puntos_base', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
