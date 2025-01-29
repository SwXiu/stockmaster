from django.contrib import admin
from django.urls import path, include
from .views import HomePage, AdminInterface, ClientInterface

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name="home"),
    path('user/', include('users.urls', namespace='user')),  
    path('clientV/', ClientInterface.as_view(), name="clientInterface"),
    path('adminV/', AdminInterface.as_view(), name="adminInterface"),
]
