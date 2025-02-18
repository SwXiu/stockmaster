from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda el usuario en la base de datos

            login(request, user, backend='users.backend.EmailBackend')  # Autentica al usuario con el backend

            return redirect('user:user')  # Redirige después de iniciar sesión
        else:
            print(form.errors)  # Imprime errores para depuración
            return render(request, 'signUp.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'signUp.html', {'form': form})


def signin(request):
    if request.method == "POST":
        email = request.POST.get("email1")
        password = request.POST.get("password")

        # Autenticar al usuario
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            # Si la autenticación es exitosa, devuelve un éxito con una URL para redirigir
            return JsonResponse({"success": True, "redirectUrl": "/user"}, status=200)
        else:
            # Si la autenticación falla, retorna un error
            return JsonResponse({"error": "Correo o contraseña incorrectos"}, status=400)

    return render(request, "signin.html")


@login_required
def signout(request):
    logout(request)
    return redirect('home')

@login_required
def userView(request):
    if request.user.is_superuser:
        return redirect('adminV:adminInterface')

    return redirect('clientV:clientInterface')


def check_field_exists(request):
    field_value = request.GET.get('value', None)
    field_type = request.GET.get('type', None)

    if field_value and field_type:
        if field_type == 'username':
            exists = CustomUser.objects.filter(username=field_value).exists()
        elif field_type == 'email':
            exists = CustomUser.objects.filter(email=field_value).exists()
        elif field_type == 'telephone':
            exists = CustomUser.objects.filter(telephone=field_value).exists()
        else:
            return JsonResponse({'error': 'Invalid field type'}, status=400)

        return JsonResponse({'exists': exists})
    
    return JsonResponse({'error': 'Missing parameters'}, status=400)