from django.shortcuts import render
from django.views.generic import View

class Login(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'login.html', context)