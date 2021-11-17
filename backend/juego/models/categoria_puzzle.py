from django.db import models

from backend.models import TimeStampedModel
from juego.models import Juego
from usuarios.models import Usuario

class CategoriaPuzzle(TimeStampedModel):
    nombre = models.CharField(max_length=200)
    puntaje_limite = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    imagen_modojuego = models.FileField(db_column="imagen_categoria_puzzle", upload_to="juego/recursos", null=True)
    
    # Foreign keys
    puntaje_maximo_jugador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='jugador_max_puzzle', null=True)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, related_name='categoria_puzzle')
