from django.urls import path, include
from .views import HomePage, adminGestor

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('user/', include('users.urls', namespace='user')),
    path('admin/', include('admin.urls', namespace='adminV')),
    path('client/', include('client.urls', namespace='clientV')),
    path('adminGestor/', adminGestor, name='adminGestor'),
]
