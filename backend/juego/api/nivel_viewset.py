from rest_framework import serializers, viewsets, status
from juego.models import Nivel, ModoJuego
from juego.api import ModoJuegoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class NivelSerializer(serializers.ModelSerializer):

    modo_juego = ModoJuegoSerializer(many=False, read_only=True)
    modo_juego_id = serializers.PrimaryKeyRelatedField(
        many=False, write_only=True, queryset=ModoJuego.objects.all(), source='modo_juego'
    )

    class Meta:
        model = Nivel
        fields = "__all__"

class NivelViewSet(viewsets.ModelViewSet):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer