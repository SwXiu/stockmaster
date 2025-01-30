from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import CustomUser
import re

class CustomUserCreationForm(UserCreationForm):
    telephone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(max_length=255, required=False)
    birth_date = forms.DateField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'telephone', 'address', 'birth_date', 'password1', 'password2']
    
