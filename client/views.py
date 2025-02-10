from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

class ClientInterface(LoginRequiredMixin, View):
      login_url = 'user:login'
      redirect_field_name = 'next'

      def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'client.html')