from django.shortcuts import render, get_object_or_404, redirect
from .models import Almacen
from .forms import AlmacenForm

def WarehouseList(request):
    almacenes = Almacen.objects.all()
    return render(request, 'admin.html')

def WarehouseDetail(request, pk):
    almacen = get_object_or_404(Almacen, pk=pk)
    return render(request, 'admin.html')

# Crear un nuevo almacén
def WarehouseCreate(request):
    if request.method == 'POST':
        form = AlmacenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin.html')
    else:
        form = AlmacenForm()
    return render(request, 'Warehouseform.html')

# Actualizar un almacén existente
def WarehouseUpdate(request, pk):
    almacen = get_object_or_404(Almacen, pk=pk)
    if request.method == 'POST':
        form = AlmacenForm(request.POST, instance=almacen)
        if form.is_valid():
            form.save()
            return redirect('almacen-list')
    else:
        form = AlmacenForm(instance=almacen)
    return render(request, 'Warehouseform.html')

# Eliminar un almacén
def WarehouseDelete(request, pk):
    almacen = get_object_or_404(Almacen, pk=pk)
    if request.method == 'POST':
        almacen.delete()
        return redirect('almacen-list')
    return render(request, 'Warehouseconfirm_delete.html')