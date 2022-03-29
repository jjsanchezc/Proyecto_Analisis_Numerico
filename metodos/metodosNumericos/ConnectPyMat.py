import matlab.engine
from numpy import double
eng = matlab.engine.start_matlab()


def busIncr(x0,delta,niter):#mas tarde defino los parametros
    eng = matlab.engine.start_matlab()
    #print(eng.busquedasIncr(float(x0),float(delta),float(niter)))
    print(eng.busquedasIncr(x0,delta,niter))
    print ("aca va el calculo final de la busqueda")
    eng.quit()

def bisecc(xi,xs,Tol,niter):
    eng2=eng
    print(eng2.biseccion(xi,xs,Tol,niter))
    print("------------------------")