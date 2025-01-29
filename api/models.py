from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    tipo_usuario = models.CharField(
        max_length=50,
        choices=[('client', 'Cliente'), ('admin', 'Administrador')],
        default='client'
    )
    
    def __str__(self):
        return self.username

class Products(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Warehouse(models.Model):
    nombre = models.CharField(max_length=255)
    capacidad_total = models.DecimalField(max_digits=10, decimal_places=2)
    direccion = models.CharField(max_length=255)
    latitud = models.FloatField()
    longitud = models.FloatField()
    
    def __str__(self):
        return self.nombre
    
