%busquedas incrementales: se ingresa el valor inicial de x (x0), el tamaño de paso(Delta) y el màximo nùmero de iteraciones (niter) 

function [s] = Bi(x0,Delta,niter)
    syms f(x)
    %f(x)=exp(2-6*x)*cos(x^2-3*x)+4*x-3;
    f(x)=cos(x)-x^2;
    f0=f(x0);
    if f==0
        s=x0;
        fprintf('%f es raiz de f(x)',x0)
    else
        x1=x0+Delta;
        c=1;                 %contador
        f1=f(x1);
        while f0*f1>0 && c<niter
            x0=x1;
            f0=f1;
            x1=x0+Delta;
            f1=f(x1);
            c=c+1;
        end
        if f1==0             %verifica que sea raiz
            s=x1;
            fprintf('%f es raiz de f(x)',x1)
        elseif f0*f1<0                             %verifica cambio de signo
            s=x1;
            fprintf('Existe una raiz de f(x) entre %f y %f',x0,x1)
        else                                       %verifica fracaso
            s=x1;
           fprintf('Fracasó en %f iteraciones',niter) 
        end
    end
    
end