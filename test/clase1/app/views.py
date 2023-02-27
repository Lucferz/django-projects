from django.shortcuts import render
from . import forms
from . import models

# Create your views here.
#Clase render(request: HttpRequest, template_name : str | Sequence[str], context : Mapping[str, Any] | None = ..., using :str | None = ... ) -> HttpResponse

#Al agregar algo aca, tambien se debe agregar en urls.py

#Se crean funciones que devuelven vistas segun peticiones

def Home(request):
    form = forms.PersonasForm(request.POST or None)
    if form.is_valid():
        print(form.data)
        print(request.user.id)
        obj = models.Personas()
        obj.estado_id = models.Estados.objects.filter(es_id = form.data.get("Estado")).first()
        obj.per_nombre = form.data.get("Nombre")
        obj.per_apellido = form.data.get("Apellido")
        obj.per_cedula = form.data.get("Documento")
        obj.per_telefono = form.data.get("Telefono")
        obj.per_email = form.data.get("Email")
        obj.usuario_alta = request.user.id
        obj.save()
    context = {
        "titulo" : "Formulario",
        "da_form": form
    }
    return render(request,"home.html", context)