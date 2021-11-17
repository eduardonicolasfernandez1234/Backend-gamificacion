from django.db import models

from backend.models import TimeStampedModel


class DatoCurioso(TimeStampedModel):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    enlace = models.CharField(max_length=500)