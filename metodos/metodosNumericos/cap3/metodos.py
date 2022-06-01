import base64
import numpy as np
import json
import sympy as sym
from scipy import interpolate
from math import sqrt
import matplotlib.pyplot as plt
import io
from pylab import mpl
from metodos.metodosNumericos.Funcion import Funcion

def vandermonde(mata,matb):
    tableListData = []
    tempMapIterData = {}
    msg=None
    x = mata
    x = json.loads(x)

    y = matb
    y = json.loads(y)

    n = (len(x) +len(y))/2

    points = zip(x, y)
    sorted_points = sorted(points)
    new_xs = [point[0] for point in sorted_points]
    new_ys = [point[1] for point in sorted_points]
    xn = np.array(new_xs)
    yn = np.array([new_ys]).T

    
    A = np.vander(xn)
    Ainv = np.linalg.inv(A)
    a = np.dot(Ainv, yn)

    
    tempMapIterData['Resultado'] = str(A)
    tempMapIterData['inversa'] = str(Ainv)
    tempMapIterData['puntos'] = str(a)

    tableListData.append(tempMapIterData.copy())
    tempMapIterData.clear()

    xp = np.linspace(min(x),max(x))
    p  = np.polyfit(x,y,len(x)-1)
    yp = np.polyval(p,xp)

    plt.figure()
    plt.plot(xp,yp,'b-', label = 'interpolant polynomial')
    plt.plot( x, y,'ro', label = 'points')
    

    buf = io.BytesIO()
    plt.savefig(buf)
    buf.seek(0)
    img = buf.read()

    str1 = ""
    for i in range(int(n)):
        str1 = str1 + "a" + str(int(n) - 1 - i) + " = " + str(a[i]) + " "
    for i in tableListData:
        print(i)
    msg=str1
    return msg


def newtonInter(a,b):
    msg=None
    tableListData = []
    tempMapIterData = {}

    x = a
    x= json.loads(x)
    
    y = b
    y = json.loads(y)

    n = len(y)
    coef = np.zeros([n, n])
    # the first column is y
    coef[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = \
        (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
        tempMapIterData['Resultado'] = str(coef)
        tableListData.append(tempMapIterData.copy())
        tempMapIterData.clear()        

    xp = np.linspace(min(x),max(x))
    p  = np.polyfit(x,y,len(x)-1)
    yp = np.polyval(p,xp)

    plt.figure()
    plt.plot(xp,yp,'b-', label = 'interpolant Newton')
    plt.plot( x, y,'ro', label = 'points')
    
    buf = io.BytesIO()
    plt.savefig(buf)
    buf.seek(0)
    img = buf.read()
    msg=str(coef)
    for i in tableListData:
        print(i)
    return msg

def spline(a,b,tipo):
    
    if tipo=='1': #lineal
        return splineal(a,b)
    if tipo=='2':#cubico
        return spcubico(a,b)
    else:
        return 'opcion de no valida'
    
def splineal(a,b):
    msg=None
    tableListData = []
    tempMapIterData = {}

    xi = a
    xi = json.loads(xi)
    fi = b
    fi = json.loads(fi)
    n = len(xi)
    x = sym.Symbol('x')
    px_tabla = []
    
    tramo = 1
    while not(tramo>=n):
        # con 1ra diferencia finita avanzada 
        numerador = fi[tramo]-fi[tramo-1]
        denominador = xi[tramo]-xi[tramo-1]
        m = numerador/denominador
        pxtramo = fi[tramo-1] + m*(x-xi[tramo-1])
        px_tabla.append(pxtramo)
        tramo = tramo + 1

        tempMapIterData['tramo'] = str(tramo)
        tempMapIterData['Numerador'] = str(numerador)
        tempMapIterData['m'] = str(m)
        tempMapIterData['pxtramo'] = str(pxtramo)
        

        tableListData.append(tempMapIterData.copy())
        tempMapIterData.clear()

    
    xp = np.linspace(min(xi),max(xi))
    p  = np.polyfit(xi,fi,len(xi)-1)
    yp = np.polyval(p,xp)

    plt.figure()
    plt.plot(xp,yp,'b-', label = 'Trazador Lineal')
    plt.plot( xi, fi,'ro', label = 'points')
    
    buf = io.BytesIO()
    plt.savefig(buf)
    buf.seek(0)
    img = buf.read()
    
    for i in tableListData:
        print(i)
    msg=str(px_tabla)
    return msg

def spcubico(a,b):
    msg=None
    tableListData = []
    tempMapIterData = {}

    x = a
    x= json.loads(x)
    
    y = b
    y = json.loads(y)

    n=len(x)-1 # Conveniente para el uso posterior de n
    h=np.zeros(n)
    for i in range (0,n):
        h[i]=x[i+1]-x[i]
    u=np.zeros(n-1)
    l=np.zeros(n-1)
    for i in range (0,n-1):
        u[i]=h[i]/(h[i]+h[i+1])
        l[i]=1-u[i]
    d=np.zeros(n-1)
    plt.figure()
    for i in range(1,n-2):
        d[i]=3*(l[i-1]*(y[i+2]-y[i+1])/h[i+1]+u[i-1]*(y[i+1]-y[i])/h[i])    
    d[0]=3*(l[0]*(y[1]-y[0])/h[0]\
            +u[0]*(y[2]-y[1])/h[1])-l[0]*0.8# 0.8 y 0.2 son condiciones de frontera de soporte fijo
    d[n-2]=3*(l[n-2]*(y[n-1]-y[n-2])/h[n-2]\
            +u[n-2]*(y[n]-y[n-1])/h[n-1])-l[n-2]*0.2

    
    
    A=np.zeros([n-1,n-1])
    for i in range(1,n-2):
        A[i,i-1]=l[i-1]
        A[i,i]=2
        A[i,i+1]=u[i]
        
    A[0,0]=A[n-2,n-2]=2
    A[0,1]=u[0]
    A[n-2,n-3]=l[n-2]
    
    M0=np.array(n)
    M0=np.linalg.solve(A,d)
    M=np.zeros(n+1)
    for i in range(1,n):
        M[i]=M0[i-1]
    M[0]=0.8
    M[n]=0.2
    
    #Dibujo
    for i in range(0,n):
        x0=np.linspace(x[i],x[i+1],10000)
        y0=y[i]*((x0-x[i+1])**2)*(h[i]+2*(x0-x[i]))/(h[i]**3)\
        +y[i+1]*((x0-x[i])**2)*(h[i]+2*(x[i+1]-x0))/(h[i]**3)\
        +M[i]*((x0-x[i+1])**2)*(x0-x[i])/(h[i]**2)\
        +M[i+1]*((x0-x[i])**2)*(x0-x[i+1])/(h[i]**2)
        plt.plot(x0,y0,color='red')
        
    plt.plot(x0,y0,color='red',label = u"Interpolación de splines cúbicos de autoedición")
    plt.plot(x,y,marker='+',mec='r',mfc='w',label = u"Primitivo")
    plt.title("Interpolación de splines cúbicos de la curva de la puerta del automóvil")

    tempMapIterData['A'] = str(A)
    tempMapIterData['d'] = str(d)
    tableListData.append(tempMapIterData.copy())
    tempMapIterData.clear()

    buf = io.BytesIO()
    plt.savefig(buf)
    buf.seek(0)
    img = buf.read()
    for i in tableListData:
        print(i)
    msg=str(M0)
    return msg

