from django.urls import path
from .views import signup, signin, signout, userView
from users import views

app_name = 'user'

urlpatterns = [
    path('', views.userView, name='user'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('login/', views.signin, name='signin'),
]