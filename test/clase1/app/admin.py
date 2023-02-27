from django.contrib import admin
from . import models
from . import forms
# Register your models here.

@admin.register(models.Estados)
class EstadosAdmin(admin.ModelAdmin):
    list_display = ["es_desc", "es_cod"]#Campos que se mostraran en el listado del CRUD
    list_filter = [] # Campos por los cuales se quiere filtrar el listado
    list_editable = [] # Campos que se pueden editar de manera rapida en el listado, no puede ser el primer campo de display
    search_field = [] # Campos sobre los cuales se quiere realizar una busqueda en el listado
    form = forms.EstadoModelForm

@admin.register(models.Personas)
class PersonasAdmin(admin.ModelAdmin):
    list_display = ["per_nombre", "per_apellido", "per_cedula", "per_telefono", "per_email", "fecha_alta", "usuario_alta", "fecha_mod"]
    list_filter = ["per_apellido", "per_cedula", "estado_id"]
    list_editable = []
    search_field = ["per_nombre", "per_apellido", "per_cedula", "per_email"]
    form = forms.PersonasModelForm
