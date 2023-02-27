from django import forms
from .models import Estados

class EstadoModelForm(forms.ModelForm):
    class Meta:
        model=Estados
        fields=["es_desc", "es_cod"]
