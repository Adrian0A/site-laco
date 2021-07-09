from . import views
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import HttpRequest as request
# Create your views here.
 
class HomePage(View):
    def get(self, request):
        return render(request,'home/main.html')