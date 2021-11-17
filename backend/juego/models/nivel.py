from django.db import models

from backend.models import TimeStampedModel
from juego.models import ModoJuego


class Nivel(TimeStampedModel):
    numero = models.IntegerField(unique=True)
    codigo_nivel = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=5000)
    imagen_nivel = models.FileField(db_column="imagen_nivel", upload_to="juego/recursos", null=True)
    imagen_juego = models.FileField(db_column="imagen_juego", upload_to="juego/recursos", null=True)

    # Foreign Keys
    modo_juego = models.OneToOneField(ModoJuego, on_delete=models.CASCADE, primary_key=True)
