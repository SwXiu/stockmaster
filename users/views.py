from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
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
            user = form.save()  # Guarda el usuario de forma correcta
            login(request, user)  # Inicia sesión con el nuevo usuario
            return redirect('user:user')  # Redirige a una página de éxito o perfil
        else:
            print(form.errors)  # Puedes revisar los errores del formulario aquí
            return render(request, 'signUp.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'signUp.html', {'form': form})


def signin(request):
    if request.method == 'GET':

        return render(request, 'signin.html', {"form": AuthenticationForm()})

    else:
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()
            login(request, user)
            return redirect('user:user')

        return render(request, 'signin.html', {"form": form, "error": "Username or password is incorrect."})


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

        return JsonResponse({'exists': exists})  # ✅ ¡CONFIRMA QUE SE ENVÍA!
    
    return JsonResponse({'error': 'Missing parameters'}, status=400)