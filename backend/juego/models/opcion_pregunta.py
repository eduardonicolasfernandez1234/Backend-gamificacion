from django.db import models

from backend.models import TimeStampedModel
from juego.models import Pregunta


class OpcionPregunta(TimeStampedModel):
    opcion = models.CharField(max_length=1000)
    # Foreign Keys
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='pregunta_opcion', null=True)
