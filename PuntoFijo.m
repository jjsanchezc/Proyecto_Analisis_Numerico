%Punto fijo: se ingresa el valor inicial (x0), la tolerancia del error (Tol) y el mÃ ximo nÃ¹mero de iteraciones (niter) 

function [n,xn,fm,E] = PuntoFijo(f,g)
    syms x
f = input("Ingrese la funcion f:");
g = input("Ingrese la funcion g:");
x0 = input("Ingrese x0:");
Tol = input("Ingrese la toleracia:"); 
niter = input ("Ingrese el numero maximo de iteraciones:");
Terr = input("Ingrese el error que quiere hallar, siendo 0 el error absoluto y 1 el error relativo: ");
x = linspace(-2,0);% Intervalo de Grafica
        c=0;
        fm(c+1) = eval(subs(f,x0));
        fe=fm(c+1);
        E(c+1)=Tol+1;
        error=E(c+1);
        xn(c+1)=x0;
        N(c+1)=c;
        while error>Tol && fe~=0 && c<niter
            xn(c+2)=eval(subs(g,x0));
            fm(c+2)=eval(subs(f,xn(c+2)));
            fe=fm(c+2);
            if Terr==0
                E(c+2)=abs(xn(c+2)-x0);
            else
                E(c+2)=abs((xn(c+2)-x0)/x0);
            end
            error=E(c+2);
            x0=xn(c+2);
            N(c+2)=(c+1);
            c=c+1;
        end
        if fe==0
           n=x0;
           fprintf('%f es raiz de f(x)',x0)
           disp('  N           Xn         F         E')
            D= [N' xn' fm' E'];
            disp(D)
        elseif error<Tol
           n=x0;
           fprintf('%f es una aproximaciÃ³n de una raiz de f(x) con una tolerancia= %f',x0,Tol)
           disp('  N           Xn         F         E')
           D= [N' xn' fm' E'];
           disp(D)
        else 
           n=x0;
           fprintf('FracasÃ³ en %f iteraciones',niter) 
        end
        y = eval(subs(f,x));
        z = eval(subs(g,x));
        r = x;
        plot (x,y,'r',x,z,'b',x,r,'g')
        hold on
        grid on
        line(xlim, [0,0], 'Color', 'k', 'LineWidth', 0.5);
        scatter(n,eval(subs(f,n)),'.');
        scatter(n,eval(subs(r,n)),'.');
end