from rest_framework import serializers, viewsets, status
from juego.models import ImagenPagina
from rest_framework.decorators import action
from rest_framework.response import Response


class ImagenPaginaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImagenPagina
        fields = "__all__"

class ImagenPaginaViewSet(viewsets.ModelViewSet):
    queryset = ImagenPagina.objects.all()
    serializer_class = ImagenPaginaSerializer
    