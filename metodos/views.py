import http
import matlab
from django.shortcuts import render
from metodos.metodosNumericos import ConnectPyMat as pm

# Create your views here.
def home(request):
    return render(request,'home.html')

def busIncr(request):
    if request.method=="POST":
        print("entraaaaaaa")
        pm.busIncr(matlab.double(-2),matlab.double(0.5),matlab.double(4))
    return render(request,'metodos/busquedasIncr.html')

def bisec(request):
    if request.method=="POST":
        print("entra en biseccion")
        pm.bisecc(-3,-2,0.5,4)
    return render(request,'metodos/biseccion.html')