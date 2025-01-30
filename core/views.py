from django.shortcuts import render
from django.views.generic import View

class HomePage(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'index.html', context)

class AdminInterface(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'admin.html')

class ClientInterface(View):
     def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'client.html')