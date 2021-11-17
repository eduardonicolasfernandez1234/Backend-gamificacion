from rest_framework import serializers, viewsets, status
from juego.models import Canjeo, ProductoCanjeo
from juego.api import CanjeoSerializer
from usuarios.models import Usuario
from rest_framework.decorators import action
from rest_framework.response import Response
from juego.functions import funciones_juego

class ProductoCanjeoSerializer(serializers.ModelSerializer):

    canjeo = CanjeoSerializer(many=False, read_only=True)
    canjeo_id = serializers.PrimaryKeyRelatedField(
        many=False, write_only=True, queryset=Canjeo.objects.all(), source='canjeo'
    )

    class Meta:
        model = ProductoCanjeo
        fields = "__all__"

class ProductoCanjeoViewSet(viewsets.ModelViewSet):
    queryset = ProductoCanjeo.objects.all()
    serializer_class = ProductoCanjeoSerializer

    @action(detail=False, methods=['post'], url_path="canjear", name="Canjear producto")
    def canjearProducto(self, request, pk=None):
        try:
            jugador_req = request.data['jugador']
            producto_req = request.data['producto']
            producto = ProductoCanjeo.objects.get(pk=producto_req['id'])
            usuario = Usuario.objects.get(pk=jugador_req['id'])
            funciones_juego.canjearProducto(usuario, producto)
            return Response({'res': 'producto canjeado'})
        except Exception as error:
            print(error)
            return Response({
                "detalle": "Ocurrio un problema al canjear el producto.",
                "status_code": 404
            }, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'], url_path="categoria", name="Producto Canjeo por categoria")
    def canjeoProductoPorCategoria(self, request, pk=None):
        if pk is None:
            return Response({
                "detalle": "Falta la llave foránea",
                "status_code": 404
            }, status=status.HTTP_404_NOT_FOUND)
        try:
            Canjeo.objects.get(id=pk)
        except Canjeo.DoesNotExist:
            return Response({
                "detalle": "No se encontro.",
                "status_code": 404
            }, status=status.HTTP_404_NOT_FOUND)

        queryset = ProductoCanjeo.objects.filter(canjeo_id=pk)
        serializer = ProductoCanjeoSerializer(queryset, many=True, read_only=True)
        return Response(serializer.data)