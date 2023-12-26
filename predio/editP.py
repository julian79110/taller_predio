from django import forms
from .models import predio,propietario

class predioEdit(forms.ModelForm):
    class Meta: 
        model = predio
        fields = '__all__'
class propietarioEdit(forms.ModelForm):
    class Meta: 
        model = propietario
        fields = '__all__'

class createPredio(forms.ModelForm):
    class Meta:
        model=predio
        fields='__all__'
class createPropietario(forms.ModelForm):
    class Meta:
        model=propietario
        fields='__all__'

