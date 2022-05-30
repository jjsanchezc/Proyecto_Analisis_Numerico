import matlab.engine
eng = matlab.engine.start_matlab()


def busIncr(x0,delta,niter):#mas tarde defino los parametros
    eng = matlab.engine.start_matlab()
    #print(eng.busquedasIncr(float(x0),float(delta),float(niter)))
    print(eng.busquedasIncr(x0,delta,niter))
    print ("aca va el calculo final de la busqueda")
    eng.quit()


#Empieza no lineales
def bisecc(xi,xs,Tol,niter,fun,err):
    print("Respuesta: ")
    print(eng.biseccion(xi,xs,Tol,niter,fun,err))
    print("------------------------")
    
def Newton(f,x0,Tol,niter,Terr):
    print("Respuesta: ")
    print(eng.Newton(f,x0,Tol,niter,Terr))
    print("------------------------")  
   
def Secante(f,xo,x1,niter,Tol):
    print("Respuesta: ")
    print(eng.Secante(f,xo,x1,niter,Tol))
    print("------------------------")  

def RegulaFalsi(f,xi,xs,tol,niter,terr):
    print("Respuesta: ")
    print(eng.RegulaFalsi(f,xi,xs,tol,niter,terr))
    print("------------------------")  

def PuntoFijo(f,g,x0,Tol,niter,Terr,x):
    print("Respuesta: ")
    print(eng.PuntoFijo(f,g,x0,Tol,niter,Terr,x))
    print("------------------------")  

#acaba no lineales

#empieza sistemas de ecuaciones
def GaussPiv(A,b,n,Piv,z):
    print("Respuesta: ")
    print(eng.GaussPiv(A,b,n,Piv,z))
    print("------------------------")  

def jacobi(A,b,x,Tol,niter):
    print("Respuesta: ")
    print(eng.jacobi(A,b,x,Tol,niter))
    print("------------------------")

def Seidel(A,b,x,itera,tole):
    print("Respuesta: ")
    print(eng.Seidel(A,b,x,itera,tole))
    print("------------------------")  

def SOR(x0,A,b,Tol,niter,w):
    print("Respuesta: ")
    print(eng.SOR(x0,A,b,Tol,niter,w))
    print("------------------------")  

def pivpar(Ab,n,k):
    print("Respuesta: ")
    print(eng.pivpar(Ab,n,k))
    print("------------------------")  

def pivtot(Ab,mark,n,k):
    print("Respuesta: ")
    print(eng.pivpar(Ab,n,k))
    print("------------------------")  

#acaba sistemas de ecuaciones

#empieza interpolacion
def Newtonint(x,y):
    print("Respuesta: ")
    print(eng.Newtonint(x,y))
    print("------------------------")    

def Newtonor(x,coef):
    print("Respuesta: ")
    print(eng.Newtonor(x,coef))
    print("------------------------")  

def SOR(x0,A,b,Tol,niter,w):
    print("Respuesta: ")
    print(eng.SOR(x0,A,b,Tol,niter,w))
    print("------------------------")  
#acaba interpolacion










