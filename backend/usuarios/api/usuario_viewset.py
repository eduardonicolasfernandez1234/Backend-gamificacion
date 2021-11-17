from rest_framework import serializers, viewsets, status
from usuarios.models import Usuario
from rest_framework.decorators import action
from rest_framework.response import Response


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = "__all__"

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @action(detail=False, methods=['post'], url_path="login",
            name="Revisar opcion de la pregunta")
    def loginUsuario(self, request, pk=None):
        try:
            username = request.data['username']
            password = request.data['password']
            usuario = Usuario.objects.all()
            for user in usuario:
                if username == user.username and password == user.password:
                    serializer = UsuarioSerializer(user, many=False)
                    return Response(serializer.data)

            return Response({'res': 'error'})
        except Exception as error:
            print(error)
            return Response({
                "detalle": "Ocurrio un problema al authenticar.",
                "status_code": 404
            }, status=status.HTTP_404_NOT_FOUND)