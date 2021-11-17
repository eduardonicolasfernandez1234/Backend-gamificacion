from rest_framework import serializers, viewsets, status
from juego.models import Articulo
from rest_framework.decorators import action
from rest_framework.response import Response


class ArticuloSerializer(serializers.ModelSerializer):

    class Meta:
        model = Articulo
        fields = "__all__"

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

    