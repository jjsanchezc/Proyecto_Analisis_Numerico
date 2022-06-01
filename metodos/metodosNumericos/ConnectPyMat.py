from sys import stdout
import matlab.engine
eng = matlab.engine.start_matlab()
import io


def busIncr(x0,delta,niter):#mas tarde defino los parametros
    eng = matlab.engine.start_matlab()
    #print(eng.busquedasIncr(float(x0),float(delta),float(niter)))
    print(eng.busquedasIncr(x0,delta,niter))
    print ("aca va el calculo final de la busqueda")
    eng.quit()


#Empieza no lineales
def bisecc(xi,xs,Tol,niter,fun,err):
    #listo
    print("Respuesta: ")
    ans=eng.biseccion(xi,xs,Tol,niter,fun,err)
    print("------------------------")
    return ans
    
def Newton(f,x0,Tol,niter,Terr):
    #listo
    print("Respuesta: ")
    ans=eng.Newton(f,x0,Tol,niter,Terr)
    print(ans)
    print("------------------------")  
    return ans
def Secante(x0,x1,tol,niter,f):
    #listo
    print("Respuesta: ")
    ans=eng.Secante(x0,x1,tol,niter,f)
    print(ans)
    print("------------------------")  
    return ans
def RegulaFalsi(f,xi,xs,tol,niter,terr):
    #listo
    print("Respuesta: ")
    ans=eng.RegulaFalsi(f,xi,xs,tol,niter,terr)
    print(ans)
    print("------------------------")  
    return ans
def PuntoFijo(f,g,x0,Tol,niter,Terr):
    #listo
    print("Respuesta: ")
    ans=eng.PuntoFijo(f,g,x0,Tol,niter,Terr)
    print(ans)
    print("------------------------") 
    return ans 

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

def SOR(x0,A,b,tole,itera,w):
    print("Respuesta: ")
    print(eng.SOR(x0,A,b,tole,itera,w))
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

def Spline(x,y,d):
    print("Respuesta: ")
    print(eng.Spline(x,y,d))
    print("------------------------")  
#acaba interpolacion










