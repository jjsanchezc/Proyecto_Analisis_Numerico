import http
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    print("si está cargando")
    return render(request,'home.html')

def segundaPantalla(request):
    return HttpResponse("holi")