from django.db import models

class tipoPredio(models.TextChoices):
    urbano='urbano'
    rural='rural'

class tiposPropietario(models.TextChoices):
    natural='natural'
    juridico='juridico'

class tipoNumeroDocumento(models.TextChoices):
    cedula='cedula de ciudadania'
    cedulaE='cedula de extranjeria'
    tributaria='numero de identificacion tributaria'
    tarjeta_identidad='tarjeta de identidad'

class predio(models.Model):
    nombre=models.CharField(max_length=30)
    numeroCatastral=models.CharField(max_length=30,unique=True,default='na')
    numeroMatricula=models.CharField( max_length=30,unique=True,default='na')
    tipo=models.CharField(max_length=6, choices=tipoPredio.choices, default=tipoPredio.urbano)
    propietario=models.CharField(max_length=35,default='na')

class propietario(models.Model):
    nombrePropietario=models.CharField(max_length=30)
    tipoPropietario=models.CharField(max_length=9,choices=tiposPropietario.choices, default=tiposPropietario.natural)
    numeroDocumento=models.CharField(max_length=10, unique=True)
    tipoDocumento=models.CharField(max_length=50, choices=tipoNumeroDocumento.choices, default=tipoNumeroDocumento.cedula)


