from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Almacen
from .forms import AlmacenForm

@login_required
def WarehouseList(request):
    warehouses = Almacen.objects.all()
    return #render(request, 'admin.html')

@login_required
def WarehouseDetail(request, pk):
    warehouse = get_object_or_404(Almacen, pk=pk)
    return #render(request, 'admin.html')

@login_required
def WarehouseCreate(request):
    if request.method == 'POST':
        form = AlmacenForm(request.POST)
        if form.is_valid():
            form.save()
            return #redirect('admin.html')
    else:
        form = AlmacenForm()
    return #render(request, 'admin.html')

@login_required
def WarehouseUpdate(request, pk):
    almacen = get_object_or_404(Almacen, pk=pk)
    if request.method == 'PUT':
        form = AlmacenForm(request.PUT, instance=almacen)
        if form.is_valid():
            form.save()
            return #redirect('admin.html')
    else:
        form = AlmacenForm(instance=almacen)
    return #render(request, 'admin.html')

@login_required
def WarehouseDelete(request, pk):
    almacen = get_object_or_404(Almacen, pk=pk)
    if request.method == 'DELETE':
        almacen.delete()
        return #redirect('admin.html')
    return #render(request, 'admin.html')