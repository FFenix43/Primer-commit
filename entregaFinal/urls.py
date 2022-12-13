from django.contrib import admin 
from django.urls import path
from LOTR import views

urlpatterns = [

    path("", views.razas_index, name="raza-index")
]



