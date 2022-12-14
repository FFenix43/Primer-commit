from django import forms

class RazaForm(forms.Form):
    raza=forms.CharField(max_length=50)
    nombre_de_personaje=forms.CharField(max_length=50)
    espectativa_de_vida=forms.IntegerField()
    historia=forms.URLField()