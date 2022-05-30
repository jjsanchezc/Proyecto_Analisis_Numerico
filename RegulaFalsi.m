function [s,E,fm,fe]= RegulaFalsi()
syms x
f = input("Escriba la funcion f(x): ");
xi = input("Escriba el valor de xi: ");
xs = input("Escriba el valor de xf: ");
tol = input("Escriba el valor de la tolerancia: ");
niter = input("Escriba el numero de iteraciones maximas: ");
terr = input("Ingrese el error que quiere hallar, siendo 0 el error absoluto y 1 el error relativo: ");
a = xi - 0.5;
b = xs + 0.5; 
x = linspace(a,b);

fi= eval(subs(f,xi));
fs= eval(subs(f,xs));
if fi==0
    s=xi;
    E=0;
    fprintf('%f f(x) tiene raiz en \n',xi)
elseif fs==0
    s=xs;
    E=0;
    fprintf('%f f(x) tiene raiz en \n ',xs)
elseif fi*fs<0
    c=0;
    xm = xi-(((fi)*(xi-xs))/(fi-fs));
    fm(c+1) = eval(subs(f,xm));
    fe= fm(c+1);
    E(c+1)=tol+1;
    error=E(c+1);
    N(c+1)=c;
    while error>tol && fe~=0 && c<niter
        if fi*fe<0
            xs = xm;
            fs = eval(subs(f,xs));
        else 
            xi=xm;
            fi= eval(subs(f,xi));
        end
        xa(c+2)=xm;
        xm= xi-(((fi)*(xi-xs))/(fi-fs));
        fm(c+2)= eval(subs(f,xm));
        fe=fm(c+2);
         if terr==0
                E(c+2)=abs((xm-xa(c+2)));
            else
                E(c+2)=abs((xm-xa(c+2))/xm);
         end
        error=E(c+2);
        N(c+2)=(c+1);
        c=c+1;
    end
    if fe==0
           s=xm;
           fprintf('%f es raiz de f(x)\n',xm)
           disp('   n       Xa        F         E')
            D= [N' xa' fm' E'];
            disp(D)
        elseif error<tol
           s=xm;
           fprintf('%f es una aproximación de una raiz de f(x) con una tolerancia= %f\n',xm,tol)
           disp('     n        Xa         F         E')
             D=[N' xa' fm' E'];
             disp(D)
           
        else 
           s=xm;
           fprintf('Fracasó en %f iteraciones \n',niter)
           disp('      n        Xa          F          E')
            D= [N' xa' fm' E'];
            disp(D)
    end
    else
       fprintf('El intervalo es inadecuado\n')         
 end
    p = eval(subs(f,x));
    plot(x,p,'r')
    grid on
    hold on
    line(xlim, [0,0], 'Color', 'k', 'LineWidth', 0.5);
    hold on
    plot([xi,xs],[fi,fs], 'Color', 'g', 'LineWidth', 1);
    scatter(s,eval(subs(f,s)),'.')   
end





