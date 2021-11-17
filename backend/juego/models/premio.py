from django.db import models

from backend.models import TimeStampedModel


class Premio(TimeStampedModel):

    CATEGORIA_PUNTOS_DIARIOS = 1
    CATEGORIA_INICIO_CONSECUTIVO = 2
    CATEGORIA_RESPUESTAS_CONSECUTIVAS = 3
    CATEGORIA_AYUDA_SOLICITADA = 4
    TIPOS_CATEGORIA = (
        (CATEGORIA_PUNTOS_DIARIOS, 'puntos diarios'),
        (CATEGORIA_INICIO_CONSECUTIVO, 'inicio consecutivo'),
        (CATEGORIA_RESPUESTAS_CONSECUTIVAS, 'respuestas consecutivas'),
        (CATEGORIA_AYUDA_SOLICITADA, 'ayuda solicitada'),
    )

    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    imagen = models.FileField(db_column="imagen_canjeo", upload_to="juego/recursos", null=True)
    miniatura = models.FileField(db_column="imagen_canjeo_miniatura", upload_to="juego/recursos", null=True)
    categoria = models.PositiveBigIntegerField(choices=TIPOS_CATEGORIA, default=1)
    puntos_requeridos = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    
