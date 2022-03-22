from symp
import numpy as np

#HAY QUE REVISAR ESTE METODO Y COMO PODEMOS HACER CADA OPERACION
def newton(x0,tol,niter,f):
    df=derivadaDe(f)   #no tengo ni idea de como hacer una derivada
    contador=0
    error=tol+1
    while error>tol and f!=0 and df!=0 and contador <niter:
        #FALTA TODA LA PARTE DE OPERACIONES
        return 0


        
    if f==0:
        print("x0 es raiz")
    elif error<tol:
        print("x1 es aproximaciona  una raiz con una tolerancia = tol")
    
        

