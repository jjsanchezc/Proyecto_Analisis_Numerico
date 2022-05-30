A = input('Ingresar la matriz A: ');%ingrese la matriz de coeficientes
b = input('Ingresar el Termino independiente b: ');%Ingrese el termino independiente
x = input('Ingresar el valor inicial para x0: ');%Ingrese un valor inicial para x0
itera = input('Numero maximo de iteraciones: ');%ingrese el número máximo de iteraciones
tole = input('Tolerancia: ');%Ingrese la tolerancia
condicion = norm(A) * norm(A^-1);%Calcule el condicional
disp('El Condicional es:')%Muestre el condicional
disp(condicion)

n = length(b);
d = diag(diag(A));
l = d - tril(A);
u = d - triu(A);

T = (d-l)^-1 * u
val_propios = eig(T)
radioe=max(abs(val_propios))%Calcule el radio espectral

if radioe > 1
    disp('El Radio Espectral es mayor que 1, por lo tanto el metodo diverge')%Muestre que el método diverge
elseif det(A)==0
	dis('el sistema no tiene solucion porque el determinante es 0')%Muestre que el sistema no tiene solución
else
	C = (d-l)^-1 * b
	i = 0;
	error = tole + 1;
	while error > tole && i < itera
		
		xi = T *x + C;
		i = i + 1;
		error = norm(xi-x)
		x = xi;
		xi'
	end
	disp('La solucion aproximada al sistema es xi:')%Muestre la solución apróximada
	disp(xi)
	disp('El Numero de iteraciones es:')%Muestre el número de iteraciones
	disp(i)
	disp('El Error es:')%Muestre el error
	disp(error)
    disp('el radio espectral es')
    disp(radioe)
end