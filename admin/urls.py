from .views import AdminInterface
from django.urls import path, include

app_name = 'adminV'

urlpatterns = [
    path('', AdminInterface.as_view(), name='adminInterface'),
    path('/warehouses/', include('warehouses.urls', namespace='warehouses'))
]