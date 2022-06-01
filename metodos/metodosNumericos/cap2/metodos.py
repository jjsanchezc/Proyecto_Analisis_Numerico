import base64
from turtle import end_poly
from numpy.linalg import inv, eigvals, norm
import numpy as np
from numpy import array, zeros, fabs, linalg
import json
from metodos.metodosNumericos.Funcion import Funcion


def eliminaiconGauss(a,b):
    tableListData = []
    tempMapIterData = {}
    a = json.loads(a)
    b = json.loads(b)

    Ma = np.append(a, b, axis=1)
    n = len(Ma)
    for k in range(0, n - 1, 1):
        for i in range(k + 1, n, 1):
            if Ma[k][k] != 0:
                mult = Ma[i][k] / Ma[k][k]
            else:
                msg='pivote en 0'
                print(tableListData)
                return msg
            for j in range(k, n + 1, 1):
                Ma[i][j] = Ma[i][j] - (mult * Ma[k][j])
                tempMapIterData[''] = str(Funcion.sust_regre(Ma))
                tableListData.append(tempMapIterData.copy())
                tempMapIterData.clear()
        
    x = Funcion.sust_regre(Ma)
    for i in tableListData:
        print(i)
    
    msg=str(x)
    return msg

def jacobi(a,b,x0,tol,n):
    tableListData = []
    tempMapIterData = {}

    a = json.loads(a)
    x0 = json.loads(x0)
    b = json.loads(b)
    n = int(n)
    tol = float(tol)


    l = -np.tril(a, -1)
    u = -np.triu(a, 1)
    d = a + l + u
    t = np.matmul(inv(d), l + u)
    c = np.matmul(inv(d), b)
    msg=None
    if max(abs(eigvals(t))) > 1:
        msg='la funcion no converge'
        for i in tableListData:
            print(i)
        return msg
        
    if x0 is None:
        x0 = []
        for i in range(len(a)):
            x0.append([0])
    if tol is None:
        tol = 10 ** -5
    xn = np.matmul(t, x0) + c
    cont = 0
    e = 1000
    
    while (x0 != xn).all() and cont < n and e > tol:
        x0 = xn
        xn = np.matmul(t, x0) + c
        cont += 1
        e = norm(x0 - xn)
        tempMapIterData['iteracion'] = str(cont)
        tempMapIterData['x0'] = str(x0)
        tempMapIterData['xn'] = str(xn)
        tempMapIterData['E'] = str(e)
        tableListData.append(tempMapIterData.copy())
        msg=None
        for i in tableListData:
            print(i)
            msg=i
        tempMapIterData.clear()
    return msg 

def seidel(mata,termb,x0,tol,niter):
    
    tableListData = []
    tempMapIterData = {}
    # todo: Generar tabla

    a = json.loads(mata)
    x0 = json.loads(x0)
    b = json.loads(termb)
    n = int(niter)
    tol = float(tol)

    l = -np.tril(a, -1)
    u = -np.triu(a, 1)
    d = a + l + u
    t = np.matmul(inv(d - l), u)
    c = np.matmul(inv(d - l), b)

    msg=None
    if max(abs(eigvals(t))) > 1:
        msg='la funcion no converge'
        for i in tableListData:
            print(i)
        return msg
        
    if x0 is None:
        x0 = []
        for i in range(len(a)):
            x0.append([0])
    if tol is None:
        tol = 10 ** -5

    xn = np.matmul(t, x0) + c
    cont = 0
    e = 1000
    while (x0 != xn).all() and cont < n and e > tol:
        x0 = xn
        xn = np.matmul(t, x0) + c
        cont += 1
        e = norm(x0 - xn)
        tempMapIterData['iteracion'] = str(cont)
        tempMapIterData['x0'] = str(x0)
        tempMapIterData['xn'] = str(xn)
        tempMapIterData['E'] = str(e)
        tableListData.append(tempMapIterData.copy())
        
        for i in tableListData:
            print(i)
            msg=i
        tempMapIterData.clear()
    return msg

def SOR():
    pass

def pivoteos():
    #aca llama a ambos
    pass
def pivTotal():
    pass
def pivParcial():
    pass


