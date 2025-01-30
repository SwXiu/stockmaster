from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

User = get_user_model()


def signup(request):
    if request.method == 'POST':
        print(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user:user')
        else:
            return render(request, 'signup.html', {'form': form})
            
    else:
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})



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


def userView(request):
    if request.user.is_superuser:
        return redirect('adminV:adminInterface')

    return redirect('clientV:clientInterface')
