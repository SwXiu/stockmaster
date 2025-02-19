from django.urls import path, include
from .views import WarehouseList, WarehouseCreate, WarehouseUpdate, WarehouseDelete, WarehouseDetail
from warehouses import views

app_name = 'warehouses'

urlpatterns = [
    path('', views.WarehouseList, name='warehouses'),
    path('create/', views.WarehouseCreate, name='warehousesCreate'),
    path('update/<int:pk>/', views.WarehouseUpdate, name='warehousesUpdate'),
    path('delete/<int:pk>/', views.WarehouseDelete, name='warehousesDelete'),
    path('detail/<int:pk>/', views.WarehouseDetail, name='warehousesDetail'),
]