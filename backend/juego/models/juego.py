from django.db import models

from backend.models import TimeStampedModel


class Juego(TimeStampedModel):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)
    imagen = models.FileField(db_column="imagen_juego", upload_to="juego/recursos", null=True)
    miniatura = models.FileField(db_column="imagen_juego_miniatura", upload_to="juego/recursos", null=True)
    enlace_juego = models.CharField(max_length=200, null=True)