from django.db import models

class TipoPredio(models.Model):
    nombre=models.CharField(max_length=30, verbose_name='Tipo De Predio', unique=True)
    def __str__(self) -> str:
        return self.nombre

class TipoPropietario(models.Model):
    nombre=models.CharField(max_length=30, verbose_name='Tipo De Propietario', unique=True)
    def __str__(self) -> str:
        return self.nombre

class TipoNumeroDocumento(models.Model):
    nombre=models.CharField(max_length=30, verbose_name='Tipo De Documento', unique=True)
    def __str__(self) -> str:
        return self.nombre