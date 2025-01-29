from django.urls import path
from .views import SignupView, LoginView, UserView

app_name = 'user'

urlpatterns = [
    path('signUp/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'), 
    path('role/', UserView.as_view(), name='user_view'),
]