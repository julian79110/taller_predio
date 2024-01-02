from django.db import models
from dominios.models import TipoNumeroDocumento,TipoPredio,TipoPropietario

class propietario(models.Model):
    nombrePropietario=models.CharField(max_length=30)
    tipoPropietario=models.ForeignKey(TipoPropietario, on_delete=models.SET_NULL,null=True)
    numeroDocumento=models.CharField(max_length=10, unique=True)
    tipoDocumento=models.ForeignKey(TipoNumeroDocumento, on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return self.nombrePropietario

class predio(models.Model):
    nombre=models.CharField(max_length=30)
    numeroCatastral=models.CharField(max_length=30,unique=True,default='na')
    numeroMatricula=models.CharField(max_length=30,unique=True,default='na')
    tipo=models.ForeignKey(TipoPredio, on_delete=models.SET_NULL, null=True)
    propietarios=models.ManyToManyField(propietario, blank=True)
    

