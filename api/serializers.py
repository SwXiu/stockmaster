from rest_framework import serializers
from .models import Users, Products, Warehouse

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'telefono', 'direccion', 'tipo_usuario']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock']

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'nombre', 'capacidad_total', 'direccion', 'latitud', 'longitud']