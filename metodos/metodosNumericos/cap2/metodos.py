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

def SOR(mata,termb,x0,tol,w):
    print('entro melo')
    tableListData = []
    tempMapIterData = {}

    a = json.loads(mata)
    a = np.array(a)
    
    x0 = json.loads(x0)
    
    b = json.loads(termb)
    b = np.array(b)
    w = float(w)
    tol = float(tol)


    step = 0
    phi = x0[:]
    residual = np.linalg.norm(np.matmul(a, phi) - b)  # Initial residual
    msg=None
    print('todo bien hasta aca')
    while residual > tol:
        for i in range(a.shape[0]):
            sigma = 0
            for j in range(a.shape[1]):
                if j != i:
                    sigma += a[i, j] * phi[j]
            phi[i] = (1 - w) * phi[i] + (w / a[i, i]) * (b[i] - sigma)
        residual = np.linalg.norm(np.matmul(a, phi) - b)
        step += 1
        print("Step {} Residual: {:10.6g}".format(step, residual))
        tempMapIterData['Iteracion'] = str(step)
        tempMapIterData['Resultado'] = str(residual)

        tableListData.append(tempMapIterData.copy())
        for i in tableListData:
            print(i)
            msg=i
        tempMapIterData.clear()
    return msg        

def pivoteos(mata,vecb,tipo_piv):
    #aca llama a ambos
    if tipo_piv=='1':
        return pivParcial(mata,vecb)
    elif tipo_piv=='2':
        return pivTotal(mata,vecb)
    else:
        return 'opcion de pivoteo no valida'
    
def pivTotal(mata,vecb):
    tableListData = []
    tempMapIterData = {}

    a = mata
    a = json.loads(a)
    a = array(a, float)
    b = vecb
    b = json.loads(b)
    b = array(b, float)

    msg=None
    n = len(b)
    x = zeros(n, float)

    #first loop specifys the fixed row
    for k in range(n-1):
        if fabs(a[k,k]) < 1.0e-12:
            for i in range(k+1, n):
                if fabs(a[i,k]) > fabs(a[k,k]):
                    a[[k,i]] = a[[i,k]]
                    b[[k,i]] = b[[i,k]]
                    
                    break

    #applies the elimination below the fixed row
        for i in range(k+1,n):
            if a[i,k] == 0:continue
            factor = a[k,k]/a[i,k]
            for j in range(k,n):
                a[i,j] = a[k,j] - a[i,j]*factor
                
                #we also calculate the b vector of each row     


    x[n-1] = b[n-1] / a[n-1, n-1]
    
    for i in range(n-2, -1, -1):
        sum_ax = 0
    
        for j in range(i+1, n):
            sum_ax += a[i,j] * x[j]
            
        x[i] = (b[i] - sum_ax) / a[i,i]
    cad = ""
    asd = Funcion.to_string(x)
    amd  = asd.split('\n')
    for i in range(0, len(x), 1):
        cad = f"x{i} ="
        amdd = amd[i]
        
        tempMapIterData['xi'] = str(cad)
        tempMapIterData['x'] = str(amdd)
        tableListData.append(tempMapIterData.copy())
        tempMapIterData.clear()
    for i in tableListData:
        print (i)
    msg=str(x)
    return msg

        


def pivParcial(mata,vecb):
    tableListData = []
    tempMapIterData = {}

    a = mata
    a = json.loads(a)
    b = vecb
    b = json.loads(b)

    Ma = np.append(a, b, axis=1)
    n = len(Ma)
    msg=None
    for k in range(0, n - 1, 1):
        columna = abs(Ma[k:, k])
        dondeMax = np.argmax(columna)
        if dondeMax != 0:
            temporal = np.copy(Ma[k, :])
            Ma[k, :] = Ma[dondeMax + k, :]
            Ma[dondeMax + k, :] = temporal
        for i in range(k + 1, n, 1):

            if Ma[k][k] != 0:
                mult = Ma[i][k] / Ma[k][k]
            else:
                msg='pivote en 0'
                for i in tableListData:
                    print(i)
                return msg

            for j in range(k, n + 1, 1):
                Ma[i][j] = Ma[i][j] - (mult * Ma[k][j])
    
    x = Funcion.sust_regre(Ma)
    amd  = x.split('\n')
    for i in range(len(Ma)):
        cad = f"x{i} ="
        if i<len(amd):
            amdd = amd[i]
            tempMapIterData['xi'] = str(cad)
            tempMapIterData['x'] = str(amdd)
            tableListData.append(tempMapIterData.copy())
            
            tempMapIterData.clear()
    
    for i in tableListData:
        print(i)
    msg=str(x)
    return msg


