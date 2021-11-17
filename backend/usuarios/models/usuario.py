from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Usuario(AbstractUser):
    puntaje_total = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    logros = ArrayField(models.CharField(max_length=200), blank=True, default=list())
    estatus_actual = models.CharField(max_length=255, null=True)
    logros_temporal = ArrayField(models.CharField(max_length=200), blank=True, default=list())
    rachas_preguntas = models.IntegerField(default=0)
    inicio_sesion_consecutivo = models.IntegerField(default=0)
    puntaje_diario = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    ultima_conexion = models.DateTimeField(auto_now=True)
    cantidad_ayuda_solicitada = models.IntegerField(default=0)
    productos_canjeados = ArrayField(models.CharField(max_length=200), blank=True, default=list())
