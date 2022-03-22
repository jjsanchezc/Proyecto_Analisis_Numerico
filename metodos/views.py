from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    print("si está cargando")
    return HttpResponse(request, 'home.html')