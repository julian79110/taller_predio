#django
from django.db import models

#dominios
from dominios.models import TipoNumeroDocumento,TipoPredio,TipoPropietario

class Propietario(models.Model):
    """
        Clase que representa un propietario y sus atributos

        author: julian tique | julian.tique@arcerojas.com
    """
    nombrePropietario=models.CharField(max_length=30)
    tipoPropietario=models.ForeignKey(TipoPropietario, on_delete=models.SET_NULL,null=True)
    numeroDocumento=models.CharField(max_length=10, unique=True)
    tipoDocumento=models.ForeignKey(TipoNumeroDocumento, on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return self.nombrePropietario

class Predio(models.Model):
    """
        Clase que representa un predio y sus atributos

        author: julian tique | julian.tique@arcerojas.com
    """
    nombre=models.CharField(max_length=30)
    numeroCatastral=models.CharField(max_length=30,unique=True,default='na')
    numeroMatricula=models.CharField(max_length=30,unique=True,default='na')
    tipo=models.ForeignKey(TipoPredio, on_delete=models.SET_NULL, null=True)
    propietarios=models.ManyToManyField(Propietario, blank=True)
    

