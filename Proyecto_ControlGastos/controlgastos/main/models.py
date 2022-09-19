from django.db import models

# Create your models here.

class Usuario(models.Model):
    Usuario = models.CharField(max_length= 300)
    Nombre = models.CharField(max_length= 300)
    Correo = models.CharField(max_length= 30)
   

def __str__(self):
        return 'Tu usuario es: %s %s %s' %(self.Usuario, self.Nombre, self.Correo)
        