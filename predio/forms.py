from django import forms
from .models import predio,propietario

class PredioEditForm(forms.ModelForm):
    class Meta: 
        model = predio
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        """
        se usa para agregar la clase form-control a todos los elementos del form
        """
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        
class PropietarioEditForm(forms.ModelForm):
    class Meta: 
        model = propietario
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        """
        se usa para agregar la clase form-control a todos los elementos del form
        """
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class CreatePredioForm(forms.ModelForm):
    class Meta:
        model=predio
        fields='__all__'
    def __init__(self, *args, **kwargs):
        """
        se usa para agregar la clase form-control a todos los elementos del form
        """
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class CreatePropietarioForm(forms.ModelForm):
    class Meta:
        model=propietario
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        """
        se usa para agregar la clase form-control a todos los elementos del form
        """
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

