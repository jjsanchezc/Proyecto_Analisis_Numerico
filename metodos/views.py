import http
from os import execv
import matlab
from django.shortcuts import render
from metodos.metodosNumericos import ConnectPyMat as pm

# Create your views here.
def home(request):
    return render(request,'home.html')

def busIncr(request):

    if request.method=="POST":
        print("entraaaaaaa")
        pm.busIncr(-2,0.5,4)
    return render(request,'metodosNoLineal/busquedasIncr.html')


def bisec(request):
    #listo
    print(request.POST)
    msg=None
    Xi=request.POST.get('Xi')
    Xs=request.POST.get('Xs')
    Tol=request.POST.get('Tol')
    nIter=request.POST.get('nIter')
    fun=request.POST.get('Fun')
    err=request.POST.get('err')
    if Xi!=None and Xs!=None and  Tol!=None and  nIter!=None and fun!=None and err!=None :
        if Xi!="" and Xs!="" and  Tol!="" and  nIter!="" and fun!="" and err!="" :
            print("entra en biseccion")
            try:
                
                msg=pm.bisecc(Xi,Xs,Tol,nIter,fun,err)
            except:
                msg='ingresaste mal un dato'
        else:
            print('dejaste un espacio vacio')
            msg="dejaste un espacio vacioooooo"
    return render(request,'metodosNoLineal/biseccion.html',{'msg':msg})

def newton(request):
    #listo
    fun=request.POST.get('fun')
    x=request.POST.get('x0')
    tol=request.POST.get('tol')
    niter=request.POST.get('niter')
    err=request.POST.get('err')
    
    if x!=None and tol!=None and niter!=None and fun!=None and err!=None:
        try:
            pm.Newton(fun,x,tol,niter,err)
        except:
            print('error en Newton')
    return render(request, 'metodosNoLineal/newton.html')

def puntoFijo(request):
    #listo
    print(request.POST)
    funf=request.POST.get('funf')
    fung=request.POST.get('fung')
    x0=request.POST.get('x0')
    tol=request.POST.get('tol')
    niter=request.POST.get('niter')
    err=request.POST.get('err')
    if x0!=None and tol!=None and niter!=None and funf!=None and fung!=None:
        try:
            pm.PuntoFijo(funf,fung,x0,tol,niter,err)
        except:
            print('error punto fijo')
    return render(request, 'metodosNoLineal/puntoFijo.html')

def reglaFalsa(request):
    #listo
    fun=request.POST.get('fun')
    xi=request.POST.get('xi')
    xf=request.POST.get('xf')
    tol=request.POST.get('tol')
    niter=request.POST.get('niter')
    err=request.POST.get('err')
    if xi!=None and xf!=None and tol!=None and niter!=None and fun!=None:
        try:
            pm.RegulaFalsi(fun,xi,xf,tol,niter,err)
        except:
            print('error en regla falsa')
    return render(request, 'metodosNoLineal/reglaFalsa.html')

def secante(request):
    #listo
    fun=request.POST.get('fun')
    x0=request.POST.get('x0')
    x1=request.POST.get('x1')
    tol=request.POST.get('tol')
    niter=request.POST.get('niter')
    if x0!=None and x1!=None and  tol!=None and  niter!=None and fun!=None:
        try:
            pm.Secante(x0,x1,tol,niter,fun)
        except:
            print('error en secante')
    return render(request, 'metodosNoLineal/secante.html')

def raicesMult(request):
    return render(request, 'metodosNoLineal/raicesMult.html')

def gauss(request):
    A=request.POST.get('matA')
    b=request.POST.get('vecb')
    n=request.POST.get('normaV')
    Piv=request.POST.get('piv')
    z=request.POST.get('normae')
    
    if b!=None and n!=None and Piv!=None and A!=None and z!=None:
        try:
            pm.GaussPiv(A,b,b,Piv,z)
        except:
            print('error en Gauss')
    return render(request, 'sistemaDeEcua/gauss.html')

def jacobi(request):
    mata=request.POST.get('mata')
    termb=request.POST.get('termb')
    x0=request.POST.get('x0')
    tol=request.POST.get('tol')
    niter=request.POST.get('niter')
    
    if termb!=None and x0!=None and tol!=None and mata!=None and niter!=None:
        try:
            pm.jacobi(mata,termb,x0,tol,niter)
        except:
            print('error en Jacobi')
    return render(request, 'sistemaDeEcua/jacobi.html')

def gaussSeidel(request):
    mata=request.POST.get('mata')
    termb=request.POST.get('termb')
    x0=request.POST.get('x0')
    tol=request.POST.get('tol')
    niter=request.POST.get('niter')
    
    if termb!=None and x0!=None and tol!=None and mata!=None and niter!=None:
        try:
            pm.Seidel(mata,termb,x0,tol,niter)
        except:
            print('error en Gauss Seidel')
    return render(request, 'sistemaDeEcua/gaussSeidel.html')

def SOR(request):
    mata=request.POST.get('mata')
    termb=request.POST.get('termb')
    x0=request.POST.get('x0')
    tole=request.POST.get('tol')
    itera=request.POST.get('niter')
    w=request.POST.get('w')
    
    if termb!=None and x0!=None and tole!=None and mata!=None and itera!=None and w!=None:
        try:
            pm.SOR(mata,termb,x0,tole,itera,w)
        except:
            print('error en SOR')
    return render(request, 'sistemaDeEcua/SOR.html')

def vandermonde(request):
    return render(request, 'interpolacion/vandermonde.html')

def spline(request):
    return render(request, 'interpolacion/spline.html')

def newtonIn(request):
    return render(request, 'interpolacion/newtonIn.html')




 