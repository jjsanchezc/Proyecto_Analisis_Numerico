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
        pm.busIncr(-2,0.5,4)
    return render(request,'metodos/busquedasIncr.html')

def bisec(request):
    """Metodo para leer los datos introducidos por el usuario y luego llamar al
    metodo ConnectPyMat

    Args:
        request : cuando lo llamen

    Returns:
        render: pagina de busquedasIncr
    """
    
    msg=None
    xi=request.POST.get('xi')
    xs=request.POST.get('xs')
    Tol=request.POST.get('Tol')
    niter=request.POST.get('niter')
    if xi!='' and xs!='' and  Tol!='' and  niter!='':
        print("entra en biseccion")
        try:
            pm.bisecc("rrrr","1","0.0005","4")
        except:
            print("error f")
    else:
        msg="dejaste un espacio vacioooooo"
    return render(request,'metodos/biseccion.html')

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
        print(f"x0: {x0} \ndelta: {delta}\nniter:{niter}")
    return render(request, 'metodos/busquedasIncr.html')