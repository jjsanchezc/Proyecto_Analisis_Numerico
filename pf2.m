function pf2

global fun

fprintf('Método del punto fijo:\n');

syms x

fx =sin(x-887*10^-3)-x; %f
fun=sin(x-887*10^-3); %g

x0=input('Ingrese el punto inicial:\n');

n=input('Ingrese el numero de iteraciones:\n');

Tol= input('Ingrese la tolerancia');
x=x0;
c=0;
x1=eval(fun);
fprintf(' Iter.\t \t x0 \t \t Tol \t \t f(x) \t \t error');
E(c+1)=Tol+1;
error=E(c+1);

while error>Tol && fx~=0 && c<n

c = c+1;

x=x0;

x1=eval(fun);

 E(c+2)=abs(x1-x0);
 error=E(c+2);

fprintf('\n%3.0f%15.10f%15.10f%15.10f%15.10f\n',c,x0,Tol,x1,abs(error));

x0=x1;

end

fprintf('\n el punto fijo aproximado es=%10.6f\n',x1);