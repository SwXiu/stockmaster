from django.db import models

class Almacen(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del almacén")
    direccion = models.CharField(max_length=200, verbose_name="Dirección")
    capacidad = models.PositiveIntegerField(verbose_name="Capacidad (en unidades)")
    capacidadOcupada = models.PositiveIntegerField(verbose_name="Capacidad ocupada (en unidades)")
    capacidadDisponible = models.PositiveIntegerField(verbose_name="Capacidad disponible (en unidades)")
    latitud = models.FloatField(verbose_name="Latitud")
    longitud = models.FloatField(verbose_name="Longitud")

    def porcentaje_lleno(self):
        if self.capacidad > 0:
            return (self.capacidadOcupada / self.capacidad) * 100
        return 0

    def __str__(self):
        return f"{self.nombre} - {self.direccion}"
