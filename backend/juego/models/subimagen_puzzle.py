from django.db import models
from backend.models import TimeStampedModel
from juego.models import ImagenPuzzle

class SubImagenPuzzle(TimeStampedModel):
    imagen = models.FileField(db_column="subimagen_puzzle", upload_to="juego/recursos")
    identificador = models.IntegerField(default=0)
    index = models.IntegerField(default=0)
    # Foreign keys
    imagen_puzzle = models.ForeignKey(ImagenPuzzle, on_delete=models.CASCADE, related_name='subimagen_puzzle_imagen')
