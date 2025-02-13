from django.db import models
from users.models import CustomUser
class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del producto")
    descripcion = models.TextField(verbose_name="Descripción", blank=True, null=True)
    estado = models.TextField(verbose_name="Estado del producto", blank=True, null=True)
    volumen = models.FloatField(verbose_name="Volumen (metros cúbicos)")
    cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='productos', verbose_name="Cliente")
    
    def __str__(self):
        return self.nombre