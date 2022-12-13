from django.urls import path
from LOTR import views

urlpatterns = [
    path("", views.razas_index, name="raza-index"),
    #path("new", views.raza_form, name="raza-form"),
    #path("search", views.razas_index, name="raza-search"),
]
