import base64
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
                tempMapIterData['Resultante'] = str(Funcion.sust_regre(Ma))
                tableListData.append(tempMapIterData.copy())
                tempMapIterData.clear()
        
    x = Funcion.sust_regre(Ma)
    msg='cre creo que es error'
    return msg

def jacobi():
    pass

def seidel():
    pass

def SOR():
    pass

def pivoteos():
    #aca llama a ambos
    pass
def pivTotal():
    pass
def pivParcial():
    pass


