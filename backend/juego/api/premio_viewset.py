from rest_framework import serializers, viewsets, status
from juego.models import Premio
from rest_framework.decorators import action
from rest_framework.response import Response


class PremioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Premio
        fields = "__all__"

class PremioViewSet(viewsets.ModelViewSet):
    queryset = Premio.objects.all()
    serializer_class = PremioSerializer