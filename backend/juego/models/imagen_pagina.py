from django.db import models

from backend.models import TimeStampedModel


class ImagenPagina(TimeStampedModel):
    imagen = models.FileField(upload_to='imagen_pagina', null=True)