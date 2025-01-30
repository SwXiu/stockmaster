from django.urls import path
from .views import ClientInterface

app_name = 'clientV'

urlpatterns = [
    path('', ClientInterface.as_view(), name='clientInterface'),
]