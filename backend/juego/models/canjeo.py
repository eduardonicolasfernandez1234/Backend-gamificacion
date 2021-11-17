from django.db import models

from backend.models import TimeStampedModel


class Canjeo(TimeStampedModel):

    CATEGORIA_ALIMENTOS = 1
    CATEGORIA_PRODUCTOS = 2
    CATEGORIA_SERVICIOS = 3
    CATEGORIA_TICKETS = 4
    TIPO_ESTATUS = (
        (CATEGORIA_ALIMENTOS, 'Alimentos'),
        (CATEGORIA_PRODUCTOS, 'Productos'),
        (CATEGORIA_SERVICIOS, 'Servicios'),
        (CATEGORIA_TICKETS, 'Tickets'),
    )

    nombre = models.CharField(max_length=200)
    imagen = models.FileField(db_column="imagen_canjeo", upload_to="juego/recursos", null=True)
    miniatura = models.FileField(db_column="imagen_canjeo_miniatura", upload_to="juego/recursos", null=True)
    categoria = models.PositiveBigIntegerField(choices=TIPO_ESTATUS, default=1)
    puntos_base = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    
