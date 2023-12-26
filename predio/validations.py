from django import forms
from .models import predio 

def clean_numeroCatastral(self):
        numeroCatastral = self.cleaned_data['numeroCatastral']
        # Verificar unicidad del número catastral
        if predio.objects.filter(numeroCatastral=numeroCatastral).exists():
            raise forms.ValidationError('El número catastral ya existe. Por favor, digite otro.')
        return numeroCatastral

def clean_numeroMatricula(self):
        numeroMatricula = self.cleaned_data['numeroMatricula']
        # Verificar unicidad del número de matrícula
        if predio.objects.filter(numeroMatricula=numeroMatricula).exists():
            raise forms.ValidationError('El número de matrícula ya existe. Por favor, digite otro.')
        return numeroMatricula