%Newtonor: Calcula los coeficioentes del polinomio simplificado de Newton, 
% teniendo los coeficientes (coef) de la tabla de diferencias divididas y 
% los puntos el conjunto de datos conocidos en la x.
function [pol] = Newtonor(x,coef)
    n=length(x);
    pol=1;
    acum=pol;
    pol=coef(1)*acum;
    for i=1:n-1
        pol=[0 pol];
        acum=conv(acum,[1 -x(i)]);
        pol=pol+coef(i+1)*acum;
    end
    
end