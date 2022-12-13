from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Raza

# Create your views here.
def razas_index(request: HttpRequest) -> HttpResponse:
    raza = Raza.objects.all()
    return render(request, "razas_index.html", {"raza": raza})
