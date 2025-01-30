from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser  # Si estás utilizando un modelo CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telephone = forms.CharField(max_length=15, required=False)
    address = forms.CharField(max_length=255, required=False)
    birth_date = forms.DateField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'telephone', 'address', 'birth_date', 'password1', 'password2']
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        
        return cleaned_data
