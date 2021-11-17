from rest_framework import serializers, viewsets, status
from juego.models import Pregunta, ModoJuego, OpcionPregunta
from juego.api import ModoJuegoSerializer, OpcionPreguntaSimpleSerializer
from usuarios.models import Usuario
from rest_framework.decorators import action
from rest_framework.response import Response
from juego.functions import funciones_juego


class PreguntaSerializer(serializers.ModelSerializer):

    modo_juego = ModoJuegoSerializer(many=False, read_only=True)
    modo_juego_id = serializers.PrimaryKeyRelatedField(
        many=False, write_only=True, queryset=ModoJuego.objects.all(), source='modo_juego'
    )

    class Meta:
        model = Pregunta
        fields = "__all__"

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer

    @action(detail=True, methods=['get'], url_path="opciones",
            name="Obtener lista de opciones por pregunta")
    def listar_opciones_por_pregunta(self, request, pk=None):
        if pk is None:
            return Response({
                "detalle": "Falta la llave foránea",
                "status_code": 404
            }, status=status.HTTP_404_NOT_FOUND)
        try:
            Pregunta.objects.get(id=pk)
        except ModoJuego.DoesNotExist:
            return Response({
                "detalle": "No se encontro.",
                "status_code": 404
            }, status=status.HTTP_404_NOT_FOUND)

        queryset = OpcionPregunta.objects.filter(pregunta_id=pk)
        serializer = OpcionPreguntaSimpleSerializer(queryset, many=True, read_only=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path="revisar-pregunta",
            name="Revisar opcion de la pregunta")
    def validarPregunta(self, request, pk=None):
        try:
            opcion_req = request.data['opcion']
            pregunta_req = request.data['pregunta']
            jugador_req = request.data['jugador']
            ayuda_req = request.data['ayuda']
            opcion = OpcionPregunta.objects.get(pk=opcion_req['id'])
            pregunta = Pregunta.objects.get(pk=pregunta_req['id'])
            usuario = Usuario.objects.get(pk=jugador_req['id'])
            if pregunta.respuesta == opcion.opcion :
                funciones_juego.registrarPuntos(usuario, pregunta, True, ayuda_req)
                return Response({'res': 'correcto'})
            else:
                funciones_juego.registrarPuntos(usuario, pregunta, False, ayuda_req)
                return Response({'res': 'incorrecto'})
        except Exception as error:
            print(error)
            return Response({
                "detalle": "Ocurrio un problema al validar la pregunta.",
                "status_code": 404
            }, status=status.HTTP_404_NOT_FOUND)
        

        