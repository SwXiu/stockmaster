from django.db import models

class Almacen(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del almacén")
    direccion = models.CharField(max_length=200, verbose_name="Dirección")
    capacidad = models.PositiveIntegerField(verbose_name="Capacidad (en unidades)")
    capacidadDisponible = models.PositiveBigIntegerField(verbose_name="Capacidad disponible(en unidades)")

    def __str__(self):
        return self.nombre