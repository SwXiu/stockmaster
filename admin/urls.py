from django.urls import path
from .views import AdminInterface

app_name = 'adminV'

urlpatterns = [
    path('', AdminInterface.as_view(), name='adminInterface'),
]