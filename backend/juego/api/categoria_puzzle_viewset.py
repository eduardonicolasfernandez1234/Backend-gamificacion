from rest_framework import serializers, viewsets, status
from juego.models import CategoriaPuzzle, Juego
from juego.api import JuegoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class CategoriaPuzzleSerializer(serializers.ModelSerializer):

    juego = JuegoSerializer(many=False, read_only=True)
    juego_id = serializers.PrimaryKeyRelatedField(
        many=False, write_only=True, queryset=Juego.objects.all(), source='juego'
    )

    class Meta:
        model = CategoriaPuzzle
        fields = "__all__"

class CategoriaPuzzleViewSet(viewsets.ModelViewSet):
    queryset = CategoriaPuzzle.objects.all()
    serializer_class = CategoriaPuzzleSerializer


    @action(detail=True, methods=['get'], url_path="imagenes",
            name="Obtener lista de imagenes de juego por categoria")
    def listar_imagenes_por_categoria(self, request, pk=None):
        if pk is None:
            return Response({
                "detalle": "Falta la llave foránea",
                "status_code": 404
            }, status=status.HTTP_404_NOT_FOUND)
        try:
            CategoriaPuzzle.objects.get(id=pk)
        except CategoriaPuzzle.DoesNotExist:
            return Response({
                "detalle": "No se encontro.",
                "status_code": 404
            }, status=status.HTTP_404_NOT_FOUND)
        from juego.models import ImagenPuzzle
        from juego.api import ImagenPuzzleSerializer

        queryset = ImagenPuzzle.objects.filter(categoria_id=pk)
        serializer = ImagenPuzzleSerializer(queryset, many=True, read_only=True)
        return Response(serializer.data)
