from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

class AdminInterface(LoginRequiredMixin, View):
    login_url = 'user:signin'
    redirect_field_name = 'next'

    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'admin.html')
