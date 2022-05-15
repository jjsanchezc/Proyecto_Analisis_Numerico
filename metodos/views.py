import http
import matlab
from django.shortcuts import render
from metodos.metodosNumericos import ConnectPyMat as pm

# Create your views here.
def home(request):
    #metodo para ir a la pantalla home
    return render(request,'home.html')

def metodosLineales(request):
    #metodo para ir a la pantalla de definicion de metodos
    return render(request,'metodosLineales.html')

def ecuaciones(request):
    return render(request,'ecuaciones.html')

def bisec(request):
    """Metodo para leer los datos introducidos por el usuario y luego llamar al
    metodo ConnectPyMat
    """
    print(request.get_full_path())
    if request.get_full_path()=='/metodosLineales/biseccion' :
        print('este es el request de biseccccccion')
    msg=None
    if request.method=="POST":
        Xi=request.POST.get('Xi')
        Xs=request.POST.get('Xs')
        Tol=request.POST.get('Tol')
        nIter=request.POST.get('nIter')
        if Xi!='' and Xs!='' and  Tol!='' and  nIter!='':
            print(Xs)
            print(Xi)
            try:
                print(type(pm.bisecc(Xi,Xs,Tol,nIter))) 
                msg=pm.bisecc(Xi,Xs,Tol,nIter)
            except:
                print("error f")
        else:
            msg="dejaste un espacio vacio"
            print('Espacio vacio')
    print('pagina normal')
    return render(request,'metodosLineales/biseccion.html',{'msg':msg})


def calculo(request):
    """este metodo va a ser llamado por cada metodo
    con el if se define que tipo de metodo es, va a recibir cada parte y lo va a calcular
    se debe de ir definiendo cada uno 
    debe retornar el valor
    este va a ser el metodo que puede 

    Args:
        request (_type_): _description_
    """
    msg=None
    print(request.get_full_path())
    if request.get_full_path()=='/metodosLineales/biseccion' :
        print('este es el request de biseccccccion')
    pass

 