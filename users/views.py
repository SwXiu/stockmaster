from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import RegisterForm

class SignupView(FormView):
    template_name = 'signUp.html'
    form_class = RegisterForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

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
