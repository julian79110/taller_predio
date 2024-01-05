#django
from django.contrib import admin

#predio
from predio.models import Propietario, Predio

#agregar las app´s en el administrador de django
admin.site.register(Propietario)
admin.site.register(Predio)
