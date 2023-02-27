from django.shortcuts import render

# Create your views here.
#Clase render(request: HttpRequest, template_name : str | Sequence[str], context : Mapping[str, Any] | None = ..., using :str | None = ... ) -> HttpResponse

#Al agregar algo aca, tambien se debe agregar en urls.py

#Se crean funciones que devuelven vistas segun peticiones

def Home(request):
    return render(request,"home.html", {} )