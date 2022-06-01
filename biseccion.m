%Bisección: se ingresa el valor inicial y final del intervalo (xi, xs), la tolerancia del error (Tol) y el màximo nùmero de iteraciones (niter) 


function [msj,s,E,fm] = Biseccion(xi,xs,Tol,niter,f,Terr)
syms x
    f=str2sym(f)
    xi=str2double(xi);
    xs=str2double(xs);
    Tol=str2double(Tol);
    niter=str2double(niter);
    
x = linspace(xi,xs);
    
    fi=eval(subs(f,xi));
    fs=eval(subs(f,xs));
    if fi==0
        s=xi;
        E=0;
        msj=sprintf('%f es raiz de f(x)',xi)
    elseif fs==0
        s=xs;
        E=0;
        msj=printf('%f es raiz de f(x)',xs)
    elseif fs*fi<0
        c=0;
        xm=(xi+xs)/2;
        fm(c+1)=eval(subs(f,xm));
        fe=fm(c+1);
        E(c+1)=Tol+1;
        error=E(c+1);
        N(c+1)=c;
        while error>Tol && fe~=0 && c<niter
            if fi*fe<0
                xs=xm;
                fs=eval(subs(f,xs));
            else
                xi=xm;
                fi=eval(subs(f,xi));
            end
            xa(c+2)=xm;
            xm=(xi+xs)/2;
            fm(c+2)=eval(subs(f,xm));
            fe=fm(c+2);
            if Terr==0
                E(c+2)=abs((xm-xa(c+2)));
            else
                E(c+2)=abs((xm-xa(c+2))/xm)
            end
            error=E(c+2);
            N(c+2)=(c+1);
            c=c+1;
        end
        if fe==0 && c==0
           s=xm;
           msj=sprintf('%f es raiz de f(x)\n',xm)
        elseif fe==0
            s=xm;
           msj=sprintf('%f es raiz de f(x)\n',xm)
           disp(['   n       Xa        F         E'])
            D= [N' xa' fm' E'];
            disp(D)
        elseif error<Tol
           s=xm;
           fprintf('%f es una aproximación de una raiz de f(x) con una tolerancia= %f\n',xm,Tol)
           disp(['     n        Xa         F         E'])
             D=[N' xa' fm' E'];
             disp(D)
            msj=sprintf('%f es una aproximacion de una raiz de f(x) con una tolerancia= %f\n',xm,Tol)
        else 
           s=xm;
           msj=sprintf('Fracasó en %f iteraciones \n',niter)
           disp('      n        Xa          F          E')
            D= [N' xa' fm' E'];
            disp(D)
        end
    else
       msj=sprintf('El intervalo es inadecuado\n')         
    end
    p = eval(subs(f,x));
    
    %Sanchez aca es donde actua la funcion grafica 
    plot(x,p,'r')
    grid on
    hold on
    %line([0,0], ylim;, 'Color', 'k', 'LineWidth', 2); % Draw line for Y axis.
    line(xlim, [0,0], 'Color', 'k', 'LineWidth', 0.5); % Draw line for X axis.
    scatter(s,eval(subs(f,s)),'.')   
end