from django.db import models

from backend.models import TimeStampedModel


class Estatus(TimeStampedModel):

    ESTATUS_BASICO = 1
    ESTATUS_MEDIO = 2
    ESTATUS_INTERMEDIO = 3
    ESTATUS_AVANZADO = 4
    ESTATUS_SUPERIOR = 5
    ESTATUS_LIDER = 6
    TIPO_ESTATUS = (
        (ESTATUS_BASICO, 'Basico'),
        (ESTATUS_MEDIO, 'Medio'),
        (ESTATUS_INTERMEDIO, 'Intermedio'),
        (ESTATUS_AVANZADO, 'Avanzado'),
        (ESTATUS_SUPERIOR, 'Superior'),
        (ESTATUS_LIDER, 'Lider'),
    )

    nombre = models.CharField(max_length=200)
    imagen = models.FileField(db_column="imagen_juego", upload_to="juego/recursos", null=True)
    miniatura = models.FileField(db_column="imagen_juego_miniatura", upload_to="juego/recursos", null=True)
    categoria = models.PositiveBigIntegerField(choices=TIPO_ESTATUS, default=1)
    puntos_recompensa = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    puntos_base = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    
