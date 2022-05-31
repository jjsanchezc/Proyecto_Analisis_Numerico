function [s,xn,n,fn,E] = Secante(x0,x1,tol,niter,f)
syms x
    f=str2sym(f)
    x0=str2double(x0);
    x1=str2double(x1);
    Tol=str2double(tol);
    niter=str2double(niter);

c=0;
xn1(c+1)=x1;
xn0(c+1)=x0;
xn1=xn1(c+1);
xn0=xn0(c+1);
fn(c+1) = eval(subs(f,xn1));
fm(c+1) = eval(subs(f,xn0));
fe= fn(c+1);
fd= fm(c+1);
E(c+1) = Tol+1;
error= E(c+1);
N(c+1)=c; 
while error >= Tol && c<niter && fe~=0
    xn(c+2)= xn1-((fe*(xn1-xn0))/(fe-fd));
    fn(c+2) = eval(subs(f,xn(c+2)));
    fm(c+2) = eval(subs(f,xn1));
    fe = fn(c+2);
    fd = fm(c+2);
    E(c+2) = abs(xn(c+2)-xn1);
    xn0=xn1;
    error=E(c+2);
    xn1=xn(c+2);
    N(c+2)=(c+1);
    c=c+1;
end
if fe==0;
    s=xn1;
    n=c;
    fprintf('%f es raiz de f(x) \n',xn1)
    disp('      n        X1          F          E')
            D= [N' xn' fn' E'];
            disp(D)
            elseif error<Tol
           s=xn1;
           n=c;
           fprintf('%f es una aproximación de una raiz de f(x) con una tolerancia= %f \n',xn1,Tol)
            disp('      n        X1          F          E')
            D= [N' xn' fn' E'];
            disp(D)
elseif fn-fm==0
       s=xn1;
       n=c;
       fprintf('%f es una posible raiz múltiple de f(x) \n',xn1)
else 
   s=xn1;
   n=c;
   fprintf('Fracasó en %f iteraciones \n',niter) 
end
        
end
    
