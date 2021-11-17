from rest_framework import serializers, viewsets, status
from juego.models import Juego
from rest_framework.decorators import action
from rest_framework.response import Response


class JuegoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Juego
        fields = "__all__"

class JuegoViewSet(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer

    @action(detail=True, methods=['get'], url_path="categorias",
            name="Obtener categorias o modo juego por juego")
    def listar_categorias_por_juego(self, request, pk=None):
        if pk is None:
            return Response({
                "detalle": "Falta la llave foránea",
                "status_code": 404
            }, status=status.HTTP_404_NOT_FOUND)
        try:
            Juego.objects.get(id=pk)
        except Juego.DoesNotExist:
            return Response({
                "detalle": "No se encontro.",
                "status_code": 404
            }, status=status.HTTP_404_NOT_FOUND)
        from juego.models import ModoJuego
        from juego.api import ModoJuegoSimpleSerializer

        queryset = ModoJuego.objects.filter(juego_id=pk)
        serializer = ModoJuegoSimpleSerializer(queryset, many=True, read_only=True)
        return Response(serializer.data)