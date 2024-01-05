#django
from django.contrib.auth.models import User

#dominios
from dominios.models import TipoPredio, TipoPropietario, TipoNumeroDocumento

#djangorestframework (creacion de api's)
from rest_framework import viewsets

#modelos
from predio.models import Predio, Propietario

#predio
from predio.api.serializers import UserSerializer, PredioSerializer, TipoPredioSerializer, PropietarioSerializer, TipoPropietarioSerializer, TipoNumeroDocumentoSerializer



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