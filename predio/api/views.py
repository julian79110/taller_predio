#django
from django.contrib.auth.models import User

#dominios
from dominios.models import TipoPredio, TipoPropietario, TipoNumeroDocumento

#djangorestframework (creacion de api's)
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

#json 
import json

#modelos
from predio.models import Predio, Propietario

#predio
from predio.api.serializers import JSONSerializer, UserSerializer, PredioSerializer, TipoPredioSerializer, PropietarioSerializer, TipoPropietarioSerializer, TipoNumeroDocumentoSerializer

#re
import re


# Uso Del Serializador y hacer acciones de crud.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TipoPredioViewSet(viewsets.ModelViewSet):
    queryset = TipoPredio.objects.all()
    serializer_class = TipoPredioSerializer

class PredioViewSet(viewsets.ModelViewSet):
    queryset = Predio.objects.all()
    serializer_class = PredioSerializer

class TipoPropietarioViewSet(viewsets.ModelViewSet):
    queryset = TipoPropietario.objects.all()
    serializer_class = TipoPropietarioSerializer

class TipoNumeroDocumentoViewSet(viewsets.ModelViewSet):
    queryset = TipoNumeroDocumento.objects.all()
    serializer_class = TipoNumeroDocumentoSerializer

class PropietarioViewSet(viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer

class SubirJSONView(APIView):
    serializer_class = JSONSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            archivo_json = serializer.validated_data.get('archivo_json')
            datos = json.load(archivo_json)
            #crear otro anotaciones para especificaciones
            #comprension de listas 
            #enumerate
            respuesta=[]
            cadena_anotaciones = str(datos['textoAnotaciones'])
            anotaciones = re.findall(r'ANOTACION: Nro [0-9]{1,3}', cadena_anotaciones)
            cadena_especificaciones = str(datos['textoAnotaciones'])
            especificaciones= re.findall(r'ESPECIFICACION: [0-9]{3,5}', cadena_especificaciones)
            listas = zip(anotaciones,especificaciones)
            anotacion_index = [(index, item) for index, item in enumerate(listas, start=1)]
            respuesta.append(anotacion_index)
            return Response({"resultado": "cargado con exito!.","respuesta=":respuesta},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)