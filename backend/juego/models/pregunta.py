from django.db import models

from backend.models import TimeStampedModel
from juego.models import ModoJuego


class Pregunta(TimeStampedModel):
    numero = models.IntegerField()
    pregunta = models.CharField(max_length=5000)
    puntos_correcto = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    puntos_incorrecto = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    respuesta = models.CharField(max_length=1000)
    ayuda = models.CharField(max_length=1000, null=True)
    imagen_pregunta = models.FileField(db_column="imagen_nivel", upload_to="juego/recursos", null=True)
    imagen_juego = models.FileField(db_column="imagen_juego", upload_to="juego/recursos", null=True)

    # Foreign Keys
    modo_juego = models.ForeignKey(ModoJuego, on_delete=models.CASCADE, related_name='modo_juego_pregunta')
