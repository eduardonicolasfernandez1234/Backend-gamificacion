from django.db import models

from backend.models import TimeStampedModel
from juego.models import Juego
from usuarios.models import Usuario

class ModoJuego(TimeStampedModel):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=2000)
    puntaje_limite = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    bloqueado = models.BooleanField(default=False)
    puntaje_maximo = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    imagen_modojuego = models.FileField(db_column="imagen_modojuego", upload_to="juego/recursos", null=True)
    color = models.CharField(max_length=12, null=True)
    
    # Foreign keys
    puntaje_maximo_jugador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='modo_jugador', null=True)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, related_name='modo_juego')
