from rest_framework import serializers, viewsets, status
from juego.models import Canjeo
from rest_framework.decorators import action
from rest_framework.response import Response


class CanjeoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Canjeo
        fields = "__all__"

class CanjeoViewSet(viewsets.ModelViewSet):
    queryset = Canjeo.objects.all()
    serializer_class = CanjeoSerializer

    