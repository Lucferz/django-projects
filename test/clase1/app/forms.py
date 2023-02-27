from django import forms
from . import models

class EstadoModelForm(forms.ModelForm):
    class Meta:
        model=models.Estados
        fields=["es_desc", "es_cod"]

class PersonasModelForm(forms.ModelForm):
    class Meta:
        model = models.Personas
        fields=["per_nombre", "per_apellido", "per_cedula", "per_telefono", "per_email", "usuario_alta", "estado_id"]
    # Agregando validaciones personalizadas
    def clean_usuario_alta(self):
        usu_alta = self.cleaned_data.get("usuario_alta")
        if usu_alta is None:
            return
        return usu_alta

class PersonasForm(forms.Form):
    Nombre = forms.CharField(max_length=100, required=True)
    Apellido = forms.CharField(max_length=100, required=True)
    Documento = forms.CharField(max_length=10)
    Telefono = forms.CharField(max_length=50)
    Email= forms.EmailField(required=True)
    Estado = forms.ModelChoiceField(queryset=models.Estados.objects.all())