from django import forms
from .models import Almacen

class AlmacenForm(forms.ModelForm):
    class Meta:
        model = Almacen
        fields = ['nombre', 'direccion', 'capacidad', 'capacidadDisponible']