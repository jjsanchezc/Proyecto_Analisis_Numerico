import numpy as np
import base64
from metodos.metodosNumericos.Funcion import Funcion

def raicesmultiples(fun,x0,tol,niter,opc):
    tableListData = []
    tempMapIterData = {}
    # funcion en terminos de x
    f = Funcion(fun)
    # Intervalo inicial
    x0 = float(x0)
    # tolerancia
    tol = float(tol)
    # iteraciones maximas
    Nmax = float(niter)
    imgxStart = float(0)
    imgxEnd = float(10)
    step = int(1000)
    cont = 0
    E = tol + 1
    df = Funcion(f.derivada())
    df2 = Funcion(df.derivada())
    factual = f.evaluar(f.getF(), x0)
    fderivada = df.evaluar(df.getF(), x0)
    fderivada2 = df2.evaluar(df2.getF(), x0)
    while (cont < Nmax) and (E > tol):
        tempMapIterData['Iter'] = str(cont)
        tempMapIterData['f_n(Xn)'] = str(factual)
        tempMapIterData["f'_n(Xn)"] = str(fderivada)
        tempMapIterData["f''_n(Xn)"] = str(fderivada2)
        xn = x0 - ((factual * fderivada) / ((fderivada * fderivada) - (factual * fderivada2)))
        tempMapIterData['Xn'] = str(xn)
        E = abs(xn - x0)
        if cont != 0:
            tempMapIterData['E'] = str(E)
        tableListData.append(tempMapIterData.copy())
        tempMapIterData.clear()

        x0 = xn
        factual = f.evaluar(f.getF(), x0)
        fderivada = df.evaluar(df.getF(), x0)
        fderivada2 = df2.evaluar(df2.getF(), x0)

        if E > tol:
            cadena = "Hay una raiz que no cumple con la tolerancia en el x = " + str(
                xn) + " en el intervalo =  " + str(
                cont) + " con error = " + str(E)
        else:
            cadena = "Hay una raiz que cumple con la tolerancia en el x = " + str(xn) + " en la iter = " + str(
                cont) + " con error = " + str(E)
        cont = cont + 1

    img = f.grafica(imgxStart, imgxEnd, step)
    if opc==1:
        return cadena
    else:
        return img