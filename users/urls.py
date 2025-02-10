from django.urls import path
from .views import check_field_exists
from users import views

app_name = 'user'

urlpatterns = [
    path('', views.userView, name='user'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('login/', views.signin, name='login'),
    path('check-field/', check_field_exists, name='check_field_exists'), 
]