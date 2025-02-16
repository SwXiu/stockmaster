from django.shortcuts import render
from django.views.generic import View

class HomePage(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'home.html', context)


def adminGestor(request):
    
    # Datos simulados para almacenes
    almacenes = [
        {"id": 1, "nombre": "Almacén Central", "stock_actual": 500, "capacidad_maxima": 1000, "porcentaje_lleno": 50},
        {"id": 2, "nombre": "Almacén Norte", "stock_actual": 200, "capacidad_maxima": 500, "porcentaje_lleno": 40},
        {"id": 3, "nombre": "Almacén Sur", "stock_actual": 900, "capacidad_maxima": 1000, "porcentaje_lleno": 90},
    ]

    # Datos simulados para kardex
    kardex = [
        {"cliente": "Empresa A", "producto": "Cajas", "stock": 100, "volumen": 10, "almacen": "Almacén Central"},
        {"cliente": "Empresa B", "producto": "Palets", "stock": 50, "volumen": 20, "almacen": "Almacén Norte"},
        {"cliente": "Empresa C", "producto": "Bidones", "stock": 80, "volumen": 15, "almacen": "Almacén Sur"},
    ]

    # Pasamos los datos simulados a la plantilla
    return render(request, 'adminGestor.html', {"almacenes": almacenes, "kardex": kardex})



