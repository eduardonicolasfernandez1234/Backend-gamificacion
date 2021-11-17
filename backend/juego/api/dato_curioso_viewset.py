from rest_framework import serializers, viewsets, status
from juego.models import DatoCurioso
from rest_framework.decorators import action
from rest_framework.response import Response


class DatoCuriosoSerializer(serializers.ModelSerializer):

    class Meta:
        model = DatoCurioso
        fields = "__all__"

class DatoCuriosoViewSet(viewsets.ModelViewSet):
    queryset = DatoCurioso.objects.all()
    serializer_class = DatoCuriosoSerializer

    