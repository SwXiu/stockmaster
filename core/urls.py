from django.contrib import admin
from django.urls import path, include
from .views import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name="home"),
    path('api/', include('api.urls'), name="api"),
]
