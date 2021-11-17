from rest_framework import serializers, viewsets, status
from juego.models import Estatus
from rest_framework.decorators import action
from rest_framework.response import Response


class EstatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estatus
        fields = "__all__"

class EstatusViewSet(viewsets.ModelViewSet):
    queryset = Estatus.objects.all()
    serializer_class = EstatusSerializer
