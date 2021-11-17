from rest_framework import serializers, viewsets, status
from juego.models import CategoriaPuzzle, ImagenPuzzle
from juego.api import CategoriaPuzzleSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class ImagenPuzzleSerializer(serializers.ModelSerializer):

    categoria = CategoriaPuzzleSerializer(many=False, read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(
        many=False, write_only=True, queryset=CategoriaPuzzle.objects.all(), source='categoria'
    )

    class Meta:
        model = ImagenPuzzle
        fields = "__all__"

class ImagenPuzzleViewSet(viewsets.ModelViewSet):
    queryset = ImagenPuzzle.objects.all()
    serializer_class = ImagenPuzzleSerializer


    @action(detail=True, methods=['get'], url_path="subimagenes",
            name="Obtener lista de subimagenes de juego por imagenes")
    def lista_subimagenes_por_imagen_puzzle(self, request, pk=None):
        if pk is None:
            return Response({
                "detalle": "Falta la llave foránea",
                "status_code": 404
            }, status=status.HTTP_404_NOT_FOUND)
        try:
            ImagenPuzzle.objects.get(id=pk)
        except ImagenPuzzle.DoesNotExist:
            return Response({
                "detalle": "No se encontro.",
                "status_code": 404
            }, status=status.HTTP_404_NOT_FOUND)
        from juego.models import SubImagenPuzzle
        from juego.api import SubImagenPuzzleSerializer

        queryset = SubImagenPuzzle.objects.filter(imagen_puzzle_id=pk)
        serializer = SubImagenPuzzleSerializer(queryset, many=True, read_only=True)
        return Response(serializer.data)
