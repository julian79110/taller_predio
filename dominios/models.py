#django
from django.db import models

class TipoPredio(models.Model):
    """
        Clase que representa los tipos de predio validos en Colombia

        author: julian tique | julian.tique@arcerojas.com
    """
    nombre=models.CharField(max_length=30, verbose_name='Tipo De Predio', unique=True)
    def __str__(self) -> str:
        return self.nombre

class TipoPropietario(models.Model):
    """
        Clase que representa los tipos de propietarios en un predio

        author: julian tique | julian.tique@arcerojas.com
    """
    nombre=models.CharField(max_length=30, verbose_name='Tipo De Propietario', unique=True)
    def __str__(self) -> str:
        return self.nombre

class TipoNumeroDocumento(models.Model):
    """
        Clase que representa los tipos de documento de un propietario

        author: julian tique | julian.tique@arcerojas.com
    """
    nombre=models.CharField(max_length=30, verbose_name='Tipo De Documento', unique=True)
    def __str__(self) -> str:
        return self.nombre