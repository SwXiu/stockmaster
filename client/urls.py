from django.urls import path, include
from .views import ClientInterface

app_name = 'clientV'

urlpatterns = [
    path('', ClientInterface.as_view(), name='clientInterface'),
     path('/products/', include('products.urls', namespace='products'))
]