from rest_framework import serializers, viewsets, status
from juego.models import Pregunta, OpcionPregunta, OpcionPregunta
from juego.api import PreguntaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class OpcionPreguntaSerializer(serializers.ModelSerializer):

    pregunta = PreguntaSerializer(many=False, read_only=True)
    pregunta_id = serializers.PrimaryKeyRelatedField(
        many=False, write_only=True, queryset=Pregunta.objects.all(), source='pregunta'
    )

    class Meta:
        model = OpcionPregunta
        fields = "__all__"

class OpcionPreguntaViewSet(viewsets.ModelViewSet):
    queryset = OpcionPregunta.objects.all()
    serializer_class = OpcionPreguntaSerializer