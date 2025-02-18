from django.urls import path
from .views import WarehouseList, WarehouseCreate, WarehouseUpdate, WarehouseDelete, WarehouseDetail
from warehouses import views

app_name = 'warehouses'

urlpatterns = [
    path('', views.WarehouseList, name='warehouses'),
    path('/create/', views.WarehouseCreate, name='warehousesCreate'),
    path('/update/', views.WarehouseUpdate, name='warehousesUpdate'),
    path('/delete/', views.WarehouseDelete, name='warehousesDelete'),
    path('/detail/', views.WarehouseDetail, name='warehousesDetail'),
]