from django.db import models
from backend.models import TimeStampedModel
from juego.models import CategoriaPuzzle

class ImagenPuzzle(TimeStampedModel):
    imagen = models.FileField(db_column="imagen_puzzle", upload_to="juego/recursos", null=True)
    puntos_recompensa = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    puntos_error = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    puntos_acierto = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    descripcion = models.CharField(max_length=1200)
    # Foreign keys
    categoria = models.ForeignKey(CategoriaPuzzle, on_delete=models.CASCADE, related_name='imagen_categoria_puzzle')
