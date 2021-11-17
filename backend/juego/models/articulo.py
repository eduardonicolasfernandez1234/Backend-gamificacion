from django.db import models

from backend.models import TimeStampedModel


class Articulo(TimeStampedModel):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=10000)