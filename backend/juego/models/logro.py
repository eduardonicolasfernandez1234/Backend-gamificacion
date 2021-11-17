from django.db import models

from backend.models import TimeStampedModel


class Logro(TimeStampedModel):

    CATEGORIA_PUNTOS_DIARIOS = 1
    CATEGORIA_INICIO_CONSECUTIVO = 2
    CATEGORIA_RESPUESTAS_CONSECUTIVAS = 3
    CATEGORIA_AYUDA_SOLICITADA = 4
    TIPOS_CATEGORIA = (
        (CATEGORIA_PUNTOS_DIARIOS, 'puntos diarios'),
        (CATEGORIA_INICIO_CONSECUTIVO, 'inicio consecutivo'),
        (CATEGORIA_RESPUESTAS_CONSECUTIVAS, 'respuestas consecutivas'),
        (CATEGORIA_AYUDA_SOLICITADA, 'ayuda solicitada'),
    )

    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)
    imagen = models.FileField(db_column="imagen_juego", upload_to="juego/recursos", null=True)
    miniatura = models.FileField(db_column="imagen_juego_miniatura", upload_to="juego/recursos", null=True)
    temporal = models.BooleanField(default=False)
    puntos_recompensa = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    categoria = models.PositiveBigIntegerField(choices=TIPOS_CATEGORIA, default=1)
    puntos_diarios = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    inicio_consecutivo = models.IntegerField(default=0)
    respuesta_consecutiva = models.IntegerField(default=0)
    ayuda_solicitada = models.IntegerField(default=0)
