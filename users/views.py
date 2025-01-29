from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages

def signupView(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Validar que las contraseñas coincidan
        if password != password_confirm:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'signup.html')

        # Verificar que el usuario no exista
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya está registrado.")
            return render(request, 'signup.html')

        # Crear usuario
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # Guardar otros datos (Django User por defecto no tiene teléfono)
        user.save()

        return redirect('home')  # Redirigir al usuario a la página principal

    return render(request, 'signup.html')

class LoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True 

class UserView(View):
    def get(self, request, *args, **kwargs):
        if request.user.profile.role == 'client':
            return redirect('clientInterface')
        elif request.user.profile.role == 'admin':
            return redirect('adminInterface')
        else:
            return redirect('home')
