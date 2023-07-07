from django import forms
from fiscales.models import Fiscales


class Formularios(forms.ModelForm):
    
    class Meta:
        model = Fiscales
        fields = '__all__'
        widgets = {'fecha_cambio': forms.DateInput(attrs={'type':'date'}), 'vencimiento_certificado_digital': forms.DateInput(attrs={'type':'date'})}
