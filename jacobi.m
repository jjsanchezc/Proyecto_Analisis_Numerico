
function [E,s] = jacobi(A,b,x,tole,itera)
/*A = input('Ingrese la matriz A:  ');%ingrese la matriz de coeficientes
b = input('Ingresar el Termino independiente b:  ');%Ingrese el termino independiente
x = input('Aproximacion Inicial X0: ');%Ingrese una aproximación inicial para x0
itera = input('Numero maximo de iteraciones: ');%ingrese el número máximo de iteraciones
tole = input('Tolerancia: ');%Ingrese la tolerancia*/
condicional = norm(A) * norm (A^-1);%Calcule el condicional
disp('El Condicional es:')%Muestre el condicional
disp(condicional)

n = length(b);
d = diag(diag(A));
l = d - tril(A);
u = d - triu(A);
T = d^-1*(l+u)
val_propios=eig(T)
radioe = max(abs(val_propios))%Calcule el radio espectral

 	A=str2mat(A);
    b=str2mat(b);    
	x=str2double(x);
	tole=str2double(tole);
    itera=str2double(itera);
	
if radioe > 1
    disp('El Radio Espectral es mayor que 1, por lo tanto el metodo diverge')%Muestre que el método diverge
    disp(radioe)
elseif det(A)==0
	dis('el sistema no tiene solucion porque el determinante es 0')%Muestre que el sistema no tiene solución
else
	C = d^-1 * b
	i = 0;
	error = tole + 1;
	while error > tole && i < itera
		
		xi = T * x + C
		i = i + 1
		error = norm(xi-x)
		x = xi;
		xi'
	%     pause
		
	end
	disp('La solucion aproximada al sistema es xi:')%Muestre la solución apróximada
	disp(xi)
	disp('El Numero de iteraciones es:')%Muestre el número de iteraciones
	disp(i)
	disp('El Error es:')%Muestre el error
	disp(error)
end