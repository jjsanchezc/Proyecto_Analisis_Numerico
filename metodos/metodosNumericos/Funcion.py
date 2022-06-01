import base64
from metodos.utils import get_graph
from sympy import *
from numpy import linspace
import matplotlib.pyplot as mpl
import io
import numpy as np
import numpy as numpy
import sympy as sym
x = Symbol('x')
from scipy import interpolate
from io import BytesIO

class Funcion:
    f = 0

    def __init__(self, f):
        self.f = f

    def getF(self):
        return self.f

    def setF(self, f):
        self.f = f

    def evaluar(self, expr, a):
        y = sympify(expr, evaluate=True).subs(x, a)
        return y

    def derivada(self):
        y = diff(self.f, x)
        return y

    def grafica(self, x_start, x_end, steps):
        lam_x = lambdify(x, self.f, modules=['numpy'])
        x_vals = linspace(x_start, x_end, num=steps)
        y_vals = lam_x(x_vals)

        mpl.figure()
        mpl.axhline(y=0, color='r', linestyle='-')
        mpl.plot(x_vals, y_vals)
        mpl.ylabel("")
        buf = io.BytesIO()
        mpl.savefig(buf)
        buf.seek(0)
        return buf.read()

    def sust_regr(A):
        n = len(A)
        cadena = ""
        x = numpy.zeros(n, dtype=float)

        for i in range(n - 1, -1, -1):
            sum = 0
            for p in range(i + 1, n, 1):
                sum = sum + A[i][p] * x[p]

            x[i] = (A[i][n] - sum) / A[i][i]

        for i in range(0, len(x), 1):
            cadena = cadena + "x" + str(i) + "= " + str(x[i]) + "\n"
    
    def sust_regre(A):
        n = len(A)
        cadena = ""
        x = numpy.zeros(n, dtype=float)

        for i in range(n - 1, -1, -1):
            sum = 0
            for p in range(i + 1, n, 1):
                sum = sum + A[i][p] * x[p]

            x[i] = (A[i][n] - sum) / A[i][i]

        for i in range(0, len(x), 1):
            if i == len(x)-1:
                 cadena = cadena + str(x[i])
            else:
                cadena = cadena + str(x[i]) + "\n"
        return cadena

    def to_string(x):
        cadena = ""
        for i in range(0, len(x), 1):
            if i == len(x)-1:
                 cadena = cadena + str(x[i])
            else:
                cadena = cadena + str(x[i]) + "\n"

        return cadena

    def get_diff_table(X,Y):
        """
        Obtenga la tabla de interpolación
        """
        n=len(X)
        A=np.zeros([n,n])
        
        for i in range(0,n):
            A[i][0] = Y[i]
        
        for j in range(1,n):
            for i in range(j,n):
                A[i][j] = (A[i][j-1] - A[i-1][j-1])/(X[i]-X[i-j])
        
        return A

    def f(x,x_points, y_points):
        tck = interpolate.splrep(x_points, y_points)
        return interpolate.splev(x, tck)
    
    def get_graph():
        buffer= BytesIO()
        mpl.savefig(buffer,format='png')
        buffer.seek(0)
        image_png=buffer.getvalue()
        graph= base64.b64encode(image_png)
        graph=graph.decode('utf-8')
        buffer.close()
        return graph

    def get_plot(x,y,nomb_tabla,nomb_x,nomb_y):
        mpl.switch_backend('AGG')
        mpl.figure(figsize=(10,3))
        mpl.title(nomb_tabla)
        mpl.plot(x,y)
        mpl.xticks(rotation=45)
        mpl.xlabel(nomb_x)
        mpl.ylabel(nomb_y)
        mpl.tight_layout()
        graph=get_graph()
        return graph