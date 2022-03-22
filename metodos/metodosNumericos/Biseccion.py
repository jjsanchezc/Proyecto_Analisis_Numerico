import math

def biseccion(xi,xs,tol,niter,fun):
	"""
	Xi = float(input("Xi:"))
	Xs = float(input("Xs:"))
	Tol = float(input("Tol:"))
	Niter = float(input("Niter:"))
	print("Function:")
	Fun = input()
"""
	Xi=xi
	Xs=xs
	Tol=tol
	Niter=niter
	Fun=fun

	
	fm=[]
	E=[]
	x=Xi
	fi=eval(Fun)
	x=Xs
	fs=eval(Fun)

	if fi==0:
		s=Xi
		E=0
		print(Xi, "es raiz de f(x)")
	elif fs==0:
		s=Xs
		E=0
		print(Xs, "es raiz de f(x)")
	elif fs*fi<0:
		c=0
		Xm=(Xi+Xs)/2
		x=Xm                 
		fe=eval(Fun)
		fm.append(fm)
		E.append(100)
		while E[c]>Tol and fe!=0 and c<Niter:
			if fi*fe<0:
				Xs=Xm
				x=Xs                 
				fs=eval(Fun)
			else:
				Xi=Xm
				x=Xi                 
				fs=eval(Fun)
				Xa=Xm
				Xm=(Xi+Xs)/2
				x=Xm 
				fe=eval(Fun)
				fm.append(fm)
				Error=abs(Xm-Xa)
				E.append(Error)
				c=c+1
		if fe==0:
			s=x
			print(s,"es raiz de f(x)")
		elif Error<Tol:
			s=x
			print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
		else :                                     
			s=x
			print("Fracaso en ",Niter, " iteraciones ") 
