from django.contrib import admin
from django.urls import path, include
from .views import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name="home"),
    path('user/', include('users.urls'), name="user")
]
