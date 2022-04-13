% Una implementación del método de la secante para búsqueda de raices en
% funciones continuas dentro de un intervalo.
%
% Por Gerardo Tinoco Guerrero
% 
% Ejemplo:
% Ejecutar las siguientes lineas dentro de la ventana de comandos:
%
% ff = @(x)(x.^2-4)
% x = secante(ff, 1, 5, 0.0001);
%
% Se buscará la raíz de la función (x^2)-4 tomando como puntos iniciales para
% el método de la secante a = 2 y b = 5, con una tolerancia tol = 0.0001.

function xs = secante(fun,a,b,tol)
fprintf('Método de la secante\n\n');
i = 1;
fa = feval(fun, a);
fb = feval(fun, b);
xs = b - ((b - a) / (fb - fa))*fb;
error = abs(b - a);

fprintf('Iter. \t \t a \t \t b \t Xs \t \t f(X) \t \t Error\n');
fprintf('%2i \t %f \t %f \t %f \t %f \n', i, a, b, xs,feval(fun,xs));


while error >= tol
    b = a;
    a = xs;
    fb = feval(fun,b);
    fa = feval(fun,a);
    xs = b - ((b - a)/(fb - fa))*fb;
    error = abs(b - a);
    i = i + 1;
   fprintf('%2i \t %f \t %f \t %f \t %f \t %f \n', i, a, b, xs,feval(fun,xs),error);
end
w = feval(fun,xs);
fprintf('\n La mejor aproximación a la raiz tomando una tolerancia de %f es \n x = %f con \n f(x)= %f\n y se realizaron %i iteraciones\n',tol, xs, w, i);
end