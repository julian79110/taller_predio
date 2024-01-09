#django
from django.contrib.auth.models import User
#from django.forms.fields import FileField

#dominios
from dominios.models import TipoPredio, TipoPropietario, TipoNumeroDocumento

#djangorestframework
from rest_framework import serializers
from rest_framework.serializers import FileField

#predio
from predio.models import Predio, Propietario



# clase que mapea objetos complejos y los convierte a objetos sencillos de leer 
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class TipoPredioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoPredio
        fields = '__all__'

class TipoPropietarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoPropietario
        fields = '__all__'

class TipoNumeroDocumentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoNumeroDocumento
        fields = '__all__'

class PropietarioSerializer(serializers.HyperlinkedModelSerializer):
    tipoPropietario = TipoPropietarioSerializer()
    tipoDocumento = TipoNumeroDocumentoSerializer()
    class Meta:
        model = Propietario
        fields = '__all__'

class PredioSerializer(serializers.HyperlinkedModelSerializer):
    tipo = TipoPredioSerializer()
    class Meta:
        model = Predio
        fields = '__all__'

class JSONSerializer(serializers.Serializer):
    archivo_json = FileField()