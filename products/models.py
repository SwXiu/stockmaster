from django.db import models
from users.models import CustomUser
class Producto(models.Model):
    cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='productos', verbose_name="Cliente")
    nombre = models.CharField(max_length=100, verbose_name="Nombre del producto")
    descripcion = models.TextField(verbose_name="Descripción", blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    def __str__(self):
        return self.nombre