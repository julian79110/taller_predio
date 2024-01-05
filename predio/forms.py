#django
from django import forms

#predio
from .models import Predio,Propietario

#Formulario De Edicion Del Predio
class PredioEditForm(forms.ModelForm):
    class Meta: 
        model = Predio
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        """
        se usa para agregar la clase form-control a todos los elementos del form
        """
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        
#Formulario De Edicion Del Propietario
class PropietarioEditForm(forms.ModelForm):
    class Meta: 
        model = Propietario
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        """
        se usa para agregar la clase form-control a todos los elementos del form
        """
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


#Formulario De Creacion De Predio
class CreatePredioForm(forms.ModelForm):
    propietarios = forms.ModelMultipleChoiceField(
        queryset=Propietario.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-select'}),
        label="Selecciona al Propietario",
        required=False
    )

    class Meta:
        model = Predio
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

#Formulario De Creacion De Propietario
class CreatePropietarioForm(forms.ModelForm):
    class Meta:
        model=Propietario
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        """
        se usa para agregar la clase form-control a todos los elementos del form
        """
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

