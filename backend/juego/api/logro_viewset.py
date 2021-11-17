from rest_framework import serializers, viewsets, status
from juego.models import Logro
from rest_framework.decorators import action
from rest_framework.response import Response


class LogroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Logro
        fields = "__all__"

class LogroViewSet(viewsets.ModelViewSet):
    queryset = Logro.objects.all()
    serializer_class = LogroSerializer