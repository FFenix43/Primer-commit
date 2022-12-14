from django.db import models

# Create your models here.

class Raza(models.Model):
    raza=models.CharField(max_length=50)
    nombre_de_personaje=models.CharField(max_length=50)
    espectativa_de_vida=models.IntegerField()
    historia=models.URLField()

    def __str__(self) -> str:
        return self.raza+" "+self.nombre_de_personaje+" "+str(self.espectativa_de_vida)+" años"
