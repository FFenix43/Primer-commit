from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Raza
from LOTR.forms import RazaForm

# Create your views here.
def razas_index(request: HttpRequest) -> HttpResponse:
    if request.GET.get('raza'):
        especie = request.GET['raza']
        raza = Raza.objects.filter(raza__icontains=especie)
    else:
        raza = Raza.objects.all()

    
    return render(request, "razas_index.html", {"raza": raza})


def new_raza(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = RazaForm(request.POST)
        if not form.is_valid():
            return render(
                request, "Raza_form.html", 
            {"error": "Algo salio mal con el formulario", 
            "form": form},
            )

        new_raza = Raza(**form.cleaned_data)
        new_raza.save()

        return redirect('raza-index')
    else:
        return render(request, "Raza_form.html", {"form": RazaForm()})

def search_raza(request: HttpRequest) -> HttpResponse:

    return render(request, "Raza_search.html")
