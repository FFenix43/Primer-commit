from django.contrib import admin 
from django.urls import path, include
from LOTR import views

urlpatterns = [

    path("admin/", admin.site.urls),
    path("LOTR/", include("LOTR.urls"))
]


