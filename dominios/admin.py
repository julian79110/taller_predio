from django.contrib import admin
from dominios.models import TipoNumeroDocumento,TipoPredio,TipoPropietario

admin.site.register(TipoPredio)
admin.site.register(TipoPropietario)
admin.site.register(TipoNumeroDocumento)


