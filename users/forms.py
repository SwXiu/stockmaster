from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    telephone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(max_length=255, required=False)
    birth_date = forms.DateField(
        required=False,
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YYYY'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'telephone', 'address', 'birth_date', 'password1', 'password2']
