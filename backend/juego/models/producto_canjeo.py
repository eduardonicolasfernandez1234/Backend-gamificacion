from django.db import models

from backend.models import TimeStampedModel
from juego.models import Canjeo


class ProductoCanjeo(TimeStampedModel):

    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)
    imagen = models.FileField(db_column="imagen_producto_canjeo", upload_to="juego/recursos", null=True)
    miniatura = models.FileField(db_column="imagen_producto_canjeo_miniatura", upload_to="juego/recursos", null=True)
    puntos_necesarios = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    # Foriegn Keys
    canjeo = models.ForeignKey(Canjeo, on_delete=models.CASCADE, related_name='producto_canjeo_canjeo')
