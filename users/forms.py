from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile

class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(label="Nombre", max_length=30, required=True)
    last_name = forms.CharField(label="Apellido", max_length=30, required=True)
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES, label="Tipo de Usuario")
    telephone = forms.CharField(max_length=15, required=False)
    direction = forms.CharField(widget=forms.Textarea, required=False)
    password_confirm = forms.CharField(widget=forms.PasswordInput, min_length=8, label="Confirmar Contraseña")
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        # Validar que las contraseñas coincidan
        if password != password_confirm:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.set_password(self.cleaned_data["password"])
        
        if commit:
            user.save()
            
            UserProfile.objects.create(
                user=user,
                role=self.cleaned_data["role"],
                telephone=self.cleaned_data["telephone"],
                direction=self.cleaned_data["direction"] 
            )
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        if not username or not password:
            raise forms.ValidationError("Se requieren tanto nombre de usuario como contraseña.")
        return cleaned_data