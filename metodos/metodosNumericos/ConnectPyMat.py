import matlab.engine
from numpy import double



#x0,Delta,niter
def busIncr(x0,delta,niter):#mas tarde defino los parametros
    eng = matlab.engine.start_matlab()
    #print(eng.busquedasIncr(float(x0),float(delta),float(niter)))
    print(eng.busquedasIncr(x0,delta,niter))
    print ("aca va el calculo final de la busqueda")
    eng.quit()