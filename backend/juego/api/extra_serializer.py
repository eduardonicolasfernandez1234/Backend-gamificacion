from django.db.models import fields
from rest_framework import serializers
from juego.models import Pregunta, OpcionPregunta, ModoJuego

class ModoJuegoSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModoJuego
        fields = ['id', 'juego_id', 'nombre', 'descripcion', 'puntaje_limite', 'bloqueado', 'puntaje_maximo',
            'imagen_modojuego', 'puntaje_maximo_jugador', 'color']

class PreguntaSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pregunta
        fields = ['id', 'modo_juego_id', 'numero', 'pregunta', 'puntos_correcto', 
            'puntos_incorrecto', 'respuesta', 'ayuda', 'imagen_pregunta', 'imagen_juego']


class OpcionPreguntaSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = OpcionPregunta
        fields = ['id', 'pregunta_id', 'opcion']