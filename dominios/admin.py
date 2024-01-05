#django
from django.contrib import admin

#dominios
from dominios.models import TipoNumeroDocumento,TipoPredio,TipoPropietario

#sitios que apareceran en el administrador de django
admin.site.register(TipoPredio)
admin.site.register(TipoPropietario)
admin.site.register(TipoNumeroDocumento)


