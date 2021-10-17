from rest_framework import serializers, viewsets

from usuarios.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = '__all__'

class UsuarioViewSet(viewsets.ViewSet):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer