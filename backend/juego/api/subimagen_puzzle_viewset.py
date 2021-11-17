from rest_framework import serializers, viewsets, status
from juego.models import SubImagenPuzzle, ImagenPuzzle
from juego.api import ImagenPaginaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class SubImagenPuzzleSerializer(serializers.ModelSerializer):

    imagen_puzzle = ImagenPaginaSerializer(many=False, read_only=True)
    imagen_puzzle_id = serializers.PrimaryKeyRelatedField(
        many=False, write_only=True, queryset=ImagenPuzzle.objects.all(), source='imagen_puzzle'
    )

    class Meta:
        model = SubImagenPuzzle
        fields = "__all__"

class SubImagenPuzzleViewSet(viewsets.ModelViewSet):
    queryset = SubImagenPuzzle.objects.all()
    serializer_class = SubImagenPuzzleSerializer


    # @action(detail=True, methods=['get'], url_path="preguntas",
    #         name="Obtener lista de imagenes de juego por categoria")
    # def listar_preguntas_por_modo_juego(self, request, pk=None):
    #     if pk is None:
    #         return Response({
    #             "detalle": "Falta la llave foránea",
    #             "status_code": 404
    #         }, status=status.HTTP_404_NOT_FOUND)
    #     try:
    #         ModoJuego.objects.get(id=pk)
    #     except ModoJuego.DoesNotExist:
    #         return Response({
    #             "detalle": "No se encontro.",
    #             "status_code": 404
    #         }, status=status.HTTP_404_NOT_FOUND)
    #     from juego.models import Pregunta
    #     from juego.api import PreguntaSimpleSerializer

    #     queryset = Pregunta.objects.filter(modo_juego_id=pk)
    #     serializer = PreguntaSimpleSerializer(queryset, many=True, read_only=True)
    #     return Response(serializer.data)
