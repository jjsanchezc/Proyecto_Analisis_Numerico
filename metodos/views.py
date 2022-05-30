import http
import matlab
from django.shortcuts import render
from metodos.metodosNumericos import ConnectPyMat as pm

# Create your views here.
def home(request):
    return render(request,'home.html')

def metodosNoLineal(request):
    return render(request,'metodosNoLineal.html')

def sistemaDeEcua(request):
    return render(request,'sistemaDeEcua.html')

def bisec(request):
    """Metodo para leer los datos introducidos por el usuario y luego llamar al
    metodo ConnectPyMat

    Args:
        request : cuando lo llamen

    Returns:
        render: pagina de busquedasIncr
    """
    
    msg=None
    Xi=request.POST.get('Xi')
    Xs=request.POST.get('Xs')
    Tol=request.POST.get('Tol')
    nIter=request.POST.get('nIter')
    if Xi!='' and Xs!='' and  Tol!='' and  nIter!='':
        print("entra en biseccion")
        try:
            pm.bisecc("-2","1","0.0005","4") #cambiar esto con los datos que se ingresen
            #hola pauli
        except:
            print("error f")
    else:
        msg="dejaste un espacio vacioooooo"
    return render(request,'metodosNoLineal/biseccion.html')

def busIncr(request):

    if request.method=="POST":
        print("entraaaaaaa")
        pm.busIncr(-2,0.5,4)
    return render(request,'metodosNoLineal/busquedasIncr.html')

def newton(request):
    return render(request, 'metodosNoLineal/newton.html')

def puntoFijo(request):
    return render(request, 'metodosNoLineal/puntoFijo.html')

def reglaFalsa(request):
    return render(request, 'metodosNoLineal/reglaFalsa.html')

def secante(request):
    return render(request, 'metodosNoLineal/secante.html')

def raicesMult(request):
    return render(request, 'metodosNoLineal/raicesMult.html')

def gauss(request):
    return render(request, 'sistemaDeEcua/gauss.html')

def jacobi(request):
    return render(request, 'sistemaDeEcua/jacobi.html')

def gaussSeidel(request):
    return render(request, 'sistemaDeEcua/gaussSeidel.html')

def SOR(request):
    return render(request, 'sistemaDeEcua/SOR.html')

def calcular(request):
    if request.method=="POST":
        x0=0
        x0=request.POST.get('x0')
        delta=request.POST.get('delta')
        niter=request.POST.get('niter')
        print(type(niter),"este es el tipo de dato de")
      #  try:
        pm.busIncr(x0,delta,niter)
    #except ValueError:
        print("hubo un error de value")
        print(f"x0: {x0} \ndelta: {delta}\niter:{niter}")
    return render(request, 'metodosNoLineal/busquedasIncr.html')



 