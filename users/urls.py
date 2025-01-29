from django.urls import path
from .views import LoginView, UserView, signupView

app_name = 'user'

urlpatterns = [
    path('signUp/', signupView, name='signup'),
    path('login/', LoginView.as_view(), name='login'), 
    path('role/', UserView.as_view(), name='user_view'),
]