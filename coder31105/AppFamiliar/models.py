from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre=models.CharField(max_length = 50)
    apellido=models.CharField(max_length = 50)
    dni = models.IntegerField()
    parentezco=models.CharField(max_length = 50)
    fecha_nacimiento= models.DateField()

    def __str__(self):
        return self.nombre, self.apellido, self.parentezco
