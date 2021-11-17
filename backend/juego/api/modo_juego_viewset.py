from rest_framework import serializers, viewsets, status
from juego.models import ModoJuego, Juego
from juego.api import JuegoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class ModoJuegoSerializer(serializers.ModelSerializer):

    juego = JuegoSerializer(many=False, read_only=True)
    juego_id = serializers.PrimaryKeyRelatedField(
        many=False, write_only=True, queryset=Juego.objects.all(), source='juego'
    )

    class Meta:
        model = ModoJuego
        fields = "__all__"

class ModoJuegoViewSet(viewsets.ModelViewSet):
    queryset = ModoJuego.objects.all()
    serializer_class = ModoJuegoSerializer


    @action(detail=True, methods=['get'], url_path="preguntas",
            name="Obtener lista de preguntas por modo de juego")
    def listar_preguntas_por_modo_juego(self, request, pk=None):
        if pk is None:
            return Response({
                "detalle": "Falta la llave foránea",
                "status_code": 404
            }, status=status.HTTP_404_NOT_FOUND)
        try:
            ModoJuego.objects.get(id=pk)
        except ModoJuego.DoesNotExist:
            return Response({
                "detalle": "No se encontro.",
                "status_code": 404
            }, status=status.HTTP_404_NOT_FOUND)
        from juego.models import Pregunta
        from juego.api import PreguntaSimpleSerializer

        queryset = Pregunta.objects.filter(modo_juego_id=pk)
        serializer = PreguntaSimpleSerializer(queryset, many=True, read_only=True)
        return Response(serializer.data)
